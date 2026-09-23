# map-coverage-space
## Purpose
Map methods, assets, or evidence against a typed problem or capability space to expose redundancy and gaps.
## Input contract
```yaml
required: [item_set, coverage_dimensions, target_space]
optional: [strength_scale, applicability_rules, evidence_links]
constraints: [dimension semantics and coverage states are declared]
```
## Procedure
1. Define cells or regions from the supplied dimensions.
2. Assign each item to supported, partial, or unsupported regions.
3. Merge duplicate coverage and identify uncovered or weakly supported regions.
4. Return the map with evidence and confidence annotations.
## Output contract
```yaml
produces: [coverage_map, redundancy_clusters, gap_register, confidence_annotations]
delta_fields: [findings, evidence_updates, uncertainties]
```
## Quality gates
- Every assignment names its dimensions and evidence.
- Coverage ratio is computed from a declared universe and numerator/denominator.
- Weak and missing coverage are distinguished.
## Parameterization
Caller supplies item schema, dimension ontology, coverage states, strength scale, and audit numerator/denominator definitions.
## Failure and counterexamples
Reject maps with implicit dimensions, unsupported assignments, or ratios lacking a declared universe.
## Provenance map
- concept: creative-ideation/method-problem-crossing
- concept: knowledge-acquisition/capability-taxonomy-mapping
- intermediate: Pass3/map-method-problem-space
- intermediate: Pass3/map-capability-coverage
