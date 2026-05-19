---
name: sample-size-estimation
description: "SOP: power analysis and required experiment count estimation"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - factor-level-design
  - comparison-design
input: "Effect size estimate + significance level + statistical power requirement + experiment design type"
output: "Required sample size/repetition count + power analysis report"
---

# SOP: Sample Size Estimation

Determine required sample size or repetition count through power analysis, ensuring the experiment has sufficient statistical power to detect the expected effect.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Sample size estimation requires multi-step calculations based on effect size, variance estimates, and design type, involving deep statistical reasoning suited for an independent subagent.
