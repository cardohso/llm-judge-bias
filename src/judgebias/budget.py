"""A daily request budget per provider, so free tiers are never pushed past their quota.

Counts are persisted in a small JSON file (git-ignored). `spend` raises BudgetExceeded when the
day's budget is used up; the harness stops, and the run resumes the next day from the cache.
A day is a calendar date in `tz` (Gemini's quota resets at midnight Pacific).
"""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


class BudgetExceeded(RuntimeError):
    pass


class DailyBudget:
    def __init__(
        self,
        path: Path,
        limits: Mapping[str, int],
        tz: str = "America/Los_Angeles",
        now: Callable[[], datetime] = lambda: datetime.now(UTC),
    ):
        self.path = path
        self.limits = dict(limits)
        self._tz = ZoneInfo(tz)
        self._now = now

    def _today(self) -> str:
        return self._now().astimezone(self._tz).date().isoformat()

    def _load(self) -> dict[str, dict[str, int]]:
        try:
            data = json.loads(self.path.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        return data if isinstance(data, dict) else {}

    def used(self, provider: str) -> int:
        return self._load().get(self._today(), {}).get(provider, 0)

    def remaining(self, provider: str) -> int:
        return max(0, self.limits[provider] - self.used(provider))

    def spend(self, provider: str, n: int = 1) -> None:
        """Reserve n requests before sending them."""
        if provider not in self.limits:
            raise KeyError(f"no daily budget set for provider {provider!r}")
        data = self._load()
        today = data.setdefault(self._today(), {})
        if today.get(provider, 0) + n > self.limits[provider]:
            raise BudgetExceeded(
                f"{provider}: {today.get(provider, 0)}/{self.limits[provider]} requests used today"
            )
        today[provider] = today.get(provider, 0) + n
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, indent=1, sort_keys=True))
