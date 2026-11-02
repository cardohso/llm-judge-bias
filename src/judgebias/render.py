"""How an answer is shown to perturbation review and to judges (docs/PREREGISTRATION.md, section 5).

Every answer, whichever generator wrote it, goes through the same normalisation so that
typography cannot reveal the generator: runs of whitespace (including no-break and narrow
no-break spaces) become one space, and non-breaking hyphens become plain hyphens. gpt-oss-120b
writes U+202F and U+2011, gemini-3.5-flash-lite never does (dated note in REPORT.md, 2026-11-02).
The raw text stays unchanged in answers/answers.jsonl.
"""

from __future__ import annotations

HYPHENS = {"‐": "-", "‑": "-"}


def render_answer(text: str) -> str:
    for src, dst in HYPHENS.items():
        text = text.replace(src, dst)
    return " ".join(text.split())
