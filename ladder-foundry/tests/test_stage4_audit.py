import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILLS = LF / "skills"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit, LeakHit

TEXT_FILES = list(SKILLS.rglob("*.md")) + list(SKILLS.rglob("*.json"))


def test_skills_tree_nonempty():
    assert len(TEXT_FILES) >= 7      # 5 SKILL.md + 2 references + schemas


def test_w5_leak_sweep_all_skill_text():
    # every committed .md / .json under skills/ is leak-clean
    for f in TEXT_FILES:
        leak_audit(f.read_text(encoding="utf-8"))


def test_no_banned_cc_flags_anywhere():
    banned = ["--resume", "--session-id", "--allowedTools",
              "drive_cc", "pexpect"]
    for f in SKILLS.rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        for b in banned:
            assert b not in t, (f.name, b)
        # "-p " print flag and bare "PTY" — guard against the claude print flag
        assert " -p " not in t, f.name
        assert "PTY" not in t, f.name


def test_no_log_path_signatures_committed():
    # 3 privacy signatures: Windows projects dir, POSIX projects dir, bare slug.
    # ponytail: literal-substring scan, the same shape T7's shell grep uses.
    sigs = ["\\.claude\\projects", "/.claude/projects", ".claude\\projects"]
    for f in TEXT_FILES:
        t = f.read_text(encoding="utf-8")
        for s in sigs:
            assert s not in t, (f.name, s)


def test_save_transcript_logs_dir_required_in_loop():
    # the optimizer skill must carry the privacy line
    sk = (SKILLS / "optimization-loop" / "SKILL.md").read_text(encoding="utf-8")
    assert "--logs-dir" in sk and "required" in sk.lower()
