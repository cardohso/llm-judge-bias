"""End-to-end: the analysis CLI's functions on a synthetic study (no real judge data)."""

import importlib.util
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def module():
    spec = importlib.util.spec_from_file_location("ra", ROOT / "analysis/run_analysis.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fake_study(n_q=12):
    rng = random.Random(0)
    items, runs = [], {(j, r): [] for j in "GOQ" for r in (1, 2, 3)}
    for q in range(n_q):
        qid = ("q" if q % 2 else "n") + f"{q:02d}"
        for g in "AB":
            items.append({"id": f"{qid}-{g}-CONTROL", "question": qid, "generator": g,
                          "type": "CONTROL", "subtype": "", "planted_index": None,
                          "sentences": ["a [1].", "b [1]."]})  # fmt: skip
            for t in ("ADD", "NUM", "CITE", "NEG", "QUAL"):
                items.append({"id": f"{qid}-{g}-{t}", "question": qid, "generator": g, "type": t,
                              "subtype": "in-context" if t == "NUM" else "", "planted_index": 2,
                              "sentences": ["a [1].", "b [2]."]})  # fmt: skip
    for i in items:
        for j in "GOQ":
            for r in (1, 2, 3):
                if i["id"] == "n00-A-CONTROL" and j == "Q" and r == 1:  # an invalid control
                    runs[j, r].append({"item": i["id"], "judge": j, "run": r, "content": ""})
                    continue
                own = (j, i["generator"]) in {("G", "A"), ("O", "B")}
                v = {1: rng.random() > 0.05, 2: rng.random() < (0.45 if own else 0.2)}
                if i["type"] == "CONTROL":
                    v[2] = rng.random() > 0.05
                body = {
                    "sentences": [{"id": k, "reason": "r", "supported": b} for k, b in v.items()]
                }
                runs[j, r].append(
                    {"item": i["id"], "judge": j, "run": r, "content": json.dumps(body)}
                )
    return items, runs


def test_full_pipeline_on_a_synthetic_study(tmp_path):
    ra = module()
    items, runs = fake_study()
    res = ra.analyse(items, runs)
    assert res["primary"]["delta"] > 0.1  # the planted self-preference is visible
    assert res["primary"]["decision"] in {"self-preference", "inconclusive"}
    assert res["S8_robustness"]["a_majority_of_3_runs"] is not None
    assert res["S4_run_to_run"]["G"]["across_runs"]["units"] > 0
    assert res["S2_false_alarm"]["Q"]["invalid_controls"] == 1
    md = ra.tables(res)
    assert "## Primary" in md and "## S8. Robustness" in md and "nan" not in md
    ra.charts(res, tmp_path)
    assert (tmp_path / "fig_delta_sp.svg").stat().st_size > 1000
    json.dumps(res, default=float)
