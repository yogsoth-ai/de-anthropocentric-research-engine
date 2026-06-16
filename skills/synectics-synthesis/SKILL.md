---
name: synectics-synthesis
description: Synthesize all synectics outputs into a structured idea report. Combines
  results from all analogy types and excursion processes.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Synectics Synthesis

Synthesize all synectics outputs into a structured idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all intermediate outputs from multiple analogy types and excursion processes simultaneously, identifying cross-cutting themes and combining complementary insights into coherent solution concepts.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
