---
name: structural-counterfactual
description: "Strategy: Pearl Three-Step counterfactual — Abduction (fit model to evidence), Action (intervene on factor), Prediction (derive counterfactual outcome)."
type: strategy
used-by: [counterfactual-probing]
tactics: [systematic-factor-ablation, causal-necessity-testing]
---

# Structural Counterfactual Strategy

Pearl Three-Step: Abduction, Action, Prediction applied to artifact validation.

## Method

1. **causal-claim-extraction** identifies causal structure in the artifact
2. **factor-enumeration** lists all factors in the causal model
3. **Abduction**: fit background variables to observed evidence
4. **Action**: **single-factor-removal** intervenes on one factor at a time
5. **Prediction**: **counterfactual-scenario-construction** derives new outcome
6. **necessity-evaluation** and **sufficiency-evaluation** score each factor
7. **load-bearing-identification** synthesizes results

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Factors modeled | 5 | 10 | 20 |
| Interventions per factor | 1 | 2 | 4 |
| Prediction depth | 2 | 4 | 8 |

## Orchestration

```
causal-claim-extraction → factor-enumeration
→ [for each factor]:
    single-factor-removal (abduction + action)
    → counterfactual-scenario-construction (prediction)
    → necessity-evaluation + sufficiency-evaluation
→ load-bearing-identification → fragility-measurement
```

## Subagents

- causal-claim-extraction (model building)
- factor-enumeration (variable identification)
- single-factor-removal (intervention)
- counterfactual-scenario-construction (prediction)
- necessity-evaluation (PN scoring)
- sufficiency-evaluation (PS scoring)
- load-bearing-identification (synthesis)
- fragility-measurement (aggregation)
