# decompose-ishikawa
## Purpose
Build an Ishikawa causal decomposition across relevant cause families.
## Input contract
```yaml
required: [effect_statement, cause_families]
optional: [evidence_records, system_boundary]
constraints: [cause families must be named and causes linked to the effect]
```
## Procedure
1. Place the normalized effect at the head of the diagram.
2. Populate relevant method, data, theory, measurement, researcher, and environment branches.
3. Subdivide each branch into testable causes and mark evidence status.
## Output contract
```yaml
produces: [ishikawa_map, cause_register, evidence_status]
delta_fields: [findings, assumption_updates, uncertainties]
```
## Quality gates
- Every cause belongs to a declared family and has a testability or evidence note.
## Failure and counterexamples
Reject a decorative fishbone with no causal links or one that treats categories as causes without support.
## Provenance map
- `deep-insight/ishikawa-decomposition`: resolved.
