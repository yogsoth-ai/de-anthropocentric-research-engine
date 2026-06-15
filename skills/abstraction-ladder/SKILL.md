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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
