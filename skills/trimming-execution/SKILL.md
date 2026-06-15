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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
