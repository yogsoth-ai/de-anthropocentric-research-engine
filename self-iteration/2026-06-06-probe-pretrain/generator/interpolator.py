# 可训练权重②：路径铺设规则。optimizer 可改 level 映射与塌档扰动策略。


def ladder_levels(n: int):
    """给定 n 档，返回每档的 {A1,A3,A2} 等级标签（梯子主轴）。"""
    rungs = []
    for i in range(n):
        t = i / (n - 1)
        lvl = round(t * 4)  # → 0..4
        tag = f"L{lvl}"
        rungs.append({"A1": tag, "A3": tag, "A2": tag, "t": t})
    return rungs


def detect_collapse(rungs):
    """返回相邻塌档的 (i, i+1) 对（A1 等级相同）。"""
    out = []
    for i in range(len(rungs) - 1):
        if rungs[i]["A1"] == rungs[i + 1]["A1"]:
            out.append((i, i + 1))
    return out


def secondary_perturbation(rung, bump: int):
    """塌档补救：在同一等级内扰动二级旋钮（追问次数 bump），拉开相邻档。"""
    r = dict(rung)
    r["followup_bump"] = bump
    return r


def rung_count_default() -> int:
    return 6
