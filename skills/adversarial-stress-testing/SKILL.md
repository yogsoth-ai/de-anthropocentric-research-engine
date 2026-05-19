---
name: adversarial-stress-testing
description: "Campaign: Logical extreme and boundary testing via reductio ad absurdum and edge-case analysis. Core question: Does this artifact collapse under logical limits and boundary conditions? Methods: Lakatos 1976, Dutilh Novaes 2016, BVA, Flyvbjerg Critical Case, Popper."
type: campaign
produces: AdversarialStressReport
artifact-types: [gap, hypothesis, research-question, idea, approach, experiment-design, claim]
---

# Adversarial Stress Testing

**Core Question:** Does this artifact collapse under logical limits and boundary conditions?

## Methodology Sources

- Lakatos (1976) — Proofs and Refutations: counterexample-driven refinement
- Dutilh Novaes (2016) — Adversarial argumentation as dialogical practice
- Clarke BVA — Boundary Value Analysis for systematic edge testing
- Flyvbjerg (2006) — Critical case methodology: most-likely/least-likely selection
- Popper (1959) — Falsificationism: seek conditions where claims break

## Strategy Routing

| Artifact Type | Primary Strategy | Rationale |
|---|---|---|
| claim, hypothesis | assumption-negation | Direct logical attack |
| gap, research-question | lakatos-heuristics | Counterexample refinement |
| idea, approach | boundary-enumeration | Parameter space testing |
| experiment-design | critical-case-design | Decisive test selection |
| any (synthesis) | validity-envelope-mapping | Comprehensive envelope |

## Budget Table

| Resource | S | M | L |
|---|---|---|---|
| Negation derivation chains | 3 | 6 | 10 |
| Counterexamples/boundary cases | 5 | 12 | 25 |
| Parameter dimensions | 3 | 6 | 10 |
| Validity envelope dimensions | 2 | 4 | 6 |

## Tactics

- contradiction-derivation — Negate, derive, detect contradiction
- boundary-probing — Map parameter space, test extremes, find breakpoints
- counterexample-heuristics — Generate monsters, bar or incorporate

## Context Management

- Persist derivation chains and counterexamples across rounds
- Track which negations produced genuine contradictions vs. benign outcomes
- Accumulate validity envelope boundaries incrementally

## Output

Produces `AdversarialStressReport` containing: identified breakpoints, validity envelope, surviving refined claims, and confidence assessment.
