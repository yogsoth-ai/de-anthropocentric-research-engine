# define-objective
## Purpose
Formalize objectives, constraints, and tradeoff preferences before an optimization or selection decision.
## Input contract
```yaml
required: [decision_context, candidate_set, stakeholder_preferences]
optional: [hard_constraints, utility_scale, priority_weights]
constraints: [objectives are measurable or operationalized; tradeoffs and constraint direction are explicit]
```
## Procedure
1. Elicit the desired outcome, affected scope, stakeholders, and time horizon.
2. Separate objectives from constraints and preferences, then define each objective's direction and measurement.
3. Record conflicts, permissible tradeoffs, and any weights or lexicographic priorities with their rationale.
4. Emit an objective schema suitable for comparison, optimization, and later audit.
## Output contract
```yaml
produces: [objective_schema, constraint_schema, tradeoff_policy, unresolved_preferences]
delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class gate: declared universe = all stakeholder objectives and hard constraints in scope; numerator = items operationalized with direction, measurement, and source; batch increment = one objective or constraint formalized; stopping reason = all items formalized or unresolved conflicts are explicit; source references = stakeholder, requirement, and decision IDs; direction/threshold reason = an objective enters optimization only when its direction and acceptable tradeoff boundary are explicit.
- At least two distinct objectives and one constraint are required unless the decision record justifies a narrower scope.
## Failure and counterexamples
Do not encode a preferred solution as an objective. If two stakeholders use the same word for different outcomes, preserve separate definitions.
## Provenance map
- resolved: objective-definition
