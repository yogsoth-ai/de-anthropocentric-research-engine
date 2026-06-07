from generator.cards import PolicyCard, AxisLevels


def test_card_roundtrips_all_fields():
    levels = AxisLevels(A1="L0", A2="L0", A3="L0", A4="C0", A5="G+", B1="F-neu")
    card = PolicyCard(
        label="id0-genius", ladder_position=0.0, axis_levels=levels,
        f0_persona="rigorous senior researcher",
        f1_substance="interrogate every claim",
        f2_operationalization="demand numbers",
        f3_legitimacy="coherent on-topic",
        f4_corrigibility="weigh arguments fairly",
        f5_framing="plain register",
        f6_acceptance="accept only when mechanism+number+coherent",
        f7_wrong_premise="",
        f8_pressure_turns=10, f8_closing_turns=2,
        f9_generativity="offer novel seeds, demand rigor",
    )
    d = card.to_dict()
    assert d["axis_levels"]["A5"] == "G+"
    assert d["f8_pressure_turns"] == 10 and d["f8_closing_turns"] == 2
    assert PolicyCard.from_dict(d).f0_persona == "rigorous senior researcher"


def test_pg_card_requires_wrong_premise_when_A4_negative():
    levels = AxisLevels(A1="L0", A2="L0", A3="L0", A4="C-", A5="G0", B1="F-neu")
    import pytest
    with pytest.raises(ValueError, match="F7 wrong_premise required"):
        PolicyCard(label="pg", ladder_position=0.0, axis_levels=levels,
                   f0_persona="x", f1_substance="x", f2_operationalization="x",
                   f3_legitimacy="x", f4_corrigibility="x", f5_framing="x",
                   f6_acceptance="x", f7_wrong_premise="", f8_pressure_turns=10,
                   f8_closing_turns=2, f9_generativity="").validate()
