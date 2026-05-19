---
name: pico-formulation
description: Construct PICO/PECO framework for the meta-analysis research question
execution: subagent
prompt: ./prompt.md
input: research_question, domain
used-by: meta-analysis
---

# PICO Formulation SOP

Construct a structured PICO (Population, Intervention, Comparator, Outcome) or PECO (Population, Exposure, Comparator, Outcome) framework from a research question to guide systematic meta-analysis planning.

## When to Use

- First step in any meta-analysis strategy
- When the research question needs formal structuring
- Before defining inclusion/exclusion criteria

## Input

- `research_question`: The research question to structure
- `domain`: The research domain (clinical, computational, social science, etc.)

## Output

A complete PICO/PECO framework with operationalized definitions for each component, suitable for driving search strategy and inclusion criteria.
