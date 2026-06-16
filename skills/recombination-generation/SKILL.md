---
name: recombination-generation
description: Reassemble decomposed system fragments into novel structural arrangements
  that create emergent value.
execution: subagent
prompt: ./prompt.md
input: component_set (string)
dependencies:
  sops:
  - spawn-agent
---

# Recombination Generation

Reassemble decomposed fragments into novel structures.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Recombination requires creative exploration of arrangement possibilities while tracking interface compatibility. Benefits from dedicated context that can systematically explore the combination space without premature convergence.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
