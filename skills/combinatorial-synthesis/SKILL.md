---
name: combinatorial-synthesis
description: Synthesize all combinatorial creativity outputs
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (object)
dependencies:
  sops:
  - spawn-agent
---

# Combinatorial Synthesis

Synthesize all combinatorial creativity outputs into a structured combinatorial idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Combinatorial synthesis requires integrating outputs from multiple prior stages (blends, emergent properties, function redistributions) into a coherent final report. Benefits from holistic integrative attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
