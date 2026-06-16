---
name: courtroom-structured
description: 'Strategy: Legal adversarial structure — prosecution presents case, defense
  responds, evidence is cross-examined, judge delivers verdict. Emphasizes evidence
  quality and procedural rigor.'
type: strategy
tactics:
- evidence-tournament
- dialectical-escalation
dependencies:
  tactics:
  - evidence-tournament
  - stress-test-dialectical-escalation
  sops:
  - cross-examination
  - debate-architect
  - debate-critic
  - debate-defender
  - debate-judge
  - evidence-scout
---

# Courtroom-Structured Strategy

Legal adversarial model with formal evidence presentation and cross-examination.

## Method

1. **debate-architect** structures the case — defines charges (weaknesses to probe)
2. **debate-critic** (prosecution) presents opening arguments with evidence
3. **evidence-scout** gathers supporting/opposing evidence from external sources
4. **debate-defender** presents counter-case
5. **cross-examination** probes both sides for inconsistencies
6. **debate-judge** delivers structured verdict per charge

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Debate rounds | 4 | 8 | 12 |
| Participating agents | 3 | 5 | 8 |
| Coverage dimensions | 3 | 5 | 7 |
| External evidence searches | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [define charges]
→ [for each charge]:
    debate-critic (prosecution) → evidence-scout
    → debate-defender → evidence-scout
    → cross-examination → debate-judge
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (case structure)
- debate-critic (prosecution)
- debate-defender (defense counsel)
- evidence-scout (evidence gathering)
- cross-examination (probing)
- debate-judge (verdict per charge)

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
| cross-examination | Probes defender responses for inconsistencies, logical gaps, and unsupported claims. Acts as follow-up interrogation after initial defense. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |

<!-- END available-tables (generated) -->
