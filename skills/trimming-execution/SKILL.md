---
name: trimming-execution
description: Progressively remove components from a system while verifying function
  preservation through redistribution.
execution: subagent
prompt: ./prompt.md
input: function_model (string)
dependencies:
  sops:
  - spawn-agent
---

# Trimming Execution

Progressively remove components and verify function preservation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Trimming requires careful step-by-step reasoning about function redistribution after each removal. Benefits from dedicated context that can track system state changes through multiple trimming iterations.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
