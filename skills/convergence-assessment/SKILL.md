---
name: convergence-assessment
description: Compare results across multiple model variants — quantitative agreement metrics and qualitative conclusion stability.
execution: subagent
prompt: ./prompt.md
input: model_outputs (string), comparison_criteria (string)
used-by: robustness-testing
---

# Convergence Assessment

Assess whether conclusions converge across model variants.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one convergence assessment pass.
