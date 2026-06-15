---
name: design-synthesis
description: 'SOP: synthesize complete experiment design report'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: All upstream SOP outputs (variables, levels, matrix, metrics, sample size,
  seeds, environment, config)
output: Complete experiment design report + feasibility assessment + risk inventory
dependencies:
  sops:
  - spawn-agent
---

# SOP: Design Synthesis

Synthesize all upstream design SOP outputs into a complete experiment design report, perform consistency checks, assess feasibility, and identify potential risks.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Design synthesis requires a global perspective to review all design decisions for consistency and completeness — serves as the final quality gate of the experiment design phase, requiring independent critical thinking space.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
