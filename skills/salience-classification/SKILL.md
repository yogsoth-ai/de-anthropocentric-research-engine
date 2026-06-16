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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
