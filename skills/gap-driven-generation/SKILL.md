---
name: gap-driven-generation
description: Generate solutions targeting specific coverage gaps — detect gaps, generate
  failure-driven solutions, and design factor-level experiments.
execution: tactic
dependencies:
  sops:
  - coverage-gap-detection
  - creative-ideation-factor-level-design
  - creative-ideation-failure-mode-cataloging
  - failure-driven-generation
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| coverage-gap-detection | Detect uncovered regions in the solution space, producing a prioritized gap list. |
| creative-ideation-factor-level-design | Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration. |
| creative-ideation-failure-mode-cataloging | Systematically catalog all failure modes in a domain or method, producing a classified failure taxonomy. |
| failure-driven-generation | Generate targeted solutions for each identified failure mode, ensuring every failure has at least one proposed mitigation. |

<!-- END available-tables (generated) -->
