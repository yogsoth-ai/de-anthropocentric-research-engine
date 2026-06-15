---
name: mechanism-mapping
description: Map causal mechanisms between variables
execution: strategy
dependencies:
  tactics:
  - counterfactual-reasoning
  - evidence-weighing
  - feedback-loop-detection
  sops:
  - mechanism-edge-creation
---

# Mechanism Mapping

Construct the directed causal graph by creating mechanism edges between the variables identified in the variable-identification phase. Each edge must carry a plain-language description of the underlying mechanism and at least one evidence citation.

## Guiding Focus

CC must treat each proposed edge as a hypothesis, not a fact. For every mechanism edge created, the description should answer three questions: what is the pathway, under what conditions does it hold, and what would falsify it. Edges without a plausible mechanism description are placeholders and must be revisited. The goal is a graph where every arrow is defensible, not merely plausible.

## Available Tactics

- counterfactual-reasoning — for each edge A→B, ask "if A were held constant, would B still change?" to stress-test the mechanism
- evidence-weighing — rank competing mechanism descriptions by the strength and independence of their supporting citations
- feedback-loop-detection — scan the emerging graph for cycles that would indicate feedback rather than one-way causation

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Mechanism edges created | 10 | 25 | 50 |
| Mechanism descriptions | 5 | 15 | 30 |
| Evidence citations | 8 | 20 | 40 |

## State Ledger Template

```
| Metric                  | Target | Current | Status |
|-------------------------|--------|---------|--------|
| Mechanism edges created | S:10 / M:25 / L:50 | 0 | ⬜ |
| Mechanism descriptions  | S:5 / M:15 / L:30  | 0 | ⬜ |
| Evidence citations      | S:8 / M:20 / L:40  | 0 | ⬜ |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>
