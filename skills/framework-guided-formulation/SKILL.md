---
name: framework-guided-formulation
description: 'Strategy: Select an RQ framework (PICO/SPIDER/SPICE/ECLIPSE) and apply
  it systematically'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- framework-selection-and-application
- question-refinement-loop
sops:
- framework-matching
- pico-application
- spider-application
- spice-application
- eclipse-application
- finer-criteria-check
dependencies:
  tactics:
  - framework-selection-and-application
  - question-refinement-loop
---

# Framework-Guided Formulation

Select the most suitable RQ framework and apply it systematically — when the research type is clear, use a standard framework to structure the question.

## When to Use

- The research type is clear (quantitative/qualitative/mixed/evaluation)
- A corresponding standard framework is available
- You need to ensure all components of the question are complete

## Thinking Framework

Core logic: Different research types have different standards for a "good question." A framework is a checklist, distilled by predecessors, of "what components a good question should contain." Pick the right framework → fill in each component → naturally arrive at a structured question.

### Framework Selection Guide

| Research type | Recommended framework | Core components |
|----------|---------|---------|
| Quantitative/intervention research | PICO/PICOTS | Population, Intervention, Comparison, Outcome (+Time, Setting) |
| Qualitative research | SPIDER | Sample, Phenomenon of Interest, Design, Evaluation, Research type |
| Evaluation research | SPICE | Setting, Perspective, Intervention, Comparison, Evaluation |
| Mixed methods | ECLIPSE | Expectation, Client group, Location, Impact, Professionals, Service |

### Framework Application Principles

- Every component must be explicitly filled in (no blanks)
- Filled content must be specific (not "relevant population" but "type 2 diabetes patients aged 18–65")
- If a component is not applicable, explicitly state why it is not applicable

## Budget Gate

| Tier | Framework candidates | Framework application | FINER check | Output |
|------|---------|---------|-----------|------|
| S | ≥2 frameworks compared | Selected framework, all components filled | All 5 items pass | ≥1 RQ |
| M | ≥3 frameworks compared | Selected framework, all components + alternative framework comparison | 5 items + success criteria | ≥2 RQ |
| L | ≥4 frameworks compared | Multiple frameworks applied in parallel + optimal selection | 5 items + criteria + sensitivity | ≥3 RQ |

## Default Reference Flow

1. Determine the research type (quantitative/qualitative/mixed/evaluation)
2. Match candidate frameworks (framework-matching SOP)
3. Apply the selected framework (pico/spider/spice/eclipse-application SOP)
4. FINER check (finer-criteria-check SOP)
5. Revise failed items → re-check
6. Produce the final RQ

## context-checkpoint

After the Strategy completes, context-checkpoint must be called, recording:
- The selected framework and rationale
- The filled content of each framework component
- The FINER check results
- The final RQ statement

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| framework-selection-and-application | Tactic: Select the most suitable RQ framework and apply it systematically |
| question-refinement-loop | Tactic: iteratively refine a research question until it passes all 5 FINER criteria |

<!-- END available-tables (generated) -->
