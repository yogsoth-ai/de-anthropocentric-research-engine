---
name: analyze-future-scenarios
description: "Construct and compare plausible future/competitive/temporal/stress scenarios and test whether the research path remains robust across them."
---

# analyze-future-scenarios

## Purpose

Construct and compare plausible future/competitive/temporal/stress scenarios and test whether the research path remains robust across them.

## Input contract

```yaml
required: [research_path, scenario_axes, uncertainty_drivers]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-scenario-drivers` to rank the horizon's high-impact uncertainties.
2. You MUST load skill `enumerate-dimension-values` to enumerate representative, boundary, and adversarial driver values.
3. You MUST load skill `evaluate-compatibility` to prune incompatible combinations while retaining near-boundary cases.
4. You MUST load skill `construct-scenario` to assemble distinct baseline, counterfactual, and extreme-but-plausible worlds.
5. You MUST load skill `evaluate-scenario-impact` to score the research path inside each fixed world and record failure triggers.
6. You MUST load skill `evaluate-scenario-robustness` to aggregate per-world results and expose fragile assumptions.
7. You MUST load skill `predict-competitive-move` to forecast credible competitor moves and preemption risk.
8. You MUST load skill `analyze-temporal-trajectory` to order outcomes through time and reveal regime changes.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [scenario_set, impact_comparison, robustness_assessment]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: experiment-execution/scenario-planning [campaign]
- resolved: morphological-scenario
- resolved: narrative-scenario
- resolved: stress-scenario
- resolved: competitive-scenario
- resolved: temporal-scenario
- resolved: parameter-space-construction
- resolved: cross-consistency-filtering
- resolved: strategy-robustness-testing

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
