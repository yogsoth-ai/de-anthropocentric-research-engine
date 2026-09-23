---
name: select-from-frontier
description: "Select a preferred frontier point/portfolio and state the sacrificed alternatives/tradeoffs."
---

# select-from-frontier
## Purpose
Select a preferred point or portfolio from a Pareto frontier and state the sacrificed alternatives and tradeoffs.
## Input contract
```yaml
required: [pareto_frontier, preference_policy, objective_schema, decision_context]
optional: [tie_breaker, stakeholder_weights, robustness_report]
constraints: [preference direction and acceptable sacrifice bounds are explicit]
```
## Procedure
1. Confirm that each selectable point is feasible and that frontier membership is current.
2. Apply the declared preference policy or tie-breaker to frontier points, preserving objective values.
3. Record the selected point, nearest alternatives, sacrificed objectives, and sensitivity to preference changes.
4. Emit the selection rationale and a re-open trigger if the preference or evidence changes.
## Output contract
```yaml
produces: [selected_frontier_point, tradeoff_record, rejected_alternatives, reopen_trigger]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- Selection includes the chosen point, its frontier position, at least one rejected alternative, and the sacrificed objective.
- A tie is resolved only by a declared tie-breaker; otherwise return co-preferred points.
## Failure and counterexamples
Do not select an interior point as if it were a frontier compromise. If preferences are missing, return the frontier and request a policy.
## Provenance map
- resolved: selection-from-frontier
