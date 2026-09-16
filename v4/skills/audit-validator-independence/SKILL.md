---
name: audit-validator-independence
description: "Audit whether a validator, benchmark, sandbox, or test can pass by construction because it embeds the same assumptions as the theory it claims to validate. Build a claim×validator-assumption matrix and demand at least one non-circular failure channel."
---

# audit-validator-independence
## Purpose
Detect validators that pass by construction because they copy the target theory's assumptions.
## Input contract
```yaml
mode_contracts:
  validator: &validator_audit_input
    required: [target_claim, validator, validator_artifacts]
    optional: [data_generation, metric, oracle, acceptance_rule]
    constraints: [validator_assumptions_and_target_assumptions_must_be_separately_listed]
  benchmark: *validator_audit_input
  sandbox: *validator_audit_input
  simulation: *validator_audit_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `enumerate-validator-assumptions` to enumerate embedded validator assumptions.
2. You MUST load skill `build-noncircularity-matrix` to cross-tabulate target and validator assumptions.
3. You MUST load skill `detect-pass-by-construction` to detect copied assumptions. You MUST load skill `design-falsification-test` to design an independent failure channel.
Deviation: if no non-circular channel is feasible, return blocked validation rather than a pass.
## Output contract
```yaml
mode_contracts:
  validator: &validator_audit_output
    produces: [noncircularity_matrix, red_cell_actions, validator_verdict, adversarial_ground_truth_set]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  benchmark: *validator_audit_output
  sandbox: *validator_audit_output
  simulation: *validator_audit_output
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
