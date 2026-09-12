# evaluate-scenario-robustness
## Purpose
Aggregate candidate performance across explicit scenarios under a declared robust-decision rule.
## Input contract
```yaml
required: [candidate_set, scenario_set, criterion_results, robustness_rule]
optional: [regret_definition, survival_thresholds, pivot_triggers]
constraints: [scenario results use common criteria and direction]
```
## Procedure
1. Verify scenario comparability and criterion direction.
2. Apply the supplied rule: worst-case, minimax regret, maximin, survival, or pivot trigger.
3. Expose scenario-specific failures and tradeoffs.
4. Return ranking, rule sensitivity, and pivot conditions.
## Output contract
```yaml
produces: [robustness_assessment, robust_ranking, regret_or_worst_case, pivot_triggers]
delta_fields: [findings, decisions, uncertainties]
```
## Quality gates
- At least 3 distinct futures are evaluated when the scenario set is intended to span uncertainty.
- Rule is declared before aggregation and applied consistently.
- A candidate failing a survival threshold is not rescued by averaging.
## Parameterization
Caller supplies scenario schema, criterion scales, aggregation rule, regret/survival definitions, and pivot policy.
## Failure and counterexamples
Reject hidden scenario weighting, incomparable metrics, or robustness claims from a single future.
## Provenance map
- concept: experiment-execution/robustness-scoring
- concept: experiment-execution/strategy-robustness-testing
- concept: convergence/portfolio-optimization/robustness-under-uncertainty
- intermediate: Pass8/score-scenario-robustness
- intermediate: Pass8/evaluate-regret-robustness
