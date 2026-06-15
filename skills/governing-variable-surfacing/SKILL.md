---
name: governing-variable-surfacing
description: Apply Argyris framework to identify governing variables — the unstated
  rules driving behavior in a research field.
execution: subagent
prompt: ./prompt.md
input: observed_behavior_patterns
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete governing variable analysis for a field/domain.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
