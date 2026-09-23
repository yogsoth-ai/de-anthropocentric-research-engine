# audit-explanatory-compression
## Purpose
Test whether an elegant explanation earns compression by excluding alternatives, subsuming independent facts, or making risky predictions.
## Input contract
```yaml
required: [explanation, covered_facts, alternatives]
optional: [predictions, evidence]
constraints: [facts and alternatives must be independently enumerated]
```
## Execution protocol
1. Classify the explanation's compression evidence (`classify-simplicity-evidence`).
2. Derive and test risky predictions (`test-risky-prediction`).
3. Attack the explanation and score the remaining support (`construct-critique`, `score-object`).
Deviation: omit prediction testing only when no nontrivial prediction can be derived, and mark the explanation non-discriminating.
## Output contract
```yaml
produces: [compression_assessment, risky_prediction_tests, critique, score]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
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
