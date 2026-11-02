"""Every table and chart in the report, from the raw judge replies in runs/. No network.

    uv run python analysis/run_analysis.py              # refuses until run 1 is complete
    uv run python analysis/run_analysis.py --status     # completion counts only

Effect estimates are computed only once run 1 is complete for all three judges, so nobody (the
author included) sees the primary estimate on partial data. Writes analysis/output/results.json,
analysis/output/tables.md and two SVG charts.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from judgebias.analysis import (  # noqa: E402
    TYPES,
    Clustered,
    Outcome,
    agreement,
    decide,
    holm,
    interaction,
    outcomes,
    own_vs_other,
    rate,
)

OUT = ROOT / "analysis/output"
JUDGE_NAMES = {"G": "gemini-3.5-flash-lite", "O": "gpt-oss-120b", "Q": "qwen-3.8-27b"}
GEN_NAMES = {"A": "gemini-3.5-flash-lite", "B": "gpt-oss-120b"}
# validated categorical slots 1-3 (dataviz reference palette, light surface)
COLORS = {"G": "#2a78d6", "O": "#eb6834", "Q": "#1baf7a"}
MARKERS = {"G": "o", "O": "s", "Q": "D"}


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []


def load():
    items = jsonl(ROOT / "perturbations/perturbations.jsonl")
    runs = {(j, r): jsonl(ROOT / f"runs/run{r}_{j}.jsonl") for j in "GOQ" for r in (1, 2, 3)}
    return items, runs


def status(items, runs) -> dict:
    return {f"run{r}_{j}": f"{len(runs[j, r])}/{len(items)}" for (j, r) in sorted(runs)}


def fmt_ci(x) -> str:
    lo, hi = x
    return "n/a" if not (math.isfinite(lo) and math.isfinite(hi)) else f"{lo:.2f} to {hi:.2f}"


def pct(x: float) -> str:
    return "n/a" if not math.isfinite(x) else f"{x:.2f}"


def rate_row(r: dict) -> str:
    return f"{r['k']}/{r['n']} | {pct(r['rate'])} | {fmt_ci(r['ci95'])}"


def diff_rates(boot: Clustered, rows, judge: str) -> dict:
    """S9: m_j(A) − m_j(B)."""
    pairs = []
    for o in rows:
        if o.judge == judge and o.miss is not None:
            vec = [0.0] * 4
            k = 0 if o.generator == "A" else 2
            vec[k], vec[k + 1] = float(o.miss), 1.0
            pairs.append((o.question, vec))

    def stat(s):
        with np.errstate(invalid="ignore", divide="ignore"):
            return s[..., 0] / s[..., 1] - s[..., 2] / s[..., 3]

    point, ci95, _ = boot.estimate(boot.sums(pairs, 4), stat)
    return {"diff": point, "ci95": ci95}


def majority(rows_by_run: dict[int, list[Outcome]]) -> list[Outcome]:
    """S8a: per (item, judge), each sentence's majority verdict across runs 1-3."""
    grouped = defaultdict(list)
    for rows in rows_by_run.values():
        for o in rows:
            grouped[o.item, o.judge].append(o)
    out = []
    for group in grouped.values():
        if len(group) < 3:
            continue
        sentences = set().union(*(o.verdicts for o in group))
        verdicts = {}
        for s in sentences:
            votes = [o.verdicts[s] for o in group if s in o.verdicts]
            if len(votes) >= 2:  # a 1-1 tie (one run skipped it) falls back to run 1
                tie = sum(votes) * 2 == len(votes)
                verdicts[s] = (
                    group[0].verdicts.get(s, False) if tie else sum(votes) * 2 > len(votes)
                )
        out.append(replace(group[0], verdicts=verdicts, run=0))
    return out


