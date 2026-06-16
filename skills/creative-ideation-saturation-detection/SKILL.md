---
name: saturation-detection
description: Determine when additional ideation yields diminishing returns. Analyzes
  latest idea batch against existing corpus to judge continue/near-saturation/saturated.
execution: subagent
prompt: ./prompt.md
input: existing_ideas (string), latest_batch (string)
dependencies:
  sops:
  - spawn-agent
---

# Saturation Detection

Determine when to stop generating — diminishing returns analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Saturation judgment requires comparing the entire existing idea corpus against the latest batch. The comparison is context-intensive and benefits from dedicated processing.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
