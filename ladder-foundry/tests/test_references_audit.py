import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
REF = LF / "skills" / "optimization-loop" / "references"
GATE = REF / "gate-thresholds.md"
BP = REF / "backprop-heuristic.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit


def test_both_exist_and_leak_clean():
    assert GATE.exists() and BP.exists()
    leak_audit(GATE.read_text(encoding="utf-8"))
    leak_audit(BP.read_text(encoding="utf-8"))


def test_gate_points_back_not_copies():
    t = GATE.read_text(encoding="utf-8")
    # names the owning constants
    assert "FIDELITY_MIN" in t and "BATCH_RATIO_MIN" in t
    assert "TAU_MIN" in t
    # explicit point-back language present
    assert "gate_eval" in t and "run_codex_loss" in t
    assert "source of truth" in t.lower() or "points back" in t.lower()


def test_gate_owns_only_unowned_numbers():
    t = GATE.read_text(encoding="utf-8")
    # 0.90 / 0.80 gate lines must NOT be re-stated as literals here
    assert "0.90" not in t
    # the 丙 calibration line 0.80 IS owned here (a judge number no script holds)
    assert "0.80" in t


def test_backprop_three_disciplines_and_subset():
    t = BP.read_text(encoding="utf-8")
    assert "attribute" in t.lower()
    assert "one weight" in t.lower() or "single-variable" in t.lower()
    # the loss-2 subtype split discipline
    assert "frozen_label" in t
    for tgt in ("axis_prose", "interp_params", "assembler_params"):
        assert tgt in t, tgt


def test_backprop_no_academic_criteria():
    t = BP.read_text(encoding="utf-8").lower()
    for forbidden in ("novelty", "baseline", "citation", "publishab"):
        assert forbidden not in t
