---
name: design-matrix-construction
description: "Build the experiment design matrix with proper orthogonality and balance"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - factor-level-design
  - scaling-design
  - robustness-design
  - budget-constrained-design
input: factors with levels, design type, budget constraint
output: complete design matrix with run order
---

# SOP: Design Matrix Construction

Build the actual design matrix specifying all experimental runs, including proper orthogonality, balance, and randomized run order.

Subagent — spawned via subagent-spawning/spawn-agent skill.
