---
name: audit-explanatory-compression
description: "Test whether an elegant/simple explanation earns its compression by forbidding alternatives, subsuming independent facts, or making risky predictions, rather than merely relabeling observations with a compact vocabulary."
---

# audit-explanatory-compression
## Purpose
Test whether an elegant explanation earns compression by excluding alternatives, subsuming independent facts, or making risky predictions.
## Input contract
```yaml
mode_contracts:
  earned-simplicity: &compression_audit_input
    required: [explanation, covered_facts, alternatives]
    optional: [predictions, evidence]
    constraints: [facts_and_alternatives_must_be_independently_enumerated]
  decorative-simplicity: *compression_audit_input
  risky-prediction: *compression_audit_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `classify-simplicity-evidence` to classify the explanation's compression evidence.
2. You MUST load skill `test-risky-prediction` to derive and test risky predictions.
3. You MUST load skill `construct-critique` to attack the explanation. You MUST load skill `score-object` to score its remaining support.
Deviation: omit prediction testing only when no nontrivial prediction can be derived, and mark the explanation non-discriminating.
## Output contract
```yaml
mode_contracts:
  earned-simplicity: &compression_audit_output
    produces: [forbidden_set, risky_predictions, accommodation_audit, deletion_test_result, elegance_verdict, earning_prediction]
    delta_fields: [findings, evidence_updates, uncertainties, decisions]
  decorative-simplicity: *compression_audit_output
  risky-prediction: *compression_audit_output
```
## Thresholds and quality gates
- Earned simplicity requires at least one independent fact compressed and one risky alternative-forbidding prediction, each evidence-linked.
- Decorative simplicity is a failure when it merely renames observations.
## Failure and counterexamples
Do not reward brevity alone. Mark weak when independent facts, exclusions, or predictions are absent.
## Provenance map
- resolved: elegance-trap-probe
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Distinguish earned simplicity from decorative relabeling. |
## Context checkpoint / Delta notes
Append covered facts, alternatives, risky predictions, critique, and score rationale.

## Mode branches
- `earned-simplicity`: seek independent compression and exclusions.
- `decorative-simplicity`: test for relabeling.
- `risky-prediction`: prioritize prospective constraints.
