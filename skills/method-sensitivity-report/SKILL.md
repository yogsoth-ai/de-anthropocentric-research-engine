---
name: method-sensitivity-report
description: Analyze how the choice of MCDA method affects final rankings and identify
  method-sensitive alternatives.
execution: subagent
prompt: ./prompt.md
input: rankings (object[]), methods (string[])
dependencies:
  sops:
  - spawn-agent
---

# Method Sensitivity Report

Analyze the impact of MCDA method choice on final rankings, identifying which conclusions are method-independent (robust) and which depend on method selection.

## Execution

Subagent receives ranking results from multiple methods and method descriptions, produces a method sensitivity analysis report.

## Why Subagent

Sensitivity analysis requires deep understanding of theoretical differences and compensation mechanisms across methods; independent execution ensures analysis completeness.

## HARD-GATE

Report must clearly distinguish "method-independent conclusions" from "method-dependent conclusions", and provide specific recommendations for each method-dependent conclusion.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
