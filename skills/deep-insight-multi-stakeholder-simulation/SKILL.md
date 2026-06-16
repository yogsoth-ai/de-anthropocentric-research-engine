---
name: deep-insight-multi-stakeholder-simulation
description: Simulate multiple stakeholder perspectives evaluating a research gap,
  method, or proposal. Identifies blind spots from single-perspective analysis.
execution: subagent
prompt: ./prompt.md
input: target (string), stakeholder_roles (string), evaluation_criteria (string)
dependencies:
  sops:
  - spawn-agent
---

# Multi-Stakeholder Simulation

Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Simulating multiple distinct expert perspectives requires dedicated context to maintain role consistency.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one multi-perspective simulation producing cross-stakeholder synthesis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
