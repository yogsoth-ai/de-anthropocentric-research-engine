---
name: perspective-assignment
description: Define distinct stakeholder or analytical perspectives with their values, concerns, and evaluation criteria.
execution: subagent
prompt: ./prompt.md
input: decision, stakeholders
used-by: [steel-manning]
---

# Perspective Assignment

Defines distinct perspectives for multi-perspective attack — each with unique values, concerns, success criteria, and likely objections. Perspectives must be genuinely different to ensure comprehensive coverage.

## Execution

Spawns a subagent that analyzes the decision context and stakeholder landscape to produce well-differentiated perspective briefs.

## Why Subagent

- Perspective design requires creative differentiation
- Each perspective must be internally coherent and genuinely distinct
- Isolation ensures perspectives are designed for challenge value, not convenience

## HARD-GATE

Output must include:
- >= 3 distinct perspective briefs
- Each perspective must have unique values (not overlapping)
- Each must include specific concerns relevant to the decision
- Each must define what "failure" looks like from that perspective
