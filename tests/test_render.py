import json
from pathlib import Path

from judgebias.render import render_answer


def test_narrow_nbsp_and_nbsp_become_spaces():
    assert render_answer("20 km and 5 m") == "20 km and 5 m"


def test_non_breaking_hyphen_becomes_plain():
    assert render_answer("night‑time 2015‑2017") == "night-time 2015-2017"


def test_curly_quotes_and_symbols_are_kept():
    assert render_answer("a ‘quieter route’ ≥ 12") == "a ‘quieter route’ ≥ 12"


def test_idempotent_and_collapses_whitespace():
    once = render_answer("a  b\n c ‑d")
    assert once == "a b c -d"
    assert render_answer(once) == once


def test_no_generator_leaves_special_characters_after_rendering():
    rows = [json.loads(line) for line in Path("answers/answers.jsonl").read_text().splitlines()]
    for r in rows:
        out = render_answer(r["answer"])
        assert " " not in out and "‑" not in out
