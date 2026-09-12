# audit-structural-equivalence
## Purpose
Audit a claimed isomorphism or equivalence and downgrade it to the strongest defensible relation when preservation fails.
## Input contract
```yaml
required: [source_structure, target_structure, equivalence_claim]
optional: [required_invariants, operations, constraints]
constraints: [mapping domains and preservation obligations must be explicit]
```
## Execution protocol
1. Construct object/relation/operation/invariant mapping (`extract-structural-mapping`).
2. Test preservation and search minimal counterexamples (`test-structure-preservation`, `generate-counterexample`).
3. Downgrade the claim and record lost invariants (`downgrade-equivalence-claim`).
Deviation: if the claim is only analogy by scope, run the analogy branch and do not report isomorphism.
## Output contract
```yaml
produces: [structural_mapping, preservation_report, counterexamples, downgraded_claim]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
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
