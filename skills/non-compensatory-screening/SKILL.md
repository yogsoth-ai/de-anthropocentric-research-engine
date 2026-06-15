---
name: non-compensatory-screening
description: Eliminate non-qualifying candidates using conjunctive rules, dominance
  filtering, lexicographic ordering, or veto thresholds.
dependencies:
  tactics:
  - screening-then-scoring
  sops:
  - conjunctive-filter
  - criterion-definition
  - dominance-check
  - threshold-setting
---

# Non-Compensatory Screening

**Purpose:** Eliminate non-qualifying alternatives using non-compensatory rules — failure on any critical criterion results in elimination, with no compensation from high scores on other criteria.

**When to use:**
- Hard constraints or safety baselines exist
- Go/no-go decisions are needed
- Need to reduce candidate set before fine-grained scoring
- Certain criteria have veto power

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| criterion-definition | 3-5 screening criteria | 2-6 |
| threshold-setting | 1 threshold set | 1 |
| conjunctive-filter | 1 pass/fail list | 1 |
| dominance-check | 1 dominance report | 1 |

## State Ledger

```yaml
strategy: non-compensatory-screening
status: pending
criteria_defined: false
thresholds_set: false
filtered: false
dominance_checked: false
survivors: []
eliminated: []
```

## Available Tactics

- **screening-then-scoring** — Score survivors after screening

## Available SOPs

### Import
- criterion-definition
- threshold-setting
- conjunctive-filter
- dominance-check

### Subagent
- (none — screening is self-contained)

## Execution Guidance

1. Identify hard constraint criteria (safety, compliance, budget, etc.)
2. Invoke threshold-setting to define minimum thresholds for each criterion
3. Invoke conjunctive-filter to execute elimination
4. Optional: invoke dominance-check for further refinement
5. Output survivor list for subsequent strategies

## Output Format

```markdown
## Screening Results

**Screening Rule:** Conjunctive rule (all criteria must be met)
**Initial Candidates:** [N]
**Survivors:** [M]
**Eliminated:** [N-M]

### Elimination Details
| Alternative | Failed Criterion | Actual Value | Threshold |
|-------------|-----------------|--------------|-----------|

### Surviving Alternatives
[List, available for subsequent fine-grained scoring]
```
