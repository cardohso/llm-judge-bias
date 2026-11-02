"""Base answers: every question is answered by each generator from the identical fixed context
(docs/PREREGISTRATION.md, section 4.4). Logic only; the CLI is generation/generate.py."""

from __future__ import annotations

import json
from collections.abc import Callable, Sequence
from typing import Any

from judgebias.llm import ChatClient


def user_message(question: str, passages: Sequence[dict]) -> str:
    """Same layout as rail-regulation-rag's generate node; markers are context numbers."""
    numbered = "\n\n".join(f"[{p['n']}] {p['text']}" for p in passages)
    return f"Question: {question}\n\nPassages:\n{numbered}"


def parse_answer(content: str) -> tuple[str, bool]:
    """(answer, insufficient) from a reply; ValueError if it is not the expected JSON."""
    start, end = content.find("{"), content.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object")
    try:
        obj = json.loads(content[start : end + 1])
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON: {e}") from e
    if not isinstance(obj, dict) or not isinstance(obj.get("answer"), str):
        raise ValueError("no string 'answer'")
    insufficient = obj.get("insufficient")
    if not isinstance(insufficient, bool):
        raise ValueError("no boolean 'insufficient'")
    return obj["answer"].strip(), insufficient


def generate_all(
    contexts: Sequence[dict],
    clients: dict[str, ChatClient],
    system: str,
    log: Callable[[str], None] = print,
) -> list[dict[str, Any]]:
    """One answer per (question, generator). A BudgetExceeded propagates; rerun tomorrow."""
    rows = []
    for ctx in contexts:
        user = user_message(ctx["question"], ctx["passages"])
        for label, client in clients.items():
            reply = client.chat(system, user, run=1, validate=parse_answer)
            answer, insufficient = parse_answer(reply.content)
            log(f"{ctx['id']} {label} {'cached' if reply.cached else 'new'}")
            rows.append({
                "id": ctx["id"],
                "generator": label,
                "model": client.model.model_id,
                "answer": answer,
                "insufficient": insufficient,
                "raw": reply.content,
                "meta": reply.meta,
            })  # fmt: skip
    return rows
