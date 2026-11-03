"""Scoring and statistics exactly as pre-registered (docs/PREREGISTRATION.md, sections 6 and 8).

Outcomes per (item, judge, run) come from the judge's per-sentence verdicts. Every interval is a
percentile bootstrap over **questions**: resampling uses multinomial weights on per-question
sums, so all copies, generators and judges of a question move together. Seed 20261102,
10 000 resamples.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field

import numpy as np

from judgebias.judging import parse_verdicts

SEED = 20261102
N_BOOT = 10_000
SESOI = 0.10
FLOOR = 0.05
TYPES = ("ADD", "NUM", "CITE", "NEG", "QUAL")


# --------------------------------------------------------------------------- outcomes (section 6)


@dataclass(frozen=True)
class Outcome:
    item: str
    question: str
    generator: str
    type: str  # CONTROL or an error type
    subtype: str
    judge: str
    run: int
    n_sentences: int
    verdicts: dict[int, bool] = field(hash=False)
    planted: int | None

    @property
    def is_control(self) -> bool:
        return self.type == "CONTROL"

    @property
    def invalid(self) -> bool:
        """No usable verdict: for a copy, none for the planted sentence; for a control, none."""
        return not self.verdicts if self.is_control else self.planted not in self.verdicts

    @property
    def miss(self) -> bool | None:
        """Primary: the planted sentence is rated supported. None if invalid or a control."""
        if self.is_control or self.invalid:
            return None
        return self.verdicts[self.planted]

    @property
    def answer_miss(self) -> bool | None:
        """No sentence of the copy is rated unsupported."""
        if self.is_control:
            return None
        return all(self.verdicts.values())

    @property
    def wrong_reason(self) -> bool | None:
        """Planted sentence rated supported, but another sentence rated unsupported."""
        if self.miss is None:
            return None
        return self.miss and any(not v for k, v in self.verdicts.items() if k != self.planted)

    @property
    def false_alarm(self) -> bool | None:
        if not self.is_control or self.invalid:
            return None
        return any(not v for v in self.verdicts.values())

    @property
    def unsupported_sentences(self) -> int:
        return sum(not v for v in self.verdicts.values())


def outcomes(items: Iterable[dict], rows: Iterable[dict]) -> list[Outcome]:
    by_id = {i["id"]: i for i in items}
    out = []
    for r in rows:
        i = by_id[r["item"]]
        try:
            verdicts = parse_verdicts(r["content"])
        except ValueError:
            verdicts = {}
        out.append(
            Outcome(
                i["id"],
                i["question"],
                i["generator"],
                i["type"],
                i["subtype"],
                r["judge"],
                r["run"],
                len(i["sentences"]),
                verdicts,
                i["planted_index"],
            )  # fmt: skip
        )
    return out


# --------------------------------------------------------------------------- bootstrap machinery


class Clustered:
    """Per-question sums of named quantities, resampled together by question."""

    def __init__(self, questions: Sequence[str], seed: int = SEED, n_boot: int = N_BOOT):
        self.questions = list(questions)
        self.index = {q: k for k, q in enumerate(self.questions)}
        rng = np.random.default_rng(seed)
        n = len(self.questions)
        self.weights = rng.multinomial(n, np.full(n, 1 / n), size=n_boot).astype(float)

    def sums(self, pairs: Iterable[tuple[str, Sequence[float]]], width: int) -> np.ndarray:
        """(Q, width) array; each pair is (question, values to add)."""
        out = np.zeros((len(self.questions), width))
        for q, values in pairs:
            out[self.index[q]] += values
        return out

    def estimate(self, per_q: np.ndarray, stat: Callable[[np.ndarray], np.ndarray]):
        """(point, 95% CI, 90% CI); `stat` maps (..., width) sums to a value per row."""
        point = float(stat(per_q.sum(axis=0)[None, :])[0])
        boot = stat(self.weights @ per_q)
        boot = boot[np.isfinite(boot)]
        if not boot.size:
            return point, (math.nan, math.nan), (math.nan, math.nan)
        ci95 = tuple(float(x) for x in np.percentile(boot, [2.5, 97.5]))
        ci90 = tuple(float(x) for x in np.percentile(boot, [5, 95]))
        return point, ci95, ci90


def _ratio(s: np.ndarray) -> np.ndarray:
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(s[..., 1] > 0, s[..., 0] / s[..., 1], np.nan)


def rate(boot: Clustered, pairs: Iterable[tuple[str, bool]]) -> dict:
    """A proportion with its question-bootstrap CI. `pairs` are (question, outcome)."""
    pairs = list(pairs)
    per_q = boot.sums(((q, (float(x), 1.0)) for q, x in pairs), 2)
    point, ci95, _ = boot.estimate(per_q, _ratio)
    return {"n": len(pairs), "k": int(sum(x for _, x in pairs)), "rate": point, "ci95": ci95}


# --------------------------------------------------------------------------- primary (section 8)

CELLS = (("G", "A"), ("G", "B"), ("O", "A"), ("O", "B"))


def _delta(s: np.ndarray) -> np.ndarray:
    """Δ_SP = ½[(m_G(A) − m_G(B)) + (m_O(B) − m_O(A))] from (…, 8) sums: misses, then counts."""
    with np.errstate(invalid="ignore", divide="ignore"):
        m = s[..., :4] / s[..., 4:]
    ga, gb, oa, ob = m[..., 0], m[..., 1], m[..., 2], m[..., 3]
    return 0.5 * ((ga - gb) + (ob - oa))


def interaction(
    boot: Clustered,
    rows: Iterable[Outcome],
    value: Callable[[Outcome], bool | None] = lambda o: o.miss,
    judges: tuple[str, str] = ("G", "O"),
) -> dict:
    """Δ_SP for one outcome definition. `value` returning None excludes the copy."""
    cells = {(judges[0], "A"): 0, (judges[0], "B"): 1, (judges[1], "A"): 2, (judges[1], "B"): 3}
    pairs = []
    for o in rows:
        k = cells.get((o.judge, o.generator))
        v = value(o)
        if k is None or v is None or o.is_control:
            continue
        vec = [0.0] * 8
        vec[k], vec[4 + k] = float(v), 1.0
        pairs.append((o.question, vec))
    per_q = boot.sums(pairs, 8)
    totals = per_q.sum(axis=0)
    point, ci95, ci90 = boot.estimate(per_q, _delta)
    pooled = float(totals[:4].sum() / totals[4:].sum()) if totals[4:].sum() else math.nan
    cell_rates = {f"{j}{g}": float(totals[k] / totals[4 + k]) if totals[4 + k] else math.nan
                  for (j, g), k in cells.items()}  # fmt: skip
    counts = {f"{j}{g}": int(totals[4 + k]) for (j, g), k in cells.items()}
    return {"delta": point, "ci95": ci95, "ci90": ci90, "pooled_miss": pooled,
            "cells": cell_rates, "n": counts}  # fmt: skip


def decide(result: dict, sesoi: float = SESOI, floor: float = FLOOR) -> str:
    """Section 8.3 decision rules, applied in order."""
    p = result["pooled_miss"]
    if not math.isfinite(p) or p < floor or p > 1 - floor:
        return "not testable (floor or ceiling)"
    lo95, hi95 = result["ci95"]
    lo90, hi90 = result["ci90"]
    positive, reverse = lo95 > 0, hi95 < 0
    equivalent = lo90 > -sesoi and hi90 < sesoi
    if positive and equivalent:
        return "self-preference smaller than 10 points"
    if positive:
        return "self-preference"
    if reverse:
        return "reverse preference"
    if equivalent:
        return "no effect of 10 points or more"
    return "inconclusive"


# --------------------------------------------------------------------------- agreement (S3, S4)


def cohen_kappa_sums(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Per-unit 2x2 indicator columns (both T, a T b F, a F b T, both F) for one pair."""
    return np.stack([a & b, a & ~b, ~a & b, ~a & ~b], axis=-1).astype(float)


