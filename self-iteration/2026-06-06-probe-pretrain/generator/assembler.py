# 可训练权重③：把轴坐标组装成整张 PolicyCard（两阶段：坐标→话术扩写）。
from generator.cards import PolicyCard, AxisLevels
from generator.axes import level_text
from generator.interpolator import ladder_levels

DEFAULT_PRESSURE_TURNS = 10
DEFAULT_CLOSING_TURNS = 2


def _assemble(rung, A4="C0", A5="G0", B1="F-neu", wrong_premise="", suffix=""):
    lv = AxisLevels(A1=rung["A1"], A2=rung["A2"], A3=rung["A3"], A4=A4, A5=A5, B1=B1)
    card = PolicyCard(
        label=f"id{rung.get('idx', '?')}{suffix}",
        ladder_position=rung["t"], axis_levels=lv,
        f0_persona="研究监督者",
        f1_substance=level_text("A1", rung["A1"]),
        f2_operationalization=level_text("A3", rung["A3"]),
        f3_legitimacy=level_text("A2", rung["A2"]),
        f4_corrigibility=level_text("A4", A4),
        f5_framing=level_text("B1", B1),
        f6_acceptance="按 A1/A3/A2 组合推导的接受门槛。",
        f7_wrong_premise=wrong_premise,
        f8_pressure_turns=DEFAULT_PRESSURE_TURNS,
        f8_closing_turns=DEFAULT_CLOSING_TURNS,
        f9_generativity=level_text("A5", A5),
    )
    return card.validate()


def build_batch(n=6, mode="ladder", wrong_premise="占位错误前提"):
    rungs = ladder_levels(n)
    for i, r in enumerate(rungs):
        r["idx"] = i
    cards = []
    if mode == "ladder":
        for r in rungs:
            a5 = "G+" if r["idx"] == 0 else "G0"  # 天才端点带才华
            cards.append(_assemble(r, A5=a5))
    elif mode == "pg-overlay":
        hi = rungs[0]
        cards.append(_assemble(hi, A4="C-", wrong_premise=wrong_premise, suffix="-pg"))
    elif mode == "ng-overlay":
        hi = rungs[0]
        cards.append(_assemble(hi, A5="G+", suffix="-ng"))
    elif mode == "confound-triplet":
        base = rungs[len(rungs) // 2]
        for b1 in ("F-rig", "F-neu", "F-buz"):
            cards.append(_assemble(base, B1=b1, suffix="-conf"))
    else:
        raise ValueError(f"unknown mode {mode}")
    return cards
