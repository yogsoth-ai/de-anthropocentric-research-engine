---
name: path-generation
description: Generate combination paths through consistent space
execution: subagent
prompt: ./prompt.md
input: reduced_space (object)
dependencies:
  sops:
  - spawn-agent
---

# Path Generation

Generate combination paths through the consistent solution space, prioritizing unexplored and novel configurations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Path generation requires strategic traversal of the reduced solution space, selecting configurations that maximize coverage, novelty, and diversity rather than random sampling.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
