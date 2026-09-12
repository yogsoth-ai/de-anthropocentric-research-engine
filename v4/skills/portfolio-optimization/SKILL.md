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

1. Declare outcome directions, hard constraints, stakeholder scope, horizon, and permissible tradeoffs before comparing candidates. (`define-objective`)
2. Remove infeasible candidates and retain only points not dominated across the normalized objective dimensions. (`optimize-pareto-frontier`)
3. Stress each surviving candidate or portfolio under a fixed scenario to expose impact, tradeoffs, and failure triggers. (`construct-scenario`)
4. Evaluate the current portfolio inside each scenario using stable criteria, explicit missingness, and counterexamples. (`evaluate-scenario-impact`)
5. Apply the preference policy to the current frontier and document the chosen point, sacrificed objectives, and nearest alternatives. (`select-from-frontier`)
6. Quantify coverage across the declared feature or failure-mode dimensions to reveal concentration and niche collapse. (`measure-portfolio-diversity`)
7. Map dependencies, cycles, critical paths, and independent branches before committing to an execution order. (`map-dependencies`)
8. Topologically order the dependent work while surfacing fail-fast and high-risk branches for the decision record. (`sequence-work`)
9. Compare immediate, deferred, staged, and information-gathering actions by reversibility, delay cost, and trigger conditions. (`evaluate-optionality`)
10. Aggregate scenario results under the declared robust-decision rule and state which portfolio assumptions remain fragile. (`evaluate-scenario-robustness`)

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
