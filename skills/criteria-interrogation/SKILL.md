---
name: criteria-interrogation
description: Challenge the evaluation criteria themselves using Assumption-based Planning,
  Critical Systems Heuristics, and Boundary Critique to ensure the framework is sound.
dependencies:
  tactics:
  - assumption-excavation
  - multi-perspective-attack
---

# Criteria Interrogation

**Purpose:** Question whether the evaluation framework used during convergence was itself valid — exposing hidden biases in criteria selection, weighting, and boundary definitions that may have predetermined the outcome.

**When to use:**
- When criteria were inherited rather than deliberately designed
- When different criteria would produce different winners
- When stakeholders disagree about what matters
- When the evaluation framework has not been challenged

## Budget

| Metric | Minimum |
|--------|---------|
| Criteria challenged | All criteria used in convergence |
| Alternative framings | >= 2 alternative criteria sets |
| Boundary questions | >= 5 (who benefits, who is excluded) |

## State Ledger

```yaml
criteria_under_review: []
challenges_raised: {}
alternative_framings: []
sensitivity_to_criteria_change: {}
verdict: null  # CRITERIA_SOUND | CRITERIA_BIASED | REWEIGHT
```

## Available Tactics

| Tactic | When to Deploy |
|--------|---------------|
| assumption-excavation | Default — treat criteria as assumptions to challenge |
| multi-perspective-attack | When criteria privilege certain stakeholders |

## Available SOPs

- assumption-extraction — surface assumptions embedded in criteria
- assumption-challenge — challenge each criterion's validity
- conclusion-sensitivity — test if outcome changes with different criteria
- perspective-assignment — assign stakeholder perspectives to criteria
- perspective-attack — attack criteria from each perspective

## Execution Guidance

1. List all criteria used in convergence with their weights
2. For each criterion, apply assumption-extraction (why this criterion?)
3. Challenge each criterion's inclusion, exclusion, and weight
4. Test conclusion sensitivity: would different weights change the winner?
5. If winner changes under reasonable alternative weighting, verdict is REWEIGHT

## Output Format

```yaml
strategy: criteria-interrogation
criteria_reviewed: <count>
challenges:
  - criterion: <name>
    challenge: <argument>
    severity: HIGH | MEDIUM | LOW
    alternative: <proposed change>
sensitivity_result: ROBUST | FRAGILE
verdict: CRITERIA_SOUND | CRITERIA_BIASED | REWEIGHT
recommended_changes: []
```
