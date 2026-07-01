"""L5 ③ — pure read of assembler_params. Assembles one coordinate card per
rung. The ONLY perturbation source is each rung's collision_offset_axis
(∈{B1,expression}); there is no path to an A1–A5 label axis — the schema lock
guarantees it.
"""
from generator.interpolator import ladder_levels


def build_batch(w, n, topic_id):
    params = w["assembler_params"]
    cards = []
    for rung in ladder_levels(w, n=n):
        cards.append({
            "topic_id": topic_id,
            "rung_id": rung["rung_id"],
            "level_idx": rung["level_idx"],
            "perturb_axis": rung["collision_offset_axis"],
            "coord": rung["coord"],
            "params": params,
        })
    return cards
