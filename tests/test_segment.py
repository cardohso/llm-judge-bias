import pytest

from judgebias.segment import markers, segment


def test_two_sentences_with_markers_before_the_stop():
    assert segment("The limit is 65 dB [1]. It is measured at 7,5 m [1][2].") == [
        "The limit is 65 dB [1].",
        "It is measured at 7,5 m [1][2].",
    ]


def test_markers_after_the_stop_stay_with_their_sentence():
    assert segment("The limit is 65 dB. [1] It is measured at 7,5 m. [2]") == [
        "The limit is 65 dB. [1]",
        "It is measured at 7,5 m. [2]",
    ]


@pytest.mark.parametrize(
    "text",
    [
        "The walkway is at least 0.8 m wide [1].",
        "APL is 0,225 for wagons [1].",
        "See point 4.2.1.6 for details [1].",
        "Section 4.2.3 applies [1].",
        "Dates such as 1.1.2024 apply [1].",
    ],
)
def test_decimals_and_section_numbers_do_not_split(text):
    assert segment(text) == [text]


def test_abbreviations_do_not_split():
    text = "Systems, e.g. ETCS, must comply [1]. No. 5 applies [2]."
    assert segment(text) == ["Systems, e.g. ETCS, must comply [1].", "No. 5 applies [2]."]


def test_question_and_exclamation_marks_split():
    assert segment("Is it so? Yes! It is [1].") == ["Is it so?", "Yes!", "It is [1]."]


def test_lowercase_after_a_stop_does_not_split():
    assert segment("Approx. half applies, e.g. in tunnels [1].") == [
        "Approx. half applies, e.g. in tunnels [1]."
    ]


def test_whitespace_is_normalised_and_round_trips():
    text = "A  first\nsentence [1].   A second one [2]."
    assert " ".join(segment(text)) == "A first sentence [1]. A second one [2]."


def test_empty_and_whitespace_only():
    assert segment("") == []
    assert segment("  \n ") == []


def test_no_final_stop():
    assert segment("One [1]. Two without a stop [2]") == ["One [1].", "Two without a stop [2]"]


def test_markers():
    assert markers("x [2][3] y [1].") == [2, 3, 1]
    assert markers("none.") == []


def test_every_saved_reference_answer_is_segmented_without_loss():
    import json
    from pathlib import Path

    rows = [json.loads(line) for line in Path("questions/questions.jsonl").read_text().splitlines()]
    for r in rows:
        text = r["reference_answer"]
        assert " ".join(segment(text)) == " ".join(text.split())
