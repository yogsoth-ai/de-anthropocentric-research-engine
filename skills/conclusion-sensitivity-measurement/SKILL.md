---
name: conclusion-sensitivity-measurement
description: Quantify how much conclusions change across all assumption negations and produce a sensitivity ranking.
execution: subagent
prompt: ./prompt.md
input: original_conclusion, re_derived_conclusions
used-by: assumption-criticality
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete sensitivity measurement and ranking across all tested assumptions.
