---
name: evolution-mechanism-transfer
description: Map evolution mechanisms to design operations. Translate selection, mutation,
  drift, radiation into design operators.
execution: subagent
prompt: ./prompt.md
input: evolution_mechanism (string)
dependencies:
  sops:
  - spawn-agent
---

# Evolution Mechanism Transfer

Map evolution mechanisms to design operations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Evolution mechanism transfer requires understanding both evolutionary biology and design methodology, creating rigorous mappings between natural selection processes and engineering design operations. Benefits from focused interdisciplinary attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
