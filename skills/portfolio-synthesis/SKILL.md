---
name: portfolio-synthesis
description: Synthesize all per-scenario evaluations into a final portfolio recommendation with robustness score and actionable guidance.
execution: subagent
prompt: ./prompt.md
input: all_evaluations
used-by: portfolio-optimization
---

# Portfolio Synthesis

Aggregate evaluations across all scenarios into a final portfolio recommendation, robustness assessment, and actionable guidance.

## Execution

Spawns a subagent that synthesizes per-scenario results into a coherent overall assessment with clear recommendation.

## Why Subagent

Synthesis requires integrating multiple scenario evaluations, identifying patterns across scenarios, and making a holistic judgment. This integrative reasoning benefits from seeing all data together with focused attention.

## HARD-GATE

Output must include a final portfolio recommendation, numeric robustness score (0-1), and specific actionable recommendations. The synthesis must reference findings from all evaluated scenarios.
