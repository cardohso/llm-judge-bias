# llm-judge-bias

[![CI](https://github.com/cardohso/llm-judge-bias/actions/workflows/ci.yml/badge.svg)](https://github.com/cardohso/llm-judge-bias/actions/workflows/ci.yml)

A small, pre-registered experiment: **do LLM judges forgive errors in answers written by their own model?**

**Status: runs in progress, no result yet.** The pre-registration ([`docs/PREREGISTRATION.md`](docs/PREREGISTRATION.md), commit `1749db0`) was public before any model was called. The method, deviations and limitations are in [`REPORT.md`](REPORT.md); its results section stays empty until the judge runs finish. The analysis script refuses to compute any estimate until run 1 is complete for all three judges.

## In 30 seconds

- 34 questions on EU railway law, answered by two models (Gemini 3.5 Flash-Lite and gpt-oss-120b) from identical passages.
- 306 copies of those answers with one planted error each (added claim, changed number, wrong citation, reversed requirement, dropped qualifier) and 68 untouched controls.
- Three judges (Gemini, gpt-oss, Qwen) rate every sentence against the passages it cites, three times each, temperature 0.
- Question: is a judge more likely to miss an error in its own model's answers? Primary test, bootstrap by question, "no effect" defined in advance as a 90% interval inside ±10 points.
- Free-tier APIs only. One domain, one reviewer, small n: see the limitations.

## Layout

| Path | What |
|---|---|
| `docs/PREREGISTRATION.md` | Hypotheses, materials, prompts, outcomes, decision rules, power simulation |
| `questions/`, `contexts/` | The 40 drafted questions (34 kept) and their fixed contexts |
| `generation/`, `answers/` | Generation prompt, base answers, review sheets and outcomes |
| `perturbations/` | Planted errors (hand-written source and generator), review sheet and outcome |
| `judges/`, `src/judgebias/` | Judge prompt, harness, cache, daily budget, scoring and statistics |
| `runs/` | Raw judge replies, one file per run and judge |
| `analysis/` | Power simulation and `run_analysis.py`, which produces every table and chart |

## Reproduce it

Needs [uv](https://docs.astral.sh/uv/) and Python 3.11+. No API key is needed to reproduce the analysis.

```bash
git clone https://github.com/cardohso/llm-judge-bias && cd llm-judge-bias
uv sync
uv run pytest                              # judges are mocked; no network
uv run python analysis/run_analysis.py     # tables and charts from runs/, once run 1 is complete
```

To re-run the judges (calls free-tier APIs), copy `.env.example` to `.env`, fill in your own keys, and run `uv run python judges/run.py --run 1`. Daily request budgets are in `src/judgebias/models.py`; finished replies are cached in `.state/`, so a rerun resumes where it stopped.

MIT licence.
