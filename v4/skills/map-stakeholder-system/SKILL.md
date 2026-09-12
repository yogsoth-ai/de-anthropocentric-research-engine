---
name: map-stakeholder-system
description: "Model the research system from stakeholder and boundary perspectives: define what is inside/outside the system, identify stakeholder jobs and stakes, classify salience, and expose conflicts that alter problem framing or feasibility."
---

# map-stakeholder-system
## Purpose
Model stakeholders and system boundaries, classify salience, and expose conflicts that alter framing or feasibility.
## Input contract
```yaml
required: [target_system, stakeholder_set]
optional: [boundary_candidates, stakeholder_evidence, contested_interests]
constraints: [inside/outside boundary and stakeholder claims must be explicit]
```
## Execution protocol
1. Assess system boundary (`assess-system-boundary`).
2. Construct perspective set (`construct-perspective-set`).
3. Map stakeholder jobs (`map-stakeholder-jobs`).
4. Classify salience (`classify-stakeholder-salience`).
5. Map disagreement (`map-disagreement`).
Deviation: boundary alternatives may branch; retain each material boundary and its consequences.
## Output contract
```yaml
produces: [system_boundary, perspective_set, stakeholder_job_map, salience_map, disagreement_map]
delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: each stakeholder has a role/job and evidence status; boundary choices expose included and excluded effects; conflicts are not silently averaged.
## Failure and counterexamples
Reject maps that treat absent voices as absent stakes or that hide boundary-dependent feasibility changes.
## Provenance map
- `deep-insight/stakeholder-mapping`, `critical-systems-heuristics`, `jobs-to-be-done-analysis`, `stakeholder-salience-analysis`: resolved/concept per exact lookup.
- Status: `deep-insight/stakeholder-mapping` resolved; the other three are concept (no exact v3 node).
## Preserved source criteria ledger
- Preserve boundary, perspective, jobs-to-be-done, salience, and disagreement semantics.
## Context checkpoint / Delta notes
Append boundary changes, stakeholder evidence, salience changes, and unresolved conflicts.
