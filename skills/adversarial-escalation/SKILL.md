---
name: adversarial-escalation
description: 'Strategy: Progressive pressure escalation — starts with surface-level
  challenges and escalates to fundamental assumption attacks based on defender confidence
  decay.'
type: strategy
tactics:
- dialectical-escalation
dependencies:
  tactics:
  - stress-test-dialectical-escalation
  sops:
  - confidence-calibration
  - debate-architect
  - debate-critic
  - debate-defender
  - debate-judge
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| stress-test-dialectical-escalation | Tactic: Progressive debate escalation based on confidence thresholds. Each round increases attack sophistication until defender collapses or proves resilient. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |

<!-- END available-tables (generated) -->
