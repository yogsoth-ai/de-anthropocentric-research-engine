---
name: baseline-selection
description: "Select appropriate baselines for experimental comparison"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - comparison-design
  - ablation-design
  - robustness-design
input: proposed method, task domain, prior work
output: ranked baseline list with justification and sources
---

# SOP: Baseline Selection

Select appropriate baselines that provide meaningful comparison points, covering SOTA, simple, and internal baselines.

Subagent — spawned via subagent-spawning/spawn-agent skill.
