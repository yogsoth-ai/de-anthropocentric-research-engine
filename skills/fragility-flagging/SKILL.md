---
name: fragility-flagging
description: Identify which specific assumption changes cause conclusion divergence. Rates fragility severity and plausibility of alternatives.
execution: subagent
prompt: ./prompt.md
input: convergence_results (string), context (string)
used-by: robustness-testing
---

# Fragility Flagging

Flag conclusions that are fragile to assumption changes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one fragility assessment pass.
