---
name: relation-typing
description: Strategy for identifying and typing relationships between concepts —
  create edges with appropriate types and weights.
execution: strategy
dependencies:
  tactics:
  - hierarchy-construction
  - knowledge-structuring-consistency-checking
  sops:
  - edge-batch-creation
---

# Relation Typing

Identify relationships between extracted concepts and type them using the edge type vocabulary. Every concept should connect to at least 2 others.

## Guiding Focus

Relationships are more important than concepts in an ontology. Focus on making the graph dense and meaningful. Choose edge types carefully — a wrong type is worse than a missing edge.

## Available Tactics

- hierarchy-construction — build is-a and part-of hierarchies
- consistency-checking — verify no contradictory edges

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Edges created | 20 | 60 | 150 |
| Edge types used | 4 | 6 | 8 |
| Orphans remaining | <3 | <5 | <8 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Edges created       | X      | 0       | ⬜     |
| Edge types used     | X      | 0       | ⬜     |
| Orphans remaining   | <X     | ?       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>
