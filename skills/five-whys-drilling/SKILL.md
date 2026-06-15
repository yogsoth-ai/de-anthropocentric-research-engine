---
name: five-whys-drilling
description: Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon
  to actionable root cause. Each level verified against evidence.
execution: subagent
prompt: ./prompt.md
input: surface_phenomenon (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Five Whys Drilling

Iterative root cause analysis via successive "Why?" questions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one 5-Whys drilling pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
