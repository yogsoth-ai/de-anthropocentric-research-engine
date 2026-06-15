---
name: dimension-assessment
description: Score a single readiness dimension for a candidate with evidence and
  gap analysis.
execution: subagent
prompt: ./prompt.md
input: candidate, dimension
dependencies:
  sops:
  - spawn-agent
---

# Dimension Assessment

Score a single feasibility dimension (e.g., technical, market, regulatory, resource, organizational) for a given candidate. Produces a readiness score on a 1-9 scale with supporting evidence and identified gaps.

## Execution

Spawns a subagent that:
1. Receives the candidate description and target dimension
2. Searches for evidence relevant to that dimension
3. Applies TRL-style scoring criteria adapted to the dimension
4. Identifies gaps between current state and full readiness
5. Returns structured score with evidence and gaps

## Why Subagent

Each dimension assessment is independent and can run in parallel. The scoring requires focused analysis of dimension-specific evidence without cross-contamination from other dimensions.

## HARD-GATE

Output MUST include: numeric score (1-9), at least 2 evidence items, and at least 1 identified gap. Reject outputs missing any of these.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
