# map-analogy
## Purpose
Map source structures, relations, or functions to a target and annotate match quality.
## Input contract
```yaml
required: [source_structure, target_structure, mapping_basis]
optional: [source_constraints, target_constraints]
constraints: [mapping basis must specify structural, functional, or relational correspondence]
```
## Procedure
1. Align source and target entities by role rather than label.
2. Map relations and functions, recording one-to-one, many-to-one, and unmatched cases.
3. Rate each correspondence and identify structural gaps requiring validation.
## Output contract
```yaml
produces: [analogy_map, correspondence_quality, unmapped_relations]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- All claimed correspondences have a basis and quality note; unmatched relations remain explicit.
## Failure and counterexamples
Reject surface-only mappings and mappings that hide incompatible directionality or constraints.
## Provenance map
- `creative-ideation/vital-relation-mapping`: resolved.
- `creative-ideation/analogy-quality-assessment`: resolved.
- `creative-ideation/biological-function-mapping`: resolved.
