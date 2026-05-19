---
name: morris-screening
description: Morris method screening — compute elementary effects to quickly identify important vs unimportant parameters.
execution: subagent
prompt: ./prompt.md
input: parameter_space_definition, model_description
used-by: parameter-screening
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Morris screening analysis (trajectories designed, elementary effects computed, parameters ranked).
