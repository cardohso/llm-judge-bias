"""Blinded review sheet for the base answers: the reviewer sees each question's context once and
two answers labelled X and Y in a random order (seed 20261102). The X/Y key is written to
.state/review_key.json and committed only after the review is done.

    uv run python answers/make_review.py
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from judgebias.render import render_answer
from judgebias.segment import segment

ROOT = Path(__file__).resolve().parent.parent
SEED = 20261102


def main() -> None:
    contexts = [json.loads(x) for x in (ROOT / "contexts/contexts.jsonl").read_text().splitlines()]
    answers = {}
    for line in (ROOT / "answers/answers.jsonl").read_text().splitlines():
        r = json.loads(line)
        answers[r["id"], r["generator"]] = r
    rng = random.Random(SEED)
    key: dict[str, dict[str, str]] = {}
    out = [
        "# Review: base answers (blinded)",
        "",
        "You see two answers per question, X and Y, in random order. You are not told which",
        "model wrote which. Judge each answer **against the passages shown**, as rendered below.",
        "",
        "**Accept an answer only if all three hold:**",
        "1. every sentence is correct and supported by the passage(s) it cites;",
        "2. every sentence that states a fact ends with a citation marker `[n]` that exists above;",
        "3. the sentences are split correctly (S1, S2, … as shown).",
        "",
        "Tick `[x] Accept` or `[x] Reject` and write the reason in **Note** for each rejection.",
        "If either answer to a question is rejected, the question is dropped for both generators",
        "(pre-registration, section 4.4). Answers are never edited. About 40 minutes in total.",
        "",
    ]
    for ctx in contexts:
        labels = ["A", "B"]
        rng.shuffle(labels)
        key[ctx["id"]] = {"X": labels[0], "Y": labels[1]}
        out += [f"## {ctx['id']}", "", f"**Question:** {ctx['question']}", ""]
        for p in ctx["passages"]:
            out += [f"**[{p['n']}]**", "", "```", p["text"], "```", ""]
        for slot, label in zip("XY", labels, strict=True):
            r = answers[ctx["id"], label]
            sentences = segment(render_answer(r["answer"]))
            out += [f"### {ctx['id']} · answer {slot}", ""]
            if not sentences:
                out += ["_(no answer given)_", ""]
            out += [f"- **S{i}:** {s}" for i, s in enumerate(sentences, 1)]
            out += ["", "- [ ] Accept  - [ ] Reject", "", "**Note:** ", ""]
    (ROOT / "answers/REVIEW.md").write_text("\n".join(out))
    (ROOT / ".state/review_key.json").write_text(json.dumps(key, indent=1))


if __name__ == "__main__":
    main()
