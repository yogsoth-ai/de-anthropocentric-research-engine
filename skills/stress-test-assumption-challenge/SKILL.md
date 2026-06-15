---
name: assumption-challenge
description: 'Strategy: Military-grade assumption testing — Key Assumptions Check,
  Devil''s Advocacy, Team A/B analysis to expose hidden dependencies and unexamined
  beliefs.'
type: strategy
tactics:
- assumption-cascade
- structured-attack-campaign
dependencies:
  tactics:
  - assumption-cascade
  - structured-attack-campaign
  sops:
  - assumption-cascade-tracer
  - devils-advocacy
  - finding-aggregation
  - key-assumptions-check
  - probe-execution
---

# Assumption Challenge Strategy

Military ACT (Analytic Confidence Testing): systematically surface and attack assumptions underlying the artifact.

## Method

1. **key-assumptions-check** enumerates all assumptions (explicit and implicit)
2. Assumptions sorted by criticality and evidence strength
3. **devils-advocacy** constructs strongest counter-argument for each critical assumption
4. Team A defends assumptions, Team B attacks — structured exchange
5. **assumption-cascade-tracer** maps dependency chains from root assumptions
6. Failed assumptions trigger cascade analysis to identify downstream impacts

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
key-assumptions-check → [enumerate and rank assumptions]
→ [for each critical assumption]:
    devils-advocacy (construct counter-argument)
    → probe-execution (test assumption)
    → assumption-cascade-tracer (map dependencies)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- key-assumptions-check (enumeration and ranking)
- devils-advocacy (counter-argument construction)
- probe-execution (assumption testing)
- assumption-cascade-tracer (dependency mapping)
- finding-aggregation (result synthesis)
