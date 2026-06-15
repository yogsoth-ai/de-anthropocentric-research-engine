---
name: evidence-weighing
description: Tactic for assessing the strength and relevance of evidence for causal
  claims — distinguishes correlation from causation.
execution: tactic
dependencies:
  sops:
  - confidence-scoring
  - contradiction-flagging
  - evidence-linking
---

# Evidence Weighing

Assess the strength of evidence for causal claims. Not all evidence is equal — RCTs > observational studies > expert opinion > anecdote.

## Available SOPs

- evidence-linking — connect evidence to claims
- confidence-scoring — assign calibrated confidence
- contradiction-flagging — identify conflicting evidence

## Guiding Principles

- **Hierarchy of evidence.** Interventional > observational > theoretical > anecdotal.
- **Effect size matters.** A statistically significant but tiny effect is weak evidence for practical causation.
- **Replication is king.** Single studies are suggestive; replicated findings are convincing.
- **Confounders weaken.** Evidence from studies with uncontrolled confounders gets lower weight.
- **Mechanism strengthens.** Evidence backed by a plausible mechanism gets higher weight.

## Minimum Yield

<HARD-GATE>
≥2 evidence assessments with explicit strength ratings per invocation.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| confidence-scoring | SOP for assigning calibrated confidence scores to causal claims based on evidence quality and quantity. |
| contradiction-flagging | SOP for flagging contradictions in the causal model — identify conflicting evidence or mechanism claims. |
| evidence-linking | SOP for linking evidence pages to causal claims — creates supported_by or contradicts edges. |

<!-- END available-tables (generated) -->
