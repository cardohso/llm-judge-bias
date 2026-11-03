"""Judge calls (docs/PREREGISTRATION.md, sections 5 and 6): one call per answer, the judge rates
each sentence against the passages it cites. This module builds the request, validates the reply
shape and runs a judge over items in the pre-registered order; scoring lives in analysis/."""

from __future__ import annotations

import hashlib
import json
import random
from collections.abc import Callable, Sequence
from typing import Any

from judgebias.llm import ChatClient

SEED = 20261102
JUDGE_INDEX = {"G": 0, "O": 1, "Q": 2}


def user_message(template: str, question: str, passages: Sequence[dict], sentences: Sequence[str]):
    return template.format(
        passages="\n".join(f"[{p['n']}] {p['text']}" for p in passages),
        question=question,
        sentences="\n".join(f"S{i}: {s}" for i, s in enumerate(sentences, 1)),
    )


def parse_verdicts(content: str) -> dict[int, bool]:
    """{sentence id: supported}. ValueError if the reply is not the expected JSON shape.
    Sentences the judge skipped are simply absent; the analysis treats a missing planted
    sentence as invalid (section 6)."""
    start, end = content.find("{"), content.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object")
    try:
        obj = json.loads(content[start : end + 1])
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON: {e}") from e
    rows = obj.get("sentences") if isinstance(obj, dict) else None
    if not isinstance(rows, list) or not rows:
        raise ValueError("no non-empty 'sentences' list")
    verdicts: dict[int, bool] = {}
    for r in rows:
        if not (
            isinstance(r, dict)
            and isinstance(r.get("id"), int)
            and not isinstance(r["id"], bool)
            and isinstance(r.get("supported"), bool)
        ):
            raise ValueError(f"bad sentence entry: {r!r:.100}")
        verdicts.setdefault(r["id"], r["supported"])
    return verdicts


def run_order(items: Sequence[dict], judge: str, run: int) -> list[dict]:
    """Items in a random order fixed by the seed 20261102 + 100*j + r (section 5.2)."""
    order = sorted(items, key=lambda i: i["id"])
    random.Random(SEED + 100 * JUDGE_INDEX[judge] + run).shuffle(order)
    return order


def request_sha256(request: dict[str, Any]) -> str:
    blob = json.dumps(request, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(blob.encode()).hexdigest()


def judge_items(
    items: Sequence[dict],
    contexts: dict[str, dict],
    client: ChatClient,
    judge: str,
    run: int,
    system: str,
    template: str,
    on_row: Callable[[dict], None],
    log: Callable[[str], None] = print,
    limit: int | None = None,
) -> None:
    """Judge every item once (the first `limit` in the seeded order), calling on_row(row) after
    each. BudgetExceeded and ChatError propagate; rows already delivered stay valid and the
    cache lets a rerun resume."""
    for n, item in enumerate(run_order(items, judge, run)[:limit], 1):
        ctx = contexts[item["question"]]
        user = user_message(template, ctx["question"], ctx["passages"], item["sentences"])
        reply = client.chat(system, user, run, validate=parse_verdicts, record_invalid=True)
        meta = {k: v for k, v in reply.meta.items() if k != "request"}
        on_row({
            "item": item["id"],
            "judge": judge,
            "run": run,
            "model": client.model.model_id,
            "content": reply.content,
            "request_sha256": request_sha256(client.request(system, user)),
            "meta": meta,
        })  # fmt: skip
        if n % 25 == 0:
            log(f"  {judge} run {run}: {n}/{len(items)}")
