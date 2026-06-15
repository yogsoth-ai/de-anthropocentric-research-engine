---
name: ecosystem-pattern-extraction
description: Extract ecosystem-level organization patterns (symbiosis, emergence,
  cycles, resilience).
execution: subagent
prompt: ./prompt.md
input: ecosystem (string)
dependencies:
  sops:
  - spawn-agent
---

# Ecosystem Pattern Extraction

Extract ecosystem-level organization patterns.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Ecosystem pattern extraction requires understanding complex multi-species interactions, emergent properties, and system-level dynamics. Benefits from dedicated systems-thinking attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
