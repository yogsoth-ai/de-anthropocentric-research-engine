---
name: hmw-formulation
description: Generate "How Might We" questions at different scope levels (narrow,
  medium, broad). Ensures each is actionable without being prescriptive.
execution: subagent
prompt: ./prompt.md
input: insight_or_tension (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# HMW Formulation

Generate generative How Might We research questions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one HMW formulation pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
