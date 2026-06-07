from generator.assembler import build_batch
from generator.leak_audit import leak_audit


def test_ladder_mode_endpoints():
    cards = build_batch(n=6, mode="ladder")
    assert cards[0].axis_levels.A1 == "L0"
    assert cards[-1].axis_levels.A1 == "L4"


def test_pg_overlay_sets_A4_negative_and_premise():
    cards = build_batch(n=6, mode="pg-overlay", wrong_premise="only method X works")
    assert any(c.axis_levels.A4 == "C-" and c.f7_wrong_premise for c in cards)


def test_ng_overlay_sets_A5_positive():
    cards = build_batch(n=6, mode="ng-overlay")
    assert any(c.axis_levels.A5 == "G+" for c in cards)


def test_confound_triplet_varies_only_B1():
    cards = build_batch(n=6, mode="confound-triplet")
    b1s = {c.axis_levels.B1 for c in cards if c.label.endswith("-conf")}
    assert b1s == {"F-rig", "F-neu", "F-buz"}


def test_leak_audit_blocks_check_vocabulary():
    bad = "make a deletable mechanism and list skills you won't invoke"
    assert leak_audit(bad) is False
    good = "demand the causal mechanism and a falsifiable hypothesis"
    assert leak_audit(good) is True
