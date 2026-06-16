---
name: dimension-discovery
description: Strategy for identifying fundamental dimensions of variation in a design
  space.
execution: strategy
dependencies:
  tactics:
  - axis-extraction
  - matrix-generation
  sops:
  - dimension-page-creation
---

# Dimension Discovery

Identify the fundamental axes of variation that define the design space. Each dimension should be independent and meaningful.

## Guiding Focus

Look for the axes that practitioners implicitly use when comparing approaches. "Fast vs accurate", "local vs global", "supervised vs unsupervised" — these are dimensions. Find the ones specific to your domain.

## Available Tactics

- axis-extraction — systematically extract axes from literature
- matrix-generation — test independence of candidate dimensions

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Candidate dimensions | 5 | 10 | 15 |
| Validated dimensions | 3 | 6 | 10 |
| Sources analyzed | 8 | 20 | 40 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Candidate dimensions| X      | 0       | ⬜     |
| Validated dimensions| X      | 0       | ⬜     |
| Sources analyzed    | X      | 0       | ⬜     |
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
| dimension-page-creation | SOP for creating a dimension page — documents an axis of variation with its values and semantics. |

<!-- END available-tables (generated) -->
