---
name: multi-stakeholder-simulation
description: Simulates diverse stakeholder perspectives and their strongest objections/support
  arguments. Shared across steel-manning and consensus campaigns.
execution: subagent
prompt: ./prompt.md
input: stakeholder_profiles[], decision_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Multi-Stakeholder Simulation

Simulates multiple stakeholder perspectives to surface objections and support arguments that a single-perspective analysis would miss.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Stakeholder simulation requires genuine perspective-taking — inhabiting each role fully without contamination from other perspectives. Dedicated context enables authentic role-play.

## HARD-GATE

Must simulate ≥3 distinct perspectives. Fewer than 3 perspectives cannot claim multi-stakeholder coverage.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
