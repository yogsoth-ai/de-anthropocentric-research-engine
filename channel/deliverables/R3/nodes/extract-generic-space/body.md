# extract-generic-space
## Purpose
Infer the shared abstract relational structure common across conceptual-blend input spaces.
## Input contract
```yaml
required: [input_space_set]
optional: [candidate_relations, blend_goal]
constraints: [generic relations must be present in at least two input spaces]
```
## Procedure
1. Compare roles and relations across the input spaces.
2. Keep only shared structure and mark source-specific attributes.
3. Validate the generic space against the blend goal before projection.
## Output contract
```yaml
produces: [generic_space, shared_relations, excluded_attributes]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- Every generic relation has at least two source traces; source-specific structure is not silently generalized.
## Failure and counterexamples
Return no generic space when the inputs share only vocabulary or when relation alignment is ambiguous.
## Provenance map
- `conceptual-blending/generic-space`: concept (no exact pool entry).
