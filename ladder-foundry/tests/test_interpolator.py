# ladder-foundry/tests/test_interpolator.py
from generator import weights
from generator.interpolator import ladder_levels


def test_rank_direction_locked(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    rungs = ladder_levels(w, n=6)
    assert [r["rung_id"] for r in rungs] == [0, 1, 2, 3, 4, 5]


def test_ladder_nondecreasing(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    levels = [r["level_idx"] for r in ladder_levels(w, n=6)]
    assert levels == [0, 1, 2, 2, 3, 4]                 # collision at level 2
    assert all(b >= a for a, b in zip(levels, levels[1:]))   # nondecreasing


def test_coord_read_from_frozen_table(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    rungs = ladder_levels(w, n=6)
    # coord comes verbatim from the frozen table (read, never computed)
    assert rungs[0]["coord"] == w["frozen_label"]["coord_table"]["0"]
    assert rungs[5]["coord"] == w["frozen_label"]["coord_table"]["5"]
    assert rungs[0]["coord"]["A1"] == "L4"
    assert rungs[5]["coord"]["A1"] == "L0"
    # mutating the returned coord must not alter a fresh read (table is source of truth)
    assert rungs[3]["coord"] == w["frozen_label"]["coord_table"]["3"]


def test_collision_offset_axis_carried(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    assert all(r["collision_offset_axis"] in {"B1", "expression"}
               for r in ladder_levels(w, n=6))
