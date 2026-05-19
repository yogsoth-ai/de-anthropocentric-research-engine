---
name: objective-definition
description: Define optimization objectives, constraints, and trade-off preferences from context and candidate information.
execution: subagent
prompt: ./prompt.md
input: context, candidates
used-by: portfolio-optimization
---

# Objective Definition

Translate problem context and candidate information into formal optimization objectives, binding constraints, and stakeholder trade-off preferences.

## Execution

Spawns a subagent that analyzes the provided context and candidate set to produce:
- Clearly defined objectives with measurement criteria
- Binding constraints with thresholds
- Trade-off preferences indicating relative importance

## Why Subagent

Objective definition requires careful analysis of context, stakeholder needs, and candidate attributes to formalize what might be implicit. This focused analytical work benefits from dedicated attention without polluting the orchestrator's context.

## HARD-GATE

Output must contain at least 2 distinct objectives and at least 1 constraint. If fewer can be identified, the subagent must flag this and request clarification.
