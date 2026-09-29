---
name: map-coverage-space
description: "Map a set of methods/assets/evidence items against a typed problem, capability, condition, or design space to expose redundancy, coverage structure, and the strength of support in each occupied region."
---

# map-coverage-space
## Purpose
Map methods, assets, or evidence against a typed problem or capability space to expose redundancy, gaps, and how strongly each occupied region is supported.
## Input contract
```yaml
required: [item_set, coverage_dimensions, target_space]
optional: [strength_scale, applicability_rules, evidence_links]
constraints: [dimension semantics and coverage states are declared]
```
## Procedure
1. Define cells or regions from the supplied dimensions.
2. Assign each item to the regions it occupies, with evidence.
3. Grade every occupied region on the caller's strength scale, or on supported, partial, or unsupported when none is supplied; a region graded below the top names what it lacks.
4. Merge duplicate coverage and identify uncovered and weakly supported regions.
5. Return the map with evidence, strength grades, and confidence annotations.

If expected and observed coverage are represented on the same space, consider `detect-coverage-gap` as the next tactic.

## Output contract
```yaml
produces: [coverage_map, redundancy_clusters, gap_register, confidence_annotations]
delta_fields: [findings, evidence_updates, uncertainties]
```
## Quality gates
- Every assignment names its dimensions and evidence.
- Coverage ratio is computed from a declared universe and numerator/denominator.
- Weak and missing coverage are distinguished.
- No region is reported as occupied without a strength grade; a region backed by one item and a region backed by many independent items remain distinguishable.
## Parameterization
Caller supplies item schema, dimension ontology, coverage states, strength scale, and audit numerator/denominator definitions.
## Failure and counterexamples
Reject maps with implicit dimensions, unsupported assignments, ungraded occupancy, or ratios lacking a declared universe.
## Provenance map
- concept: creative-ideation/method-problem-crossing
- concept: knowledge-acquisition/capability-taxonomy-mapping
- intermediate: Pass3/map-method-problem-space
- intermediate: Pass3/map-capability-coverage
