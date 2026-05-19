---
name: systematic-probing
description: "Strategy: AI-safety systematic probing — enumerate all threat surfaces, generate attack vectors per surface, execute probes, and aggregate findings across the full attack space."
type: strategy
used-by: [red-teaming]
tactics: [structured-attack-campaign, assumption-cascade]
---

# Systematic Probing Strategy

Anthropic-style systematic probing: exhaustive coverage of all threat surfaces with structured attack generation and execution.

## Method

1. **threat-surface-mapping** enumerates all attackable surfaces of the artifact
2. **attack-vector-generation** produces specific attacks per surface
3. Vectors prioritized by expected severity and likelihood
4. **probe-execution** executes each attack, records success/failure/partial
5. Failed probes trigger deeper investigation via follow-up vectors
6. **attack-resilience-scoring** computes coverage and resilience metrics

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
threat-surface-mapping → [enumerate surfaces]
→ [for each surface]:
    attack-vector-generation (generate vectors)
    → [for each vector]:
        probe-execution (execute attack)
        → (if partial success: generate follow-up vectors)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- threat-surface-mapping (surface enumeration)
- attack-vector-generation (vector design)
- probe-execution (attack execution)
- finding-aggregation (result synthesis)
- attack-resilience-scoring (metric computation)
