---
name: alternative-analysis
description: 'Strategy: What-If Analysis, Alternative Futures, and Four Ways of Seeing
  — generate competing explanations and scenarios to challenge the dominant narrative.'
type: strategy
tactics:
- structured-attack-campaign
- adversarial-roleplay
dependencies:
  tactics:
  - adversarial-roleplay
  - structured-attack-campaign
  sops:
  - alternative-futures
  - attack-vector-generation
  - finding-aggregation
  - probe-execution
  - threat-surface-mapping
---

# Alternative Analysis Strategy

CIA SAT alternative analysis: generate multiple competing interpretations to prevent anchoring on a single explanation.

## Method

1. **alternative-futures** builds 2-4 divergent scenarios from the same evidence base
2. What-If Analysis: systematically vary key variables to explore outcome sensitivity
3. Four Ways of Seeing: examine artifact through lenses of opportunity, risk, structure, and agency
4. **probe-execution** tests each alternative against available evidence
5. Diagnostic indicators identified that would discriminate between alternatives
6. **finding-aggregation** compares explanatory power across alternatives

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Attack vectors | 5 | 12 | 20 |
| Probing rounds | 3 | 6 | 10 |
| Personas | 2 | 4 | 6 |
| Assumption checks | 5 | 10 | 20 |

## Orchestration

```
threat-surface-mapping → [identify variable dimensions]
→ alternative-futures (generate 2-4 scenarios)
→ [for each alternative]:
    attack-vector-generation (find discriminating tests)
    → probe-execution (test alternative)
→ finding-aggregation → attack-resilience-scoring
```

## Subagents

- threat-surface-mapping (dimension identification)
- alternative-futures (scenario generation)
- attack-vector-generation (discriminating test design)
- probe-execution (alternative testing)
- finding-aggregation (comparative synthesis)
