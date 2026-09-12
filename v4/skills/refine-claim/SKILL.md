---
name: refine-claim
description: "Repair a claim via scope narrowing, lemma incorporation, or decomposition while preserving explanatory power."
---

# refine-claim
## Purpose
Repair a claim by narrowing scope, adding a lemma, or decomposing it while preserving explanatory power.
## Input contract
```yaml
required: [claim, failure_or_counterexample, supporting_evidence]
optional: [scope_options, mechanism]
constraints: [every repair must state what was narrowed or added]
```
## Procedure
1. Identify the failed commitment.
2. Generate scope, lemma, or decomposition repairs.
3. Select a repair and record retained explanatory content.
## Output contract
```yaml
produces: [refined_claim, repair_rationale, retained_scope, lost_commitments]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Repair cannot silently exclude a counterexample without a principled boundary.
## Failure and counterexamples
Do not relabel an unsupported claim as refined.
## Provenance map
- resolved: claim-refinement
- resolved: monster-barring-attempt
