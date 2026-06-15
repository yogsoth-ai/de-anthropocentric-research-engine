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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| concept-decomposition | Tactic for breaking compound concepts into atomic parts — split over-broad concepts, identify sub-components, create child pages. |
| knowledge-structuring-consistency-checking | Tactic for verifying ontology consistency — detect contradictions, cycles, orphans, and type violations. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| alias-resolution | SOP for detecting and resolving concept aliases — merge duplicate pages, redirect edges. |
| confidence-update | SOP for updating confidence scores on claims and evidence pages based on new information. |
| gap-detection | SOP for finding structural gaps in the ontology — missing concepts, thin branches, disconnected clusters. |
| merge-candidates | SOP for identifying near-duplicate concepts that should be merged. |
| ontology-export | SOP for exporting ontology summary — generate a readable overview of the current ontology state. |

<!-- END available-tables (generated) -->
