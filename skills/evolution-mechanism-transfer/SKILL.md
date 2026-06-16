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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
