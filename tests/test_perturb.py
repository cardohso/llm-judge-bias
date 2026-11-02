import pytest

from judgebias.perturb import (
    InvalidPerturbation,
    add_sentence,
    apply_edit,
    base_sentences,
    cite_wrong,
    num_out_of_context,
    validate,
)

PASSAGES = [
    {"n": 1, "role": "gold", "text": "NOI TSI, 4.2.1\nEMUs | 65 dB. Wagons | 72 dB."},
    {"n": 2, "role": "distractor", "text": "OPE TSI, 4.7\nStaff examinations every 5 years."},
    {"n": 3, "role": "distractor", "text": "SRT TSI, 4.4\nExercises before opening tunnels."},
]
BASE = base_sentences("The limit for an EMU is 65 dB [1]. It is measured at 7,5 m [1].")


def test_base_sentences_render_and_split():
    assert BASE == ("The limit for an EMU is 65 dB [1].", "It is measured at 7,5 m [1].")
    assert base_sentences("night‑time only [1].") == ("night-time only [1].",)


def test_num_out_of_context_changes_one_sentence_only():
    p = num_out_of_context("q1", "A", BASE, PASSAGES)
    assert p.type == "NUM" and p.subtype == "out-of-context" and p.planted_index == 1
    assert p.sentences[1] == BASE[1] and p.sentences[0] != BASE[0]
    assert "65" not in p.planted_sentence


def test_num_out_of_context_none_without_a_qualifying_number():
    assert (
        num_out_of_context("q1", "A", base_sentences("It is a requirement [1]."), PASSAGES) is None
    )


def test_cite_wrong_swaps_only_the_marker():
    p = cite_wrong("q1", "A", BASE, PASSAGES)
    assert p.type == "CITE" and p.planted_index == 1
    assert p.planted_sentence.startswith("The limit for an EMU is 65 dB [")
    assert p.planted_sentence.endswith("].") and "[1]" not in p.planted_sentence
    assert p.sentences[1] == BASE[1]


def test_cite_wrong_needs_a_distractor_without_shared_numbers():
    passages = [PASSAGES[0], {"n": 2, "role": "distractor", "text": "Value 65 dB elsewhere."}]
    single = base_sentences("The limit for an EMU is 65 dB [1].")
    assert cite_wrong("q1", "A", single, passages) is None


def test_add_sentence_cites_the_last_marker_and_is_last():
    p = add_sentence("q1", "A", BASE, "Exceptions can be granted on written request")
    assert p.planted_index == 3 and p.planted_sentence == (
        "Exceptions can be granted on written request [1]."
    )
    assert p.sentences[:2] == BASE


def test_apply_edit_requires_a_unique_find():
    p = apply_edit("q1", "A", "NEG", "", BASE, 1, "is 65 dB", "is not 65 dB")
    assert p.planted_sentence == "The limit for an EMU is not 65 dB [1]."
    with pytest.raises(InvalidPerturbation):
        apply_edit("q1", "A", "NEG", "", BASE, 1, "zzz", "y")
    with pytest.raises(InvalidPerturbation):  # "m [1]" would be fine; "[1]" occurs once in S1
        apply_edit("q1", "A", "NEG", "", BASE, 1, "x", "y")


def test_validate_rejects_extra_changes():
    with pytest.raises(InvalidPerturbation):
        validate(BASE, ("changed [1].", "also changed [1]."), 1, "NUM")
    with pytest.raises(InvalidPerturbation):
        validate(BASE, (*BASE, "x [1].", "y [1]."), 3, "ADD")
    with pytest.raises(InvalidPerturbation):
        validate(BASE, (BASE[0],), 1, "NEG")