def analyse(items, runs) -> dict:
    questions = sorted({i["question"] for i in items})
    boot = Clustered(questions)
    by_run = {r: [o for j in "GOQ" for o in outcomes(items, runs[j, r])] for r in (1, 2, 3)}
    run1 = by_run[1]
    res: dict = {"questions": len(questions), "items": len(items), "status": status(items, runs)}

    # primary (8.1-8.3)
    primary = interaction(boot, run1)
    primary["decision"] = decide(primary)
    res["primary"] = primary

    # S1 miss rate per judge x type, and NUM subtypes; S2 false alarms; invalid counts
    s1, s2 = {}, {}
    for j in "GOQ":
        mine = [o for o in run1 if o.judge == j]
        s1[j] = {t: rate(boot, [(o.question, o.miss) for o in mine if o.type == t and o.miss is not None])
                 for t in TYPES}  # fmt: skip
        s1[j]["all"] = rate(boot, [(o.question, o.miss) for o in mine if o.miss is not None])
        for sub in ("in-context", "out-of-context"):
            s1[j][f"NUM {sub}"] = rate(
                boot, [(o.question, o.miss) for o in mine if o.type == "NUM" and o.subtype == sub
                       and o.miss is not None])  # fmt: skip
        s1[j]["invalid"] = sum(o.invalid for o in mine)
        s1[j]["wrong_reason"] = rate(
            boot, [(o.question, o.wrong_reason) for o in mine if o.wrong_reason is not None]
        )
        controls = [o for o in mine if o.is_control]
        s2[j] = {
            "answer": rate(boot, [(o.question, o.false_alarm) for o in controls]),
            "sentence": rate(boot, [(o.question, not v) for o in controls for v in o.verdicts.values()]),
        }  # fmt: skip
    res["S1_miss_by_type"], res["S2_false_alarm"] = s1, s2

    # S3 agreement between judges (run 1), all sentences and planted only
    res["S3_agreement"] = {
        "all": agreement(boot, run1, "GOQ", lambda o: o.judge),
        "planted": agreement(boot, run1, "GOQ", lambda o: o.judge, planted_only=True),
    }

    # S4 run-to-run variation (needs runs 2-3)
    s4 = {}
    for j in "GOQ":
        rows = [o for r in (1, 2, 3) for o in by_run[r] if o.judge == j]
        s4[j] = {
            "across_runs": agreement(boot, rows, (1, 2, 3), lambda o: o.run),
            "miss_by_run": {r: rate(boot, [(o.question, o.miss) for o in by_run[r]
                                            if o.judge == j and o.miss is not None])
                            for r in (1, 2, 3)},
        }  # fmt: skip
    res["S4_run_to_run"] = s4

    # S5 same-model judge vs neutral judge; S6 per type; S9 generator difficulty (judge Q)
    g_vs_q = interaction(boot, run1, judges=("G", "Q"))
    q_vs_o = interaction(boot, run1, judges=("Q", "O"))
    res["S5_vs_neutral"] = {
        "G": {"diff": 2 * g_vs_q["delta"], "ci95": tuple(2 * x for x in g_vs_q["ci95"])},
        "O": {"diff": 2 * q_vs_o["delta"], "ci95": tuple(2 * x for x in q_vs_o["ci95"])},
    }
    res["S6_by_type"] = {t: interaction(boot, [o for o in run1 if o.type == t]) for t in TYPES}
    res["S9_generator_difficulty_Q"] = diff_rates(boot, run1, "Q")

    # S7 own vs other within judge, exact McNemar, Holm over G and O
    s7 = {"G": own_vs_other(run1, "G", "A"), "O": own_vs_other(run1, "O", "B")}
    adj = holm({j: s7[j]["p"] for j in s7})
    for j in s7:
        s7[j]["p_holm"] = adj[j]
    res["S7_own_vs_other"] = s7

    # S8 robustness of the primary estimate
    flagged = {(o.question, o.generator, o.judge) for o in run1 if o.is_control and o.false_alarm}
    s8 = {
        "a_majority_of_3_runs": interaction(boot, majority(by_run)) if all(by_run.values()) else None,
        "b_invalid_as_miss": interaction(boot, run1, lambda o: True if o.invalid else o.miss),
        "b_invalid_as_catch": interaction(boot, run1, lambda o: False if o.invalid else o.miss),
        "c_answer_level": interaction(boot, run1, lambda o: o.answer_miss),
        "d_without_CITE": interaction(boot, [o for o in run1 if o.type != "CITE"]),
        "e_original_questions": interaction(boot, [o for o in run1 if o.question.startswith("q")]),
        "e_new_questions": interaction(boot, [o for o in run1 if o.question.startswith("n")]),
        "f_without_flagged_controls": interaction(
            boot, [o for o in run1 if (o.question, o.generator, o.judge) not in flagged]),
    }  # fmt: skip
    res["S8_robustness"] = s8
    return res


