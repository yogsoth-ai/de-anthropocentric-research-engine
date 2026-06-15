---
name: baseline-selection
description: Select appropriate baselines for experimental comparison
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: proposed method, task domain, prior work
output: ranked baseline list with justification and sources
dependencies:
  sops:
  - spawn-agent
---

# SOP: Baseline Selection

Select appropriate baselines that provide meaningful comparison points, covering SOTA, simple, and internal baselines.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
