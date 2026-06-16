---
name: consequence-following
description: Follow a provocation's logical consequences step by step to extract viable
  insights and new research directions.
execution: subagent
prompt: ./prompt.md
input: provocation_statement
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete consequence chain (3-5 steps) for one provocation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
