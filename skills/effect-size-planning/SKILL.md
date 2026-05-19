---
name: effect-size-planning
description: Determine effect size types and calculation methods for meta-analytic synthesis
execution: subagent
prompt: ./prompt.md
input: outcome_measures, study_designs
used-by: meta-analysis
---

# Effect Size Planning SOP

Determine the appropriate effect size metric, calculation methods, and conversion formulas for the meta-analysis.

## When to Use

- After inclusion criteria are defined
- Before data extraction begins
- When studies report outcomes in different metrics

## Input

- `outcome_measures`: Types of outcome measures across included studies
- `study_designs`: Study designs present in the evidence base

## Output

Complete effect size specification including primary metric, calculation formulas for each reporting format, and conversion procedures.
