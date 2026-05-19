---
name: adversarial-escalation
description: "Strategy: Progressive pressure escalation — starts with surface-level challenges and escalates to fundamental assumption attacks based on defender confidence decay."
type: strategy
used-by: [multiagent-debate]
tactics: [dialectical-escalation]
---

# Adversarial Escalation Strategy

Progressive pressure: escalate attack sophistication based on defender performance.

## Method

1. **debate-architect** designs escalation ladder (surface → structural → foundational)
2. Level 1: **debate-critic** probes surface claims and evidence quality
3. **confidence-calibration** measures defender resilience
4. Level 2: **debate-critic** attacks structural coherence and logical dependencies
5. Level 3: **debate-critic** challenges foundational assumptions and paradigm fit
6. Each level only reached if defender survives previous level

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [design escalation ladder]
→ [for each level]:
    debate-critic (level-appropriate attack)
    → debate-defender → debate-judge
    → confidence-calibration
    → (escalate if survived, terminate if collapsed)
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (escalation design)
- debate-critic (multi-level attacks)
- debate-defender (responses)
- debate-judge (level adjudication)
- confidence-calibration (escalation trigger)
