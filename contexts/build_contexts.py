"""Build the fixed context of every question: gold passages + the 2 highest-ranked non-gold
passages by dense cosine similarity (BAAI/bge-small-en-v1.5, the rail repo's embedder), with
no LLM rewrite or grading step (docs/PREREGISTRATION.md, section 4.3).

Needs the rail repo's environment (fastembed and rail_rag), so it is run once and its output,
contexts/contexts.jsonl, is committed. The search is exact cosine over every passage.

    <rail-repo>/.venv/bin/python contexts/build_contexts.py --rail <rail-repo>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

N_DISTRACTORS = 2
ROOT = Path(__file__).resolve().parent.parent


def build(questions: list[dict], passages: list, embedder) -> list[dict]:
    """Pure function of its inputs; passages need .id, .doc_short, .heading, .text, .embed_text."""
    import numpy as np

    vectors = np.array(embedder.embed_documents([p.embed_text for p in passages]))
    index = {p.id: i for i, p in enumerate(passages)}
    out = []
    for q in questions:
        scores = vectors @ np.array(embedder.embed_query(q["question"]))
        gold = list(q["gold_passages"])
        ranked = [passages[i].id for i in np.argsort(-scores, kind="stable")]
        distractors = [pid for pid in ranked if pid not in gold][:N_DISTRACTORS]
        ordered = sorted(gold + distractors, key=lambda pid: (-scores[index[pid]], pid))
        out.append({
            "id": q["id"],
            "question": q["question"],
            "gold": gold,
            "distractors": distractors,
            "passages": [
                {
                    "n": n,
                    "id": pid,
                    "role": "gold" if pid in gold else "distractor",
                    "score": round(float(scores[index[pid]]), 4),
                    "text": f"{passages[index[pid]].doc_short}, {passages[index[pid]].heading}\n"
                    f"{passages[index[pid]].text}",
                }
                for n, pid in enumerate(ordered, start=1)
            ],
        })  # fmt: skip
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rail", type=Path, required=True, help="rail-regulation-rag checkout")
    args = ap.parse_args()
    sys.path.insert(0, str(args.rail / "src"))
    from rail_rag.chunking import load_passages
    from rail_rag.embeddings import LocalEmbedder

    questions = [
        json.loads(line) for line in (ROOT / "questions/questions.jsonl").read_text().splitlines()
    ]
    contexts = build(questions, load_passages(args.rail / "data/processed"), LocalEmbedder())
    with (ROOT / "contexts/contexts.jsonl").open("w") as f:
        for c in contexts:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"wrote {len(contexts)} contexts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
