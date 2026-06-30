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
    # D2: real endpoint + intermediate persona prose. axis_prose stays
    # L0..L4-indexed for all 5 axes (STAGE 1 schema lock). A4/A5 unused slots
    # carry a short placeholder (never selected: coord[axis] only names a used
    # level). All bodies are leak-clean (W5) — no check/primitive vocabulary.
    return {
        "A1": {
            "L0": "Accepts whatever is offered and asks for nothing more; makes no demand on the substance of an answer.",
            "L1": "Occasionally nudges for a little more depth but is satisfied quickly.",
            "L2": "Expects a reasonable amount of substance and pushes back when an answer is thin.",
            "L3": "Demands well-supported substance and keeps pressing where an answer is underdeveloped.",
            "L4": "Relentlessly demands the deepest possible substance, never satisfied until every claim is fully grounded.",
        },
        "A2": {
            "L0": "Makes incoherent, self-contradictory requests with no legitimate through-line.",
            "L1": "Requests are mostly muddled, with only occasional coherence.",
            "L2": "Requests are workable though sometimes loosely framed.",
            "L3": "Requests are clear, coherent, and well-motivated.",
            "L4": "Every request is fully coherent, legitimate, and precisely scoped.",
        },
        "A3": {
            "L0": "Never asks for anything to be made concrete or operational; abstractions are fine as-is.",
            "L1": "Rarely asks how something would actually be done.",
            "L2": "Sometimes asks for a concrete procedure when it matters.",
            "L3": "Usually insists that proposals be turned into operational steps.",
            "L4": "Insists relentlessly that every idea be operationalized into concrete, executable steps.",
        },
        "A4": {
            "L0": "Clings to original premises and resists any correction even when shown to be wrong.",
            "L1": "(unused A4 slot)",
            "L2": "Will revise a premise when given a clear reason.",
            "L3": "(unused A4 slot)",
            "L4": "Readily corrects own premises the moment a better framing appears.",
        },
        "A5": {
            "L0": "Stays narrowly on the single given thread; spawns no new directions.",
            "L1": "(unused A5 slot)",
            "L2": "(unused A5 slot)",
            "L3": "(unused A5 slot)",
            "L4": "Generatively spawns new research directions and adjacent questions from any starting point.",
        },
    }


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
