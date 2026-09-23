---
name: cross-examine
description: "Probe responses for inconsistency, logic gaps, and unsupported claims."
---

# cross-examine
## Purpose
Probe responses for inconsistency, logic gaps, and unsupported claims.
## Input contract
```yaml
required: [claim, response, questions, evidence]
optional: [criteria, prior_rounds]
constraints: [questions must target explicit claims or assumptions]
```
## Procedure
1. Identify unsupported or inconsistent assertions.
2. Ask targeted follow-up questions.
3. Record answers, unresolved gaps, and evidence requests.
## Output contract
```yaml
produces: [cross_examination_record, inconsistency_findings, evidence_requests]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```
## Quality gates
- Each question maps to a claim, premise, or inference step.
## Failure and counterexamples
Do not treat refusal or verbosity as inconsistency without a claim-level comparison.
## Provenance map
- resolved: cross-examination
