import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sandbox"))
from smoke_test import build_injection, diverged


def test_injection_contains_config_and_stimulus(tmp_path):
    cfg = tmp_path / "config_0.json"
    cfg.write_text('{"F0":"role header X","F1":"demand substance"}', encoding="utf-8")
    stim = tmp_path / "stimulus.md"
    stim.write_text("A research proposal to react to.", encoding="utf-8")
    msg = build_injection(str(cfg), str(stim))
    assert "role header X" in msg
    assert "research proposal" in msg
    assert "DONE" in msg            # the reply convention is present


def test_diverged_true_when_reactions_differ():
    t0 = [{"role": "assistant", "text": "I demand far more rigorous substance here."}]
    t5 = [{"role": "assistant", "text": "Sounds great, no notes, ship it."}]
    assert diverged(t0, t5) is True


def test_diverged_false_when_identical():
    t = [{"role": "assistant", "text": "Same exact reaction text."}]
    assert diverged(t, t) is False
