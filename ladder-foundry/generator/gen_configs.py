"""L7 — deterministic config-generation pipeline.

Wires every STAGE 1/2 component: weights -> ladder_levels (via build_batch) ->
per-rung prose selected by the LOCKED coord (never level_idx) -> assemble
F0..F9 -> validate_card + leak_audit -> config JSON. One placeholder topic in
2A => 6 config personas (the full 48 = 6 rungs x 8 topics waits for D3).
"""
import json
from pathlib import Path

from generator import weights
from generator.axes import level_text
from generator.assembler import build_batch
from generator.cards import PolicyCard, to_dict
from generator.contract import validate_card, A4_TAGS, A5_TAGS
from generator.leak_audit import leak_audit

_PLACEHOLDER_TOPIC = {
    "topic_id": "topic00",
    "F7_prerequisite": "No special prerequisites for this placeholder research topic.",
}

# inverse of the fixed A4/A5 level<->tag convention (contract.py owns the forward map)
_A4_TAG_TO_LEVEL = {tag: lvl for lvl, tag in A4_TAGS.items()}   # "C+"->"L4"
_A5_TAG_TO_LEVEL = {tag: lvl for lvl, tag in A5_TAGS.items()}   # "G+"->"L4"

_B1_FRAMING = {
    "neu": "Frame every request in a neutral, businesslike tone.",
    "buz": "Frame every request in a buzzword-heavy, hype-driven tone.",
}


def _audit_all(card):
    for f in ("F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"):
        # ponytail: 2A prose is static — a hit is an authored-prose bug, so
        # fail loud. The regenerate-then-reaudit retry loop belongs to the
        # later LLM-text path (STAGE 5), which has something to regenerate.
        leak_audit(getattr(card, f))


def build_one(w, card, topic):
    coord = card["coord"]
    if coord is None:
        raise ValueError(
            f"rung {card['rung_id']} coord=None — coord_table not populated; "
            "refusing to fall back to level_idx (label-drift guard)")
    params = card["params"]
    pc = PolicyCard(
        F0=f"Research-supervisor persona at ladder rung {card['rung_id']} of 6.",
        F1=level_text(w, "A1", coord["A1"]),
        F2=level_text(w, "A2", coord["A2"]),
        F3=level_text(w, "A3", coord["A3"]),
        F4=level_text(w, "A4", _A4_TAG_TO_LEVEL[coord["A4"]]),
        F5=level_text(w, "A5", _A5_TAG_TO_LEVEL[coord["A5"]]),
        F6=(f"Accept a reply only when it meets the substance (A1={coord['A1']}), "
            f"operationalization (A3={coord['A3']}), and legitimacy (A2={coord['A2']}) bar."),
        F7=f"Prerequisites: {topic['F7_prerequisite']} Premise stance: {coord['A4']}.",
        F8=f"{params['turn_budget']} turns total for this interaction.",
        F9=_B1_FRAMING.get(coord["B1"], f"Framing tone directive: {coord['B1']}."),
        axis_levels={ax: coord[ax] for ax in ("A1", "A2", "A3", "A4", "A5", "B1")},
    )
    validate_card(pc)
    _audit_all(pc)
    return pc


def gen_configs(w, topic=_PLACEHOLDER_TOPIC, n=6):
    return [build_one(w, card, topic)
            for card in build_batch(w, n=n, topic_id=topic["topic_id"])]


def main(out_dir, w=None):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    if w is None:
        w = weights.dump_initial(str(Path(out_dir) / "_batch0.json"))
    cards = gen_configs(w)
    for card in cards:
        rung = card.F0.split("rung ")[1].split(" ")[0]   # "0".."5" from F0 header
        p = Path(out_dir) / f"config_{rung}.json"
        p.write_text(json.dumps(to_dict(card), indent=2, ensure_ascii=False), encoding="utf-8")
    return cards


if __name__ == "__main__":   # ponytail: thin CLI for the human-eye gate
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "configs")
    print("wrote 6 configs to", sys.argv[1] if len(sys.argv) > 1 else "configs")
