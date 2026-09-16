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
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `enumerate-failure-modes` to enumerate failure modes. You MUST load skill `build-failure-chain` to construct their propagation chains.
2. You MUST load skill `score-fmea-risk` to score severity, occurrence, detectability, and priority.
3. You MUST load skill `design-mitigation` to design mitigations. You MUST load skill `validate-mitigation-effect` to re-run the relevant test and validate the effect.
   If a failure chain requires explicit intervention counterfactuals, consider `counterfactual-causal-analysis` as the next tactic.
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
