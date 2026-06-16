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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| hierarchy-construction | Tactic for building is-a and part-of hierarchies — establish parent-child relationships, verify transitivity, detect cycles. |
| knowledge-structuring-consistency-checking | Tactic for verifying ontology consistency — detect contradictions, cycles, orphans, and type violations. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| edge-batch-creation | SOP for creating multiple edges in a batch — efficient bulk relationship creation. |

<!-- END available-tables (generated) -->
