---
name: scaling-regime-detection
description: Detect regime changes in scaling behavior — breakpoints where behavior qualitatively shifts, mechanisms behind transitions.
execution: subagent
prompt: ./prompt.md
input: performance_data (string), scale_dimensions (string)
used-by: failure-mode-analysis, scaling-frontier
---

# Scaling Regime Detection

Detect where scaling behavior qualitatively changes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one scaling regime analysis.
