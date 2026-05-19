---
name: removability-assessment
description: Assess how removable a constraint is with effort estimate and dependency analysis.
execution: subagent
prompt: ./prompt.md
input: constraint
used-by: feasibility-assessment
---

# Removability Assessment

For a given constraint, assess how removable it is on a 0-1 scale, estimate the effort required to remove it, and identify dependencies that affect removability.

## Execution

Spawns a subagent that:
1. Receives a single constraint with its classification and context
2. Evaluates removability across multiple factors
3. Estimates effort (time, cost, expertise) to remove
4. Identifies dependencies and prerequisites for removal
5. Returns removability score with supporting analysis

## Why Subagent

Removability assessment requires focused analysis of a single constraint's characteristics, including research into analogous situations where similar constraints were or were not removed.

## HARD-GATE

Output MUST include: removability score (0.0-1.0), effort estimate, and at least 1 dependency identified. Reject if score is provided without supporting rationale.
