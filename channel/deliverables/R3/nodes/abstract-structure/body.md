# abstract-structure
## Purpose
Strip domain surface detail and retain transferable relations or mechanisms at a declared abstraction level.
## Input contract
```yaml
required: [source_case, abstraction_level]
optional: [relation_schema, invariants]
constraints: [preserve causal or functional roles while removing incidental labels]
```
## Procedure
1. List entities, actions, constraints, and outcomes in the source case.
2. Replace domain labels with role and relation types at the requested level.
3. Record invariants and details intentionally discarded.
## Output contract
```yaml
produces: [abstract_structure, retained_invariants, discarded_details]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- The abstraction level is named; every retained relation has source support; no causal relation is introduced by analogy.
## Failure and counterexamples
Return an abstraction gap when role mapping is ambiguous or when removing a detail changes the mechanism.
## Provenance map
- `creative-ideation/abstraction-extraction`: resolved.
- `creative-ideation/abstraction-ladder`: resolved.
- `creative-ideation/generic-space-extraction`: resolved.
