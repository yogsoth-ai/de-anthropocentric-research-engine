---
name: constraint-identification-sop
description: Identify constraints for a candidate using TOC, TRIZ, and Pre-mortem
  methods.
execution: subagent
prompt: ./prompt.md
input: candidate, context
dependencies:
  sops:
  - spawn-agent
---

# Constraint Identification SOP

Systematically discover all constraints that could prevent a candidate from being implemented. Applies three complementary methods: Theory of Constraints (find the bottleneck), TRIZ contradiction analysis (surface technical/physical contradictions), and Pre-mortem (imagine failure and trace causes).

## Execution

Spawns a subagent that:
1. Receives candidate description and implementation context
2. Applies TOC to identify system bottlenecks
3. Applies TRIZ to surface contradictions
4. Runs Pre-mortem to imagine failure scenarios
5. Deduplicates and returns consolidated constraint list

## Why Subagent

Constraint discovery requires creative, divergent thinking across multiple frameworks. Running as a subagent prevents premature filtering and ensures all three methods are fully applied.

## HARD-GATE

Output MUST include: at least 3 constraints identified, method attribution for each, and initial severity estimate. Reject if fewer than 3 constraints found.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
