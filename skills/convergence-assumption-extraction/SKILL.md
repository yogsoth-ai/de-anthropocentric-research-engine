---
name: convergence-assumption-extraction
description: Systematically surface hidden assumptions underlying a decision with
  confidence levels.
execution: subagent
prompt: ./prompt.md
input: decision, evidence
dependencies:
  sops:
  - spawn-agent
---

# Assumption Extraction

Surfaces all hidden assumptions underlying a decision — the unstated beliefs that must be true for the decision to be correct. Each assumption is tagged with a confidence level indicating how certain we are that it holds.

## Execution

Spawns a subagent that systematically examines the decision and its evidence base to extract implicit assumptions across multiple categories.

## Why Subagent

- Assumption extraction requires focused, systematic attention
- The extractor must examine the decision from outside, without the decision-maker's blind spots
- Isolation prevents rationalization of assumptions as "obvious"

## HARD-GATE

Output must include:
- >= 5 distinct assumptions
- Confidence level for each (HIGH/MEDIUM/LOW)
- Category for each (causal, scope, temporal, resource, stakeholder, technical)
- Brief justification for each confidence rating

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
