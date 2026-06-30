import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "optimization-loop" / "SKILL.md"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit
from generator.weights import TRAINABLE, INTERP_KEYS


def txt():
    return SKILL.read_text(encoding="utf-8")


def test_skill_exists_and_leak_clean():
    assert SKILL.exists()
    leak_audit(txt())


def test_names_all_seven_leaves_by_relative_anchor():
    t = txt()
    for leaf in ("new_run_id.py", "trace_emit.py", "save_transcript.py",
                 "concat_triple.py", "gate_eval.py", "apply_weight_update.py",
                 "write_dataset.py"):
        assert f"../../scripts/{leaf}" in t, leaf
    assert "../../generator/gen_configs.py" in t
    assert "scripts/run_codex_loss.py" in t          # own leaf, local anchor


def test_named_leaf_flags_actually_exist():
    # introspect a couple of leaves: the flags the skill names must be real
    t = txt()
    help_save = subprocess.run([sys.executable, "scripts/save_transcript.py", "-h"],
                               cwd=str(LF), capture_output=True, text=True).stdout
    assert "--logs-dir" in help_save and "--logs-dir" in t
    help_gate = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic", "-h"],
                               cwd=str(LF), capture_output=True, text=True).stdout
    for flag in ("--fidelity-rate", "--mono", "--endpoint"):
        assert flag in help_gate and flag in t


def test_backprop_targets_subset_of_weights_vocab():
    t = txt()
    # every target the skill says it can change must be a real trainable segment
    assert "axis_prose" in t and "interp_params" in t and "assembler_params" in t
    assert TRAINABLE == {"axis_prose", "interp_params", "assembler_params"}
    # interp knobs named must be the locked key-set
    for k in INTERP_KEYS:
        assert k in t, k


def test_threshold_point_back_not_copied():
    t = txt()
    # the skill points back to the module constants, does not re-state the digits
    assert "FIDELITY_MIN" in t and "BATCH_RATIO_MIN" in t


def test_banned_flags_and_driver_absent():
    t = txt()
    for banned in ("-p ", "--resume", "--session-id", "--allowedTools",
                   "drive_cc", "pexpect", "PTY"):
        assert banned not in t, banned


def test_logs_dir_required_privacy_line_present():
    t = txt()
    assert "--logs-dir" in t and "required" in t.lower()
