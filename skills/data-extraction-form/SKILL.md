---
name: data-extraction-form
description: Design structured data extraction form for systematic meta-analysis data collection
execution: subagent
prompt: ./prompt.md
input: pico_framework, effect_size_type, moderator_variables
used-by: meta-analysis
---

# Data Extraction Form SOP

Design a structured, comprehensive data extraction form tailored to the specific meta-analysis, ensuring all necessary data points are captured systematically.

## When to Use

- After PICO, inclusion criteria, and effect size type are determined
- Before beginning full data extraction from included studies
- When standardizing extraction across multiple reviewers

## Input

- `pico_framework`: The structured PICO/PECO framework
- `effect_size_type`: The chosen effect size metric and calculation methods
- `moderator_variables`: Pre-specified moderator variables for heterogeneity investigation

## Output

A complete data extraction form with field definitions, coding instructions, and examples for each variable.
