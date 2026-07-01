"""Layer-2: downstream really ingests L1's dump_initial output."""
from generator import weights
from generator.axes import level_text
from generator.interpolator import ladder_levels
from generator.assembler import build_batch


def test_L3_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert isinstance(level_text(w, "A3", "L4"), str)


def test_L4_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    w["frozen_label"]["coord_table"] = {"0": [0.0], "5": [9.0]}   # fixture coords
    rungs = ladder_levels(w, n=6)
    assert len(rungs) == 6
    assert [r["rung_id"] for r in rungs] == [0, 1, 2, 3, 4, 5]


def test_L5_consumes_dump_initial(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert len(cards) == 6
    assert all(c["perturb_axis"] in {"B1", "expression"} for c in cards)
