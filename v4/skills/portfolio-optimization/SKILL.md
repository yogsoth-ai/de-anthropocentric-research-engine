---
name: portfolio-optimization
description: "Formalize objectives/constraints, construct a Pareto frontier, stress across scenarios, and select a robust portfolio."
---

# portfolio-optimization

## Purpose

Formalize objectives/constraints, construct a Pareto frontier, stress across scenarios, and select a robust portfolio.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Formalize objectives, dependencies, resource limits, and scenario assumptions for the candidate portfolio. (`define-objective`)
2. Construct the Pareto frontier, test impact and robustness across scenarios, and measure diversity and optionality. (`optimize-pareto-frontier`)
3. Select a feasible portfolio and sequence it with a traceable tradeoff and residual risk statement. (`construct-scenario`)
4. Formalize objectives, dependencies, resource limits, and scenario assumptions for the candidate portfolio. (`evaluate-scenario-impact`)
5. Construct the Pareto frontier, test impact and robustness across scenarios, and measure diversity and optionality. (`select-from-frontier`)
6. Select a feasible portfolio and sequence it with a traceable tradeoff and residual risk statement. (`measure-portfolio-diversity`)
7. Formalize objectives, dependencies, resource limits, and scenario assumptions for the candidate portfolio. (`map-dependencies`)
8. Construct the Pareto frontier, test impact and robustness across scenarios, and measure diversity and optionality. (`sequence-work`)
9. Select a feasible portfolio and sequence it with a traceable tradeoff and residual risk statement. (`evaluate-optionality`)
10. Formalize objectives, dependencies, resource limits, and scenario assumptions for the candidate portfolio. (`evaluate-scenario-robustness`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [pareto_frontier, selected_portfolio, scenario_risk_summary]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: portfolio-optimization [campaign]
- resolved: value-maximization
- resolved: diversity-maximization
- resolved: risk-balancing
- resolved: temporal-sequencing
- resolved: robustness-under-uncertainty
- resolved: pareto-frontier-construction
- resolved: scenario-stress-testing
- resolved: niche-coverage-analysis

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
