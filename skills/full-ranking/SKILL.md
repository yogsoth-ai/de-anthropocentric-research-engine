---
name: full-ranking
description: Produce a complete ordering of all candidates using PROMETHEE I/II, ELECTRE
  III, or MAVT methods.
dependencies:
  tactics:
  - convergence-scoring-matrix-construction
  - multi-method-triangulation
---

# Full Ranking

**Purpose:** Produce a complete priority ranking of all candidate alternatives, supporting PROMETHEE I/II, ELECTRE III, MAVT, and other ranking methods.

**When to use:**
- User needs a complete ranking of all alternatives (league table)
- Need to distinguish partial order from total order relationships
- Large number of candidates requiring systematic ordering

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| criterion-definition | 5-8 criteria | 4-9 |
| weight-elicitation-sop | 1 weight vector | 1 |
| alternative-scoring | 1 score matrix | 1 |
| normalization | 1 normalized matrix | 1 |
| rank-comparison | 1 agreement matrix | 1 |
| scoring-synthesis | 1 full ranking | 1 |

## State Ledger

```yaml
strategy: full-ranking
status: pending
criteria_defined: false
weights_computed: false
scores_computed: false
ranking_produced: false
methods_compared: false
result: null
```

## Available Tactics

- **scoring-matrix-construction** — Build scoring foundation
- **multi-method-triangulation** — Multi-method comparison to ensure ranking robustness

## Available SOPs

### Import (from tactics)
- criterion-definition
- weight-elicitation-sop
- alternative-scoring
- normalization
- rank-comparison

### Subagent
- scoring-synthesis

## Execution Guidance

1. Invoke scoring-matrix-construction to build the score matrix
2. Select >=2 ranking methods (recommended: PROMETHEE II + MAVT)
3. Invoke multi-method-triangulation to compare ranking consistency
4. Pay attention to incomparable pairs in partial orders (specific to ELECTRE III)
5. Synthesize and produce the final ranking

## Output Format

```markdown
## Complete Ranking Results

**Method:** [PROMETHEE II / ELECTRE III / MAVT]

### Ranking Table
| Rank | Alternative | Net Flow/Utility Value | Notes |
|------|-------------|------------------------|-------|

### Method Consistency
| Method Pair | Kendall tau | Divergent Alternatives |
|-------------|-------------|------------------------|

### Robustness Notes
[Sensitivity of ranking to weight changes]
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| convergence-scoring-matrix-construction | Build a complete scoring matrix through criterion definition, weighting, scoring, normalization, and sensitivity testing. |
| multi-method-triangulation | Apply 2-3 MCDA methods to the same candidates, compare rankings, and identify method-sensitive options. |

<!-- END available-tables (generated) -->
