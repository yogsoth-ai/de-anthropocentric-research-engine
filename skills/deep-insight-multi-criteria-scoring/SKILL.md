---
name: deep-insight-multi-criteria-scoring
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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
