---
name: parameter-identification
description: Identify the key parameters/dimensions of a problem space. Produces a
  structured parameter list with value ranges for morphological analysis.
execution: subagent
prompt: ./prompt.md
input: system_description (string)
dependencies:
  sops:
  - spawn-agent
---

# Parameter Identification

Identify the key parameters/dimensions of a problem space.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Parameter identification requires systematic decomposition of a system into orthogonal dimensions. Benefits from focused analytical attention to ensure completeness and independence of parameters.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
