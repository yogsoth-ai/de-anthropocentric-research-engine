---
name: function-redistribution
description: Redistribute functions across different components
execution: subagent
prompt: ./prompt.md
input: function_model (object)
dependencies:
  sops:
  - spawn-agent
---

# Function Redistribution

Redistribute functions across different components — move, merge, split, or eliminate functions to create novel system architectures.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Function redistribution requires systematic exploration of all possible function-component reassignments, evaluating each for feasibility and novelty. Benefits from exhaustive combinatorial attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
