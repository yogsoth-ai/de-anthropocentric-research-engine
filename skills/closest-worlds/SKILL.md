---
name: closest-worlds
description: 'Strategy: Lewis Possible Worlds — find the minimal change to reality
  that would flip the conclusion, measuring how close the nearest world where the
  conclusion fails.'
type: strategy
tactics:
- minimal-change-search
- systematic-factor-ablation
dependencies:
  tactics:
  - minimal-change-search
  - systematic-factor-ablation
  sops:
  - causal-claim-extraction
  - counterfactual-scenario-construction
  - factor-enumeration
  - flip-point-detection
  - fragility-measurement
  - load-bearing-identification
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| minimal-change-search | Tactic: Generate candidate changes, detect flip-points where conclusion reverses, measure fragility as distance to nearest flip. |
| systematic-factor-ablation | Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| counterfactual-scenario-construction | Construct precise, internally consistent counterfactual scenarios where specified factors are altered, then reason about the resulting conclusion. |
| factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| flip-point-detection | Find the minimal change magnitude along a dimension that causes the conclusion to flip from true to false. |
| fragility-measurement | Compute a fragility index from flip-point distances and degradation scores, summarizing how robust the conclusion is. |
| load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |

<!-- END available-tables (generated) -->
