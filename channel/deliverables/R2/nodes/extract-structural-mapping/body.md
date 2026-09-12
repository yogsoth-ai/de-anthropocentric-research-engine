# extract-structural-mapping
## Purpose
Construct an explicit source-to-target mapping over objects, relations, operations, constraints, and invariants.
## Input contract
```yaml
required: [source_structure, target_structure, mapping_claim]
optional: [required_objects, required_relations, invariants]
constraints: [mapping must preserve identity and provenance of mapped elements]
```
## Procedure
1. Enumerate source and target elements.
2. Map objects, relations, operations, constraints, and invariants.
3. Mark unmatched, ambiguous, and many-to-one mappings.
## Output contract
```yaml
produces: [structural_mapping, unmatched_elements, ambiguity_report, invariant_inventory]
delta_fields: [findings, evidence_updates, uncertainties]
```
## Quality gates
- Every claimed preserved element has an explicit mapping or is marked absent.
## Failure and counterexamples
Do not infer mapping from labels or surface resemblance.
## Provenance map
- resolved: isomorphism-falsification
