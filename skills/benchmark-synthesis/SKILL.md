---
name: benchmark-synthesis
description: Produce final structured audit report
execution: subagent
prompt: ./prompt.md
input: all_analysis_results
used-by: benchmark-archaeology
---

# Benchmark Synthesis SOP

Synthesize all analysis results from a benchmark archaeology campaign into a final structured report with cross-cutting findings, prioritized recommendations, and actionable conclusions.

## Input

- **all_analysis_results**: Combined outputs from all prior analysis SOPs and tactics (audit scores, saturation data, validity assessments, coverage maps, protocol forensics)

## Procedure

1. Aggregate findings across all analysis dimensions
2. Identify cross-cutting themes and systemic issues
3. Prioritize findings by impact and actionability
4. Produce executive summary and detailed report
5. Generate specific recommendations for benchmark users and creators

## Output

Final synthesis report suitable for publication or decision-making.
