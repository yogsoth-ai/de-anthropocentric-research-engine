---
name: seed-protocol-design
description: 'SOP: design random seed strategy for reproducibility'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: Experiment design + list of randomness sources + repetition requirements
output: Seed allocation strategy + seed value table + reproducibility guarantee plan
dependencies:
  sops:
  - spawn-agent
---

# SOP: Seed Protocol Design

Design random seed strategy to ensure experiment reproducibility while quantifying variance from randomness through multi-seed runs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Seed strategy requires identifying all randomness sources in the system (initialization, data sampling, dropout, etc.) and designing a consistent seed propagation scheme — demands deep understanding of system architecture.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
