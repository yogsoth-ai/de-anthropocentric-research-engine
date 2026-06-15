---
name: multi-criteria-scoring
description: Score gaps on multiple dimensions (importance, feasibility, novelty,
  urgency, impact) using weighted multi-criteria decision analysis.
execution: subagent
prompt: ./prompt.md
input: gap_list (string), scoring_criteria (string)
dependencies:
  sops:
  - spawn-agent
---

# Multi-Criteria Scoring

Score and rank gaps using weighted multi-criteria decision analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one scoring pass over a set of gaps.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
