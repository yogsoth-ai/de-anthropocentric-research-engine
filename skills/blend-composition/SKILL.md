---
name: blend-composition
description: Compose new connections in blended space
execution: subagent
prompt: ./prompt.md
input: input_spaces (object), generic_space (object)
dependencies:
  sops:
  - spawn-agent
---

# Blend Composition

Compose new connections in blended space by selectively projecting structure from input spaces and creating novel relations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Blend composition is the creative core of conceptual integration — it requires selective projection decisions and the generation of genuinely novel connections. Benefits from dedicated creative attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