def _cohen(s: np.ndarray) -> np.ndarray:
    n = s.sum(axis=-1)
    tt, tf, ft, ff = (s[..., i] for i in range(4))
    with np.errstate(invalid="ignore", divide="ignore"):
        po = (tt + ff) / n
        pe = ((tt + tf) * (tt + ft) + (ft + ff) * (tf + ff)) / n**2
        return (po - pe) / (1 - pe)


def _fleiss(m: int) -> Callable[[np.ndarray], np.ndarray]:
    """From sums of (P_i, n_i, 1) over units with m binary ratings each."""

    def f(s: np.ndarray) -> np.ndarray:
        with np.errstate(invalid="ignore", divide="ignore"):
            p_bar = s[..., 0] / s[..., 2]
            p = s[..., 1] / (s[..., 2] * m)
            pe = p**2 + (1 - p) ** 2
            return (p_bar - pe) / (1 - pe)

    return f


def fleiss_unit(ratings: Sequence[bool]) -> tuple[float, float, float]:
    m, k = len(ratings), sum(ratings)
    return ((k * (k - 1) + (m - k) * (m - k - 1)) / (m * (m - 1)), float(k), 1.0)


def units(rows: Iterable[Outcome], key: Callable[[Outcome], str], planted_only=False):
    """{(item, sentence): {key(o): verdict}} plus each unit's question."""
    table: dict[tuple[str, int], dict[str, bool]] = defaultdict(dict)
    question = {}
    for o in rows:
        for s, v in o.verdicts.items():
            if planted_only and s != o.planted:
                continue
            table[o.item, s][key(o)] = v
            question[o.item, s] = o.question
    return table, question


