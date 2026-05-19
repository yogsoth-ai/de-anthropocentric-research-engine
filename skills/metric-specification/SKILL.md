---
name: metric-specification
description: "Define experiment metrics and significance standards"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - factor-level-design
  - ablation-design
  - comparison-design
  - scaling-design
  - robustness-design
  - statistical-method-selection
input: hypothesis, task domain, evaluation requirements
output: metric definitions with significance thresholds
---

# SOP: Metric Specification

Define primary and secondary metrics, measurement procedures, and pre-registered significance thresholds for the experiment.

Subagent — spawned via subagent-spawning/spawn-agent skill.

**Shared**: This SOP is used across all strategies as every experiment requires well-defined metrics.
