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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
