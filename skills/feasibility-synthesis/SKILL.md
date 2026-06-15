---
name: feasibility-synthesis
description: Synthesize all assessments into a feasibility matrix, recommendation,
  and risk summary.
execution: subagent
prompt: ./prompt.md
input: all_assessments
dependencies:
  sops:
  - spawn-agent
---

# Feasibility Synthesis

Combine all feasibility assessment outputs — readiness scores, constraint analyses, resource estimates, and gate verdicts — into a final feasibility matrix with clear recommendation and risk summary.

## Execution

Spawns a subagent that:
1. Receives all assessment outputs for one or more candidates
2. Constructs a comparative feasibility matrix
3. Synthesizes findings into a clear recommendation
4. Produces risk summary with mitigation priorities
5. Returns decision-ready output

## Why Subagent

Final synthesis requires integrating diverse assessment types into a coherent whole. A dedicated subagent can weigh conflicting signals and produce a balanced recommendation without anchoring to any single assessment.

## HARD-GATE

Output MUST include: feasibility matrix, clear recommendation (proceed/defer/abandon), and risk summary with top 3 risks. Reject if recommendation is not supported by the matrix data.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
