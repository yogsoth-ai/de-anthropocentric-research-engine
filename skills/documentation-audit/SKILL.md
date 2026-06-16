---
name: documentation-audit
description: Assess documentation completeness against BetterBench/Datasheets standards
execution: subagent
prompt: ./prompt.md
input: benchmark_documentation
dependencies:
  sops:
  - spawn-agent
---

# Documentation Audit SOP

Assess benchmark documentation completeness against established standards: BetterBench 46-criterion framework, Datasheets for Datasets, and Data Statements for NLP.

## Input

- **benchmark_documentation**: All available documentation for the benchmark (paper, README, website, datasheet)

## Procedure

1. Check documentation against BetterBench 46 criteria
2. Check against Datasheets for Datasets questions
3. Identify critical missing information
4. Assess reproducibility from documentation alone
5. Grade overall documentation quality

## Output

Documentation completeness score with per-criterion pass/fail and prioritized gaps.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
