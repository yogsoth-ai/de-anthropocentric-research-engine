---
name: rank-comparison
description: Compare multiple ranking results to assess agreement and identify divergent items.
execution: subagent
prompt: ./prompt.md
input: rankings (object[])
used-by: multi-criteria-scoring
---

# Rank Comparison

Compare ranking results produced by multiple methods or weight sets, compute consistency metrics, and identify alternatives with significant ranking differences.

## Execution

Subagent receives multiple ranking results, computes rank correlation metrics, and outputs a consistency matrix and difference analysis.

## Why Subagent

Rank comparison involves statistical computation (Kendall tau, Spearman rho) and difference attribution analysis; independent execution ensures computational accuracy.

## HARD-GATE

Must report at least one rank correlation metric (Kendall tau or Spearman rho), and must list all alternatives with ranking differences >= 2 positions.
