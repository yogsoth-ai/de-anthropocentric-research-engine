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
