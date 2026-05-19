---
name: documentation-audit
description: Assess documentation completeness against BetterBench/Datasheets standards
execution: subagent
prompt: ./prompt.md
input: benchmark_documentation
used-by: benchmark-archaeology
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
