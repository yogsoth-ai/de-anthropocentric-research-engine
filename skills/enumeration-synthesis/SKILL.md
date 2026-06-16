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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
