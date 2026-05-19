---
name: weight-elicitation
description: Determine criteria weights using AHP, Swing, BWM, MACBETH, or Simos methods.
used-by: multi-criteria-scoring
---

# Weight Elicitation

**Purpose:** Determine relative weights for evaluation criteria through structured methods, supporting AHP, Swing, BWM, MACBETH, Simos, and other weighting methods.

**When to use:**
- Need to determine criteria importance ranking and quantified weights
- Multiple stakeholders disagree on weights
- Need to compare result differences across weighting methods

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| criterion-definition | 5-8 criteria | 4-9 |
| weight-elicitation-sop | ≥2 methods | 2-3 |
| rank-comparison | 1 comparison | 1 |

## State Ledger

```yaml
strategy: weight-elicitation
status: pending
criteria_defined: false
method_1: null
method_2: null
weights_1: []
weights_2: []
compared: false
final_weights: []
```

## Available Tactics

- **multi-method-triangulation** — Multi-method comparison to ensure weight robustness

## Available SOPs

### Import
- criterion-definition
- weight-elicitation-sop
- rank-comparison

### Subagent
- method-sensitivity-report

## Execution Guidance

1. Invoke criterion-definition to confirm criteria to be weighted
2. Select >=2 weighting methods (recommended: AHP + BWM or Swing + Simos)
3. Invoke weight-elicitation-sop separately for each method to compute weights
4. Invoke rank-comparison to compare weight ranking consistency
5. If significant differences exist, analyze causes and select the most suitable method for the scenario
6. Output final weight vector

## Output Format

```markdown
## Weight Determination Results

### Weight Comparison
| Criterion | AHP Weight | BWM Weight | Average | Difference |
|-----------|------------|------------|---------|------------|

### Consistency Check
- AHP CR: [value] (< 0.1 ✓)
- BWM ξ*: [value]

### Final Weights
| Criterion | Weight | Rank |
|-----------|--------|------|

### Method Selection Rationale
[Why the chosen method's weights are used as the final result]
```
