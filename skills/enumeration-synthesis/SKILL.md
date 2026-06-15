---
name: enumeration-synthesis
description: Synthesize all systematic enumeration outputs into a structured idea
  report with prioritized recommendations.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (object)
dependencies:
  sops:
  - spawn-agent
---

# Enumeration Synthesis

Synthesize all intermediate outputs from systematic enumeration into a coherent, prioritized idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating diverse outputs (matrices, ablation results, failure taxonomies, factorial designs) into a coherent narrative. Benefits from dedicated context to hold all inputs simultaneously.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
