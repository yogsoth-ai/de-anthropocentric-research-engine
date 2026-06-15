---
name: consistency-pair-evaluation
description: Pairwise consistency assessment using Cross-Consistency Assessment (CCA)
  matrix
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: Zwicky Box (parameter × value matrix), evaluation criteria
output: CCA matrix with pairwise consistency scores, surviving configurations list
dependencies:
  sops:
  - spawn-agent
---

# SOP: Consistency Pair Evaluation

Evaluate all pairwise combinations of parameter values for internal consistency using Cross-Consistency Assessment (CCA). Produce a matrix that enables filtering of the morphological field to retain only plausible configurations.

Subagent — spawned via subagent-spawning/spawn-agent skill.
