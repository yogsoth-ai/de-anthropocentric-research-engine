---
name: mitigation-design
description: 'Strategy: Design prevention, detection, and response measures for high-priority
  failure modes. Produces actionable countermeasures validated via re-scoring.'
type: strategy
tactics:
- mitigation-validation
dependencies:
  tactics:
  - mitigation-validation
  sops:
  - action-priority-matrix
  - mitigation-design-sop
  - re-scoring
---

# Mitigation Design Strategy

Design countermeasures for high-priority failure modes across three layers: prevention, detection, response.

## Method

1. **mitigation-design-sop** generates countermeasures for each H-priority failure:
   - Prevention: eliminate or reduce occurrence
   - Detection: improve ability to detect before impact
   - Response: contingency plan if failure occurs
2. **re-scoring** re-evaluates S/O/D with mitigations in place
3. **mitigation-validation** runs mini-FMEA on mitigations themselves
4. Iterate until all H-priority items reach M or L after mitigation

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Mitigations per failure mode | 1 | 2 | 3 |
| Re-scoring rounds | 1 | 2 | 3 |
| Mitigation validation depth | shallow | standard | full FMEA |

## Orchestration

```
[H-priority failures] → mitigation-design-sop
  → re-scoring → action-priority-matrix (re-classify)
  → [still H?] → mitigation-validation → iterate
  → [M or L?] → accept, document residual risk
```

## Subagents

- mitigation-design-sop (countermeasure generation)
- re-scoring (post-mitigation S/O/D)
- action-priority-matrix (re-classification)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| mitigation-validation | Tactic: Run mini-FMEA on proposed mitigations to verify they do not introduce new failure modes. Prevents mitigation-induced risks. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| re-scoring | Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected. |

<!-- END available-tables (generated) -->
