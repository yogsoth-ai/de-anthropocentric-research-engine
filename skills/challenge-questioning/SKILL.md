---
name: challenge-questioning
description: Non-threatening 'Why?' questioning of current practices to reveal historical
  accidents vs. genuine constraints.
execution: subagent
prompt: ./prompt.md
input: current_practices (string)
dependencies:
  sops:
  - spawn-agent
---

# Challenge Questioning

Non-threatening 'Why?' questioning of current practices.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Challenge questioning requires maintaining a non-judgmental stance while systematically probing every aspect of current practice. Benefits from dedicated context that can track which practices have been challenged and which remain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
