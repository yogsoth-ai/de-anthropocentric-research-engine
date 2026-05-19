---
name: critic-defender-judge
description: "Strategy: Classic triangular debate — Critic attacks, Defender responds, Judge adjudicates. Based on Irving AI Safety via Debate with Toulmin argumentation structure."
type: strategy
used-by: [multiagent-debate]
tactics: [dialectical-escalation, evidence-tournament]
---

# Critic-Defender-Judge Strategy

Classic adversarial triangle: one agent attacks, one defends, one judges.

## Method

1. **debate-architect** designs attack vectors based on artifact type
2. **debate-critic** generates structured attacks using Toulmin model
3. **debate-defender** responds with counter-evidence and rebuttals
4. **debate-judge** evaluates exchange quality and produces round verdict
5. Repeat with escalating pressure (dialectical-escalation tactic)

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [for each round]:
  debate-critic → debate-defender → debate-judge
  → confidence-calibration → (escalate or terminate)
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (structure design)
- debate-critic (attack generation)
- debate-defender (defense generation)
- debate-judge (round adjudication)
- confidence-calibration (escalation decision)
- evidence-scout (when evidence-tournament tactic active)
