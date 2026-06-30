import pytest
from generator.cards import PolicyCard
from generator.contract import validate_card, A4_TAGS, A5_TAGS, AXIS_LEVEL_KEYS


def _good_card(**over):
    base = dict(
        F0="role header", F1="f1", F2="f2", F3="f3", F4="f4",
        F5="f5", F6="f6", F7="f7", F8="12 turns", F9="f9",
        axis_levels={"A1": "L4", "A2": "L4", "A3": "L4",
                     "A4": "C+", "A5": "G+", "B1": "neu"},
    )
    base.update(over)
    return PolicyCard(**base)


def test_tag_conventions_are_fixed():
    assert A4_TAGS == {"L0": "C-", "L2": "C0", "L4": "C+"}
    assert A5_TAGS == {"L0": "G0", "L4": "G+"}
    assert AXIS_LEVEL_KEYS == {"A1", "A2", "A3", "A4", "A5", "B1"}


def test_good_card_passes():
    assert validate_card(_good_card()) is None


def test_missing_axis_key_rejected():
    c = _good_card()
    del c.axis_levels["B1"]
    with pytest.raises(ValueError):
        validate_card(c)


def test_a1_level_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L9", "A2": "L4",
            "A3": "L4", "A4": "C+", "A5": "G+", "B1": "neu"}))


def test_a4_tag_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L4", "A2": "L4",
            "A3": "L4", "A4": "C5", "A5": "G+", "B1": "neu"}))


def test_a5_tag_out_of_enum_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(axis_levels={"A1": "L4", "A2": "L4",
            "A3": "L4", "A4": "C+", "A5": "GG", "B1": "neu"}))


def test_empty_field_rejected():
    with pytest.raises(ValueError):
        validate_card(_good_card(F3=""))
