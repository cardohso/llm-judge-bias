import json
from pathlib import Path


def load():
    return [json.loads(line) for line in Path("contexts/contexts.jsonl").read_text().splitlines()]


def test_one_context_per_question_with_gold_and_two_distractors():
    questions = {
        json.loads(line)["id"]: json.loads(line)
        for line in Path("questions/questions.jsonl").read_text().splitlines()
    }
    contexts = load()
    assert [c["id"] for c in contexts] == list(questions)
    for c in contexts:
        roles = [p["role"] for p in c["passages"]]
        assert roles.count("gold") == len(questions[c["id"]]["gold_passages"])
        assert roles.count("distractor") == 2
        assert {p["id"] for p in c["passages"] if p["role"] == "gold"} == set(
            questions[c["id"]]["gold_passages"]
        )


def test_passages_are_numbered_from_one_and_ordered_by_score():
    for c in load():
        assert [p["n"] for p in c["passages"]] == list(range(1, len(c["passages"]) + 1))
        scores = [p["score"] for p in c["passages"]]
        assert scores == sorted(scores, reverse=True)
