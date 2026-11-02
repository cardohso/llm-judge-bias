"""Planted errors (docs/PREREGISTRATION.md, section 4.5).

Every perturbed copy is a base answer, rendered and split into sentences, with exactly one
change: one sentence rewritten (NUM, CITE, NEG, QUAL) or one sentence appended (ADD). The
`Perturbation` records which sentence is the planted one, because a judge "misses" an error when
it rates that sentence supported. `validate` enforces the one-change rule for every source of
edits, code or hand-written, so no copy can differ from its base anywhere else.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import asdict, dataclass

from goldpass.perturb import numbers_in, perturb_number

from judgebias.render import render_answer
from judgebias.segment import MARKER, markers, segment

TYPES = ("ADD", "NUM", "CITE", "NEG", "QUAL")
WORD = re.compile(r"[a-z]{4,}")


class InvalidPerturbation(ValueError):
    pass


@dataclass(frozen=True)
class Perturbation:
    id: str  # "<question>-<generator>-<type>"
    question: str
    generator: str
    type: str
    subtype: str  # NUM: "out-of-context" | "in-context"; otherwise ""
    author: str  # "code" or "claude"
    planted_index: int  # 1-based index of the planted sentence in `sentences`
    change: str  # human-readable description for the reviewer
    sentences: tuple[str, ...]  # the perturbed answer, sentence by sentence

    @property
    def answer(self) -> str:
        return " ".join(self.sentences)

    @property
    def planted_sentence(self) -> str:
        return self.sentences[self.planted_index - 1]

    def to_dict(self) -> dict:
        return {**asdict(self), "sentences": list(self.sentences)}


def base_sentences(raw_answer: str) -> tuple[str, ...]:
    return tuple(segment(render_answer(raw_answer)))


def validate(base: Sequence[str], new: Sequence[str], planted_index: int, kind: str) -> None:
    """Exactly one sentence differs from the base (or one is appended, for ADD)."""
    if kind == "ADD":
        if len(new) != len(base) + 1 or list(new[:-1]) != list(base):
            raise InvalidPerturbation("ADD must append exactly one sentence")
        if planted_index != len(new):
            raise InvalidPerturbation("ADD's planted sentence must be the last one")
        return
    if len(new) != len(base):
        raise InvalidPerturbation(f"sentence count changed: {len(base)} -> {len(new)}")
    differing = [i for i, (a, b) in enumerate(zip(base, new, strict=True), 1) if a != b]
    if differing != [planted_index]:
        raise InvalidPerturbation(f"sentences {differing} differ, expected [{planted_index}]")


def _make(qid, gen, kind, subtype, author, base, new, idx, change) -> Perturbation:
    validate(base, new, idx, kind)
    return Perturbation(
        f"{qid}-{gen}-{kind}", qid, gen, kind, subtype, author, idx, change, tuple(new)
    )


def num_out_of_context(qid: str, gen: str, base: Sequence[str], passages: Sequence[dict]):
    """goldpass's rule: change a supported number to the nearest value found in no passage."""
    p = perturb_number(qid, " ".join(base), [x["text"] for x in passages])
    if p is None:
        return None
    new = tuple(segment(p.answer))
    changed = [i for i, (a, b) in enumerate(zip(base, new, strict=False), 1) if a != b]
    if len(new) != len(base) or len(changed) != 1:
        return None
    return _make(qid, gen, "NUM", "out-of-context", "code", base, new, changed[0],
                 f"{p.original} -> {p.planted}")  # fmt: skip


def _words(text: str) -> set[str]:
    return set(WORD.findall(MARKER.sub("", text).lower()))


def cite_wrong(qid: str, gen: str, base: Sequence[str], passages: Sequence[dict]):
    """Re-point the first cited sentence at the distractor least like it. The text is unchanged.
    The chosen distractor is a heuristic: the author's review confirms it does not support it."""
    distractors = [p for p in passages if p["role"] == "distractor"]
    for i, sentence in enumerate(base, 1):
        cited = set(markers(sentence))
        if not cited:
            continue
        body = MARKER.sub("", sentence).rstrip()
        stop = body[-1] if body[-1] in ".!?" else ""
        body = body[: len(body) - len(stop)].rstrip()
        options = []
        for d in distractors:
            if d["n"] in cited or numbers_in(body) & numbers_in(d["text"]):
                continue
            a, b = _words(body), _words(d["text"])
            options.append((len(a & b) / max(1, len(a | b)), d["n"]))
        if not options:
            continue
        n = min(options)[1]
        new_sentence = f"{body} [{n}]{stop}"
        new = [*base[: i - 1], new_sentence, *base[i:]]
        return _make(qid, gen, "CITE", "", "code", base, new, i,
                     f"citation {sorted(cited)} -> [{n}]")  # fmt: skip
    return None


def apply_edit(qid, gen, kind, subtype, base, index, find, replace, change="") -> Perturbation:
    """Hand-written NUM/NEG/QUAL: `find` must occur exactly once in sentence `index`."""
    sentence = base[index - 1]
    if sentence.count(find) != 1:
        raise InvalidPerturbation(
            f"{qid} {gen}: {find!r} occurs {sentence.count(find)}x in S{index}"
        )
    new = [*base[: index - 1], sentence.replace(find, replace), *base[index:]]
    return _make(
        qid, gen, kind, subtype, "claude", base, new, index, change or f"{find!r} -> {replace!r}"
    )


def add_sentence(qid: str, gen: str, base: Sequence[str], text: str) -> Perturbation:
    """Append `text` (a sentence without markers) citing the marker of the last sentence."""
    cited = markers(base[-1])
    if not cited:
        raise InvalidPerturbation(f"{qid} {gen}: the last sentence has no citation to reuse")
    body = text.strip().rstrip(".")
    sentence = f"{body} [{cited[-1]}]."
    return _make(qid, gen, "ADD", "", "claude", base, [*base, sentence], len(base) + 1, "appended")
