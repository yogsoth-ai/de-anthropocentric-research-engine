---
name: multi-judge-aggregation
description: Collect independent rankings from multiple judges, aggregate using social
  choice methods, and identify disagreement hotspots.
execution: tactic
dependencies:
  sops:
  - aggregation-method
  - ballot-collection
  - cycle-detection
---

# Multi-Judge Aggregation

Collect independent ballots from multiple judges or perspectives, aggregate them into a consensus ranking using social choice theory, and surface disagreement patterns for further investigation.

## Stages

1. **Collect** — ballot-collection gathers independent rankings from each judge/perspective
2. **Aggregate** — aggregation-method applies social choice method to produce consensus
3. **Audit** — cycle-detection checks for Condorcet cycles in the aggregated preference matrix

## Available SOPs

| Stage | SOP | Input | Output |
|-------|-----|-------|--------|
| Collect | ballot-collection | candidates[], perspectives[] | ballots[] |
| Aggregate | aggregation-method | ballots[], method | consensus_ranking |
| Audit | cycle-detection | comparison_matrix | cycles[], transitivity_score |

## Execution Guidance

- Ensure judges evaluate independently (no anchoring or information leakage)
- Use ≥3 judges for meaningful aggregation
- Default to Schulze method (satisfies many desirable social choice properties)
- Cross-validate with Borda count as sanity check
- Flag pairs where judge agreement < 60% as disagreement hotspots
- If Condorcet cycles exist, report them explicitly — do not silently resolve

## Minimum Yield

- Consensus ranking + disagreement heatmap
- Consensus ranking with method used and confidence
- Disagreement heatmap: for each pair, what fraction of judges agree
- Condorcet winner identification (or explicit statement of cycle)
- Per-judge deviation from consensus (who disagrees most, on what)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| aggregation-method | Aggregate multiple ranking ballots into a consensus ranking using a specified social choice method. |
| ballot-collection | Gather independent ranking ballots from multiple judges or perspectives for a given candidate set. |
| cycle-detection | Scan a pairwise comparison matrix for preference cycles and compute transitivity metrics. |

<!-- END available-tables (generated) -->
