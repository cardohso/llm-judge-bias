"""Power simulation for the primary hypothesis (self-preference interaction), run before any
judge call. Every number in the pre-registration's power table comes from this script.

Model (assumptions, not data):
- Q questions, 2 generators (A, B), 5 error types. Each (question, generator, type) has a
  planted error with probability P_APPLICABLE.
- Miss probability on the logit scale = intercept + question effect + answer effect + item
  effect + error-type effect + judge effect. The intercept is solved so the mean miss rate
  equals `base`. Two scenarios for the item effect: `shared` (an error hard for one judge is
  hard for all) and `judge_specific` (each judge finds different errors hard). Shared effects
  cancel in the interaction, so `judge_specific` is the pessimistic case.
- Self-preference adds `delta` (probability scale) to judge G on A's answers and to judge O on
  B's answers, so the true interaction equals `delta` (minus clipping at 1).

Estimator and decision rules are those in docs/PREREGISTRATION.md: pooled miss rates, the
interaction Δ = ½[(m_G(A) − m_G(B)) + (m_O(B) − m_O(A))], a question-level cluster bootstrap,
"self-preference" if the 95% CI is above 0, "no effect larger than SESOI" if the 90% CI lies
inside ±SESOI.

    uv run --python 3.12 --with numpy python analysis/power.py
"""

from __future__ import annotations

import csv
import sys
from itertools import product
from pathlib import Path

import numpy as np

SEED = 20261102
N_SIMS = 1000
N_BOOT = 1000
P_APPLICABLE = 0.9
SESOI = 0.10
SD_QUESTION, SD_ANSWER, SD_ITEM = 1.0, 0.5, 1.0
TYPE_EFFECTS = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
JUDGE_EFFECTS = np.array([0.3, -0.3])  # judge G is a little more lenient than judge O
SCENARIOS = ["shared", "judge_specific"]
GRID_Q = [30, 40]
GRID_BASE = [0.10, 0.20, 0.35]
GRID_DELTA = [0.0, 0.05, 0.10, 0.15, 0.20]
OUT = Path(__file__).parent / "output" / "power.csv"


def expit(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def latent(rng: np.random.Generator, n_q: int, scenario: str) -> np.ndarray:
    """Logit miss probability without intercept, shape (Q, judge, generator, type)."""
    u = rng.normal(0, SD_QUESTION, (n_q, 1, 1, 1))
    v = rng.normal(0, SD_ANSWER, (n_q, 1, 2, 1))
    e = rng.normal(0, SD_ITEM, (n_q, 1 if scenario == "shared" else 2, 2, 5))
    return u + v + e + TYPE_EFFECTS[None, None, None, :] + JUDGE_EFFECTS[None, :, None, None]


def solve_intercept(base: float, scenario: str, rng: np.random.Generator) -> float:
    """Intercept whose mean miss rate over the random effects equals `base`."""
    draws = latent(rng, 20_000, scenario)
    lo, hi = -10.0, 10.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if expit(draws + mid).mean() < base else (lo, mid)
    return (lo + hi) / 2


def simulate(
    rng: np.random.Generator, n_q: int, scenario: str, intercept: float, delta: float
) -> np.ndarray:
    """Per-question sums, shape (Q, 8): misses then counts for (G,A) (G,B) (O,A) (O,B)."""
    p = expit(latent(rng, n_q, scenario) + intercept)
    own = np.zeros((1, 2, 2, 1))
    own[0, 0, 0, 0] = own[0, 1, 1, 0] = 1.0  # G judging A, O judging B
    p = np.clip(p + delta * own, 0.0, 1.0)
    present = rng.random((n_q, 1, 2, 5)) < P_APPLICABLE
    miss = (rng.random(p.shape) < p) & present
    misses = miss.sum(axis=3).reshape(n_q, 4)
    counts = np.broadcast_to(present.sum(axis=3), (n_q, 2, 2)).reshape(n_q, 4)
    return np.hstack([misses, counts]).astype(float)


def interaction(sums: np.ndarray) -> np.ndarray:
    """Δ from summed (…, 8) arrays; works on one row or a batch of bootstrap rows."""
    m = sums[..., :4] / np.maximum(sums[..., 4:], 1)
    ga, gb, oa, ob = m[..., 0], m[..., 1], m[..., 2], m[..., 3]
    return 0.5 * ((ga - gb) + (ob - oa))


def main() -> int:
    rng = np.random.default_rng(SEED)
    rows = []
    intercepts = {(sc, b): solve_intercept(b, sc, rng) for sc in SCENARIOS for b in GRID_BASE}
    for scenario, base, n_q, delta in product(SCENARIOS, GRID_BASE, GRID_Q, GRID_DELTA):
        intercept = intercepts[scenario, base]
        pos = equiv = 0
        widths = []
        for _ in range(N_SIMS):
            per_q = simulate(rng, n_q, scenario, intercept, delta)
            w = rng.multinomial(n_q, np.full(n_q, 1 / n_q), size=N_BOOT)
            boot = interaction(w @ per_q)
            lo95, hi95 = np.quantile(boot, [0.025, 0.975])
            lo90, hi90 = np.quantile(boot, [0.05, 0.95])
            pos += lo95 > 0
            equiv += (lo90 > -SESOI) and (hi90 < SESOI)
            widths.append(hi95 - lo95)
        rows.append({
            "scenario": scenario, "base_miss": base, "questions": n_q, "true_delta": delta,
            "p_detect": pos / N_SIMS, "p_equivalence": equiv / N_SIMS,
            "median_ci95_width": float(np.median(widths)),
        })  # fmt: skip
        print(
            f"{scenario} base={base:.2f} Q={n_q} delta={delta:.2f} "
            f"detect={pos / N_SIMS:.2f} equiv={equiv / N_SIMS:.2f} "
            f"ci95_width={np.median(widths):.3f}",
            flush=True,
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
