---
name: validate-research-gap
description: "Test whether an apparent gap is real, persistent, and not an evidence-acquisition artifact, keeping every candidate rejected as closed on record. Tool choice is left to the host AI."
---

# validate-research-gap
## Purpose
Test whether an apparent research gap is real, persistent, and not an evidence-acquisition artifact, and keep the candidates rejected along the way auditable.
## Input contract
```yaml
required: [gap_claim, evidence_set, search_scope]
optional: [independent_sources, time_slices, candidate_gap_types]
constraints: [absence claims require an explicit scope and retrieval record]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `verify-evidence-independence` to check source independence.
2. You MUST load skill `filter-false-gap` to separate open, touched-but-not-closed, and false gaps.
3. You MUST load skill `analyze-temporal-trajectory` to test persistence across time.
4. You MUST load skill `classify-research-gap` to classify each validated gap, including those prior work touches without closing.
   If several validated gaps require comparative priority, consider `rank-candidates`. If stakeholder boundaries determine whether the gap matters, consider `map-stakeholder-system`.
Deviation: if temporal data are unavailable, return persistence unknown rather than infer stability.
## Output contract
```yaml
produces: [gap_validity_verdict, independence_check, persistence_assessment, typed_gap, rejection_register]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: independence, search adequacy, persistence, and gap type are separately reported; unsearched space is not a confirmed gap.
- B: every candidate rejected as resolved appears in the rejection register with its closing work; a rejection resting on a single source is flagged.
- When the typology admits contradiction, measurement, or boundary gaps and none is reported, the verdict states why.
## Failure and counterexamples
Reject gaps caused by duplicate sources, narrow retrieval, prior work that closes the question, or unanswerable wording. Do not reject a gap because prior work exists in its region.
## Provenance map
- `deep-insight/gap-validation`, `cross-validation`, `cross-database-verification`, `false-gap-filtering`, `temporal-sensitivity-testing`: resolved.
## Preserved source criteria ledger
- Preserve cross-source verification, false-gap filtering, and temporal persistence checks.
## Context checkpoint / Delta notes
Append source set, independence findings, temporal updates, gap verdicts, rejection register, and next action.
