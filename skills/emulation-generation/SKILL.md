---
name: emulation-generation
description: Generate technical solutions emulating biological strategies. Bridge
  from design principle to concrete implementation.
execution: subagent
prompt: ./prompt.md
input: design_principle (string)
dependencies:
  sops:
  - spawn-agent
---

# Emulation Generation

Generate technical solutions emulating biological strategies.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Emulation generation requires creative engineering synthesis, translating abstract design principles into concrete technical solutions with materials, manufacturing, and performance considerations. Benefits from dedicated creative-engineering attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
