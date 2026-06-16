---
name: gap-prioritization
description: Strategy for ranking unexplored combinations by novelty, feasibility,
  and potential impact.
execution: strategy
dependencies:
  tactics:
  - axis-extraction
  - matrix-generation
  sops:
  - knowledge-structuring-novelty-scoring
  - matrix-export
  - question-generation
---

# Gap Prioritization

Rank the empty cells (unexplored combinations) by their potential value. Not all gaps are worth filling — prioritize by novelty, feasibility, and expected impact.

## Guiding Focus

An empty cell is only an opportunity if it's feasible and valuable. Rank gaps by: (1) how novel the combination is, (2) how feasible it is to realize, (3) what impact it would have if successful.

## Available Tactics

- matrix-generation — refine the matrix with priority annotations
- axis-extraction — verify gap is truly unexplored (not just differently named)

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Gaps scored | 3 | 8 | 15 |
| Questions generated | 3 | 8 | 15 |
| Top priorities identified | 2 | 4 | 8 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Gaps scored         | X      | 0       | ⬜     |
| Questions generated | X      | 0       | ⬜     |
| Top priorities      | X      | 0       | ⬜     |
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
| knowledge-structuring-novelty-scoring | SOP for scoring empty cells by novelty potential — how surprising and valuable would this combination be? |
| matrix-export | SOP for exporting the dimensional matrix as a readable document or structured data. |
| question-generation | SOP for generating research questions from promising gaps in the design space. |

<!-- END available-tables (generated) -->
