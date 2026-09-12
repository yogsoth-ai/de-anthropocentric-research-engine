---
name: validate-research-gap
description: "Test whether an apparent gap is real, persistent, and not an evidence-acquisition artifact. Tool choice is left to the host AI."
---

# validate-research-gap
## Purpose
Test whether an apparent research gap is real, persistent, and not an evidence-acquisition artifact.
## Input contract
```yaml
required: [gap_claim, evidence_set, search_scope]
optional: [independent_sources, time_slices, candidate_gap_types]
constraints: [absence claims require an explicit scope and retrieval record]
```
## Execution protocol
1. Check source independence (`verify-evidence-independence`).
2. Filter false gaps (`filter-false-gap`).
3. Test persistence across time (`analyze-temporal-trajectory`).
4. Classify the validated gap (`classify-research-gap`).
Deviation: if temporal data are unavailable, return persistence unknown rather than infer stability.
## Output contract
```yaml
produces: [gap_validity_verdict, independence_check, persistence_assessment, typed_gap]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: independence, search adequacy, persistence, and gap type are separately reported; unsearched space is not a confirmed gap.
## Failure and counterexamples
Reject gaps caused by duplicate sources, narrow retrieval, resolved prior work, or unanswerable wording.
## Provenance map
- `deep-insight/gap-validation`, `cross-validation`, `cross-database-verification`, `false-gap-filtering`, `temporal-sensitivity-testing`: resolved.
## Preserved source criteria ledger
- Preserve cross-source verification, false-gap filtering, and temporal persistence checks.
## Context checkpoint / Delta notes
Append source set, independence findings, temporal updates, gap verdict, and next action.
