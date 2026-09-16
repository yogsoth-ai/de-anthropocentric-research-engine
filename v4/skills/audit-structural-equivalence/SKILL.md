---
name: audit-structural-equivalence
description: "Audit a claimed isomorphism/equivalence by constructing an explicit mapping, testing which structures/operations/invariants are preserved, searching counterexamples, and downgrading the claim to the strongest defensible relation when full isomorphism fails."
---

# audit-structural-equivalence
## Purpose
Audit a claimed isomorphism or equivalence and downgrade it to the strongest defensible relation when preservation fails.
## Input contract
```yaml
mode_contracts:
  isomorphism: &structural_audit_input
    required: [source_structure, target_structure, equivalence_claim]
    optional: [required_invariants, operations, constraints]
    constraints: [mapping_domains_and_preservation_obligations_must_be_explicit]
  substructure: *structural_audit_input
  homomorphism: *structural_audit_input
  shared-invariant: *structural_audit_input
  analogy: *structural_audit_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `extract-structural-mapping` to construct the object, relation, operation, and invariant mapping.
2. You MUST load skill `test-structure-preservation` to test preservation. You MUST load skill `generate-counterexample` to search minimal counterexamples.
3. You MUST load skill `downgrade-equivalence-claim` to downgrade the claim and record lost invariants.
Deviation: if the claim is only analogy by scope, run the analogy branch and do not report isomorphism.
## Output contract
```yaml
mode_contracts:
  isomorphism: &structural_audit_output
    produces: [claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]
    delta_fields: [findings, evidence_updates, uncertainties, decisions]
  substructure: *structural_audit_output
  homomorphism: *structural_audit_output
  shared-invariant: *structural_audit_output
  analogy: *structural_audit_output
```
## Thresholds and quality gates
- All required relations, operations, and invariants must have pass/fail/unknown status.
- A full equivalence claim fails on one unprincipled preservation counterexample.
## Failure and counterexamples
Do not infer equivalence from surface similarity. Exclusions introduced only after a counterexample are ad hoc unless independently justified.
## Provenance map
- resolved: isomorphism-falsification
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Preserve structures/operations/invariants; downgrade when full equivalence fails. |
## Context checkpoint / Delta notes
Append mapping, tested invariants, counterexamples, and final relation.

## Mode branches
- `isomorphism`: all declared structures and operations must preserve.
- `substructure`: test inclusion only.
- `homomorphism`: test operation-preserving mapping with relaxed structure.
- `shared-invariant`: test named invariant subset.
- `analogy`: report transferable relation without equivalence claim.
