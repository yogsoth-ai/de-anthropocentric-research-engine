---
name: analogy-quality-assessment
description: Assess analogy depth (surface/structural/systemic). Determines whether
  an analogy warrants transfer investment.
execution: subagent
prompt: ./prompt.md
input: analogy_mapping (string)
dependencies:
  sops:
  - spawn-agent
---

# Analogy Quality Assessment

Assess analogy depth (surface/structural/systemic).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Quality assessment requires rigorous, unbiased evaluation of analogy depth. Benefits from a dedicated evaluator role that is not invested in the analogy's success and can apply strict classification criteria without creative bias.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
