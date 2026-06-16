---
name: assumption-enumeration
description: Surface, perturb, and prioritize assumptions by disruption potential.
  Orchestrates assumption surfacing → perturbation → sacred cow identification → prioritization.
execution: tactic
dependencies:
  sops:
  - creative-ideation-assumption-perturbation
  - sacred-cow-identification
---

# Assumption Enumeration

Surface, perturb, and prioritize assumptions by disruption potential.

## Stages

### Stage 1: Assumption Surfacing

Use assumption-surfacing SOP to enumerate all implicit assumptions in the target. Cover all 8 categories (physical, temporal, spatial, economic, technical, social, logical, paradigmatic).

### Stage 2: Assumption Perturbation

For each surfaced assumption, use assumption-perturbation SOP to systematically perturb it. Observe what breaks, what new spaces open, and what remains stable.

### Stage 3: Sacred Cow Identification

From the perturbation results, use sacred-cow-identification SOP to flag assumptions that are deeply held but poorly justified — the true sacred cows with highest disruption potential.

### Stage 4: Prioritization

Rank all assumptions by disruption potential × challengeability. Select top candidates for downstream negation and inversion work.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Assumptions surfaced | ≥8 |
| Categories covered | ≥5/8 |
| Assumptions perturbed | ≥6 |
| High-disruption identified | ≥3 |
| Sacred cows flagged | ≥2 |

## Available SOPs

| SOP | Role |
|-----|------|
| assumption-surfacing | Stage 1 — enumerate assumptions (shared, existing) |
| assumption-perturbation | Stage 2 — perturb and observe |
| sacred-cow-identification | Stage 3 — flag unquestioned beliefs |
| novelty-scoring | Stage 4 — score disruption potential |
| saturation-detection | Pre — check if more surfacing needed |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| creative-ideation-assumption-perturbation | Perturb each assumption, observe system response. Systematic stress-testing of assumptions to reveal fragility and opportunity. |
| sacred-cow-identification | Find domain's unquestioned beliefs. Systematic identification of dogma that constrains innovation. |

<!-- END available-tables (generated) -->
