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
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `negate-claim` to negate the claim. You MUST load skill `derive-consequences` to derive the consequences.
2. You MUST load skill `detect-contradiction` to detect contradictions. You MUST load skill `generate-counterexample` to generate counterexamples.
3. You MUST load skill `refine-claim` to refine the claim without deleting surviving evidence.
   If the surviving claim needs an explicit region of validity, consider `map-validity-envelope` as the next tactic.
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
