---
name: gap-driven-generation
description: Generate solutions targeting specific coverage gaps — detect gaps, generate failure-driven solutions, and design factor-level experiments.
execution: tactic
used-by: systematic-enumeration, failure-taxonomy, factorial-ideation
---

# Gap-Driven Generation

Detect coverage gaps in the solution space, then generate targeted solutions using failure analysis and factorial design.

## Stages

### Stage 1: Coverage Gap Detection

Run coverage-gap-detection SOP to identify uncovered regions in the solution space. Output: gap list with priority ranking based on impact and feasibility.

### Stage 2: Failure-Driven Generation

Run failure-driven-generation SOP to generate solutions that specifically target identified failure modes or gaps. Output: one or more targeted solutions per gap.

### Stage 3: Factor-Level Design

Run factor-level-design SOP to identify key factors in the gap space, define levels, and design an experiment matrix for systematic exploration. Output: factorial design ready for implementation.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Coverage gaps identified | ≥3 |
| Gaps with priority ranking | 100% |
| Solutions generated per gap | ≥1 |
| Total targeted solutions | ≥3 |
| Factor-level matrix produced | yes |

## Available SOPs

| SOP | Role |
|-----|------|
| coverage-gap-detection | Stage 1 — detect uncovered regions |
| failure-driven-generation | Stage 2 — generate targeted solutions |
| factor-level-design | Stage 3 — factorial experiment design |
