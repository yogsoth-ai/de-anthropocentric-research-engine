---
name: ladder-quality-order
description: loss-2 judge - pairwise quality comparison across the n rungs within one topic; decide monotonicity and endpoint separation. check-blind, D1-D5 only.
---

# ladder-quality-order (loss-2)

You receive: the n samples under one topic, each with (research_graph, research_result),
plus their intended_order (the id order from the interpolator: id0 should be best ->
idN-1 should be worst).

## Task (pairwise ranking, no absolute scores)
1. Enumerate all i<j pairs; for each pair ask: **in the D1-D5 sense, which research design
   is more substantive?** (D1 more meaningful / D2 more skill-research value / D3 more
   usable to DARE / D4 better respects the 4 layers / D5 firmer prerequisites). Output
   winner + a one-line reason.
2. Aggregate into an induced order; compute Kendall tau against intended_order.
3. Endpoints: directly compare id0 vs idN-1; across K repeats, check whether id0 wins stably.

## Output (JSON)
{"tau": float, "monotonicity_pass": bool,   // tau>=0.7 and no endpoint inversion
 "endpoint_separation_pass": bool,          // id0 wins >= K-allowance of K repeats
 "rigor_floor_flag": bool,                  // if id0 ~ idN-1 endpoints collapse (feed risk register)
 "pairwise_log": [{i,j,winner,reason}]}

## check-blind contract (hard constraint)
- The judge prompt may use **only** D1-D5 wording.
- **Forbidden**: 32-check vocabulary, 6-primitive, "pseudo-good/novel-good" categories,
  any detection signature.
- z-perp-C: on the B1 confound triplet (same substance, different framing) your order
  **must stay invariant**; if it varies with framing -> you were dragged by the confound,
  tighten back to D1-D5 substance.
