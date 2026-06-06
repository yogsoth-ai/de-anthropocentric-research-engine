from pathlib import Path
from generator.leak_audit import DENY  # noqa: F401 (import verifies availability)

SKILLS = Path(__file__).parent.parent / "skills"


def test_loss_skills_have_no_check_vocabulary_in_judging_logic():
    # The two loss skills must not use check vocabulary as a judging criterion.
    # Note: deny terms may legitimately appear in a "forbidden list" context,
    # so we only require an explicit check-blind contract.
    for name in ("injection-fidelity", "ladder-quality-order"):
        txt = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        low = txt.lower()
        # must explicitly declare a check-blind contract
        assert "check-blind" in low
        # 32-check must not be used as a scoring input (only allowed in a "forbidden/never" context)
        assert "32-check" not in low or "forbidden" in low or "never" in low
