---
name: aggregation-method
description: Aggregate multiple ranking ballots into a consensus ranking using a specified social choice method.
execution: subagent
prompt: ./prompt.md
input: ballots(array), method(string)
used-by: pairwise-ranking
---

# Aggregation Method

Applies a social choice aggregation method to a set of ranking ballots to produce a consensus ranking. Supports Schulze, Borda, Kemeny-Young, Copeland, and Condorcet methods.

## Execution

Runs as a subagent. Receives ballots and method specification, returns the aggregated consensus ranking.

## Why Subagent

Aggregation algorithms (especially Kemeny-Young) involve combinatorial computation and method-specific logic. Isolating this ensures correct algorithm application and clear separation from collection and interpretation.

## HARD-GATE

Output MUST produce a complete ranking of all candidates. The method field MUST match the input method. If a Condorcet winner exists, it MUST be ranked first (for Condorcet-consistent methods).
