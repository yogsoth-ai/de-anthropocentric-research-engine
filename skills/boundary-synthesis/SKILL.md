---
name: boundary-synthesis
description: Compile all boundary analysis products into a coherent report — validity envelopes, robustness results, failure catalogs, scaling maps, safe operating conditions.
execution: subagent
prompt: ./prompt.md
input: intermediate_products (string), synthesis_scope (string)
used-by: boundary-analysis
---

# Boundary Synthesis

Compile boundary analysis into a final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one synthesis report generation.
