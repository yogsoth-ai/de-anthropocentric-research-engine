---
name: alternative-model-generation
description: Generate alternative model formulations by relaxing, replacing, or generalizing specific assumptions.
execution: subagent
prompt: ./prompt.md
input: original_model (string), assumption_to_relax (string)
used-by: robustness-testing
---

# Alternative Model Generation

Generate model variants by relaxing assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one alternative model generation pass.
