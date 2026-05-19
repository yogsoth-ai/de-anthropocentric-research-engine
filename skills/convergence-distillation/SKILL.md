---
name: convergence-distillation
description: Iterative convergence to a single answer through Classic Delphi, Modified Delphi, or Nominal Group Technique rounds.
used-by: structured-consensus
---

# Convergence Distillation

**Purpose:** Drive multiple independent perspectives toward a single shared answer through iterative anonymous feedback rounds. Each round narrows the distribution of judgments until consensus threshold is met or stability is reached.

**When to use:**
- Need a single definitive answer from diverse experts
- Establishing guidelines, thresholds, or standards
- Quantitative estimates requiring group calibration
- Situations where social pressure would bias face-to-face discussion

## Budget

| Parameter | Constraint |
|-----------|-----------|
| Rounds | 2–4 (stop at consensus or stability) |
| Perspectives | ≥4 independent |
| Consensus threshold | ≥70% agreement or IQR ≤ 1 |

## State Ledger

| Key | Type | Description |
|-----|------|-------------|
| question | string | The focal question being converged |
| perspectives | array | List of perspective descriptions |
| rounds | array | History of all round results |
| current_round | integer | Current round number |
| consensus_score | float | Latest consensus measurement |
| stability | boolean | Whether scores stopped changing |

## Available Tactics

- **iterative-convergence-round** — Core loop: collect → feedback → revise → measure → decide

## Available SOPs

- judgment-collection
- feedback-distribution
- consensus-measurement
- round-decision
- consensus-synthesis

## Execution Guidance

1. Frame the question clearly with response format (Likert, numeric, ranking)
2. Run iterative-convergence-round until round-decision returns "stop"
3. If max rounds reached without consensus, document dissent
4. Run consensus-synthesis to produce final report

## Output Format

```yaml
consensus_reached: true/false
final_answer: <aggregated result>
consensus_score: <float>
rounds_completed: <int>
dissent_record: <items that did not converge>
```
