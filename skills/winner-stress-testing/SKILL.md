---
name: winner-stress-testing
description: Stress-test the winning candidate using Pre-mortem, Red Teaming, and Failure Mode Analysis to expose hidden weaknesses before commitment.
used-by: steel-manning
---

# Winner Stress-Testing

**Purpose:** Subject the convergence winner to rigorous adversarial pressure, identifying failure modes, hidden assumptions, and boundary conditions that could cause the decision to fail in practice.

**When to use:**
- After a winner has been selected but before final commitment
- When the decision carries high stakes or irreversibility
- When the winner was selected by narrow margin
- When implementation risk is uncertain

## Budget

| Metric | Minimum |
|--------|---------|
| Attack angles | >= 3 distinct failure vectors |
| Assumptions challenged | >= 5 |
| Pre-mortem scenarios | >= 3 |
| Severity threshold | All HIGH severity findings must be addressed |

## State Ledger

```yaml
winner: <candidate>
attack_vectors_applied: []
assumptions_found: []
failure_modes: []
severity_ratings: {}
verdict: null  # ACCEPT | REJECT | REVISE
conditions_for_acceptance: []
```

## Available Tactics

| Tactic | When to Deploy |
|--------|---------------|
| assumption-excavation | Default — extract and challenge winner's assumptions |
| adversarial-debate-protocol | When specific weaknesses need formal debate |
| multi-perspective-attack | When winner affects multiple stakeholder groups |

## Available SOPs

- assumption-extraction — surface hidden assumptions in the winner
- assumption-challenge — attack each assumption
- conclusion-sensitivity — map which assumptions are load-bearing
- critic-attack — direct attack on winner's case
- judge-verdict — render accept/reject/revise

## Execution Guidance

1. Deploy assumption-excavation to surface and challenge assumptions
2. Identify critical assumptions from sensitivity map
3. For each critical assumption, assess mitigation feasibility
4. If >= 1 unmitigable critical assumption, verdict is REVISE or REJECT
5. Record all findings in Challenge Ledger

## Output Format

```yaml
strategy: winner-stress-testing
winner: <candidate>
assumptions_found: <count>
critical_assumptions: <count>
failure_modes:
  - mode: <description>
    severity: HIGH | MEDIUM | LOW
    mitigable: true | false
verdict: ACCEPT | REJECT | REVISE
conditions: []
recommended_modifications: []
```
