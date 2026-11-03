"""Providers, models and daily request budgets (docs/PREREGISTRATION.md, sections 4.4 and 5).

Free tiers only. The daily limits are conservative request counts, not the providers' published
quotas, which are not all visible for a new key. Raise them here, in a commit, if a provider
allows more.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Provider:
    name: str
    base_url: str
    key_env: str
    min_interval_s: float  # shared pace: 5 requests/min is 12 s
    daily_requests: int
    host: str = ""


@dataclass(frozen=True)
class Model:
    label: str  # A, B for generators; G, O, Q for judges
    provider: str
    model_id: str
    family: str
    extra_body: dict[str, Any] = field(default_factory=dict)


PROVIDERS: dict[str, Provider] = {
    "gemini": Provider(
        "gemini",
        "https://generativelanguage.googleapis.com/v1beta/openai",
        "GEMINI_API_KEY",
        min_interval_s=4.0,
        daily_requests=400,  # 100 until 2026-11-03; no 429 seen in ~200 calls (REPORT.md, 4.6)
    ),
    "cerebras": Provider(
        "cerebras", "https://api.cerebras.ai/v1", "CEREBRAS_API_KEY", 12.5, daily_requests=300
    ),
    "groq": Provider(  # contingency only
        "groq", "https://api.groq.com/openai/v1", "GROQ_API_KEY", 2.0, daily_requests=300
    ),
}

GEMINI_FLASH_LITE = Model("A", "gemini", "gemini-3.5-flash-lite", "google")
GPT_OSS = Model("B", "cerebras", "gpt-oss-120b", "openai", {"reasoning_effort": "low"})
QWEN = Model("Q", "cerebras", "qwen-3.8-27b", "alibaba")

GENERATORS = {"A": GEMINI_FLASH_LITE, "B": GPT_OSS}
JUDGES = {
    "G": Model("G", "gemini", "gemini-3.5-flash-lite", "google"),
    "O": Model("O", "cerebras", "gpt-oss-120b", "openai", {"reasoning_effort": "low"}),
    "Q": QWEN,
}
