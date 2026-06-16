---
name: pareto-visualization
description: Create visual representation of the Pareto frontier showing trade-offs
  between objectives with narrative explanation.
execution: subagent
prompt: ./prompt.md
input: pareto_front
dependencies:
  sops:
  - spawn-agent
---

# Pareto Visualization

Transform the Pareto front data into a visual representation and narrative that makes trade-offs between objectives intuitive for decision-makers.

## Execution

Spawns a subagent that produces visualization data (coordinates, labels, regions) and a natural-language narrative explaining the trade-off landscape.

## Why Subagent

Visualization requires translating abstract multi-dimensional data into comprehensible representations with appropriate framing for the audience. This interpretive work benefits from focused attention.

## HARD-GATE

Output must include both structured visualization data and a trade-off narrative. The narrative must reference specific points on the frontier and explain what is gained/lost moving between them.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
