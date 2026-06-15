---
name: benchmark-challenge
description: Identify and negate benchmark assumptions. Deconstruct best practices
  to reveal hidden constraints and open new spaces.
execution: subagent
prompt: ./prompt.md
input: benchmark_or_best_practice (string), domain_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Benchmark Challenge

Identify and negate benchmark assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Benchmark challenge requires deep analysis of why a best practice exists, what assumptions it encodes, and what happens when those assumptions are violated. Benefits from dedicated critical focus.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
