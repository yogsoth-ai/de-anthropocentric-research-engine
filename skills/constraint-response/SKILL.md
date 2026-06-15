---
name: constraint-response
description: Generate creative solutions under extreme constraints — no "impossible"
  allowed, find a way.
execution: subagent
prompt: ./prompt.md
input: constraint (string), problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Constraint Response

Generate creative solutions under extreme constraints.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Constraint-forced creativity requires sustained divergent thinking under pressure, benefiting from dedicated context that fully commits to the constraint.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
