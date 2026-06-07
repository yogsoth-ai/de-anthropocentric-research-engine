# Trainable weight 2: path-laying rules. The optimizer may edit the level mapping and collapse-perturbation strategy.


def ladder_levels(n: int):
    """Given n rungs, return each rung's {A1,A3,A2} level tags (the ladder spine)."""
    rungs = []
    for i in range(n):
        t = i / (n - 1)
        lvl = round(t * 4)  # -> 0..4
        tag = f"L{lvl}"
        rungs.append({"A1": tag, "A3": tag, "A2": tag, "t": t})
    return rungs


def detect_collapse(rungs):
    """Return adjacent collapsed pairs (i, i+1) where the A1 level is identical."""
    out = []
    for i in range(len(rungs) - 1):
        if rungs[i]["A1"] == rungs[i + 1]["A1"]:
            out.append((i, i + 1))
    return out


def secondary_perturbation(rung, bump: int):
    """Collapse remedy: perturb a secondary knob (followup count bump) within the same level to separate adjacent rungs."""
    r = dict(rung)
    r["followup_bump"] = bump
    return r


def rung_count_default() -> int:
    return 6

