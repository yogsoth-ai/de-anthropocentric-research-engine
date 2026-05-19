---
name: conjunctive-filter
description: Apply conjunctive screening rules to eliminate candidates that fail any threshold.
execution: subagent
prompt: ./prompt.md
input: candidates (string[]), thresholds (object[])
used-by: multi-criteria-scoring
---

# Conjunctive Filter

Screen candidate alternatives using conjunctive rules (all criteria must be met); any criterion failing to meet its threshold results in elimination.

## Execution

Subagent receives candidate list and threshold definitions, checks each alternative against all thresholds one by one, and outputs pass/eliminate classification.

## Why Subagent

Screening logic is simple but requires strict execution; independent operation ensures no violations are missed.

## HARD-GATE

Each elimination decision must specify the violated criterion, actual value, and threshold value; no vague eliminations allowed.
