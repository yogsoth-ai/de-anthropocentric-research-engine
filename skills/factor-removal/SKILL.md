---
name: factor-removal
description: 'Strategy: Systematic factor removal — remove factors one at a time and
  observe whether the conclusion remains stable, identifying which factors are load-bearing.'
type: strategy
tactics:
- systematic-factor-ablation
- minimal-change-search
dependencies:
  tactics:
  - minimal-change-search
  - systematic-factor-ablation
  sops:
  - counterfactual-scenario-construction
  - factor-enumeration
  - flip-point-detection
  - fragility-measurement
  - load-bearing-identification
  - single-factor-removal
---

# Factor Removal Strategy

Ablation study approach: systematically remove each factor and observe conclusion stability.

## Method

1. **factor-enumeration** lists all factors supporting the conclusion
2. **single-factor-removal** removes one factor at a time
3. **counterfactual-scenario-construction** reasons about the modified scenario
4. **fragility-measurement** scores how much the conclusion degrades
5. **load-bearing-identification** ranks factors by impact of removal
6. Optional: **flip-point-detection** for partial removal (dose-response)

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Factors removed | 5 | 10 | 20 |
| Removal iterations | 1 | 2 | 3 |
| Combination removals | 0 | 3 | 8 |

## Orchestration

```
factor-enumeration → [rank by suspected importance]
→ [for each factor]:
    single-factor-removal
    → counterfactual-scenario-construction
    → fragility-measurement
→ [if budget allows, test combinations]:
    single-factor-removal (multiple factors)
    → counterfactual-scenario-construction
→ load-bearing-identification (final ranking)
```

## Subagents

- factor-enumeration (factor listing)
- single-factor-removal (ablation)
- counterfactual-scenario-construction (scenario reasoning)
- fragility-measurement (degradation scoring)
- load-bearing-identification (ranking)
- flip-point-detection (dose-response, optional)
