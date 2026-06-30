from generator import weights
from generator.assembler import build_batch


def test_build_batch_one_card_per_rung(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert len(cards) == 6
    assert [c["rung_id"] for c in cards] == [0, 1, 2, 3, 4, 5]
    assert all(c["topic_id"] == "topic00" for c in cards)


def test_collision_offset_never_label_axis(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    label_axes = {"A1", "A2", "A3", "A4", "A5"}
    assert all(c["perturb_axis"] not in label_axes for c in cards)
    assert all(c["perturb_axis"] in {"B1", "expression"} for c in cards)


def test_params_externalized_from_assembler_segment(tmp_path):
    w = weights.dump_initial(str(tmp_path / "b0.json"))
    cards = build_batch(w, n=6, topic_id="topic00")
    assert cards[0]["params"]["turn_budget"] == w["assembler_params"]["turn_budget"]
