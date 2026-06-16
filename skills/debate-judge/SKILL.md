---
name: debate-judge
description: Evaluates debate exchanges, adjudicates argument quality, and produces
  round verdicts with confidence scores and reasoning.
execution: subagent
prompt: ./prompt.md
input: attacks (string), defenses (string), round_number (string), judging_criteria
  (string)
dependencies:
  sops:
  - spawn-agent
---

# Debate Judge

Evaluates exchanges and produces round verdicts.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Judgment requires neutral stance isolated from both attack and defense reasoning. Dedicated context prevents bias from prior participation.

## Input

- **attacks**: Structured attacks from debate-critic
- **defenses**: Structured defenses from debate-defender
- **round_number**: Current round in the debate
- **judging_criteria**: Specific criteria for this debate type

## Output

- **round_verdict**: Which side prevailed this round (critic/defender/draw)
- **scores**: Per-attack scoring (attack quality, defense quality, net result)
- **confidence**: Judge's confidence in artifact viability (0.0–1.0)
- **key_findings**: Most important insights from this round

## Budget

One unit = one round verdict.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
