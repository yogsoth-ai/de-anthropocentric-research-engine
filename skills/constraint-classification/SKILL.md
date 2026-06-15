---
name: constraint-classification
description: Classify constraints into hard constraints, soft constraints, and assumptions.
execution: subagent
prompt: ./prompt.md
input: constraints[]
dependencies:
  sops:
  - spawn-agent
---

# Constraint Classification

Take a list of identified constraints and classify each into one of three categories: hard constraints (immovable, must be accepted), soft constraints (can be worked around or mitigated), and assumptions (unvalidated beliefs that may or may not be real constraints).

## Execution

Spawns a subagent that:
1. Receives list of identified constraints
2. Evaluates each constraint against classification criteria
3. Assigns category with justification
4. Identifies which assumptions are most dangerous if wrong
5. Returns classified constraint inventory

## Why Subagent

Classification requires careful judgment about what is truly immovable vs. what merely appears so. A dedicated subagent can focus on this distinction without being biased by prior analysis.

## HARD-GATE

Output MUST include: all input constraints classified, at least one constraint in each category (hard/soft/assumption), and justification for each classification. Reject if any input constraint is missing from output.
