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
