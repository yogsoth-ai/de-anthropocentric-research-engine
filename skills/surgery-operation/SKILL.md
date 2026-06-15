---
name: surgery-operation
description: Execute component surgery operations (subtract/multiply/divide/unify/redirect)
  from Systematic Inventive Thinking.
execution: subagent
prompt: ./prompt.md
input: component_analysis (string)
dependencies:
  sops:
  - spawn-agent
---

# Surgery Operation

Apply SIT surgical operators to system components for structural innovation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Component surgery requires careful reasoning about system integrity during each operation. Benefits from dedicated context that can track component states and verify function preservation after each cut.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
