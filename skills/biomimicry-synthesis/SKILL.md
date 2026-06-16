---
name: biomimicry-synthesis
description: Synthesize all biomimicry outputs into a structured idea report. Integrate
  biological strategies, design principles, and technical solutions.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Biomimicry Synthesis

Synthesize all biomimicry outputs into a structured idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating diverse outputs from multiple SOPs, identifying cross-cutting themes, resolving conflicts, and producing a coherent final report. Benefits from dedicated integrative attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
