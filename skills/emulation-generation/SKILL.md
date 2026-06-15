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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
