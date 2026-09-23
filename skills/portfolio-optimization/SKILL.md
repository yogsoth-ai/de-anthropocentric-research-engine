---
name: portfolio-optimization
description: "Formalize objectives/constraints, construct a Pareto frontier, stress across scenarios, and select a robust portfolio."
---

# portfolio-optimization

## Purpose

Formalize objectives/constraints, construct a Pareto frontier, stress across scenarios, and select a robust portfolio.

## Input contract

```yaml
required: [candidate_set, objective_vector, resource_constraints, scenario_set]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `define-objective` to declare outcome directions, hard constraints, stakeholder scope, horizon, and permissible tradeoffs before comparing candidates.
2. You MUST load skill `optimize-pareto-frontier` to remove infeasible candidates and retain only points not dominated across the normalized objective dimensions.
3. You MUST load skill `construct-scenario` to stress each surviving candidate or portfolio under a fixed scenario and expose impact, tradeoffs, and failure triggers.
4. You MUST load skill `evaluate-scenario-impact` to evaluate the current portfolio inside each scenario using stable criteria, explicit missingness, and counterexamples.
5. You MUST load skill `select-from-frontier` to apply the preference policy and document the chosen point, sacrificed objectives, and nearest alternatives.
6. You MUST load skill `measure-portfolio-diversity` to quantify coverage and reveal concentration and niche collapse.
7. You MUST load skill `map-dependencies` to map dependencies, cycles, critical paths, and independent branches before committing to an execution order.
8. You MUST load skill `sequence-work` to topologically order the dependent work while surfacing fail-fast and high-risk branches.
9. You MUST load skill `evaluate-optionality` to compare immediate, deferred, staged, and information-gathering actions by reversibility, delay cost, and trigger conditions.
10. You MUST load skill `evaluate-scenario-robustness` to aggregate scenario results and state which portfolio assumptions remain fragile.
    If the selected portfolio needs a strong challenge before commitment, consider `adversarial-deliberation` as the next tactic.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [pareto_frontier, selected_portfolio, scenario_risk_summary]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

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
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
