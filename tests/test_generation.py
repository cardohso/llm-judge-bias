import importlib.util
import json
from pathlib import Path

import httpx
import pytest

from judgebias.budget import BudgetExceeded, DailyBudget
from judgebias.cache import RunCache
from judgebias.generate import generate_all, parse_answer, user_message
from judgebias.llm import ChatClient, ChatError
from judgebias.models import GENERATORS, PROVIDERS

ROOT = Path(__file__).resolve().parent.parent
CTX = [
    {
        "id": "q1",
        "question": "How wide?",
        "passages": [{"n": 1, "text": "TSI, 4.2\nWidth is 0.8 m."}, {"n": 2, "text": "Other."}],
    }
]


def ok_body(answer="It is 0.8 m [1].", insufficient=False):
    content = json.dumps({"answer": answer, "insufficient": insufficient})
    return {
        "id": "x1",
        "model": "m",
        "system_fingerprint": "fp",
        "usage": {"total_tokens": 9},
        "choices": [{"message": {"content": content}}],
    }


def make_client(tmp_path, handler, label="A", limit=100):
    budget = DailyBudget(tmp_path / "b.json", {n: limit for n in PROVIDERS})
    return ChatClient(
        GENERATORS[label],
        RunCache(tmp_path / "c.sqlite"),
        budget,
        api_key="test-key-not-real",
        transport=httpx.MockTransport(handler),
        sleep=lambda s: None,
    )


def test_prompt_matches_the_preregistration():
    spec = importlib.util.spec_from_file_location("p", ROOT / "generation/prompts.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    prereg = (ROOT / "docs/PREREGISTRATION.md").read_text()
    for line in mod.GENERATE.splitlines():
        if line.strip():
            assert line in prereg, line


def test_user_message_numbers_passages():
    msg = user_message("How wide?", CTX[0]["passages"])
    assert msg == "Question: How wide?\n\nPassages:\n[1] TSI, 4.2\nWidth is 0.8 m.\n\n[2] Other."


def test_parse_answer():
    assert parse_answer('```json\n{"answer": " A [1]. ", "insufficient": false}\n```') == (
        "A [1].",
        False,
    )
    for bad in ["no json", '{"answer": 3, "insufficient": false}', '{"answer": "a"}']:
        with pytest.raises(ValueError):
            parse_answer(bad)


def test_generate_all_calls_once_then_uses_the_cache(tmp_path):
    seen = []

    def handler(request):
        seen.append(json.loads(request.content))
        return httpx.Response(200, json=ok_body())

    client = make_client(tmp_path, handler)
    rows = generate_all(CTX, {"A": client}, "SYS", log=lambda s: None)
    assert rows[0]["answer"] == "It is 0.8 m [1]." and rows[0]["generator"] == "A"
    assert rows[0]["meta"]["system_fingerprint"] == "fp"
    assert seen[0]["temperature"] == 0 and seen[0]["messages"][0]["content"] == "SYS"
    generate_all(CTX, {"A": client}, "SYS", log=lambda s: None)
    assert len(seen) == 1  # second pass came from the cache


def test_gpt_oss_gets_low_reasoning_effort(tmp_path):
    seen = []

    def handler(request):
        seen.append(json.loads(request.content))
        return httpx.Response(200, json=ok_body())

    generate_all(CTX, {"B": make_client(tmp_path, handler, "B")}, "S", log=lambda s: None)
    assert seen[0]["reasoning_effort"] == "low"


def test_rate_limit_is_retried_then_succeeds(tmp_path):
    replies = [
        httpx.Response(429, headers={"Retry-After": "1"}),
        httpx.Response(200, json=ok_body()),
    ]
    client = make_client(tmp_path, lambda r: replies.pop(0))
    assert generate_all(CTX, {"A": client}, "S", log=lambda s: None)[0]["answer"]
    assert client.calls == 2


def test_malformed_reply_is_retried_then_fails(tmp_path):
    bad = {"id": "x", "choices": [{"message": {"content": "not json"}}]}
    client = make_client(tmp_path, lambda r: httpx.Response(200, json=bad))
    with pytest.raises(ChatError):
        generate_all(CTX, {"A": client}, "S", log=lambda s: None)
    assert client.calls == 3


def test_budget_stops_before_sending(tmp_path):
    client = make_client(tmp_path, lambda r: httpx.Response(200, json=ok_body()), limit=0)
    with pytest.raises(BudgetExceeded):
        generate_all(CTX, {"A": client}, "S", log=lambda s: None)
    assert client.calls == 0


def test_auth_error_is_not_retried(tmp_path):
    client = make_client(tmp_path, lambda r: httpx.Response(401, json={"error": "bad key"}))
    with pytest.raises(ChatError, match="401"):
        generate_all(CTX, {"A": client}, "S", log=lambda s: None)
    assert client.calls == 1
