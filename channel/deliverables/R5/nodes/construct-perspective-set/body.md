# construct-perspective-set
## Purpose
Construct an explicit set of relevant viewpoints or epistemic lenses for one object.
## Input contract
```yaml
required: [target_object, perspective_basis, selection_goal]
optional: [stakeholder_set, domain_roles, worldview_constraints]
constraints: [each perspective must have a distinct warrant and scope]
```
## Procedure
1. Enumerate candidate roles, worldviews, and stakeholder positions.
2. Select a coverage-complete set and state inclusion rationale.
3. Record each lens's assumptions, objectives, and blind spots.
4. Return the set with mapping to the target object.
## Output contract
```yaml
produces: [perspective_set, selection_rationale, assumption_map, blind_spot_map]
delta_fields: [findings, assumptions_updates, uncertainties]
```
## Quality gates
- Perspectives are non-duplicate and relevant to the target.
- At least 3 stakeholder or worldview lenses and 4 role lenses are used when applicable.
- At least 2 previously overlooked framings are recorded when the caller requests reframing.
## Parameterization
Caller supplies target schema, perspective taxonomy, minimum counts, relevance test, and overlap policy.
## Failure and counterexamples
Reject decorative personas, duplicate lenses, or perspectives lacking a changed assumption or objective.
## Provenance map
- concept: multi-worldview-comparison
- concept: six-thinking-hats
- concept: role-storming
- concept: stakeholder-objection-simulation
