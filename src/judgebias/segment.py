"""Deterministic sentence segmentation of cited answers (docs/PREREGISTRATION.md, section 4.4).

A sentence ends at ., ! or ? followed by whitespace and an upper-case letter or digit. Citation
markers stay with the sentence they cite, whether the model wrote them before the full stop
("65 dB [1].") or after it ("65 dB. [1]"). Decimals ("0,225", "2.25"), section numbers
("4.2.1") and common abbreviations do not end a sentence. Whitespace is normalised, so
`" ".join(segment(text))` is `text` with runs of whitespace collapsed.
"""

from __future__ import annotations

import re

MARKER = re.compile(r"\[(\d+)\]")
# . ! ? then optional markers (kept with this sentence), then whitespace and a sentence start
_BOUNDARY = re.compile(r"[.!?](?:\s*\[\d+\])*(?=\s+[A-Z0-9])")
ABBREVIATIONS = {"e.g", "i.e", "vs", "cf", "no", "nos", "art", "arts", "approx", "para", "paras",
                 "fig", "eg", "ie"}  # fmt: skip


def _is_abbreviation(text: str, end: int) -> bool:
    """True if the full stop at text[end] closes an abbreviation such as 'e.g' or 'No'."""
    start = end
    while start > 0 and (text[start - 1].isalpha() or text[start - 1] == "."):
        start -= 1
    return text[start:end].lower().strip(".") in ABBREVIATIONS


def segment(text: str) -> list[str]:
    text = " ".join(text.split())
    sentences, start = [], 0
    for m in _BOUNDARY.finditer(text):
        if text[m.start()] == "." and _is_abbreviation(text, m.start()):
            continue
        sentences.append(text[start : m.end()].strip())
        start = m.end()
    if tail := text[start:].strip():
        sentences.append(tail)
    return sentences


def markers(sentence: str) -> list[int]:
    """Citation markers in a sentence, in order, e.g. 'x [2][3].' -> [2, 3]."""
    return [int(n) for n in MARKER.findall(sentence)]
