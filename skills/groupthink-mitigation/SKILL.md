---
name: groupthink-mitigation
description: "Strategy: 10th Man Rule and Liberating Structures — institutionalized dissent to prevent premature consensus and expose suppressed objections."
type: strategy
used-by: [red-teaming]
tactics: [adversarial-roleplay, assumption-cascade]
---

# Groupthink Mitigation Strategy

Prevent premature consensus by mandating structured dissent. Based on Israeli intelligence 10th Man doctrine and Lipmanowicz Liberating Structures.

## Method

1. **persona-construction** builds mandatory dissenter (10th Man) regardless of consensus
2. 10th Man must argue against the dominant conclusion even if personally agreeing
3. Liberating Structures applied: 1-2-4-All, TRIZ (worst possible outcome), Wicked Questions
4. **devils-advocacy** generates strongest case against current consensus
5. **probe-execution** tests dissenting arguments against evidence
6. Findings recorded even if dissent ultimately fails — the process matters

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
persona-construction → [build 10th Man dissenter]
→ devils-advocacy (construct dissenting case)
→ [for each dissenting claim]:
    probe-execution (test claim)
    → key-assumptions-check (verify consensus assumptions)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- persona-construction (dissenter role creation)
- devils-advocacy (dissent argument generation)
- probe-execution (dissent testing)
- key-assumptions-check (consensus assumption audit)
- finding-aggregation (dissent documentation)
