---
name: mitigation-validation
description: 'Tactic: Run mini-FMEA on proposed mitigations to verify they do not
  introduce new failure modes. Prevents mitigation-induced risks.'
type: tactic
strategies:
- design-fmea
- process-fmea
- mitigation-design
dependencies:
  sops:
  - failure-mode-extraction
  - mitigation-design-sop
  - re-scoring
  - severity-scoring
---

# Mitigation Validation Tactic

Validate that proposed mitigations do not introduce new failure modes — a mini-FMEA on the mitigations themselves.

## Orchestration

1. Receive proposed mitigation measures from mitigation-design-sop
2. **failure-mode-extraction** identifies potential failure modes of each mitigation:
   - Could the prevention measure fail?
   - Could the detection mechanism produce false negatives?
   - Could the response plan create new problems?
3. **severity-scoring** rates new failure modes
4. If any new mode scores H-priority:
   - Flag mitigation as risky
   - **mitigation-design-sop** redesigns or adds safeguards
   - Re-validate (max 2 iterations to prevent infinite loops)
5. **re-scoring** confirms final S/O/D with validated mitigations

## Iteration Control

- Max validation iterations: 2 (prevent infinite recursion)
- If still H-priority after 2 iterations: escalate to human review
- Document residual risk for accepted mitigations

## Subagents Dispatched

- failure-mode-extraction (mitigation failure identification)
- severity-scoring (new risk assessment)
- mitigation-design-sop (redesign if needed)
- re-scoring (final confirmation)

## Termination Conditions

- All mitigations validated as not introducing H-priority risks
- Max iterations reached (escalate with documentation)
- Residual risk accepted and documented

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| re-scoring | Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
