---
name: comparative-formulation
description: 'Strategy: Construct comparative research questions — systematic comparison
  of A vs B'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- framework-selection-and-application
sops:
- framework-matching
- pico-application
- finer-criteria-check
- success-criteria-definition
dependencies:
  tactics:
  - framework-selection-and-application
  sops:
  - finer-criteria-check
  - success-criteria-definition
---

# Comparative Formulation

Construct comparative research questions — when research requires comparing A vs B, systematically construct a fair, meaningful comparison.

## When to Use

- Need to compare two methods/conditions/groups
- The hypothesis involves "X is better than / different from Y"
- Need to ensure the fairness and validity of the comparison

## Thinking Framework

Core logic: a good comparative research question requires clarifying four elements — what is compared (objects), along what dimension (metrics), under what conditions (controls), and what counts as "different" (threshold).

### Comparison Design Principles

- **Fairness**: the comparison conditions are fair to both sides (not a strawman)
- **Clear dimensions**: along which dimension(s) the comparison is made
- **Controlled variables**: all conditions are the same except the compared objects
- **Effect size**: not just "whether there is a difference" but "how large a difference is meaningful"

### Comparison Types

| Type | Example | Key considerations |
|------|------|---------|
| Method comparison | Method A vs Method B | Implementation fairness, dataset selection |
| Condition comparison | With X vs Without X | Controlled variables, confounding factors |
| Group comparison | Group A vs Group B | Matching, selection bias |
| Temporal comparison | Before vs After | History effects, maturation effects |

## Budget Gate

| Tier | Comparison design | Fairness argument | Output |
|------|---------|-----------|------|
| S | Comparison objects + clear dimensions | Basic fairness statement | ≥1 comparative RQ |
| M | + controlled variables + effect size | Fairness argument + identification of potential bias | ≥2 comparative RQs |
| L | + multi-dimensional + sensitivity | Full fairness analysis + bias mitigation strategy | ≥3 comparative RQs |

## Default Reference Flow

1. Determine the comparison objects (what A and B are)
2. Determine the comparison dimensions (along what metrics to compare)
3. Determine the control conditions (what to keep constant)
4. Argue fairness (whether the comparison is fair)
5. Structure it with the PICO framework (the C component is core)
6. FINER check
7. Define success criteria (what counts as a "meaningful difference")

## context-checkpoint

After the Strategy completes, context-checkpoint must be called, recording:
- Comparison objects and selection rationale
- Comparison dimensions
- Fairness argument
- Final comparative RQ

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| framework-selection-and-application | Tactic: Select the most suitable RQ framework and apply it systematically |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| finer-criteria-check | SOP: check research-question quality against each of the 5 FINER criteria |
| success-criteria-definition | SOP: Define measurable success criteria for a research question |

<!-- END available-tables (generated) -->
