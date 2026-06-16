---
name: framework-selection-and-application
description: 'Tactic: Select the most suitable RQ framework and apply it systematically'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- framework-matching
- pico-application
- spider-application
- spice-application
- eclipse-application
dependencies:
  sops:
  - eclipse-application
  - framework-matching
  - pico-application
  - spice-application
  - spider-application
---

# Framework Selection and Application

Select the most suitable RQ framework and apply it systematically — from framework matching to full population.

## Orchestration Intent

Decompose "structuring a research question with a framework" into: first select the framework → then apply the framework. Selection and application are two independent steps, handled by different SOPs.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| framework-matching | Match the most suitable framework based on research type | First step, always called |
| pico-application | Apply the PICO/PICOTS framework | Quantitative/intervention research |
| spider-application | Apply the SPIDER framework | Qualitative research |
| spice-application | Apply the SPICE framework | Evaluation research |
| eclipse-application | Apply the ECLIPSE framework | Mixed methods research |

## Orchestration Pattern

**Standard pattern**:
1. framework-matching → obtain recommended framework + rationale
2. Call the corresponding application SOP based on the recommendation (pico/spider/spice/eclipse)
3. Check population completeness

**Comparison pattern (M/L tier)**:
1. framework-matching → obtain top 2-3 candidates
2. Call the corresponding application SOP for each candidate
3. Compare which framework yields the more precise RQ
4. Select the best

## Minimum Yield

- ≥2 candidate frameworks are evaluated (with selection rationale)
- Every component of the selected framework is explicitly filled in (no blanks)
- Filled content is specific (not vague description)

## Yield Report

After execution completes, report:
- Number of frameworks evaluated
- The selected framework and rationale
- Completeness of each component's population
- Whether any component could not be filled due to insufficient information

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| eclipse-application | SOP: apply the ECLIPSE framework to structure a mixed-methods research question |
| framework-matching | SOP: Match the most suitable RQ framework based on research type |
| pico-application | SOP: apply the PICO/PICOTS framework to structure a research question |
| spice-application | SOP: Apply the SPICE framework to structure an evaluation research question |
| spider-application | SOP: Apply the SPIDER framework to structure a qualitative research question |

<!-- END available-tables (generated) -->
