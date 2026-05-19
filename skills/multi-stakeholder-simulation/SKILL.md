---
name: multi-stakeholder-simulation
description: Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis.
execution: subagent
prompt: ./prompt.md
input: target (string), stakeholder_roles (string), evaluation_criteria (string)
used-by: gap-analysis, insight, problem-reformulation
---

# Multi-Stakeholder Simulation

Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Simulating multiple distinct expert perspectives requires dedicated context to maintain role consistency.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one multi-perspective simulation producing cross-stakeholder synthesis.