def tables(res: dict) -> str:
    p = res["primary"]
    L = ["## Primary (run 1, judges G and O)", "",
         "| Cell | Miss rate | Copies |", "|---|---|---|"]  # fmt: skip
    for c, name in (
        ("GA", "G on A (own)"),
        ("GB", "G on B"),
        ("OA", "O on A"),
        ("OB", "O on B (own)"),
    ):
        L.append(f"| {name} | {pct(p['cells'][c])} | {p['n'][c]} |")
    L += ["", f"**Δ_SP = {pct(p['delta'])}** (95% CI {fmt_ci(p['ci95'])}; 90% CI "
          f"{fmt_ci(p['ci90'])}). Pooled miss rate {pct(p['pooled_miss'])}. "
          f"**Decision: {p['decision']}.**", ""]  # fmt: skip

    L += ["## S1. Miss rate by judge and error type (run 1)", "",
          "| Judge | Type | Missed/n | Rate | 95% CI |", "|---|---|---|---|---|"]  # fmt: skip
    for j, rows in res["S1_miss_by_type"].items():
        for t in (*TYPES, "NUM in-context", "NUM out-of-context", "all"):
            L.append(f"| {j} | {t} | {rate_row(rows[t])} |")
    L += ["", "| Judge | Invalid outcomes | Caught for the wrong reason (rate, 95% CI) |",
          "|---|---|---|"]  # fmt: skip
    for j, rows in res["S1_miss_by_type"].items():
        w = rows["wrong_reason"]
        L.append(
            f"| {j} | {rows['invalid']} | {pct(w['rate'])} ({fmt_ci(w['ci95'])}), n={w['n']} |"
        )

    L += ["", "## S2. False alarms on controls (run 1)", "",
          "| Judge | Level | Flagged/n | Rate | 95% CI |", "|---|---|---|---|---|"]  # fmt: skip
    for j, r in res["S2_false_alarm"].items():
        L.append(f"| {j} | answer | {rate_row(r['answer'])} |")
        L.append(f"| {j} | sentence | {rate_row(r['sentence'])} |")

    L += ["", "## S3. Agreement between judges (run 1)", "",
          "| Units | n | Fleiss κ | κ G–O | κ G–Q | κ O–Q | % agree |",
          "|---|---|---|---|---|---|---|"]  # fmt: skip
    for name, a in res["S3_agreement"].items():
        if a["units"]:
            k = lambda key, a=a: f"{pct(a[key][0])} ({fmt_ci(a[key][1])})"  # noqa: E731
            L.append(f"| {name} | {a['units']} | {k('fleiss_kappa')} | {k('kappa_GO')} | "
                     f"{k('kappa_GQ')} | {k('kappa_OQ')} | {pct(a['percent_agreement']['rate'])} |")  # fmt: skip

    L += ["", "## S4. Run-to-run variation", "",
          "| Judge | Units in all 3 runs | Verdicts differing | Fleiss κ across runs | "
          "Miss rate run 1 / 2 / 3 |", "|---|---|---|---|---|"]  # fmt: skip
    for j, r in res["S4_run_to_run"].items():
        a = r["across_runs"]
        runs = " / ".join(pct(r["miss_by_run"][k]["rate"]) for k in (1, 2, 3))
        if a["units"]:
            L.append(f"| {j} | {a['units']} | {rate_row(a['share_differing'])} | "
                     f"{pct(a['fleiss_kappa'][0])} ({fmt_ci(a['fleiss_kappa'][1])}) | {runs} |")  # fmt: skip
        else:
            L.append(f"| {j} | 0 | not available | not available | {runs} |")

    s5 = res["S5_vs_neutral"]
    L += ["", "## S5, S6, S9. Contrasts", "", "| Contrast | Estimate | 95% CI |", "|---|---|---|",
          f"| S5: G own-vs-other, minus Q's | {pct(s5['G']['diff'])} | {fmt_ci(s5['G']['ci95'])} |",
          f"| S5: O own-vs-other, minus Q's | {pct(s5['O']['diff'])} | {fmt_ci(s5['O']['ci95'])} |"]  # fmt: skip
    for t, r in res["S6_by_type"].items():
        L.append(f"| S6: Δ_SP, {t} only | {pct(r['delta'])} | {fmt_ci(r['ci95'])} |")
    s9 = res["S9_generator_difficulty_Q"]
    L.append(f"| S9: m_Q(A) − m_Q(B) | {pct(s9['diff'])} | {fmt_ci(s9['ci95'])} |")

    L += ["", "## S7. Own vs other generator within a judge (exact McNemar, Holm)", "",
          "| Judge | Matched pairs | Missed on own only | Missed on other only | p | p (Holm) |",
          "|---|---|---|---|---|---|"]  # fmt: skip
    for j, r in res["S7_own_vs_other"].items():
        L.append(f"| {j} | {r['pairs']} | {r['own_only']} | {r['other_only']} | "
                 f"{r['p']:.3f} | {r['p_holm']:.3f} |")  # fmt: skip

    L += ["", "## S8. Robustness of Δ_SP", "", "| Variant | Δ_SP | 95% CI | Decision rule result |",
          "|---|---|---|---|"]  # fmt: skip
    for name, r in res["S8_robustness"].items():
        if r is None:
            L.append(f"| {name} | not available (runs 2-3 incomplete) | | |")
        else:
            L.append(f"| {name} | {pct(r['delta'])} | {fmt_ci(r['ci95'])} | {decide(r)} |")
    return "\n".join(L) + "\n"


