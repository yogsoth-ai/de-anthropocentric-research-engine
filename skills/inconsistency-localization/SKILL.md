---
name: inconsistency-localization
description: Identify which specific comparison pairs are most responsible for preference cycles and inconsistencies.
execution: subagent
prompt: ./prompt.md
input: comparison_matrix(object), cycles(array)
used-by: pairwise-ranking
---

# Inconsistency Localization

Given detected cycles in a preference graph, identifies which specific pairwise judgments are most likely erroneous. Ranks problematic pairs by their participation in cycles and weakness of evidence.

## Execution

Runs as a subagent. Receives the comparison matrix and detected cycles, returns prioritized list of pairs to re-evaluate.

## Why Subagent

Localization requires cross-referencing cycle membership with edge confidence scores and computing centrality metrics on the inconsistency subgraph. This focused analysis benefits from isolation.

## HARD-GATE

Output MUST contain at least one problematic pair if cycles input is non-empty. Each pair MUST appear in at least one of the input cycles. Pairs MUST be ordered by priority (most problematic first).
