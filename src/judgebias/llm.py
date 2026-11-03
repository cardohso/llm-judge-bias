"""One OpenAI-compatible chat call with a disk cache, a daily budget and retries.

Every reply is cached with its full request, the provider's response metadata (model, id,
fingerprint, usage) and a timestamp, so `runs/` can reproduce the analysis offline. Retries and
pacing come from goldpass. The daily budget is spent per HTTP attempt, retries included.
"""

from __future__ import annotations

import json
import os
import time
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import httpx
from goldpass.ratelimit import RateLimiter
from goldpass.retry import GaveUp, RetryableError, RetryPolicy, call_with_retry, parse_retry_after

from judgebias.budget import DailyBudget
from judgebias.cache import RunCache
from judgebias.models import PROVIDERS, Model, Provider

RETRY_STATUS = {408, 425, 429, 500, 502, 503, 504}
MAX_TOKENS = 4096
MALFORMED_RETRIES = 2


class ChatError(RuntimeError):
    pass


@dataclass(frozen=True)
class Reply:
    content: str
    meta: dict[str, Any]
    cached: bool


class ChatClient:
    def __init__(
        self,
        model: Model,
        cache: RunCache,
        budget: DailyBudget,
        api_key: str | None = None,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        retry: RetryPolicy | None = None,
        log: Callable[[str], None] | None = None,
    ):
        self.model = model
        self.provider: Provider = PROVIDERS[model.provider]
        self.cache, self.budget, self._log = cache, budget, log
        key = api_key if api_key is not None else os.environ.get(self.provider.key_env, "")
        self._client = httpx.Client(
            headers={"Authorization": f"Bearer {key}"} if key else {},
            timeout=120.0,
            transport=transport,
        )
        self._sleep = sleep
        self._retry = retry or RetryPolicy(attempts=6, backoff_s=5.0, max_wait_s=120.0)
        self.limiter = RateLimiter(self.provider.min_interval_s, sleep=sleep)
        self.calls = 0  # HTTP attempts actually sent

    def request(self, system: str, user: str) -> dict[str, Any]:
        return {
            "model": self.model.model_id,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": 0,
            "max_tokens": MAX_TOKENS,
            "response_format": {"type": "json_object"},
            **self.model.extra_body,
        }

    def chat(
        self,
        system: str,
        user: str,
        run: int,
        *,
        validate: Callable[[str], Any],
        record_invalid: bool = False,
    ) -> Reply:
        """Cached by (request, run). `validate` raises ValueError for a reply to retry. After
        the retries a malformed reply raises ChatError, or with `record_invalid` is stored and
        returned flagged `meta["invalid"]` (pre-registration section 5.2: the item's outcome is
        then "invalid" and the run goes on)."""
        payload = self.request(system, user)
        if (hit := self.cache.get(payload, run)) is not None:
            stored = json.loads(hit)
            return Reply(stored["content"], stored["meta"], cached=True)
        for attempt in range(MALFORMED_RETRIES + 1):
            content, meta = self._post(payload)
            try:
                validate(content)
            except ValueError as e:
                if attempt < MALFORMED_RETRIES:
                    continue
                if not record_invalid:
                    raise ChatError(f"malformed reply after retries: {e}: {content[:200]!r}") from e
                meta |= {"invalid": f"{e}", "attempts": attempt + 1}
            meta |= {"run": run, "request": payload, "provider": self.provider.name}
            self.cache.set(payload, run, json.dumps({"content": content, "meta": meta}))
            return Reply(content, meta, cached=False)
        raise AssertionError("unreachable")

    def _post(self, payload: dict[str, Any]) -> tuple[str, dict[str, Any]]:
        url = self.provider.base_url.rstrip("/") + "/chat/completions"

        def call() -> httpx.Response:
            self.limiter.wait()
            self.budget.spend(self.provider.name)  # BudgetExceeded stops everything
            self.calls += 1
            try:
                resp = self._client.post(url, json=payload)
            except httpx.TransportError as e:
                raise RetryableError(f"{type(e).__name__}: {e}") from e
            if resp.status_code in RETRY_STATUS:
                wait = parse_retry_after(resp.headers.get("Retry-After"))
                if wait:
                    self.limiter.defer(min(wait, self._retry.max_wait_s))
                raise RetryableError(f"HTTP {resp.status_code}: {resp.text[:200]}", wait)
            return resp

        def on_retry(attempt: int, wait: float, e: RetryableError) -> None:
            if self._log:
                self._log(f"  {self.model.model_id}: {e}; retry {attempt} in {wait:.0f}s")

        try:
            resp = call_with_retry(call, self._retry, self._sleep, on_retry)
        except GaveUp as e:
            raise ChatError(str(e)) from e
        if resp.status_code >= 400:
            raise ChatError(f"HTTP {resp.status_code}: {resp.text[:300]}")
        try:
            body = resp.json()
            choice = body["choices"][0]
            content = choice["message"].get("content")
        except (ValueError, KeyError, IndexError, TypeError, AttributeError) as e:
            raise ChatError(f"unexpected response shape: {resp.text[:300]}") from e
        extra = {}
        if not isinstance(content, str) or not content.strip():
            # e.g. a reasoning model that spent all max_tokens thinking (finish_reason "length")
            content, extra = "", {"empty_reply_finish_reason": choice.get("finish_reason")}
        meta = {
            **extra,
            "response_model": body.get("model"),
            "response_id": body.get("id"),
            "system_fingerprint": body.get("system_fingerprint"),
            "usage": body.get("usage"),
            "created_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        }
        return content, meta
