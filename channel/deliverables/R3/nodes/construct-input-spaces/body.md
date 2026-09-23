# construct-input-spaces
## Purpose
Define the explicit source spaces used by conceptual blending.
## Input contract
```yaml
required: [source_domains, blend_goal]
optional: [entities, relations, constraints, salient_dynamics]
constraints: [each source needs entities, relations, goals, and constraints or an explicit unknown]
```
## Procedure
1. Partition each source domain into entities, relations, goals, constraints, and dynamics.
2. Normalize equivalent roles without erasing source-specific structure.
3. Record the blend goal and the items eligible for projection.
## Output contract
```yaml
produces: [input_space_set, normalized_roles, projection_candidates]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- Every input space is independently reconstructible and source-specific relations remain visible.
## Failure and counterexamples
Reject an input space that is only a keyword list or that merges incompatible roles before blending.
## Provenance map
- `conceptual-blending/input-space-construction`: resolved.
