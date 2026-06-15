---
name: evidence-grading
description: Assess evidence quality using GRADE/SOE framework. Rates certainty level
  and identifies downgrade reasons.
execution: subagent
prompt: ./prompt.md
input: evidence_collection (string), grading_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Evidence Grading

Assess the quality and certainty of evidence supporting or surrounding a gap.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one evidence grading assessment.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