def charts(res: dict, out: Path = OUT) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                         "svg.hashsalt": "judgebias", "axes.edgecolor": "#8a8a85",
                         "text.color": "#2b2b29", "axes.labelcolor": "#2b2b29"})  # fmt: skip

    # 1. Δ_SP: primary and robustness variants, with the ±10-point band
    rows = [("Primary (run 1)", res["primary"])] + [
        (k.replace("_", " "), v) for k, v in res["S8_robustness"].items() if v is not None
    ]
    fig, ax = plt.subplots(figsize=(7, 0.42 * len(rows) + 1.2))
    ax.axvspan(
        -0.10, 0.10, color="#e8e7e2", zorder=0, label="±10 points (smallest effect of interest)"
    )
    ax.axvline(0, color="#8a8a85", lw=1)
    for y, (_, r) in enumerate(reversed(rows)):
        lo, hi = r["ci95"]
        ax.plot([lo, hi], [y, y], color="#2a78d6", lw=2, solid_capstyle="round")
        ax.plot(r["delta"], y, "o", color="#2a78d6", ms=8, mec="#fcfcfb", mew=2)
    ax.set_yticks(range(len(rows)), [n for n, _ in reversed(rows)])
    ax.set_xlabel("Δ_SP: extra miss rate on the judge's own model's answers (95% CI)")
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "fig_delta_sp.svg")
    plt.close(fig)

    # 2. miss rate by judge and error type (S1)
    cats = [*TYPES, "all"]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for k, j in enumerate("GOQ"):
        for x, t in enumerate(cats):
            r = res["S1_miss_by_type"][j][t]
            if not math.isfinite(r["rate"]):
                continue
            xx = x + (k - 1) * 0.22
            ax.plot([xx, xx], r["ci95"], color=COLORS[j], lw=2, solid_capstyle="round")
            ax.plot(xx, r["rate"], MARKERS[j], color=COLORS[j], ms=7, mec="#fcfcfb", mew=1.5,
                    label=f"{j}: {JUDGE_NAMES[j]}" if x == 0 else None)  # fmt: skip
    ax.set_xticks(range(len(cats)), cats)
    ax.set_ylabel("Miss rate (95% CI)")
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", color="#e8e7e2", lw=0.8)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(out / "fig_miss_by_type.svg")
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true", help="completion counts only")
    args = ap.parse_args()
    items, runs = load()
    st = status(items, runs)
    print(json.dumps(st, indent=1))
    if args.status:
        return 0
    if any(len(runs[j, 1]) < len(items) for j in "GOQ"):
        print("Run 1 is not complete for every judge: no estimates computed (by design).")
        return 2
    res = analyse(items, runs)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(res, indent=1, default=float) + "\n")
    (OUT / "tables.md").write_text(tables(res))
    charts(res)
    print(f"Decision on H1: {res['primary']['decision']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
