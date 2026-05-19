---
name: seed-protocol-design
description: "SOP: design random seed strategy for reproducibility"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - reproducibility-protocol
input: "Experiment design + list of randomness sources + repetition requirements"
output: "Seed allocation strategy + seed value table + reproducibility guarantee plan"
---

# SOP: Seed Protocol Design

Design random seed strategy to ensure experiment reproducibility while quantifying variance from randomness through multi-seed runs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Seed strategy requires identifying all randomness sources in the system (initialization, data sampling, dropout, etc.) and designing a consistent seed propagation scheme — demands deep understanding of system architecture.
