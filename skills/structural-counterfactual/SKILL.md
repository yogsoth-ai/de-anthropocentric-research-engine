---
name: structural-counterfactual
description: 'Strategy: Pearl Three-Step counterfactual — Abduction (fit model to
  evidence), Action (intervene on factor), Prediction (derive counterfactual outcome).'
type: strategy
tactics:
- systematic-factor-ablation
- causal-necessity-testing
dependencies:
  tactics:
  - causal-necessity-testing
  - systematic-factor-ablation
  sops:
  - causal-claim-extraction
  - counterfactual-scenario-construction
  - factor-enumeration
  - fragility-measurement
  - load-bearing-identification
  - necessity-evaluation
  - single-factor-removal
  - sufficiency-evaluation
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| causal-necessity-testing | Tactic: Extract causal claims, evaluate probability of necessity (PN) and sufficiency (PS) for each, classify into necessity-sufficiency quadrants. |
| systematic-factor-ablation | Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| counterfactual-scenario-construction | Construct precise, internally consistent counterfactual scenarios where specified factors are altered, then reason about the resulting conclusion. |
| factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| fragility-measurement | Compute a fragility index from flip-point distances and degradation scores, summarizing how robust the conclusion is. |
| load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |
| necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor — would the conclusion fail if this factor were absent? |
| single-factor-removal | Remove one specified factor from the artifact's support structure and reason about how the conclusion changes. |
| sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor — would this factor alone be enough to produce the conclusion? |

<!-- END available-tables (generated) -->
