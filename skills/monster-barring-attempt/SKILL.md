---
name: monster-barring-attempt
description: Attempt to exclude a counterexample as illegitimate by tightening definitions
  or preconditions (Lakatos monster-barring).
execution: subagent
prompt: ./prompt.md
dependencies:
  sops:
  - spawn-agent
---

# Monster-Barring Attempt

Subagent that evaluates whether a counterexample can be legitimately excluded by refining the claim's scope or definitions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
