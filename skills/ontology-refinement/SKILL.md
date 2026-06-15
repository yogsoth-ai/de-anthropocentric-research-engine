---
name: ontology-refinement
description: Strategy for iterative ontology improvement — merge duplicates, fill
  gaps, update confidence, prune dead branches.
execution: strategy
dependencies:
  tactics:
  - concept-decomposition
  - knowledge-structuring-consistency-checking
  sops:
  - alias-resolution
  - confidence-update
  - gap-detection
  - merge-candidates
  - ontology-export
---

# Ontology Refinement

Iteratively improve the ontology. Merge near-duplicates, fill identified gaps, update confidence scores based on new evidence, prune concepts that proved irrelevant.

## Guiding Focus

Refinement is where ontologies become useful. The first pass is always rough — refinement makes it precise. Be willing to delete concepts that don't earn their place.

## Available Tactics

- concept-decomposition — split over-broad concepts
- consistency-checking — verify refinements don't introduce conflicts

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Merges performed | 2 | 5 | 12 |
| Gaps filled | 3 | 8 | 15 |
| Confidence updates | 5 | 15 | 30 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Merges performed    | X      | 0       | ⬜     |
| Gaps filled         | X      | 0       | ⬜     |
| Confidence updates  | X      | 0       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>
