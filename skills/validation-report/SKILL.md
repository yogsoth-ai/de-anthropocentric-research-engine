---
name: validation-report
description: SOP for generating a causal model validation report — summarize coverage,
  confidence, gaps, contradictions.
execution: sop
---

# Validation Report

Generate a summary report of the causal model's current state and validity.

## Tool

`vault_graph_stats` + `vault_lint` + CC file write

## Protocol

1. Run vault_graph_stats for quantitative metrics
2. Run vault_lint for structural issues
3. Count claims by confidence tier (high >0.7, medium 0.4-0.7, low <0.4)
4. List unresolved contradictions
5. Write summary to `topics/causal-model-report.md`

## HARD-GATE

<HARD-GATE>
Report must include: total variables, total edges, confidence distribution, open contradictions, structural issues.
</HARD-GATE>

## Yield

Returns: `{ variables: number, edges: number, high_confidence: number, contradictions: number, report_path: string }`
