---
name: assumption-challenging
description: Challenge each assumption's validity — shared cross-repo SOP
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
shared: true
input: list of assumptions with context
output: validity assessment with confidence scores and evidence
dependencies:
  sops:
  - spawn-agent
---

# SOP: Assumption Challenging

Challenge each assumption's validity using systematic questioning. Determine which assumptions are well-founded, which are fragile, and which are likely false.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: This SOP is used across multiple strategies (assumption-constraint, conflict-resolution, constraint-breaking) and campaigns.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
