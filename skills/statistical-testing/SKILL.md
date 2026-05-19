---
name: statistical-testing
description: "Execute statistical tests — bootstrap, permutation, Bayesian ROPE — on experiment results"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - result-analysis
  - result-validation-loop
shared-with: experiment-design
input: structured result set and pre-registered hypotheses with ROPE
output: statistical test results with effect sizes, CIs, and ROPE judgment
---

# SOP: Statistical Testing

Execute pre-registered statistical tests on experiment results using bootstrap, permutation, and/or Bayesian ROPE methods.

Subagent — spawned via subagent-spawning/spawn-agent skill.
