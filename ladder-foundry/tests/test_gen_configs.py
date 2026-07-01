# tests/test_gen_configs.py
import json
import pytest
from generator import weights
from generator.axes import level_text
from generator.gen_configs import gen_configs, build_one, _PLACEHOLDER_TOPIC, main
from generator.cards import to_dict
from generator.contract import validate_card


def _w(tmp_path):
    return weights.dump_initial(str(tmp_path / "b0.json"))


def test_pipeline_yields_six_cards(tmp_path):
    cards = gen_configs(_w(tmp_path))
    assert len(cards) == 6


def test_every_card_validates(tmp_path):
    for card in gen_configs(_w(tmp_path)):
        assert validate_card(card) is None


def test_f1_selected_by_coord_not_level_idx(tmp_path):
    w = _w(tmp_path)
    cards = gen_configs(w)
    # rung 0 coord A1 = L4 -> F1 must be the A1.L4 body verbatim
    assert level_text(w, "A1", "L4") in cards[0].F1
    assert level_text(w, "A1", "L0") in cards[5].F1


def test_f4_f5_map_tag_to_level(tmp_path):
    w = _w(tmp_path)
    cards = gen_configs(w)
    # rung0 A4=C+ -> A4.L4 body; A5=G+ -> A5.L4 body
    assert level_text(w, "A4", "L4") in cards[0].F4
    assert level_text(w, "A5", "L4") in cards[0].F5
    # rung5 A4=C- -> A4.L0 body; A5=G0 -> A5.L0 body
    assert level_text(w, "A4", "L0") in cards[5].F4
    assert level_text(w, "A5", "L0") in cards[5].F5


def test_coord_none_fails_loud(tmp_path):
    w = _w(tmp_path)
    bad = {"topic_id": "t", "rung_id": 9, "level_idx": 0,
           "perturb_axis": "B1", "coord": None, "params": w["assembler_params"]}
    with pytest.raises(ValueError):
        build_one(w, bad, _PLACEHOLDER_TOPIC)


def test_endpoints_diverge(tmp_path):
    cards = gen_configs(_w(tmp_path))
    assert cards[0].F1 != cards[5].F1
    assert cards[0].axis_levels["A1"] == "L4"
    assert cards[5].axis_levels["A1"] == "L0"
    assert cards[0].axis_levels["B1"] != cards[5].axis_levels["B1"]


def test_pipeline_is_deterministic(tmp_path):
    a = [to_dict(c) for c in gen_configs(_w(tmp_path))]
    b = [to_dict(c) for c in gen_configs(_w(tmp_path))]
    assert a == b


def test_main_writes_six_config_files(tmp_path):
    w = _w(tmp_path)
    main(str(tmp_path / "configs"), w=w)
    files = sorted((tmp_path / "configs").glob("config_*.json"))
    assert len(files) == 6
    doc = json.loads(files[0].read_text(encoding="utf-8"))
    assert set(doc.keys()) >= {"F0", "F1", "axis_levels"}
