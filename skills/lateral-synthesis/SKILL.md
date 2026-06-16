---
name: lateral-synthesis
description: Synthesize all lateral thinking intermediate outputs into a structured
  idea report.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Lateral Synthesis

Synthesize all lateral thinking outputs into a structured report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires reviewing all intermediate outputs from multiple SOPs and tactics, identifying patterns, resolving conflicts, and producing a coherent final report. Benefits from dedicated context that can hold all outputs simultaneously.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
