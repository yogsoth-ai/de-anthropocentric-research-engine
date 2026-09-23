---
name: drill-five-whys
description: "Iteratively ask why, evidence-checking each causal step, to move from symptom toward root cause."
---

# drill-five-whys
## Purpose
Iteratively ask why, checking evidence at each causal step, to move from symptom toward root cause.
## Input contract
```yaml
required: [symptom_statement, causal_evidence]
optional: [initial_cause, max_depth]
constraints: [each why answer must explain the preceding statement and cite evidence or uncertainty]
```
## Procedure
1. Normalize the symptom as an observable effect.
2. Ask why the effect occurs and record the proposed cause.
3. Test the cause against evidence before asking the next why.
4. Stop at a controllable root, an evidence boundary, or a documented unresolved branch.
## Output contract
```yaml
produces: [why_chain, root_cause_candidate, evidence_gaps]
delta_fields: [findings, assumption_updates, uncertainties]
```
## Quality gates
- Each link is directional and evidence-checked; stopping reason is explicit.
## Failure and counterexamples
Do not force exactly five levels or accept circular answers as root causes.
## Provenance map
- `deep-insight/five-whys-drilling`: resolved.
