---
name: best-option-selection
description: Select the single best candidate from a set using WSM, TOPSIS, AHP, MAUT,
  or VIKOR methods.
dependencies:
  tactics:
  - convergence-scoring-matrix-construction
---

# Best-Option Selection

**Purpose:** Select the single best-performing alternative from a candidate set, supporting WSM, TOPSIS, AHP, MAUT, VIKOR, and other methods.

**When to use:**
- User needs to select "the best one" from multiple candidates
- Decision scenario allows compensatory trade-offs (high scores offset low scores)
- Moderate number of candidates (3-15)

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| criterion-definition | 5-8 criteria | 4-9 |
| weight-elicitation-sop | 1 weight vector | 1 |
| alternative-scoring | 1 score matrix | 1 |
| normalization | 1 normalized matrix | 1 |
| scoring-synthesis | 1 recommendation | 1 |

## State Ledger

```yaml
strategy: best-option-selection
status: pending
criteria_defined: false
weights_computed: false
scores_computed: false
normalized: false
synthesized: false
selected_method: null
result: null
```

## Available Tactics

- **scoring-matrix-construction** — Standard workflow: define criteria → assign weights → score → aggregate → sensitivity

## Available SOPs

### Import (from scoring-matrix-construction)
- criterion-definition
- weight-elicitation-sop
- alternative-scoring
- normalization

### Subagent
- scoring-synthesis

## Execution Guidance

1. Invoke scoring-matrix-construction tactic to build the score matrix
2. Select aggregation method based on problem characteristics (WSM for simple scenarios, TOPSIS when ideal solution reference is needed, VIKOR when compromise solution is needed)
3. Invoke scoring-synthesis to produce final recommendation
4. If user questions the result, switch methods, recompute, and compare

## Output Format

```markdown
## Best Option Recommendation

**Recommended:** [Alternative name]
**Overall Score:** [Score value]
**Method Used:** [WSM/TOPSIS/AHP/MAUT/VIKOR]

### Score Ranking
| Rank | Alternative | Overall Score | Key Strengths |
|------|-------------|---------------|---------------|

### Sensitivity Notes
[Impact of weight changes on the result]
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| convergence-scoring-matrix-construction | Build a complete scoring matrix through criterion definition, weighting, scoring, normalization, and sensitivity testing. |

<!-- END available-tables (generated) -->
