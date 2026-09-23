---
name: map-stakeholder-jobs
description: "Represent stakeholder jobs, desired outcomes, pains, gains, dependencies, and conflicts relevant to the research target."
---

# map-stakeholder-jobs
## Purpose
Represent stakeholder jobs, desired outcomes, pains, gains, dependencies, and conflicts.
## Input contract
```yaml
required: [stakeholder_set, research_target]
optional: [interviews, observed_behaviors, service_context]
constraints: [jobs must be stated as outcomes sought, not product features]
```
## Procedure
1. Identify functional, social, and emotional jobs for each stakeholder.
2. Record desired outcomes, pains, gains, and dependencies.
3. Map conflicts between jobs and implications for the research target.
## Output contract
```yaml
produces: [job_map, outcome_register, pain_gain_map, conflict_map]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Each job has a stakeholder and evidence status; feature descriptions are not accepted as jobs.
## Failure and counterexamples
Do not infer stakeholder priorities from organizational titles alone.
## Provenance map
- `jobs-to-be-done-analysis`: concept (no exact pool entry).
- `job-mapping`: concept (no exact pool entry).
