---
name: counterexample-generation
description: Systematically generate counterexamples (monsters) to a given claim using
  diverse heuristic strategies.
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Counterexample Generation

Subagent that produces counterexamples to a claim using boundary cases, degenerate cases, and domain-specific heuristics.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
