"""Run judges over the frozen items. This makes API calls (free tiers, daily budget in
src/judgebias/models.py) unless --dry-run. Run 1 must finish for every judge before runs 2-3.

    uv run python judges/run.py --run 1 --judges G O Q [--dry-run]

Raw replies go to runs/run<r>_<judge>.jsonl (rewritten from the cache after every invocation, so
a budget stop leaves a valid partial file). Safe to re-run: cached replies cost nothing.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text().splitlines()]


def main() -> int:
    from judgebias.budget import BudgetExceeded, DailyBudget
    from judgebias.cache import RunCache
    from judgebias.judging import judge_items
    from judgebias.llm import ChatClient, ChatError
    from judgebias.models import JUDGES, PROVIDERS

    ap = argparse.ArgumentParser()
    ap.add_argument("--run", type=int, required=True, choices=[1, 2, 3])
    ap.add_argument("--judges", nargs="+", default=["G", "O", "Q"], choices=sorted(JUDGES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, help="only the first N items of the seeded order")
    args = ap.parse_args()

    spec = importlib.util.spec_from_file_location("jp", ROOT / "judges/prompts.py")
    prompts = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prompts)
    items = jsonl(ROOT / "perturbations/perturbations.jsonl")
    contexts = {c["id"]: c for c in jsonl(ROOT / "contexts/contexts.jsonl")}
    load_env(ROOT / ".env")
    cache = RunCache(ROOT / ".state/cache.sqlite")
    budget = DailyBudget(
        ROOT / ".state/budget.json", {n: p.daily_requests for n, p in PROVIDERS.items()}
    )
    if args.run > 1:
        for j in JUDGES:  # section 5.2: run 1 is complete for all judges first
            done = ROOT / f"runs/run1_{j}.jsonl"
            if not done.exists() or len(jsonl(done)) < len(items):
                print(f"Run 1 is not complete for judge {j}; finish it before run {args.run}.")
                return 2
    worst = (
        0  # a stop for one judge (budget, error) must not skip the others: their providers differ
    )
    for j in args.judges:
        model = JUDGES[j]
        client = ChatClient(model, cache, budget, log=print)
        if args.dry_run:
            from judgebias.judging import run_order, user_message

            todo = [
                i for i in items
                if cache.get(client.request(prompts.SYSTEM, user_message(
                    prompts.USER_TEMPLATE, contexts[i["question"]]["question"],
                    contexts[i["question"]]["passages"], i["sentences"])), args.run) is None
            ]  # fmt: skip
            left = budget.remaining(model.provider)
            print(f"{j} {model.model_id}: {len(todo)} calls to make, "
                  f"{left} left in today's {model.provider} budget "
                  f"(~{-(-len(todo) // max(left, 1))} day(s))")  # fmt: skip
            run_order(items, j, args.run)
            continue
        rows: dict[str, dict] = {}
        out = ROOT / f"runs/run{args.run}_{j}.jsonl"
        if out.exists():
            rows = {r["item"]: r for r in jsonl(out)}
        try:
            judge_items(
                items,
                contexts,
                client,
                j,
                args.run,
                prompts.SYSTEM,
                prompts.USER_TEMPLATE,
                lambda r, rows=rows: rows.__setitem__(r["item"], r),
                limit=args.limit,
            )
        except BudgetExceeded as e:
            print(f"Stopped: {e}. Re-run after the daily reset; finished replies are cached.")
            worst = max(worst, 3)
        except ChatError as e:
            print(f"Stopped: {e}")
            worst = max(worst, 1)
        finally:
            out.parent.mkdir(exist_ok=True)
            ordered = [
                rows[i["id"]] for i in sorted(items, key=lambda i: i["id"]) if i["id"] in rows
            ]
            out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in ordered))
            print(f"{j}: {len(ordered)}/{len(items)} rows in {out.relative_to(ROOT)}")
    return worst


if __name__ == "__main__":
    sys.exit(main())