def agreement(
    boot: Clustered, rows: Sequence[Outcome], raters: Sequence[str], key, planted_only=False
):
    """Pairwise Cohen's κ, Fleiss' κ and percent agreement over units rated by every rater."""
    table, question = units(rows, key, planted_only)
    full = [(u, r) for u, r in table.items() if all(x in r for x in raters)]
    out: dict = {"units": len(full)}
    if not full:
        return out
    for i, a in enumerate(raters):
        for b in raters[i + 1 :]:
            pairs = [(question[u], cohen_kappa_sums(np.array(r[a]), np.array(r[b])))
                     for u, r in full]  # fmt: skip
            out[f"kappa_{a}{b}"] = boot.estimate(boot.sums(pairs, 4), _cohen)[:2]
    per_q = boot.sums(((question[u], fleiss_unit([r[x] for x in raters])) for u, r in full), 3)
    out["fleiss_kappa"] = boot.estimate(per_q, _fleiss(len(raters)))[:2]
    agree = [(question[u], len({r[x] for x in raters}) == 1) for u, r in full]
    out["percent_agreement"] = rate(boot, agree)
    out["share_differing"] = rate(boot, [(q, not a) for q, a in agree])
    return out


# --------------------------------------------------------------------------- S7: exact McNemar


def mcnemar_exact(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2**n
    return min(1.0, 2 * tail)


def holm(pvalues: dict[str, float]) -> dict[str, float]:
    order = sorted(pvalues, key=pvalues.get)
    adjusted, running = {}, 0.0
    for rank, key in enumerate(order):
        running = max(running, min(1.0, (len(order) - rank) * pvalues[key]))
        adjusted[key] = running
    return adjusted


def own_vs_other(rows: Sequence[Outcome], judge: str, own: str) -> dict:
    """Matched (question, type) pairs: b = missed on own only, c = missed on the other only."""
    cell: dict[tuple[str, str], dict[str, bool]] = defaultdict(dict)
    for o in rows:
        if o.judge == judge and o.miss is not None:
            cell[o.question, o.type][o.generator] = o.miss
    other = "B" if own == "A" else "A"
    pairs = [v for v in cell.values() if own in v and other in v]
    b = sum(v[own] and not v[other] for v in pairs)
    c = sum(v[other] and not v[own] for v in pairs)
    return {"pairs": len(pairs), "own_only": b, "other_only": c, "p": mcnemar_exact(b, c)}
