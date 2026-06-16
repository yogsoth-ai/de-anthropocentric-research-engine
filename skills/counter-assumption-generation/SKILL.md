---
name: counter-assumption-generation
description: Generate dialectical opposites for governing variables — coherent alternative
  worldviews where the opposite is true.
execution: subagent
prompt: ./prompt.md
input: governing_variables
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete counter-assumption set for a list of governing variables.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
