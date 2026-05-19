---
name: interaction-detection
description: Detect and characterize significant parameter interactions from Sobol decomposition results.
execution: subagent
prompt: ./prompt.md
input: sobol_results
used-by: variance-decomposition
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete interaction analysis (detection, characterization, implications).
