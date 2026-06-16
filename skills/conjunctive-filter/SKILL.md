---
name: conjunctive-filter
description: Apply conjunctive screening rules to eliminate candidates that fail any
  threshold.
execution: subagent
prompt: ./prompt.md
input: candidates (string[]), thresholds (object[])
dependencies:
  sops:
  - spawn-agent
---

# Conjunctive Filter

Screen candidate alternatives using conjunctive rules (all criteria must be met); any criterion failing to meet its threshold results in elimination.

## Execution

Subagent receives candidate list and threshold definitions, checks each alternative against all thresholds one by one, and outputs pass/eliminate classification.

## Why Subagent

Screening logic is simple but requires strict execution; independent operation ensures no violations are missed.

## HARD-GATE

Each elimination decision must specify the violated criterion, actual value, and threshold value; no vague eliminations allowed.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
