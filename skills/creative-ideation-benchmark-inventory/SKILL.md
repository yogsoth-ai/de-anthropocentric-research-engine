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
