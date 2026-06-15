---
name: design-fmea
description: 'Strategy: Research design-level FMEA — function analysis, failure mode
  identification, severity/occurrence/detection scoring per AIAG-VDA 2019.'
type: strategy
tactics:
- failure-chain-tracing
- mitigation-validation
dependencies:
  tactics:
  - failure-chain-tracing
  - mitigation-validation
  sops:
  - action-priority-matrix
  - detection-scoring
  - failure-chain-construction
  - failure-mode-extraction
  - function-analysis
  - mitigation-design-sop
  - occurrence-scoring
  - severity-scoring
---

# Design FMEA Strategy

Systematic failure analysis at the research design level: what functions can fail, how, and with what consequence?

## Method

1. **function-analysis** decomposes artifact into function tree
2. **failure-mode-extraction** identifies how each function can fail
3. **failure-chain-construction** builds cause → mode → effect chains
4. **severity-scoring**, **occurrence-scoring**, **detection-scoring** rate each mode
5. **action-priority-matrix** classifies priority (H/M/L)
6. **mitigation-design-sop** proposes countermeasures for H-priority items

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Functions analyzed | 4 | 10 | 20 |
| Failure modes per function | 2 | 3 | 5 |
| Chain depth (cause levels) | 2 | 4 | 6 |
| Mitigations designed | 3 | 8 | 15 |

## Orchestration

```
function-analysis → failure-mode-extraction → failure-chain-construction
  → [severity-scoring, occurrence-scoring, detection-scoring] (parallel)
  → action-priority-matrix → mitigation-design-sop
  → re-scoring (mitigation-validation tactic)
```

## Subagents

- function-analysis (decompose function tree)
- failure-mode-extraction (identify failure modes)
- failure-chain-construction (cause-mode-effect chains)
- severity-scoring, occurrence-scoring, detection-scoring (S/O/D)
- action-priority-matrix (priority classification)
- mitigation-design-sop (countermeasure design)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| failure-chain-tracing | Tactic: Trace upstream causes and downstream effects of each failure mode. Builds multi-level cause-mode-effect chains for systemic understanding. |
| mitigation-validation | Tactic: Run mini-FMEA on proposed mitigations to verify they do not introduce new failure modes. Prevents mitigation-induced risks. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| detection-scoring | Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact. |
| failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| function-analysis | FMEA Step 3: Decompose artifact into function tree — identify what each component is supposed to do before analyzing how it can fail. |
| mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| occurrence-scoring | Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |

<!-- END available-tables (generated) -->
