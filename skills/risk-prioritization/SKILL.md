---
name: risk-prioritization
description: 'Strategy: Action Priority matrix — classifies failure modes into H/M/L
  priority using severity-weighted scoring per AIAG-VDA 2019 Action Priority tables.'
type: strategy
tactics:
- premortem-to-fmea-pipeline
dependencies:
  tactics:
  - premortem-to-fmea-pipeline
  sops:
  - action-priority-matrix
  - severity-scoring
---

# Risk Prioritization Strategy

Classifies failure modes into High/Medium/Low action priority using severity-weighted S/O/D scoring.

## Method

1. Collect S/O/D scores from upstream FMEA analysis
2. **action-priority-matrix** applies AIAG-VDA Action Priority logic:
   - H (High): Mandatory action required — severity >= 8, or combined S*O >= 36
   - M (Medium): Action recommended — moderate risk combinations
   - L (Low): Optional action — acceptable risk level
3. Rank all failure modes by priority class, then by RPN within class
4. Feed H-priority items to mitigation-design strategy

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Failure modes classified | 8 | 20 | 40 |
| Priority threshold tuning | fixed | 1 round | 2 rounds |
| Sensitivity analysis | none | top-5 | full |

## Orchestration

```
[S/O/D scores from upstream] → action-priority-matrix
  → priority-ranked failure catalog
  → [H-priority items] → mitigation-design
```

## Subagents

- action-priority-matrix (RPN computation and H/M/L classification)
- severity-scoring (re-evaluation if needed)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| premortem-to-fmea-pipeline | Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
