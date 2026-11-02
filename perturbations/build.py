"""Build every judged item: one control and up to five planted errors per retained base answer
(docs/PREREGISTRATION.md, section 4.5). Deterministic; no API calls.

- NUM: the hand-written in-context edit if there is one, otherwise goldpass's out-of-context rule.
- CITE: code. ADD, NEG, QUAL: hand-written (perturbations/handwritten.jsonl, by Claude Opus 5.5).
Every copy passes judgebias.perturb.validate (exactly one sentence changed or appended).
Checks that need a human are printed as warnings and repeated in the review sheet.

    uv run python perturbations/build.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from goldpass.perturb import numbers_in

from judgebias.perturb import (
    add_sentence,
    apply_edit,
    base_sentences,
    cite_wrong,
    num_out_of_context,
)
from judgebias.segment import markers

ROOT = Path(__file__).resolve().parent.parent


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines()]


def main() -> int:
    retained = json.loads((ROOT / "answers/review_outcome.json").read_text())["retained_questions"]
    ctx = {c["id"]: c for c in jsonl(ROOT / "contexts/contexts.jsonl")}
    answers = {(a["id"], a["generator"]): a for a in jsonl(ROOT / "answers/answers.jsonl")}
    hand = jsonl(ROOT / "perturbations/handwritten.jsonl")
    items, warnings = [], []
    for q in retained:
        passages = ctx[q]["passages"]
        all_numbers = set().union(*(numbers_in(p["text"]) for p in passages))
        for gen in "AB":
            base = base_sentences(answers[q, gen]["answer"])
            items.append({"id": f"{q}-{gen}-CONTROL", "question": q, "generator": gen,
                          "type": "CONTROL", "subtype": "", "author": "", "planted_index": None,
                          "change": "", "sentences": list(base)})  # fmt: skip
            mine = [h for h in hand if h["question"] == q and gen in h["generator"]]
            made = {}
            for h in mine:
                if h["type"] == "ADD":
                    p = add_sentence(q, gen, base, h["text"])
                    extra = numbers_in(h["text"]) & all_numbers
                    if extra:
                        warnings.append(f"{p.id}: ADD uses numbers found in the context: {extra}")
                else:
                    p = apply_edit(q, gen, h["type"], h["subtype"], base, h["sentence"],
                                   h["find"], h["replace"])  # fmt: skip
                    new = numbers_in(h["replace"]) - numbers_in(h["find"])
                    if h["subtype"] == "in-context":
                        cited = set(markers(base[h["sentence"] - 1]))
                        cited_text = " ".join(x["text"] for x in passages if x["n"] in cited)
                        if not new <= numbers_in(cited_text):
                            warnings.append(f"{p.id}: in-context value {new} not in cited passage")
                    elif h["subtype"] == "out-of-context" and new & all_numbers:
                        warnings.append(f"{p.id}: out-of-context value {new} is in the context")
                if p.type in made:
                    raise SystemExit(f"two {p.type} edits for {q} {gen}")
                made[p.type] = p
            if "NUM" not in made and (p := num_out_of_context(q, gen, base, passages)):
                made["NUM"] = p
            if p := cite_wrong(q, gen, base, passages):
                made["CITE"] = p
            for kind in ("ADD", "NUM", "CITE", "NEG", "QUAL"):
                if kind in made:
                    items.append(made[kind].to_dict())
    out = ROOT / "perturbations/perturbations.jsonl"
    out.write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items))
    from collections import Counter

    counts = Counter((i["type"], i["generator"]) for i in items)
    print(f"wrote {len(items)} items to {out.relative_to(ROOT)}")
    for kind in ("CONTROL", "ADD", "NUM", "CITE", "NEG", "QUAL"):
        print(f"  {kind:8} A={counts[kind, 'A']:3}  B={counts[kind, 'B']:3}")
    for w in warnings:
        print("WARNING", w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
