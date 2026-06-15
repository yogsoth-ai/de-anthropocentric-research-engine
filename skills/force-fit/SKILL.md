---
name: force-fit
description: Force-fit excursion discoveries back to the original problem. Deliberately
  create connections between unrelated findings and the challenge.
execution: subagent
prompt: ./prompt.md
input: excursion_discoveries (string), original_problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Force-Fit

Force-fit excursion discoveries back to the original problem.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Force-fitting requires holding two unrelated domains in mind simultaneously and deliberately creating connections that don't naturally exist. Benefits from focused creative tension without premature judgment.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
