---
name: factor-identification
description: Identify independent, dependent, and control variables for an experiment
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: hypothesis, system description, prior work
output: structured factor list with classifications
dependencies:
  sops:
  - spawn-agent
---

# SOP: Factor Identification

Identify all independent variables (factors to manipulate), dependent variables (outcomes to measure), and control variables (confounds to hold constant) for the experiment.

Subagent — spawned via subagent-spawning/spawn-agent skill.
