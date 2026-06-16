---
name: critic-defender-judge
description: 'Strategy: Classic triangular debate — Critic attacks, Defender responds,
  Judge adjudicates. Based on Irving AI Safety via Debate with Toulmin argumentation
  structure.'
type: strategy
tactics:
- dialectical-escalation
- evidence-tournament
dependencies:
  tactics:
  - evidence-tournament
  - stress-test-dialectical-escalation
  sops:
  - confidence-calibration
  - debate-architect
  - debate-critic
  - debate-defender
  - debate-judge
  - evidence-scout
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| evidence-tournament | Tactic: Evidence gathering, cross-examination, and quality judgment. External evidence is collected, presented, challenged, and scored for relevance and reliability. |
| stress-test-dialectical-escalation | Tactic: Progressive debate escalation based on confidence thresholds. Each round increases attack sophistication until defender collapses or proves resilient. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |

<!-- END available-tables (generated) -->
