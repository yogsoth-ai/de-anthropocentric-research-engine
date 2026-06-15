---
name: sobol-decomposition
description: Sobol variance decomposition — compute first-order and total-order sensitivity
  indices for precise variance attribution.
execution: subagent
prompt: ./prompt.md
input: model_description, input_distributions, sample_size
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Sobol decomposition (sampling, index computation, interpretation).
