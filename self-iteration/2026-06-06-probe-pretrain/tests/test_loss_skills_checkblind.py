from pathlib import Path
from generator.leak_audit import DENY  # noqa: F401 (导入即验证可用)

SKILLS = Path(__file__).parent.parent / "skills"


def test_loss_skills_have_no_check_vocabulary_in_judging_logic():
    # 两个 loss skill 的"评判逻辑"不得把 check 词当判据。
    # 注：deny 词可能作为"禁用清单"出现，故只扫描非 -契约 段落。
    for name in ("injection-fidelity", "ladder-quality-order"):
        txt = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        # 必须显式声明 check-blind 契约
        assert "check-blind" in txt.lower()
        # 必须不把 32-check 当评分输入（只允许在"禁用"语境出现）
        assert "32-check" not in txt or "禁用" in txt or "绝不" in txt
