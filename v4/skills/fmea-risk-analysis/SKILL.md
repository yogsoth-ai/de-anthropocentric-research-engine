---
name: fmea-risk-analysis
description: "Enumerate failure modes, trace cause-mode-effect chains, score risk, design mitigations, and re-evaluate residual risk."
---

# fmea-risk-analysis
## Purpose
Enumerate failure modes, trace cause-mode-effect chains, score risk, design mitigations, and re-evaluate residual risk.
## Input contract
```yaml
required: [system_or_process, functions, operating_conditions]
optional: [failure_history, severity_scale, occurrence_scale, detectability_scale]
constraints: [scales and scoring direction must be declared]
```
## Execution protocol
1. Enumerate failure modes and chains (`enumerate-failure-modes`, `build-failure-chain`).
2. Score severity, occurrence, detectability, and priority (`score-fmea-risk`).
3. Design mitigations and re-run the relevant test (`design-mitigation`, `validate-mitigation-effect`).
Deviation: omit an unavailable score dimension only with an explicit unknown and no hidden imputation.
## Output contract
```yaml
produces: [failure_mode_register, failure_chains, risk_scores, mitigation_plan, residual_risk_report]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- Risk scores must preserve severity, occurrence, detectability, scale definitions, and rationale.
- A mitigation passes only when re-testing demonstrates reduced risk without unacceptable new failure modes.
## Failure and counterexamples
Do not rank a failure mode without a cause/effect chain. Mark residual risk unknown when mitigation was not re-tested.
## Provenance map
- resolved: failure-anticipation
- resolved: design-fmea
- resolved: process-fmea
- resolved: risk-prioritization
- resolved: mitigation-design
- resolved: failure-chain-tracing
- resolved: mitigation-validation
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Enumerate failure modes, score risk, mitigate, and re-evaluate residual risk. |
## Context checkpoint / Delta notes
Append failure modes, chains, scores, mitigations, retest evidence, and residual uncertainties.
