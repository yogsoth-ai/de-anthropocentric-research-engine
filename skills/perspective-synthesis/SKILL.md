---
name: perspective-synthesis
description: Synthesize all perspective outputs into a structured multi-perspective
  idea report.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Perspective Synthesis

Synthesize all perspective outputs into structured report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all perspective outputs simultaneously and finding patterns across them, benefiting from a fresh context that can see the forest rather than individual trees.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
