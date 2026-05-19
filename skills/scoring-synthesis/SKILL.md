---
name: scoring-synthesis
description: Synthesize score matrix, rankings, and sensitivity analysis into a final recommendation.
execution: subagent
prompt: ./prompt.md
input: score_matrix (object), rankings (object), sensitivity (object)
used-by: multi-criteria-scoring
---

# Scoring Synthesis

Synthesize scoring matrix, ranking results, and sensitivity analysis to produce final decision recommendations.

## Execution

Subagent receives complete scoring data, ranking results, and sensitivity analysis, produces a structured final recommendation.

## Why Subagent

Comprehensive recommendation requires weighing multiple signals and making judgments; independent execution ensures recommendation completeness and traceability.

## HARD-GATE

Final recommendation must include a clear recommended alternative, confidence assessment, key assumptions, and risk warnings; reports without conclusions are not allowed.
