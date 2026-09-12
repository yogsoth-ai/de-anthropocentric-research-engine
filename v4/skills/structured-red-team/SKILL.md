---
name: structured-red-team
description: "Map attack surfaces, generate attack vectors, execute probes, and aggregate weaknesses into a resilience picture."
---

# structured-red-team
## Purpose
Map attack surfaces, generate attack vectors, execute probes, and aggregate weaknesses into a resilience picture.
## Input contract
```yaml
required: [artifact, threat_model, probe_scope]
optional: [access_assumptions, severity_scale]
constraints: [attack surface and probe authority must be explicit]
```
## Execution protocol
1. Map attackable dimensions and exposure (`map-threat-surface`).
2. Generate concrete attack vectors (`generate-attack-vector`).
3. Execute probes and trace downstream assumption failures (`execute-probe`, `trace-assumption-cascade`).
Deviation: stop a probe when its scope is exhausted; record untested attack surface and do not infer resilience.
## Output contract
```yaml
produces: [threat_surface, attack_vectors, probe_records, weakness_aggregate, resilience_picture]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- A-class attack coverage: declared universe = enumerated attack-surface dimensions; numerator = dimensions with at least one executed probe or explicit exclusion; batch increment = one probe batch; stopping reason = marginal new weakness yield saturates or scope is exhausted; source references = artifact versions, probe IDs, threat-model sources; direction/threshold reason = expand until new-probe weakness yield falls below a justified threshold.
- Aggregate findings by severity and preserve failed probes.
## Failure and counterexamples
Do not claim resilience from untested surfaces. A probe that cannot execute is an uncertainty, not a pass.
## Provenance map
- resolved: red-teaming
- resolved: systematic-probing
- resolved: structured-attack-campaign
- resolved: adversarial-roleplay
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Map attack surfaces, generate vectors, execute probes, aggregate weaknesses. |
## Context checkpoint / Delta notes
Append threat surface, vectors, probe evidence, severity, and untested dimensions.
