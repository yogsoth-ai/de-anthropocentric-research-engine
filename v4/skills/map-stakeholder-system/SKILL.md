---
name: map-stakeholder-system
description: "Model the research system from stakeholder and boundary perspectives: define what is inside/outside the system, identify stakeholder jobs and stakes, classify salience, and expose conflicts that alter problem framing or feasibility."
---

# map-stakeholder-system
## Purpose
Model stakeholders and system boundaries, classify salience, and expose conflicts that alter framing or feasibility.
## Input contract
```yaml
mode_contracts:
  critical-systems-heuristics: &stakeholder_input
    required: [target_system, stakeholder_set]
    optional: [boundary_candidates, stakeholder_evidence, contested_interests]
    constraints: [inside_outside_boundary_and_stakeholder_claims_must_be_explicit]
  jobs-to-be-done: *stakeholder_input
  stakeholder-salience: *stakeholder_input
```
## Execution protocol
1. Assess system boundary (`assess-system-boundary`).
2. Construct perspective set (`construct-perspective-set`).
3. Map stakeholder jobs (`map-stakeholder-jobs`).
4. Classify salience (`classify-stakeholder-salience`).
5. Map disagreement (`map-disagreement`).
Deviation: boundary alternatives may branch; retain each material boundary and its consequences.

## Mode branches

- `critical-systems-heuristics`: test who defines the system boundary, whose interests it serves, and which excluded effects change the feasibility judgment.
- `jobs-to-be-done`: map each stakeholder's functional, social, and emotional job so the system model reflects the outcomes they actually seek.
- `stakeholder-salience`: classify stakeholder power, legitimacy, and urgency with evidence, making priority and neglected voices explicit.

## Output contract
```yaml
mode_contracts:
  critical-systems-heuristics:
    produces: [system_boundary, perspective_set, disagreement_map]
    delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
  jobs-to-be-done:
    produces: [stakeholder_job_map, perspective_set]
    delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
  stakeholder-salience:
    produces: [salience_map, perspective_set, disagreement_map]
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
