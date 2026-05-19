---
name: method-sensitivity-report
description: Analyze how the choice of MCDA method affects final rankings and identify method-sensitive alternatives.
execution: subagent
prompt: ./prompt.md
input: rankings (object[]), methods (string[])
used-by: multi-criteria-scoring
---

# Method Sensitivity Report

Analyze the impact of MCDA method choice on final rankings, identifying which conclusions are method-independent (robust) and which depend on method selection.

## Execution

Subagent receives ranking results from multiple methods and method descriptions, produces a method sensitivity analysis report.

## Why Subagent

Sensitivity analysis requires deep understanding of theoretical differences and compensation mechanisms across methods; independent execution ensures analysis completeness.

## HARD-GATE

Report must clearly distinguish "method-independent conclusions" from "method-dependent conclusions", and provide specific recommendations for each method-dependent conclusion.
