---
name: closest-worlds
description: "Strategy: Lewis Possible Worlds — find the minimal change to reality that would flip the conclusion, measuring how close the nearest world where the conclusion fails."
type: strategy
used-by: [counterfactual-probing]
tactics: [minimal-change-search, systematic-factor-ablation]
---

# Closest Worlds Strategy

Lewis semantics: evaluate counterfactuals by finding the nearest possible world where the antecedent holds and checking whether the consequent follows.

## Method

1. **causal-claim-extraction** identifies the conclusion and its supporting factors
2. **factor-enumeration** maps the space of possible changes
3. **flip-point-detection** searches for minimal changes that flip the conclusion
4. **counterfactual-scenario-construction** builds the nearest world where conclusion fails
5. **fragility-measurement** computes distance from actuality to flip-point
6. **load-bearing-identification** ranks factors by proximity to flip

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Change candidates explored | 5 | 12 | 25 |
| Flip-point searches | 3 | 8 | 15 |
| World-distance comparisons | 3 | 6 | 12 |

## Orchestration

```
causal-claim-extraction → factor-enumeration
→ [generate change candidates]:
    flip-point-detection (binary search for minimal flip)
    → counterfactual-scenario-construction (build nearest world)
    → fragility-measurement (compute distance)
→ load-bearing-identification (rank by proximity)
```

## Subagents

- causal-claim-extraction (conclusion identification)
- factor-enumeration (change space mapping)
- flip-point-detection (minimal flip search)
- counterfactual-scenario-construction (world building)
- fragility-measurement (distance computation)
- load-bearing-identification (proximity ranking)
