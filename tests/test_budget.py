from datetime import UTC, datetime, timedelta

import pytest

from judgebias.budget import BudgetExceeded, DailyBudget


class Clock:
    def __init__(self):
        self.t = datetime(2026, 11, 3, 12, 0, tzinfo=UTC)

    def __call__(self):
        return self.t


def make(tmp_path, clock, **limits):
    return DailyBudget(tmp_path / "b.json", limits or {"gemini": 3}, now=clock)


def test_spends_up_to_limit_then_raises(tmp_path):
    b = make(tmp_path, Clock())
    for _ in range(3):
        b.spend("gemini")
    assert b.remaining("gemini") == 0
    with pytest.raises(BudgetExceeded):
        b.spend("gemini")


def test_batch_that_does_not_fit_is_refused_whole(tmp_path):
    b = make(tmp_path, Clock())
    b.spend("gemini", 2)
    with pytest.raises(BudgetExceeded):
        b.spend("gemini", 2)
    assert b.used("gemini") == 2


def test_new_day_resets(tmp_path):
    clock = Clock()
    b = make(tmp_path, clock)
    b.spend("gemini", 3)
    clock.t += timedelta(days=1)
    assert b.remaining("gemini") == 3


def test_day_rolls_over_at_pacific_midnight(tmp_path):
    clock = Clock()
    b = make(tmp_path, clock)
    clock.t = datetime(2026, 11, 3, 7, 30, tzinfo=UTC)  # 23:30 on 2 Nov in Los Angeles
    b.spend("gemini", 3)
    clock.t = datetime(2026, 11, 3, 8, 30, tzinfo=UTC)  # 00:30 on 3 Nov
    assert b.remaining("gemini") == 3


def test_state_persists_and_providers_are_independent(tmp_path):
    clock = Clock()
    make(tmp_path, clock, gemini=3, cerebras=5).spend("cerebras", 4)
    again = make(tmp_path, clock, gemini=3, cerebras=5)
    assert again.used("cerebras") == 4
    assert again.used("gemini") == 0


def test_unknown_provider_is_an_error(tmp_path):
    with pytest.raises(KeyError):
        make(tmp_path, Clock()).spend("nope")


def test_corrupt_state_file_is_treated_as_empty(tmp_path):
    (tmp_path / "b.json").write_text("{not json")
    assert make(tmp_path, Clock()).used("gemini") == 0
