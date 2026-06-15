---
name: catwoe-analysis
description: Apply Checkland's CATWOE analysis from a specific stakeholder perspective
  to reveal how the problem looks from that viewpoint.
execution: subagent
prompt: ./prompt.md
input: system_description, stakeholder_perspective
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CATWOE analysis from one stakeholder perspective.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
