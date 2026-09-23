# build-noncircularity-matrix
## Purpose
Cross-tabulate target claims/assumptions against validator assumptions and expose circularity.
## Input contract
```yaml
required: [target_claims, target_assumptions, validator_assumptions]
optional: [evidence_channels]
constraints: [each cell is independent/shared/derived-from-target/unknown]
```
## Procedure
1. Enumerate both assumption sets.
2. Populate dependency cells with evidence.
3. Identify copied assumptions and independent failure channels.
## Output contract
```yaml
produces: [noncircularity_matrix, dependency_summary, independent_channels]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Unknown dependencies remain unknown; they are not counted independent.
- At least one non-circular channel is required for validation.
## Failure and counterexamples
A validator that embeds the target claim cannot corroborate it by construction.
## Provenance map
- resolved: circular-validation-audit
