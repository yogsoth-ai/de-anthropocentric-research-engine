---
name: competitor-simulation
description: Competitor perspective — design strategies to defeat this solution, then
  use attack vectors to improve it.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Competitor Simulation

Competitor perspective: how to defeat this solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Competitive analysis requires adversarial thinking that benefits from dedicated context to avoid contaminating constructive ideation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
