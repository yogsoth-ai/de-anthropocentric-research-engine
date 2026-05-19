---
name: competitive-move-prediction
description: "Predict competitor progress, publications, and strategic moves"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - competitive-scenario
input: competitor profile, publication history, resource level, research field context
output: predicted actions, timelines, preemption risk assessment
---

# SOP: Competitive Move Prediction

Predict what key competitors will do next based on their publication patterns, resource levels, hiring signals, and strategic positioning. Assess preemption risk and time windows.

Subagent — spawned via subagent-spawning/spawn-agent skill.
