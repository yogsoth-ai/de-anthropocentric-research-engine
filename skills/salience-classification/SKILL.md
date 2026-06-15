---
name: salience-classification
description: Classify stakeholders by Mitchell et al. framework (Power, Legitimacy,
  Urgency). Assigns salience category and identifies systematically excluded parties.
execution: subagent
prompt: ./prompt.md
input: stakeholder_list (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Salience Classification

Classify stakeholder salience to prioritize perspectives.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one salience classification pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
