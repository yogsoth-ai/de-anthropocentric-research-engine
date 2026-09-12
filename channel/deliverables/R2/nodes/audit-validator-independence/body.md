# audit-validator-independence
## Purpose
Detect validators that pass by construction because they copy the target theory's assumptions.
## Input contract
```yaml
required: [target_claim, validator, validator_artifacts]
optional: [data_generation, metric, oracle, acceptance_rule]
constraints: [validator assumptions and target assumptions must be separately listed]
```
## Execution protocol
1. Enumerate embedded validator assumptions (`enumerate-validator-assumptions`).
2. Cross-tabulate target and validator assumptions (`build-noncircularity-matrix`).
3. Detect copied assumptions and design an independent failure channel (`detect-pass-by-construction`, `design-falsification-test`).
Deviation: if no non-circular channel is feasible, return blocked validation rather than a pass.
## Output contract
```yaml
produces: [assumption_inventory, noncircularity_matrix, circularity_findings, falsification_test]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- At least one validator path must be independent of the target's defining assumptions.
- Shared or derived-from-target dependencies must be explicit in the matrix.
## Failure and counterexamples
Pass-by-construction is a finding, not evidence of corroboration. Unknown dependencies remain unresolved.
## Provenance map
- resolved: circular-validation-audit
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Build claim-validator assumption matrix and require a non-circular failure channel. |
## Context checkpoint / Delta notes
Append assumptions, matrix cells, circularity findings, and proposed independent test.

## Mode branches
- `validator`: inspect validator implementation assumptions.
- `benchmark`: inspect benchmark construction and metric assumptions.
- `sandbox`: inspect environment/oracle assumptions.
- `simulation`: inspect simulator and initialization assumptions.
