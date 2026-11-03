import json
import math

import numpy as np
import pytest

from judgebias.analysis import (
    Clustered,
    Outcome,
    _cohen,
    agreement,
    cohen_kappa_sums,
    decide,
    holm,
    interaction,
    mcnemar_exact,
    own_vs_other,
    rate,
)


def o(item="i", q="q1", gen="A", typ="NUM", judge="G", run=1, verdicts=None, planted=1, n=2):
    return Outcome(
        item,
        q,
        gen,
        typ,
        "",
        judge,
        run,
        n,
        {1: True, 2: True} if verdicts is None else verdicts,
        planted,
    )


def test_outcome_definitions():
    assert o(verdicts={1: True, 2: True}).miss is True
    assert o(verdicts={1: False, 2: True}).miss is False
    assert o(verdicts={2: True}).invalid and o(verdicts={2: True}).miss is None
    assert o(verdicts={1: True, 2: False}).wrong_reason is True
    assert o(verdicts={1: True, 2: False}).answer_miss is False
    ctrl = o(typ="CONTROL", planted=None, verdicts={1: True, 2: False})
    assert ctrl.false_alarm is True and ctrl.miss is None and ctrl.unsupported_sentences == 1


def synthetic(rates, n_q=40, per_cell=5, seed=1):
    """Miss indicators per cell with exact proportions in every question."""
    rows = []
    for qi in range(n_q):
        for (j, g), r in rates.items():
            k = round(r * per_cell)
            for t in range(per_cell):
                miss = t < k
                rows.append(o(f"q{qi}-{g}-{t}", f"q{qi}", g, "NUM", j, 1, {1: miss}, 1, 1))
    return rows


def test_interaction_recovers_a_known_effect_with_zero_width_ci():
    rows = synthetic({("G", "A"): 0.6, ("G", "B"): 0.2, ("O", "A"): 0.2, ("O", "B"): 0.2})
    boot = Clustered([f"q{i}" for i in range(40)], n_boot=500)
    res = interaction(boot, rows)
    assert res["delta"] == pytest.approx(0.2)
    assert res["ci95"][0] == pytest.approx(0.2) and res["ci95"][1] == pytest.approx(0.2)
    assert res["cells"]["GA"] == pytest.approx(0.6) and res["n"]["OB"] == 200
    assert res["pooled_miss"] == pytest.approx(0.3)


def test_interaction_cancels_judge_and_generator_main_effects():
    rows = synthetic({("G", "A"): 0.8, ("G", "B"): 0.6, ("O", "A"): 0.4, ("O", "B"): 0.2})
    res = interaction(Clustered([f"q{i}" for i in range(40)], n_boot=200), rows)
    assert res["delta"] == pytest.approx(0.0, abs=1e-12)


def test_controls_and_invalid_are_excluded():
    rows = synthetic({("G", "A"): 0.6, ("G", "B"): 0.2, ("O", "A"): 0.2, ("O", "B"): 0.2})
    rows.append(o("c", "q0", "A", "CONTROL", "G", 1, {1: True}, None, 1))
    rows.append(o("x", "q0", "A", "NUM", "G", 1, {2: True}, 1, 2))
    res = interaction(Clustered([f"q{i}" for i in range(40)], n_boot=100), rows)
    assert res["n"]["GA"] == 200


def base(delta, ci95, ci90, pooled=0.3):
    return {"delta": delta, "ci95": ci95, "ci90": ci90, "pooled_miss": pooled}


@pytest.mark.parametrize(
    "res,want",
    [
        (base(0, (-0.01, 0.01), (-0.01, 0.01), pooled=0.02), "not testable (floor or ceiling)"),
        (base(0, (-0.01, 0.01), (-0.01, 0.01), pooled=0.97), "not testable (floor or ceiling)"),
        (base(0.2, (0.05, 0.35), (0.07, 0.33)), "self-preference"),
        (base(0.04, (0.01, 0.08), (0.015, 0.07)), "self-preference smaller than 10 points"),
        (base(-0.2, (-0.35, -0.05), (-0.33, -0.07)), "reverse preference"),
        (base(0.0, (-0.08, 0.08), (-0.06, 0.06)), "no effect of 10 points or more"),
        (base(0.05, (-0.05, 0.15), (-0.03, 0.13)), "inconclusive"),
    ],
)
def test_decision_rules_in_order(res, want):
    assert decide(res) == want


def test_rate_ci_brackets_point():
    boot = Clustered([f"q{i}" for i in range(20)], n_boot=500)
    pairs = [(f"q{i}", i % 4 == 0) for i in range(20) for _ in range(3)]
    r = rate(boot, pairs)
    assert r["rate"] == pytest.approx(0.25) and r["ci95"][0] <= 0.25 <= r["ci95"][1]


def test_cohen_kappa_matches_hand_computation():
    # 20 units: 8 both T, 2 a-only, 3 b-only, 7 both F -> po=.75, pe=.5*.55+.5*.45=.5, kappa=.5
    a = np.array([1] * 8 + [1] * 2 + [0] * 3 + [0] * 7, bool)
    b = np.array([1] * 8 + [0] * 2 + [1] * 3 + [0] * 7, bool)
    s = cohen_kappa_sums(a, b).sum(axis=0)
    assert float(_cohen(s[None, :])[0]) == pytest.approx(0.5)


def test_agreement_perfect_is_one():
    rows = [o(f"i{k}", f"q{k % 5}", "A", "NUM", j, 1, {1: k % 2 == 0, 2: True}, 1)
            for k in range(30) for j in "GOQ"]  # fmt: skip
    res = agreement(
        Clustered([f"q{i}" for i in range(5)], n_boot=100), rows, "GOQ", lambda x: x.judge
    )
    assert res["units"] == 60
    assert res["fleiss_kappa"][0] == pytest.approx(1.0) and res["kappa_GO"][0] == pytest.approx(1.0)
    assert res["percent_agreement"]["rate"] == 1.0


def test_mcnemar_and_holm():
    assert mcnemar_exact(0, 5) == pytest.approx(0.0625)
    assert mcnemar_exact(3, 3) == 1.0 and mcnemar_exact(0, 0) == 1.0
    assert holm({"G": 0.01, "O": 0.04}) == {"G": 0.02, "O": 0.04}
    assert holm({"G": 0.03, "O": 0.02}) == {"O": 0.04, "G": 0.04}


def test_own_vs_other_counts_discordant_matched_pairs():
    rows = [
        o("1", "q1", "A", "NUM", "G", 1, {1: True}, 1, 1),
        o("2", "q1", "B", "NUM", "G", 1, {1: False}, 1, 1),
        o("3", "q2", "A", "NEG", "G", 1, {1: True}, 1, 1),
        o("4", "q2", "B", "NEG", "G", 1, {1: True}, 1, 1),
        o("5", "q3", "A", "ADD", "G", 1, {1: True}, 1, 1),
    ]  # fmt: skip
    r = own_vs_other(rows, "G", "A")
    assert (r["pairs"], r["own_only"], r["other_only"]) == (2, 1, 0)
    assert math.isclose(r["p"], 1.0)
    json.dumps(r)


def test_empty_verdicts_make_a_control_invalid_not_a_clean_pass():
    ctrl = o(typ="CONTROL", planted=None, verdicts={})
    assert ctrl.invalid and ctrl.false_alarm is None
    assert o(verdicts={}).invalid
