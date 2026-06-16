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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
