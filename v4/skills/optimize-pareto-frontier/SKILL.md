---
name: optimize-pareto-frontier
description: "Generate a non-dominated frontier for a multi-objective candidate/portfolio problem."
---

# optimize-pareto-frontier
## Purpose
Generate a non-dominated frontier for a multi-objective candidate or portfolio problem while preserving objective tradeoffs.
## Input contract
```yaml
required: [candidate_set, objective_schema, constraint_schema, evaluation_records]
optional: [dominance_rule, feasibility_policy, tie_policy]
constraints: [objective directions, scales, feasibility rules, and missing-value handling are explicit]
```
## Procedure
1. Normalize candidate evaluations to the declared objective directions and units without erasing provenance.
2. Remove infeasible candidates according to hard constraints and mark unknown feasibility separately.
3. Compare every feasible candidate pair for dominance; retain candidates not dominated on all objectives.
4. Verify frontier membership, record sacrificed objectives, and emit unresolved comparisons.
## Output contract
```yaml
produces: [pareto_frontier, dominance_matrix, excluded_candidates, unresolved_comparisons]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- Frontier membership requires a complete comparison against all declared objectives or an explicit unresolved flag.
- A candidate excluded by dominance includes the dominating candidate and the objective-wise evidence.
## Failure and counterexamples
Do not collapse objectives into one score unless the objective schema explicitly authorizes it. Unknown values cannot establish dominance.
## Provenance map
- resolved: optimization-run
