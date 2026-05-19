---
name: validity-envelope-construction
description: Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects.
execution: subagent
prompt: ./prompt.md
input: perturbation_data (string), axes (string)
used-by: validity-envelope-mapping
---

# Validity Envelope Construction

Construct the multi-dimensional validity boundary.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one envelope construction from perturbation data.
