---
name: stakeholder-objection-simulation
description: Simulate stakeholder objections through role-play and political feasibility analysis to test whether the decision survives real-world opposition.
used-by: steel-manning
---

# Stakeholder Objection Simulation

**Purpose:** Anticipate and simulate the strongest objections that real stakeholders would raise against the convergence decision, testing political feasibility and identifying resistance vectors before implementation.

**When to use:**
- When the decision affects multiple stakeholder groups
- When implementation requires buy-in from parties not in the room
- When political dynamics could block execution
- When prior decisions failed due to unanticipated opposition

## Budget

| Metric | Minimum |
|--------|---------|
| Stakeholder perspectives | >= 3 distinct groups |
| Objection depth | Full argument construction per stakeholder |
| Feasibility assessment | Explicit for each objection |

## State Ledger

```yaml
stakeholders_simulated: []
objections_raised: {}
severity_ratings: {}
mitigation_strategies: {}
political_feasibility: null  # HIGH | MEDIUM | LOW
```

## Available Tactics

| Tactic | When to Deploy |
|--------|---------------|
| multi-perspective-attack | Default — assign and attack from stakeholder perspectives |
| adversarial-debate-protocol | When a specific stakeholder objection needs formal resolution |

## Available SOPs

- perspective-assignment — define stakeholder perspectives and interests
- perspective-attack — simulate attacks from each stakeholder
- steel-manning-synthesis — synthesize across all stakeholder objections
- advocate-construction — build case for stakeholder's preferred alternative
- judge-verdict — assess whether objections are fatal

## Execution Guidance

1. Identify all affected stakeholder groups (minimum 3)
2. Deploy multi-perspective-attack with stakeholder-specific briefs
3. For each HIGH severity objection, assess mitigation feasibility
4. If any objection is both HIGH severity and LOW mitigability, escalate
5. Produce political feasibility rating with evidence

## Output Format

```yaml
strategy: stakeholder-objection-simulation
stakeholders_simulated: <count>
objections:
  - stakeholder: <group>
    objection: <core argument>
    severity: HIGH | MEDIUM | LOW
    mitigable: true | false
    mitigation: <if applicable>
political_feasibility: HIGH | MEDIUM | LOW
blocking_objections: []
recommended_accommodations: []
```
