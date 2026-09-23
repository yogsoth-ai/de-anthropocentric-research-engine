---
name: update-confidence-from-evidence
description: "Update confidence in a concept, relation, claim, or model component from new supporting/contradicting evidence with explicit rationale."
---

# update-confidence-from-evidence
## Purpose
Update confidence in a concept, relation, claim, or model component from new supporting or contradicting evidence.
## Input contract
```yaml
required: [target_record, prior_confidence, new_evidence, update_rule]
optional: [support_weights, contradiction_weights, confidence_floor]
constraints: [each update cites evidence direction, provenance, weight rule, and prior state]
```
## Procedure
1. Verify target identity and freeze the prior confidence and evidence ledger.
2. Classify each new item as supporting, contradicting, or non-informative under the declared rule.
3. Apply the update rule, record the weight and direction, and cap the result to the permitted confidence range.
4. Emit the updated confidence, evidence trace, and unresolved conflicts.
## Output contract
```yaml
produces: [updated_confidence, evidence_trace, conflict_register, update_rationale]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Every confidence change is reproducible from the prior state, evidence classification, and update rule.
- Contradicting evidence cannot be omitted from the ledger merely because the net score rises.
## Failure and counterexamples
Do not treat repeated copies of one source as independent support. If evidence polarity is ambiguous, leave confidence unchanged and mark uncertainty.
## Provenance map
- resolved: confidence-update
- resolved: confidence-scoring
