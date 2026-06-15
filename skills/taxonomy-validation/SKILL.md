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
