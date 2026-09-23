---
name: assess-ranking-consistency
description: "Audit pairwise/ranking coherence and identify inconsistent cycles/triads."
---

# assess-ranking-consistency
## Purpose
Audit pairwise and aggregate rankings for incoherent cycles, reversals, and unsupported rank transitions.
## Input contract
```yaml
required: [ranked_items, pairwise_judgments, comparison_criteria]
optional: [weights, tie_policy, prior_consistency_report]
constraints: [judgments identify compared items, direction, confidence, and criterion]
```
## Procedure
1. Reconstruct the directed comparison graph and normalize ties and missing edges.
2. Search triads and longer cycles for violations of declared transitivity or criterion direction.
3. Compare aggregate order with its supporting pairwise judgments and flag reversals or low-support placements.
4. Return inconsistency records, affected items, and the minimum judgments requiring review.
## Output contract
```yaml
produces: [comparison_graph, inconsistency_records, review_set]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```
## Quality gates
- Each inconsistency cites the smallest cycle or reversal and the judgments that create it.
- Ties remain ties unless the input model explicitly supplies a tie-break rule.
## Failure and counterexamples
Do not call a sparse graph inconsistent merely because it lacks a comparison. Distinguish missing edges from contradictory edges.
## Provenance map
- resolved: consistency-check
- resolved: rank-comparison
