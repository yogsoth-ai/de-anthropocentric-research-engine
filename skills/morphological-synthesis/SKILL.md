---
name: morphological-synthesis
description: Synthesize all morphological exploration outputs
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (object)
dependencies:
  sops:
  - spawn-agent
---

# Morphological Synthesis

Synthesize all intermediate morphological exploration outputs into a structured final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Morphological synthesis requires integrating matrix construction, CCA results, path generation, white-space analysis, and combination evaluations into a coherent report with actionable recommendations.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
