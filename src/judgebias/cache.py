"""Judge/generator reply cache keyed by the full request AND the run number.

goldpass's cache key is the request alone, so a second temperature-0 run would be a cache hit
and show zero run-to-run variance. Here `run` is part of the key: runs 2 and 3 are real calls,
and re-running run 1 is free.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from goldpass.cache import DiskCache, cache_key


class RunCache:
    def __init__(self, path: Path):
        self._disk = DiskCache(path)

    @staticmethod
    def key(request: dict[str, Any], run: int) -> str:
        return cache_key({"run": run, "request": request})

    def get(self, request: dict[str, Any], run: int) -> str | None:
        return self._disk.get(self.key(request, run))

    def set(self, request: dict[str, Any], run: int, reply: str) -> None:
        self._disk.set(self.key(request, run), reply)

    def close(self) -> None:
        self._disk.close()
