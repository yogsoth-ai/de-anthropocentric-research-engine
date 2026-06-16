---
name: analogy-chain
description: Chain analogies to deeper levels (3-5 layers). Each layer reveals new
  aspects and insights not visible at the surface.
execution: subagent
prompt: ./prompt.md
input: initial_analogy (string)
dependencies:
  sops:
  - spawn-agent
---

# Analogy Chain

Chain analogies to deeper levels (3-5 layers).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Analogy chaining requires sustained deepening of a single thread without distraction. Each layer builds on the previous, requiring unbroken focus on progressive abstraction and re-concretization.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
