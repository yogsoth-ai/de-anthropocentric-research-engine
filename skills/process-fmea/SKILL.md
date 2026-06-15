---
name: process-fmea
description: 'Strategy: Research execution process FMEA — analyzes how the research
  process itself can fail during execution, distinct from design-level failures.'
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

# Process FMEA Strategy

Analyzes failure modes in the research execution process — not what the design gets wrong, but what can go wrong during implementation.

## Method

1. **function-analysis** maps the execution process steps
2. **failure-mode-extraction** identifies process-level failure modes (data collection errors, methodology drift, resource constraints)
3. **failure-chain-construction** traces process failures to outcome impacts
4. **severity-scoring**, **occurrence-scoring**, **detection-scoring** rate each mode
5. **action-priority-matrix** classifies priority
6. **mitigation-design-sop** designs process controls

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Process steps analyzed | 4 | 10 | 20 |
| Failure modes per step | 2 | 3 | 4 |
| Chain depth | 2 | 3 | 5 |
| Process controls designed | 2 | 6 | 12 |

## Orchestration

```
function-analysis (process mode) → failure-mode-extraction
  → failure-chain-construction
  → [severity-scoring, occurrence-scoring, detection-scoring] (parallel)
  → action-priority-matrix → mitigation-design-sop
  → re-scoring
```

## Subagents

- function-analysis (process step mapping)
- failure-mode-extraction (process failure identification)
- failure-chain-construction (process-to-outcome chains)
- severity-scoring, occurrence-scoring, detection-scoring (S/O/D)
- action-priority-matrix (priority classification)
- mitigation-design-sop (process control design)

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
