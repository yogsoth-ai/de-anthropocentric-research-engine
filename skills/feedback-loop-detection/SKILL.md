---
name: feedback-loop-detection
description: Tactic for identifying circular causation — detect feedback loops, classify
  as reinforcing or balancing, document loop structure.
execution: tactic
dependencies:
  sops:
  - causal-chain-query
  - loop-documentation
  - mechanism-edge-creation
---

# Feedback Loop Detection

Identify circular causation in the causal graph. Most real systems have feedback loops — they must be documented explicitly.

## Available SOPs

- causal-chain-query — trace paths looking for cycles
- loop-documentation — document identified loops
- mechanism-edge-creation — create edges that close loops

## Guiding Principles

- **Loops are normal.** Don't assume acyclicity. Real causal systems almost always have feedback.
- **Classify loops.** Reinforcing (positive feedback, amplification) vs balancing (negative feedback, homeostasis).
- **Time delays matter.** A loop with a 10-year delay behaves differently from one with a 10ms delay.
- **Dominant loops.** In systems with multiple loops, identify which loop dominates behavior.
- **Break points.** Identify where interventions could break harmful loops.

## Minimum Yield

<HARD-GATE>
≥1 loop identified and classified (or explicit confirmation that no loops exist in the current subgraph) per invocation.
</HARD-GATE>
