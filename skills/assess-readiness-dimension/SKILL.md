---
name: assess-readiness-dimension
description: "Assess one readiness dimension against explicit anchors/evidence."
---

# assess-readiness-dimension
## Purpose
Assess one readiness dimension against explicit anchors, evidence, and known deficits.
## Input contract
```yaml
required: [subject_record, readiness_dimension, anchor_definition, evidence_register]
optional: [scoring_scale, prior_assessment]
constraints: [anchor levels are ordered and observable; every score cites evidence and a deficit statement]
```
## Procedure
1. Define the dimension, scale, anchor descriptions, and decision relevance.
2. Map each supplied evidence item to the strongest supported anchor and record contrary evidence.
3. Assign the lowest defensible level whose requirements are met; record missing requirements separately.
4. Emit the dimension score, evidence basis, deficits, and reassessment trigger.
## Output contract
```yaml
produces: [readiness_level, evidence_basis, deficit_list, reassessment_trigger]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class gate: declared universe = all requirements of the readiness dimension; numerator = requirements supported by at least two independent evidence items; batch increment = one requirement assessed; stopping reason = all requirements assessed or a blocking deficit is established; source references = evidence and anchor IDs; direction/threshold reason = level rises only when its anchor requirements are met and falls when blocking contrary evidence dominates.
- A level without a deficit or uncertainty statement is invalid.
## Failure and counterexamples
Do not average incomparable readiness dimensions. A high score on one dimension cannot erase an unmet hard requirement on another.
## Provenance map
- resolved: dimension-assessment
