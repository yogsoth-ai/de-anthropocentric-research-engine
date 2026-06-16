---
name: abstraction-ladder
description: Perform bisociation at multiple abstraction levels
execution: subagent
prompt: ./prompt.md
input: concept (string)
dependencies:
  sops:
  - spawn-agent
---

# Abstraction Ladder

Perform bisociation at multiple abstraction levels — decompose a concept into concrete, functional, structural, and abstract levels, identifying collision opportunities at each.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Abstraction laddering requires careful level-by-level decomposition and the identification of non-obvious collision opportunities at each level. Benefits from systematic dedicated attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
