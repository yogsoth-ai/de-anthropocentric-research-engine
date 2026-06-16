---
name: stakeholder-confirmation
description: Simulate stakeholder perspectives to validate gap priorities. Assesses
  gap value from researcher, practitioner, funder, and end-user viewpoints.
execution: subagent
prompt: ./prompt.md
input: gap (string), stakeholder_roles (string)
dependencies:
  sops:
  - spawn-agent
---

# Stakeholder Confirmation

Validate gap priorities across multiple stakeholder perspectives.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one stakeholder confirmation pass for a single gap.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
