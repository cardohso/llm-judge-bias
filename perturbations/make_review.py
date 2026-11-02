"""Blinded review sheet for the planted errors (docs/PREREGISTRATION.md, section 4.5).

Each question's passages are shown once, then every planted error for that question with the
sentence before and after the change. Items are labelled R001, R002, … in an order shuffled
within each question (seed 20261102), so the generator is not shown. The key goes to
.state/perturbation_review_key.json and is committed after the review.

    uv run python perturbations/make_review.py
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from judgebias.perturb import base_sentences

ROOT = Path(__file__).resolve().parent.parent
SEED = 20261102
WHAT = {
    "ADD": "a sentence was appended that no passage supports",
    "NUM": "a number was changed",
    "CITE": "the citation now points to a passage that does not support the sentence",
    "NEG": "a requirement was negated or its direction reversed",
    "QUAL": "an obligation was weakened/strengthened, or a condition/exception was removed",
}


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines()]


def main() -> None:
    ctx = {c["id"]: c for c in jsonl(ROOT / "contexts/contexts.jsonl")}
    answers = {(a["id"], a["generator"]): a for a in jsonl(ROOT / "answers/answers.jsonl")}
    items = [i for i in jsonl(ROOT / "perturbations/perturbations.jsonl") if i["type"] != "CONTROL"]
    rng = random.Random(SEED)
    key, out, n = {}, [], 0
    out += [
        "# Review: planted errors (blinded)",
        "",
        f"{len(items)} planted errors. Each shows one sentence before and after the change; every",
        "other sentence of the answer is unchanged (checked by code). The generator is hidden.",
        "",
        "**Accept an item only if all four hold:**",
        "1. the *after* sentence is **not supported** by the passage(s) it cites, read carefully;",
        "2. it is grammatical and plausible (something a model could have written);",
        "3. the type label is right;",
        "4. for `CITE`: the newly cited passage really does not support the sentence.",
        "",
        "Tick `[x] Accept` or `[x] Reject`; write a reason in **Note** for each rejection.",
        "A rejected item gets one replacement of the same type, which you review again.",
        "",
        "**Tip:** if you accept everything for a question, you may write `ALL OK` under its",
        "heading instead of ticking each box.",
        "",
    ]
    for q in dict.fromkeys(i["question"] for i in items):
        group = [i for i in items if i["question"] == q]
        rng.shuffle(group)
        out += [f"## {q}", "", f"**Question:** {ctx[q]['question']}", ""]
        for p in ctx[q]["passages"]:
            out += [f"<details><summary>[{p['n']}] {p['text'].splitlines()[0]}</summary>", "",
                    "```", p["text"], "```", "", "</details>", ""]  # fmt: skip
        for i in group:
            n += 1
            rid = f"R{n:03d}"
            key[rid] = i["id"]
            base = base_sentences(answers[q, i["generator"]]["answer"])
            k = i["planted_index"]
            out += [f"### {rid} · `{i['type']}`{' · ' + i['subtype'] if i['subtype'] else ''}",
                    "", f"_{WHAT[i['type']]}_", ""]  # fmt: skip
            if i["type"] == "ADD":
                out += [f"- **Answer:** {' '.join(base)}", f"- **Appended:** {i['sentences'][-1]}"]
            else:
                out += [f"- **Before:** {base[k - 1]}", f"- **After:** {i['sentences'][k - 1]}"]
            out += ["", "- [ ] Accept  - [ ] Reject", "", "**Note:** ", ""]
    (ROOT / "perturbations/REVIEW.md").write_text("\n".join(out))
    (ROOT / ".state/perturbation_review_key.json").write_text(json.dumps(key, indent=1))
    print(f"{n} items in perturbations/REVIEW.md")


if __name__ == "__main__":
    main()
