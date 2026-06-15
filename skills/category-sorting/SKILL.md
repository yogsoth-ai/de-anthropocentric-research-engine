---
name: category-sorting
description: Classify candidates into predefined categories using ELECTRE-Tri, FlowSort,
  AHPSort, or DRSA methods.
dependencies:
  tactics:
  - convergence-scoring-matrix-construction
  - screening-then-scoring
---

# Category Sorting

**Purpose:** Classify candidate alternatives into predefined categories (e.g., A/B/C grades, compliant/non-compliant), supporting ELECTRE-Tri, FlowSort, AHPSort, DRSA, and other classification methods.

**When to use:**
- User needs to classify alternatives rather than rank them
- Predefined category boundaries exist (e.g., pass/fail, excellent/good/poor)
- Need to independently determine category membership for each alternative

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| criterion-definition | 5-8 criteria | 4-9 |
| weight-elicitation-sop | 1 weight vector | 1 |
| threshold-setting | 1 threshold set | 1 |
| alternative-scoring | 1 score matrix | 1 |
| scoring-synthesis | 1 classification | 1 |

## State Ledger

```yaml
strategy: category-sorting
status: pending
categories_defined: false
criteria_defined: false
weights_computed: false
thresholds_set: false
scores_computed: false
classified: false
result: null
```

## Available Tactics

- **scoring-matrix-construction** — Build scoring foundation
- **screening-then-scoring** — Hybrid workflow: screen first, then classify

## Available SOPs

### Import (from tactics)
- criterion-definition
- weight-elicitation-sop
- alternative-scoring
- threshold-setting

### Subagent
- scoring-synthesis

## Execution Guidance

1. Define category definitions and boundary conditions
2. Invoke criterion-definition to determine classification criteria
3. Invoke threshold-setting to set category boundaries
4. Score each alternative independently and determine category membership
5. Handle borderline cases (pessimistic vs optimistic assignment)

## Output Format

```markdown
## Classification Results

**Method:** [ELECTRE-Tri / FlowSort / AHPSort / DRSA]
**Category Definitions:** [A=Excellent, B=Good, C=Needs Improvement, D=Unqualified]

### Classification Table
| Alternative | Category | Confidence | Boundary Distance |
|-------------|----------|------------|-------------------|

### Borderline Cases
[List alternatives near category boundaries and their sensitivity]
```
