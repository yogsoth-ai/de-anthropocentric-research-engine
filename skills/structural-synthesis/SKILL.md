---
name: structural-synthesis
description: Synthesize all structural transformation outputs into a coherent, ranked
  idea report with lineage tracking.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Structural Synthesis

Synthesize all structural transformation outputs into a final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating outputs from multiple diverse operations, deduplicating, clustering, and ranking. Benefits from dedicated context that can hold all intermediate results simultaneously for cross-referencing.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
