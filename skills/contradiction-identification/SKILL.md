---
name: contradiction-identification
description: Identify technical and physical contradictions in a system through functional modeling and matrix analysis.
execution: tactic
used-by: structural-deconstruction, triz-contradiction-resolution
---

# Contradiction Identification

Identify technical and physical contradictions in a system, providing resolution paths for each.

## Stages

### Stage 1: Function Model Construction

Build substance-field model of the system using function-model-construction SOP. Annotate useful, harmful, and insufficient interactions.

### Stage 2: Contradiction Matrix Lookup

For each identified technical contradiction (improving parameter vs worsening parameter), query the 39×39 TRIZ contradiction matrix via contradiction-matrix-lookup SOP.

### Stage 3: Separation Principle Selection

For physical contradictions (same parameter must be both X and not-X), identify applicable separation principles (time, space, condition, scale) via separation-principle SOP.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Technical contradictions identified | ≥2 |
| Physical contradictions identified | ≥1 |
| Resolution paths per contradiction | ≥2 |
| Applicable principles listed | ≥4 |

## Available SOPs

| SOP | Role |
|-----|------|
| function-model-construction | Stage 1 — build substance-field model |
| contradiction-matrix-lookup | Stage 2 — query matrix for principles |
| separation-principle | Stage 3 — resolve physical contradictions |
| triz-principle-application | Post — apply selected principles |
