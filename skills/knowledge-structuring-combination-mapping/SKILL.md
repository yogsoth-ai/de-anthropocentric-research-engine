---
name: combination-mapping
description: Strategy for enumerating meaningful combinations across dimensions and
  marking existing work.
execution: strategy
dependencies:
  tactics:
  - axis-extraction
  - matrix-generation
  sops:
  - combination-enumeration
---

# Combination Mapping

Enumerate combinations across identified dimensions. Mark which cells are occupied (existing work), which are empty (opportunities), and which are impossible (constraints).

## Guiding Focus

The matrix is the map. Populate it systematically — for each combination, determine if existing work covers it, if it's feasible but unexplored, or if it's impossible due to constraints.

## Available Tactics

- matrix-generation — generate and populate the combination matrix
- axis-extraction — refine axes based on what combinations reveal

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Combinations explored | 8 | 25 | 50 |
| Existing work mapped | 5 | 15 | 30 |
| Empty cells identified | 3 | 10 | 20 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Combinations explored| X     | 0       | ⬜     |
| Existing work mapped| X      | 0       | ⬜     |
| Empty cells found   | X      | 0       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| axis-extraction | Tactic for systematically extracting axes of variation from literature — identify how practitioners compare approaches. |
| matrix-generation | Tactic for generating and populating combination matrices — cross dimensions to enumerate the design space. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| combination-enumeration | SOP for systematically enumerating combinations across dimensions. |

<!-- END available-tables (generated) -->
