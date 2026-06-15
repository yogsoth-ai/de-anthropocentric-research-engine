---
name: evidence-linking-arg
description: Strategy for linking evidence to claims — find supporting/contradicting
  evidence, create typed edges, assess evidence quality, identify gaps in evidential
  coverage.
execution: strategy
dependencies:
  tactics:
  - strength-assessment
  sops:
  - evidence-attachment
  - strength-scoring
---

# Evidence Linking (Argument)

Link evidence to claims with typed relationships. Searches for supporting and contradicting evidence, creates structured edges, assesses evidence quality, and identifies claims lacking sufficient evidential support.

## Budget Slice

| Metric | Small | Medium | Large |
|--------|-------|--------|-------|
| Evidence links created | 15 | 40 | 80 |
| Claims with evidence | 8 | 20 | 40 |
| Contradictions found | 2 | 6 | 12 |

## State Ledger

<HARD-GATE>
Print before every iteration:

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Evidence links created | — | — | — |
| Claims with evidence | — | — | — |
| Contradictions found | — | — | — |
</HARD-GATE>

## Budget Gate

Cannot exit until 80% of budget targets met.

## Adversarial Completeness Probe

After budget gate passes, self-check:
- Are there claims with only supporting evidence (confirmation bias)?
- Are there high-confidence claims with weak evidence?
- Is evidence diversity sufficient (multiple independent sources)?

Max 2 extra iterations if gaps found.

## Tactics Available

- **strength-assessment** — evaluate the strength of evidence-claim relationships

## SOPs Available

- **evidence-attachment** — attach evidence to a claim with typed edge
- **strength-scoring** — assign strength scores to claims based on evidence

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| strength-assessment | Tactic for assessing argument strength — evaluate evidence quality, count independent sources, check for defeaters, assign calibrated confidence scores. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| evidence-attachment | SOP for attaching evidence to a claim — create typed edge (supported_by, contradicts, qualifies) with evidence quality metadata. |
| strength-scoring | SOP for assigning calibrated strength scores to claims — evaluate evidence weight, count independent sources, check defeaters, produce scored assessment. |

<!-- END available-tables (generated) -->
