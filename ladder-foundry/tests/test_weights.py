import pytest
from generator import weights


def _w(tmp_path):
    return weights.dump_initial(str(tmp_path / "batch-0.json"))


def test_dump_initial_has_four_segments(tmp_path):
    w = _w(tmp_path)
    assert set(w.keys()) == {"axis_prose", "interp_params", "assembler_params", "frozen_label"}


def test_interp_params_key_set_locked(tmp_path):
    w = _w(tmp_path)
    assert set(w["interp_params"].keys()) == {"collision_offset_axis", "endpoint_spread", "granularity_map"}
    w["interp_params"]["sneaky_coord"] = [1, 2]      # smuggle a coord under a new key
    with pytest.raises(ValueError):
        weights.revise(w, "assembler_params", "turn_budget", 13, "trigger keyset check")


def test_coord_table_empty_in_batch0(tmp_path):
    w = _w(tmp_path)
    assert w["frozen_label"]["coord_table"] == {}


def test_rank_order_locked_values(tmp_path):
    w = _w(tmp_path)
    assert w["frozen_label"]["rank_order"]["direction"] == [0, 1, 2, 3, 4, 5]
    assert w["frozen_label"]["rank_order"]["primary_sort"] == ["A1", "A3", "A2"]


def test_revise_rejects_frozen_label(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "frozen_label", "rank_order", {}, "must reject")


def test_revise_rejects_unknown_target(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "bogus_segment", "k", "v", "must reject")


def test_collision_offset_rejects_label_axis(tmp_path):
    w = _w(tmp_path)
    with pytest.raises(ValueError):
        weights.revise(w, "interp_params", "collision_offset_axis", "A2", "must reject")


def test_collision_offset_accepts_b1_expression(tmp_path):
    w = _w(tmp_path)
    rec = weights.revise(w, "interp_params", "collision_offset_axis", "expression", "ok")
    assert rec["new"] == "expression"
    assert w["interp_params"]["collision_offset_axis"] == "expression"


def test_revise_axis_prose_dotted_key(tmp_path):
    w = _w(tmp_path)
    rec = weights.revise(w, "axis_prose", "A1.L0", "new body", "ok")
    assert rec == {"target": "axis_prose", "key": "A1.L0",
                   "old": rec["old"], "new": "new body", "reason": "ok"}
    assert w["axis_prose"]["A1"]["L0"] == "new body"


def test_revise_axis_prose_malformed_path(tmp_path):
    w = _w(tmp_path)
    for bad in ["A1", "A1.L0.x", "Z9.L0", "A1.L9"]:
        with pytest.raises(ValueError):
            weights.revise(w, "axis_prose", bad, "x", "must reject")


def test_load_roundtrip_and_keyset_validation(tmp_path):
    p = str(tmp_path / "batch-0.json")
    weights.dump_initial(p)
    w = weights.load(p)
    assert set(w.keys()) == {"axis_prose", "interp_params", "assembler_params", "frozen_label"}


def test_load_rejects_bad_interp_keyset(tmp_path):
    import json
    p = tmp_path / "tampered.json"
    w = weights.dump_initial(str(p))                 # valid batch-0 on disk
    w["interp_params"]["sneaky_coord"] = [1, 2]      # smuggle a coord under a new key
    p.write_text(json.dumps(w), encoding="utf-8")    # persist the tampered weights
    with pytest.raises(ValueError):
        weights.load(str(p))                          # load() must reject the bad keyset
