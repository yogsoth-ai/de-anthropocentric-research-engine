---
name: benchmark-challenge
description: Identify and negate benchmark assumptions. Deconstruct best practices to reveal hidden constraints and open new spaces.
execution: subagent
prompt: ./prompt.md
input: benchmark_or_best_practice (string), domain_context (string)
used-by: anti-benchmark, sacred-cow-hunting
---

# Benchmark Challenge

Identify and negate benchmark assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Benchmark challenge requires deep analysis of why a best practice exists, what assumptions it encodes, and what happens when those assumptions are violated. Benefits from dedicated critical focus.
