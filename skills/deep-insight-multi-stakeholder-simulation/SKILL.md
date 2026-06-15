---
name: multi-stakeholder-simulation
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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
