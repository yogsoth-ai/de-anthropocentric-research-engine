---
name: matrix-generation
description: Tactic for generating and populating combination matrices — cross dimensions
  to enumerate the design space.
execution: tactic
dependencies:
  sops:
  - combination-enumeration
  - knowledge-structuring-novelty-scoring
  - matrix-export
  - question-generation
---

# Matrix Generation

Generate combination matrices by crossing dimensions. Populate cells with existing work, mark empty cells as opportunities, flag impossible combinations.

## Available SOPs

- combination-enumeration — systematically enumerate all combinations
- novelty-scoring — score empty cells by novelty potential
- question-generation — generate research questions from promising gaps
- matrix-export — export matrix as readable document

## Guiding Principles

- **Start 2D.** Begin with pairs of dimensions before attempting higher-dimensional matrices.
- **Sparse is normal.** Most real design spaces are sparsely populated — that's the point.
- **Impossible ≠ unexplored.** Mark truly impossible combinations (physical constraints, logical contradictions) differently from merely unexplored ones.
- **Cluster patterns.** Look for patterns in which cells are populated — they reveal community preferences and blind spots.

## Minimum Yield

<HARD-GATE>
≥1 matrix generated with ≥50% of cells classified (occupied/empty/impossible) per invocation.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| combination-enumeration | SOP for systematically enumerating combinations across dimensions. |
| knowledge-structuring-novelty-scoring | SOP for scoring empty cells by novelty potential — how surprising and valuable would this combination be? |
| matrix-export | SOP for exporting the dimensional matrix as a readable document or structured data. |
| question-generation | SOP for generating research questions from promising gaps in the design space. |

<!-- END available-tables (generated) -->
