from generator.axes import AXES, level_text


def test_ladder_axes_have_five_levels():
    for ax in ("A1", "A3", "A2"):
        assert len(AXES[ax]["levels"]) == 5  # L0..L4


def test_overlay_axes_levels():
    assert set(AXES["A4"]["levels"]) == {"C+", "C0", "C-"}
    assert set(AXES["A5"]["levels"]) == {"G0", "G+"}
    assert set(AXES["B1"]["levels"]) == {"F-rig", "F-neu", "F-buz"}


def test_level_text_returns_means_layer_prose():
    txt = level_text("A1", "L0")
    assert isinstance(txt, str) and len(txt) > 10
