---
name: taxonomy-validation
description: Strategy for validating ontology consistency — check hierarchy, detect
  cycles, verify completeness.
execution: strategy
dependencies:
  tactics:
  - hierarchy-construction
  - knowledge-structuring-consistency-checking
  sops:
  - gap-detection
  - hierarchy-visualization
  - ontology-export
---

# Taxonomy Validation

Validate the constructed ontology for structural integrity. Check for cycles in hierarchies, orphaned branches, inconsistent typing, and coverage gaps.

## Guiding Focus

An ontology that contradicts itself is worse than no ontology. Validation is not optional — it's the quality gate that separates useful structure from noise.

## Available Tactics

- consistency-checking — systematic integrity verification
- hierarchy-construction — repair broken hierarchies

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Lint issues resolved | 5 | 15 | 30 |
| Hierarchy levels verified | 2 | 3 | 4 |
| Cross-checks performed | 3 | 8 | 15 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Lint issues resolved| X      | 0       | ⬜     |
| Levels verified     | X      | 0       | ⬜     |
| Cross-checks done   | X      | 0       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| hierarchy-construction | Tactic for building is-a and part-of hierarchies — establish parent-child relationships, verify transitivity, detect cycles. |
| knowledge-structuring-consistency-checking | Tactic for verifying ontology consistency — detect contradictions, cycles, orphans, and type violations. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| gap-detection | SOP for finding structural gaps in the ontology — missing concepts, thin branches, disconnected clusters. |
| hierarchy-visualization | SOP for inspecting the current hierarchy structure — query graph to display parent-child relationships. |
| ontology-export | SOP for exporting ontology summary — generate a readable overview of the current ontology state. |

<!-- END available-tables (generated) -->
