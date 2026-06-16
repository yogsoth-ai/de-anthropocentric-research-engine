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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
