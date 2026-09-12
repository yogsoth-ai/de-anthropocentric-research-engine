---
name: test-risky-prediction
description: "Derive a risky/nontrivial prediction uniquely or strongly implied by an explanation and test whether available evidence supports it; distinguish post-hoc accommodation from prospective constraint."
---

# test-risky-prediction
## Purpose
Derive a risky prediction uniquely or strongly implied by an explanation and test it against evidence.
## Input contract
```yaml
required: [explanation, alternatives, available_evidence]
optional: [prospective_predictions, test_conditions]
constraints: [prediction must distinguish the explanation from at least one alternative]
```
## Procedure
1. Derive prediction and its distinguishing conditions.
2. Check whether it was prospective or post-hoc.
3. Compare evidence and classify support, failure, or accommodation.
## Output contract
```yaml
produces: [risky_prediction, distinction_test, evidence_comparison, accommodation_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A prediction that fits every outcome is not risky.
## Failure and counterexamples
Post-hoc reinterpretation cannot count as prospective constraint.
## Provenance map
- resolved: elegance-trap-probe
