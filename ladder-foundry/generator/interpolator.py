"""L4 ② — pure read of interp_params (spread layer). The rank direction and
the coordinate table are LOCKED (read-only); the spread layer NEVER computes a
coordinate, it only READS coord_table — the locked coordinate layer is
load-bearing by construction (audit requirement).
"""

_L = 5  # number of axis levels L0..L4


def _round_strategy(t):
    # round(t*(L-1)). Python round() is banker's-rounding on exact .5 ties; not
    # biting [0,1,2,2,3,4] for n=6/L=5, but a semantics trap if L/n change.
    return round(t * (_L - 1))


GRANULARITY = {"round": _round_strategy}   # name->curve dispatch, NO eval()


def ladder_levels(w, n=6):
    direction = w["frozen_label"]["rank_order"]["direction"]
    coord_table = w["frozen_label"]["coord_table"]
    offset_axis = w["interp_params"]["collision_offset_axis"]
    strat = GRANULARITY[w["interp_params"]["granularity_map"]]
    rungs = []
    for i in direction[:n]:
        t = i / (n - 1)
        rungs.append({
            "rung_id": i,
            "level_idx": strat(t),
            "collision_offset_axis": offset_axis,
            "coord": coord_table.get(str(i)),   # READ, never computed
        })
    return rungs
