---
name: reductio-counterexample-analysis
description: "Negate claims, derive consequences, search contradictions/counterexamples, then refine scope rather than merely defend the original wording."
---

# reductio-counterexample-analysis
## Purpose
Negate claims, derive consequences, detect contradictions and counterexamples, then refine scope.
## Input contract
```yaml
required: [claim, scope, supporting_reasoning]
optional: [known_counterexamples, boundary_conditions]
constraints: [negation must preserve the stated scope]
```
## Execution protocol
1. Negate the claim and derive consequences (`negate-claim`, `derive-consequences`).
2. Detect contradictions and generate counterexamples (`detect-contradiction`, `generate-counterexample`).
3. Refine the claim without deleting surviving evidence (`refine-claim`).
Deviation: if negation is outside the claim scope, mark it out-of-scope rather than a failure.
## Output contract
```yaml
produces: [negated_claim, consequence_chain, contradiction_report, counterexamples, refined_claim]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Thresholds and quality gates
- Counterexamples must satisfy the original stated scope.
- Refinement must identify which commitment was narrowed.
## Failure and counterexamples
Do not use a counterexample that violates the claim's declared boundary.
## Provenance map
- resolved: assumption-negation
- resolved: contradiction-derivation
- resolved: monster-barring-attempt
- resolved: claim-refinement
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Negate, derive, detect contradiction/counterexample, refine scope. |
## Context checkpoint / Delta notes
Append negation, consequences, counterexamples, and scope revision.
