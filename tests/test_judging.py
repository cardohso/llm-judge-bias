import importlib.util
import json
import re
from pathlib import Path

import httpx
import pytest

from judgebias.budget import BudgetExceeded, DailyBudget
from judgebias.cache import RunCache
from judgebias.judging import judge_items, parse_verdicts, run_order, user_message
from judgebias.llm import ChatClient
from judgebias.models import JUDGES, PROVIDERS

ROOT = Path(__file__).resolve().parent.parent


def prompts():
    spec = importlib.util.spec_from_file_location("jp", ROOT / "judges/prompts.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def prereg_blocks():
    t = (ROOT / "docs/PREREGISTRATION.md").read_text()
    sec = t[t.index("### 5.1 Judge prompt") : t.index("### 5.2 Runs")]
    return re.findall(r"```\n(.*?)\n```", sec, re.S)


def test_system_prompt_is_the_preregistered_text():
    assert prompts().SYSTEM.strip() == prereg_blocks()[0].strip()


def test_user_layout_follows_the_preregistration():
    p = prompts()
    got = user_message(
        p.USER_TEMPLATE,
        "<question>",
        [{"n": 1, "text": "<passage text>"}, {"n": 2, "text": "<passage text>"}],
        ["<sentence with its [n] markers>", "..."],
    ).splitlines()
    want = [x for x in prereg_blocks()[1].splitlines() if x != "..."]
    assert [x for x in got if x != "S2: ..."] == [x for x in want if x != "S2: ..."]
    assert "S2: ..." in got


def test_parse_verdicts():
    ok = (
        '{"sentences": [{"id": 1, "reason": "r", "supported": true},'
        ' {"id": 2, "supported": false}]}'
    )
    assert parse_verdicts(ok) == {1: True, 2: False}
    assert parse_verdicts("```json\n" + ok + "\n```") == {1: True, 2: False}
    for bad in [
        "nope",
        '{"sentences": []}',
        '{"sentences": [{"id": "1", "supported": true}]}',
        '{"sentences": [{"id": 1, "supported": "yes"}]}',
        '{"verdicts": []}',
    ]:
        with pytest.raises(ValueError):
            parse_verdicts(bad)


ITEMS = [
    {"id": f"q{i}-A-CONTROL", "question": "q", "sentences": [f"S one {i} [1].", "S two [1]."]}
    for i in range(12)
]
CTX = {"q": {"question": "Q?", "passages": [{"n": 1, "text": "P"}]}}


def test_run_order_is_seeded_and_differs_by_judge_and_run():
    ids = lambda j, r: [i["id"] for i in run_order(ITEMS, j, r)]  # noqa: E731
    assert ids("G", 1) == ids("G", 1)
    assert ids("G", 1) != ids("O", 1) and ids("G", 1) != ids("G", 2)
    assert sorted(ids("Q", 3)) == sorted(i["id"] for i in ITEMS)


def make_client(tmp_path, handler, judge="O", limit=100):
    budget = DailyBudget(tmp_path / "b.json", {n: limit for n in PROVIDERS})
    return ChatClient(
        JUDGES[judge],
        RunCache(tmp_path / "c.sqlite"),
        budget,
        api_key="test-key-not-real",
        transport=httpx.MockTransport(handler),
        sleep=lambda s: None,
    )


def ok(request):
    user = json.loads(request.content)["messages"][1]["content"]
    n = len(re.findall(r"^S\d+:", user, re.M))
    body = {"sentences": [{"id": i, "reason": "r", "supported": True} for i in range(1, n + 1)]}
    return httpx.Response(
        200, json={"id": "x", "choices": [{"message": {"content": json.dumps(body)}}]}
    )


def run(tmp_path, client, run_no=1, items=ITEMS):
    rows = []
    p = prompts()
    judge_items(
        items, CTX, client, "O", run_no, p.SYSTEM, p.USER_TEMPLATE, rows.append, log=lambda s: None
    )
    return rows


def test_every_item_is_judged_once_and_rerun_is_free(tmp_path):
    client = make_client(tmp_path, ok)
    rows = run(tmp_path, client)
    assert len(rows) == 12 and client.calls == 12
    assert {r["item"] for r in rows} == {i["id"] for i in ITEMS}
    assert len(rows[0]["request_sha256"]) == 64 and "request" not in rows[0]["meta"]
    run(tmp_path, client)
    assert client.calls == 12


def test_second_run_makes_real_calls(tmp_path):
    client = make_client(tmp_path, ok)
    run(tmp_path, client, 1)
    run(tmp_path, client, 2)
    assert client.calls == 24


def test_budget_stop_keeps_finished_rows_and_resumes(tmp_path):
    client = make_client(tmp_path, ok, limit=5)
    rows = []
    p = prompts()
    with pytest.raises(BudgetExceeded):
        judge_items(
            ITEMS, CTX, client, "O", 1, p.SYSTEM, p.USER_TEMPLATE, rows.append, log=lambda s: None
        )
    assert len(rows) == 5
    client.budget.limits["cerebras"] = 100
    again = run(tmp_path, client)
    assert len(again) == 12 and client.calls == 12


def empty_reply(request):
    msg = {"reasoning": "thinking...", "content": None}
    return httpx.Response(
        200, json={"id": "x", "choices": [{"finish_reason": "length", "message": msg}]}
    )


def test_reply_without_content_is_retried_then_recorded_invalid_and_the_run_goes_on(tmp_path):
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        user = json.loads(request.content)["messages"][1]["content"]
        return empty_reply(request) if "S one 0 " in user else ok(request)

    client = make_client(tmp_path, handler)
    rows = run(tmp_path, client)
    assert len(rows) == 12  # the run did not stop
    bad = [r for r in rows if r["content"] == ""]
    assert len(bad) == 1 and bad[0]["meta"]["invalid"] and bad[0]["meta"]["attempts"] == 3
    assert bad[0]["meta"]["empty_reply_finish_reason"] == "length"
    assert calls["n"] == 11 + 3  # three tries for the bad item
    run(tmp_path, client)
    assert calls["n"] == 14  # the invalid outcome is cached, not retried forever
