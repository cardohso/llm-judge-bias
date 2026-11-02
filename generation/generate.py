"""Generate the base answers. This makes API calls (free tiers; daily budget in models.py).

    uv run python generation/generate.py

Reads contexts/contexts.jsonl and .env; writes answers/answers.jsonl. Safe to re-run: replies
are cached in .state/cache.sqlite, and a budget stop resumes the next day.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_env(path: Path) -> None:
    import os

    for line in path.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def main() -> int:
    from judgebias.budget import BudgetExceeded, DailyBudget
    from judgebias.cache import RunCache
    from judgebias.generate import generate_all
    from judgebias.llm import ChatClient, ChatError
    from judgebias.models import GENERATORS, PROVIDERS

    load_env(ROOT / ".env")
    spec = importlib.util.spec_from_file_location("gen_prompts", ROOT / "generation/prompts.py")
    prompts = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prompts)

    cache = RunCache(ROOT / ".state/cache.sqlite")
    budget = DailyBudget(
        ROOT / ".state/budget.json", {n: p.daily_requests for n, p in PROVIDERS.items()}
    )
    clients = {label: ChatClient(m, cache, budget, log=print) for label, m in GENERATORS.items()}
    contexts = [
        json.loads(line) for line in (ROOT / "contexts/contexts.jsonl").read_text().splitlines()
    ]
    try:
        rows = generate_all(contexts, clients, prompts.GENERATE)
    except BudgetExceeded as e:
        print(f"Stopped: {e}. Re-run after the daily reset; finished replies are cached.")
        return 3
    except ChatError as e:
        print(f"Stopped: {e}")
        return 1
    out = ROOT / "answers/answers.jsonl"
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"wrote {len(rows)} answers to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
