# identify-obstacles
## Purpose
Enumerate obstacles blocking a target goal or direction, with evidence and blocking relations.
## Input contract
```yaml
required: [target_goal, current_state, domain_context]
optional: [timeline, resource_inventory, prior_failures]
constraints: [each obstacle has type, evidence, and blocking relation]
```
## Procedure
1. Compare target requirements with current capabilities and constraints.
2. Enumerate technical, evidential, resource, temporal, and dependency obstacles.
3. Link each obstacle to blocked outcomes and supporting evidence.
4. Return severity, uncertainty, and candidate removal questions.
## Output contract
```yaml
produces: [obstacle_register, blocking_relations, evidence_links, removal_questions]
delta_fields: [findings, uncertainties, open_questions]
```
## Quality gates
- Every listed obstacle has a blocking relation and evidence or an explicit uncertainty label.
- Duplicate obstacles are merged only when mechanism and remedy coincide.
- Obstacles are separated from symptoms and desired outcomes.
## Parameterization
Caller supplies goal schema, obstacle taxonomy, evidence fields, severity scale, and merge policy.
## Failure and counterexamples
Reject generic risks, unsupported blockers, or lists with no relation to the target goal.
## Provenance map
- concept: north-star-crystallization/identify-obstacles
- concept: experiment-execution/obstacle-identification
