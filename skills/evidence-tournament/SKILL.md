---
name: evidence-tournament
description: 'Tactic: Evidence gathering, cross-examination, and quality judgment.
  External evidence is collected, presented, challenged, and scored for relevance
  and reliability.'
type: tactic
strategies:
- courtroom-structured
- critic-defender-judge
dependencies:
  sops:
  - cross-examination
  - debate-critic
  - debate-defender
  - debate-judge
  - evidence-scout
---

# Evidence Tournament Tactic

Structured evidence competition — gather, present, cross-examine, and judge evidence quality.

## Orchestration

1. **evidence-scout** searches for evidence supporting the artifact's claims
2. **evidence-scout** searches for evidence opposing the artifact's claims
3. **debate-critic** presents opposing evidence as structured arguments
4. **debate-defender** presents supporting evidence as counter-arguments
5. **cross-examination** probes both evidence sets:
   - Source reliability assessment
   - Relevance to specific claims
   - Recency and applicability
   - Potential confounds or alternative interpretations
6. **debate-judge** scores each piece of evidence and produces tournament bracket result

## Evidence Quality Criteria

- **Relevance**: Direct bearing on the claim (0.0–1.0)
- **Reliability**: Source credibility and methodology (0.0–1.0)
- **Recency**: Temporal applicability (0.0–1.0)
- **Specificity**: How precisely it addresses the claim (0.0–1.0)

## Subagents Dispatched

- evidence-scout × 2 (pro and con evidence gathering)
- debate-critic (opposing evidence presentation)
- debate-defender (supporting evidence presentation)
- cross-examination (evidence probing)
- debate-judge (evidence scoring and verdict)

## Termination Conditions

- All claims have been evidenced and cross-examined
- Evidence search budget exhausted (2/5/10 searches)
- No further relevant evidence discoverable
- Judge has scored all evidence pairs

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| cross-examination | Probes defender responses for inconsistencies, logical gaps, and unsupported claims. Acts as follow-up interrogation after initial defense. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |

<!-- END available-tables (generated) -->
