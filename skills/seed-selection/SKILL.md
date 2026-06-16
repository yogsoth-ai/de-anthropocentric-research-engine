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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
