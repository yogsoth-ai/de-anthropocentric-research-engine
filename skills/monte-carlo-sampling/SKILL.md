---
name: monte-carlo-sampling
description: Design and execute Monte Carlo sampling strategy for uncertainty propagation through a model.
execution: subagent
prompt: ./prompt.md
input: input_distributions, model_structure
used-by: uncertainty-propagation
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Monte Carlo propagation (sampling design, execution, output characterization).
