---
name: component-decomposition
description: Decompose system into functional components, identify dependencies, and
  surface trimming candidates.
execution: tactic
dependencies:
  sops:
  - function-model-construction
  - trimming-execution
---

# Component Decomposition

Decompose a system into its functional components, map dependencies, and identify candidates for trimming or surgical modification.

## Stages

### Stage 1: Function Model Construction

Build complete functional model using function-model-construction SOP. Identify all components and their interactions (useful, harmful, insufficient, excessive).

### Stage 2: Parameter Identification

For each component, identify key parameters using parameter-identification SOP. Map which parameters are shared, conflicting, or independent.

### Stage 3: Trimming Candidate Selection

Evaluate each component for trimming potential via trimming-execution SOP criteria: high harmful-function ratio, function redistributable to neighbors, low integration cost.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Components identified | ≥5 |
| Interactions mapped | ≥8 |
| Trimming candidates | ≥3 |
| Parameters per component | ≥2 |

## Available SOPs

| SOP | Role |
|-----|------|
| function-model-construction | Stage 1 — build functional model |
| parameter-identification | Stage 2 — extract component parameters |
| trimming-execution | Stage 3 — evaluate trimming feasibility |
| surgery-operation | Post — apply surgical operations to candidates |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| function-model-construction | Build substance-field functional model of a system, annotating useful, harmful, insufficient, and excessive interactions. |
| trimming-execution | Progressively remove components from a system while verifying function preservation through redistribution. |

<!-- END available-tables (generated) -->
