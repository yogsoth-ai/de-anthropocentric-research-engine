"""L1 — the data-core: 4-segment weights schema + load/dump_initial/revise.

Data-oriented principle: training changes the JSON DATA segments only; this
source never moves. frozen_label is NOT trainable (dump_initial is its sole
writer). interp_params key-set is structurally locked (AS-3).
"""
import json
from pathlib import Path

TRAINABLE = {"axis_prose", "interp_params", "assembler_params"}
AXES = {"A1", "A2", "A3", "A4", "A5"}
LEVELS = {"L0", "L1", "L2", "L3", "L4"}
INTERP_KEYS = {"collision_offset_axis", "endpoint_spread", "granularity_map"}
COLLISION_ENUM = {"B1", "expression"}


def _default_axis_prose():
    # ponytail: seed prose only — STAGE 2 (D2 endpoint personas) authors the
    # real bodies. STAGE 1 just needs structure to prove read/write/lock.
    return {axis: {level: f"{axis}.{level} seed prose" for level in sorted(LEVELS)}
            for axis in sorted(AXES)}


def _check_interp_keyset(w):
    got = set(w["interp_params"].keys())
    if got != INTERP_KEYS:
        raise ValueError(f"interp_params key-set locked to {INTERP_KEYS}, got {got}")


def dump_initial(path):
    """Export batch-0 from the three weights' defaults. SOLE writer of frozen_label."""
    w = {
        "axis_prose": _default_axis_prose(),
        "interp_params": {
            "collision_offset_axis": "B1",
            "endpoint_spread": 1.0,
            "granularity_map": "round",
        },
        "assembler_params": {
            "two_stage": {"pressure_turns": 10, "closing_turns": 2},
            "field_template": {"F0": "research supervisor"},
            "f6_derivation": "derived_from:A1+A3+A2",
            "turn_budget": 12,
        },
        "frozen_label": {
            "rank_order": {"direction": [0, 1, 2, 3, 4, 5], "primary_sort": ["A1", "A3", "A2"]},
            "coord_table": {},
        },
    }
    Path(path).write_text(json.dumps(w, indent=2, ensure_ascii=False), encoding="utf-8")
    return w


def load(path):
    w = json.loads(Path(path).read_text(encoding="utf-8"))
    _check_interp_keyset(w)
    return w


def revise(w, target, key, new, reason):
    if target == "frozen_label":
        raise ValueError("frozen_label not trainable (lifeline of the label)")
    if target not in TRAINABLE:
        raise ValueError(f"unknown target {target!r}")
    _check_interp_keyset(w)
    if target == "axis_prose":
        parts = key.split(".")
        if len(parts) != 2:
            raise ValueError(f"axis_prose key must be 'AXIS.LEVEL', got {key!r}")
        axis, level = parts
        if axis not in AXES or level not in LEVELS:
            raise ValueError(f"unknown axis/level in {key!r}")
        old = w["axis_prose"][axis][level]
        w["axis_prose"][axis][level] = new
    else:
        if key not in w[target]:
            raise ValueError(f"unknown key {key!r} for {target}")
        if target == "interp_params" and key == "collision_offset_axis" and new not in COLLISION_ENUM:
            raise ValueError(f"collision_offset_axis must be B1/expression, got {new!r}")
        old = w[target][key]
        w[target][key] = new
    return {"target": target, "key": key, "old": old, "new": new, "reason": reason}
