---
name: reproducibility-verification
description: "Verify result reproducibility via re-runs with different seeds and ICC comparison"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - result-analysis
  - result-validation-loop
shared-with: experiment-design
input: experiment design, original results, re-run parameters (n_reruns, seeds)
output: reproducibility assessment with ICC scores and variance decomposition
---

# SOP: Reproducibility Verification

Re-run the experiment with different seeds and compare results to assess reproducibility via ICC and variance analysis.

Subagent — spawned via subagent-spawning/spawn-agent skill.
