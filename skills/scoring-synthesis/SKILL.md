---
name: scoring-synthesis
description: Synthesize score matrix, rankings, and sensitivity analysis into a final
  recommendation.
execution: subagent
prompt: ./prompt.md
input: score_matrix (object), rankings (object), sensitivity (object)
dependencies:
  sops:
  - spawn-agent
---

# Scoring Synthesis

Synthesize scoring matrix, ranking results, and sensitivity analysis to produce final decision recommendations.

## Execution

Subagent receives complete scoring data, ranking results, and sensitivity analysis, produces a structured final recommendation.

## Why Subagent

Comprehensive recommendation requires weighing multiple signals and making judgments; independent execution ensures recommendation completeness and traceability.

## HARD-GATE

Final recommendation must include a clear recommended alternative, confidence assessment, key assumptions, and risk warnings; reports without conclusions are not allowed.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
