---
name: practitioner-hat
description: Engineer perspective — assess buildability, cost, timeline, and integration
  challenges.
execution: subagent
prompt: ./prompt.md
input: solution (string)
dependencies:
  sops:
  - spawn-agent
---

# Practitioner Hat

Engineer perspective: assess buildability.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Engineering assessment requires systematic evaluation of implementation details that benefits from focused, uninterrupted analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
