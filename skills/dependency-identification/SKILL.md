---
name: dependency-identification
description: Identify critical dependencies from ablation results, producing a dependency
  graph and highlighting critical components.
execution: subagent
prompt: ./prompt.md
input: ablation_results (object)
dependencies:
  sops:
  - spawn-agent
---

# Dependency Identification

Extract a dependency graph from ablation results, identifying which components are critical and how they relate.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Dependency analysis requires synthesizing ablation data into graph structures and identifying non-obvious transitive dependencies. Benefits from focused analytical context.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
