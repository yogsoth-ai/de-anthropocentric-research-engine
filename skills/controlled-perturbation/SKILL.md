---
name: controlled-perturbation
description: Systematically vary parameters along defined axes, recording performance at each point to identify degradation thresholds.
execution: subagent
prompt: ./prompt.md
input: method (string), variation_axis (string), range (string)
used-by: validity-envelope-mapping
---

# Controlled Perturbation

Systematically perturb to find degradation thresholds.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one perturbation curve along one axis.
