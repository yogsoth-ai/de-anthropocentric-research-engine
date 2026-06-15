---
name: csh-12-question
description: Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions
  (motivation, control, expertise, legitimacy) comparing is vs ought.
execution: subagent
prompt: ./prompt.md
input: system_description (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# CSH 12-Question

Critical Systems Heuristics boundary analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CSH 12-question analysis pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
