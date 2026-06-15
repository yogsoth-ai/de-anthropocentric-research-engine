---
name: evaporating-cloud
description: Model conflicts as Goldratt's Evaporating Cloud — expose hidden assumptions
  behind opposing needs to dissolve the conflict.
execution: subagent
prompt: ./prompt.md
input: opposing_needs (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Evaporating Cloud

Dissolve conflicts by exposing hidden assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one evaporating cloud construction.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
