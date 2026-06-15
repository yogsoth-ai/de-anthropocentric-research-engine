---
name: reformulation-synthesis
description: Compile all problem reformulation analyses into a coherent report with
  a recommended new problem definition.
execution: subagent
prompt: ./prompt.md
input: dominant_ideas, provocations, perspectives, dialectics, wickedness_assessment,
  appreciative_findings
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete reformulation synthesis report.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
