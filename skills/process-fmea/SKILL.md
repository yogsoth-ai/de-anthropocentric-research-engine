---
name: process-fmea
description: "Strategy: Research execution process FMEA — analyzes how the research process itself can fail during execution, distinct from design-level failures."
type: strategy
used-by: [failure-anticipation]
tactics: [failure-chain-tracing, mitigation-validation]
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
