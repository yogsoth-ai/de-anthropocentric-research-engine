---
name: edge-case-generation
description: Systematically generate boundary inputs — boundary values, adversarial constructions, distribution shifts, rare combinations, scale extremes.
execution: subagent
prompt: ./prompt.md
input: method_description (string), domain (string)
used-by: failure-mode-analysis
---

# Edge Case Generation

Generate systematic edge cases to probe failures.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one edge case generation pass (minimum 20 cases).
