---
name: seed-selection
description: Validate and prioritize starting papers for snowball surveys. Evaluates
  which seeds will yield the richest citation traces based on citation count, recency,
  and network position.
execution: subagent
prompt: ./prompt.md
input: seed_papers (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Seed Selection

Validate and prioritize starting papers for snowball surveys.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Seed evaluation requires analyzing citation networks and making strategic judgments about which papers will yield the richest traces. Dedicated context for this analytical work.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
