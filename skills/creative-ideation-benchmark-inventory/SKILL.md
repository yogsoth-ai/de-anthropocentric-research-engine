---
name: benchmark-inventory
description: Catalog all known solutions/methods in a domain with performance, applicability,
  and limitations.
execution: subagent
prompt: ./prompt.md
input: domain (string)
dependencies:
  sops:
  - spawn-agent
---

# Benchmark Inventory

Catalog all known solutions/methods in a domain. Produces a structured inventory with performance metrics, applicability scope, and known limitations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Comprehensive benchmarking requires deep, focused research across multiple sources (papers, benchmarks, surveys). Benefits from dedicated context that can accumulate findings without polluting the orchestrator's state.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
