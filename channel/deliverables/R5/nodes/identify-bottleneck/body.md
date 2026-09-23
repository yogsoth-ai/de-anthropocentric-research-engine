# identify-bottleneck
## Purpose
Identify the limiting dimension or dependency currently constraining progress.
## Input contract
```yaml
required: [goal_state, dependency_or_factor_set, progress_evidence]
optional: [capacity_limits, intervention_history, bottleneck_definition]
constraints: [bottleneck claim requires a limiting relation and evidence]
```
## Procedure
1. Map factors and dependencies to the blocked outcome.
2. Compare capacities, delays, and failure frequencies.
3. Test candidate limits by tracing counterfactual relief or substitution.
4. Return primary bottleneck, alternatives, and evidence gaps.
## Output contract
```yaml
produces: [bottleneck_assessment, limiting_relation, candidate_reliefs, evidence_gaps]
delta_fields: [findings, decisions, uncertainties]
```
## Quality gates
- Limiting dimension is distinguished from a visible symptom.
- At least one alternative bottleneck is considered when evidence allows.
- Claimed bottleneck has a traceable dependency or capacity relation.
## Parameterization
Caller supplies goal schema, dependency graph, capacity metrics, bottleneck definition, and counterfactual test.
## Failure and counterexamples
Reject bottlenecks inferred from salience alone or without a relation to the blocked outcome.
## Provenance map
- concept: convergence/bottleneck-identification
- concept: deep-insight/critical-path-identification
