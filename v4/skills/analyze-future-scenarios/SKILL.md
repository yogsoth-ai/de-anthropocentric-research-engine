---
name: analyze-future-scenarios
description: "Construct and compare plausible future/competitive/temporal/stress scenarios and test whether the research path remains robust across them."
---

# analyze-future-scenarios

## Purpose

Construct and compare plausible future/competitive/temporal/stress scenarios and test whether the research path remains robust across them.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Define the time horizon, scenario axes, and driver uncertainties that can change the research path. (`identify-scenario-drivers`)
2. Construct internally compatible scenarios and compare impact, competitive timing, temporal trajectory, and robustness. (`enumerate-dimension-values`)
3. Select the conclusions that survive scenario variation and mark the assumptions that make them fragile. (`evaluate-compatibility`)
4. Define the time horizon, scenario axes, and driver uncertainties that can change the research path. (`construct-scenario`)
5. Construct internally compatible scenarios and compare impact, competitive timing, temporal trajectory, and robustness. (`evaluate-scenario-impact`)
6. Select the conclusions that survive scenario variation and mark the assumptions that make them fragile. (`evaluate-scenario-robustness`)
7. Define the time horizon, scenario axes, and driver uncertainties that can change the research path. (`predict-competitive-move`)
8. Construct internally compatible scenarios and compare impact, competitive timing, temporal trajectory, and robustness. (`analyze-temporal-trajectory`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [scenario_set, impact_comparison, robustness_assessment]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: scenario-planning
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
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
