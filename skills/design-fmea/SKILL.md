---
name: design-fmea
description: "Strategy: Research design-level FMEA — function analysis, failure mode identification, severity/occurrence/detection scoring per AIAG-VDA 2019."
type: strategy
used-by: [failure-anticipation]
tactics: [failure-chain-tracing, mitigation-validation]
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
