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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
