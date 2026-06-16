---
name: anomaly-driven-abduction
description: 'Tactic: Inductive/abductive path — describe anomalous phenomena, generate
  candidate explanations, rank by plausibility'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- anomaly-characterization
- explanation-generation
- plausibility-ranking
dependencies:
  sops:
  - anomaly-characterization
  - explanation-generation
  - plausibility-ranking
---

# Anomaly Driven Abduction

Inductive/abductive path — precisely describe anomalous phenomena that existing theory cannot explain, generate multiple candidate explanations, rank by plausibility, and provide a structured basis for abductive hypotheses.

## Orchestration Intent

The starting point of abduction is "surprise" — an observed phenomenon inconsistent with existing theoretical predictions. This tactic forces CC to first precisely describe the anomaly (no vagueness allowed), then systematically generate explanations (not allowed to think of only one), and finally rank by plausibility (no subjective preference allowed).

None of the three steps can be omitted: imprecise description means explanations cannot be focused; insufficient explanations make ranking meaningless; ranking without basis turns hypothesis selection into guesswork.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| anomaly-characterization | Precisely describe the anomalous phenomenon: what was observed, deviation from expectation, conditions of occurrence, excluded trivial explanations | Required in all modes, execute first |
| explanation-generation | Generate multiple candidate explanations (abductive hypotheses); each explanation must fully account for the anomaly | Required in all modes, after anomaly-characterization |
| plausibility-ranking | Rank candidate explanations by plausibility criteria (prior probability, explanatory power, parsimony, testability) | Required in all modes, execute last |

## Orchestration Pattern

**Simplified (S tier, single anomaly)**
- Sequential execution: anomaly-characterization → explanation-generation (≥3 explanations) → plausibility-ranking
- Applicable: a single clear anomalous phenomenon with sufficient background information

**Standard (M tier, 1-3 related anomalies)**
- anomaly-characterization executes independently for each anomaly; explanation-generation generates ≥3 explanations (explanations may be shared across anomalies); plausibility-ranking ranks all explanations uniformly
- Applicable: multiple related anomalies may have a common explanation, requiring cross-anomaly integration

**Deep (L tier, complex anomaly cluster)**
- All 3 SOPs execute; explanation-generation additional requirement: each explanation must state why existing theory cannot explain the anomaly; plausibility-ranking additional output: which explanations can be distinguished by a single experiment
- Applicable: complex, interrelated anomalous phenomena requiring systematic abductive analysis

## Minimum Yield

- Structured anomaly description: including observed content, deviation from expectation, conditions of occurrence, excluded trivial explanations
- ≥3 candidate explanations, each explanation:
  - The mechanism that fully explains the anomaly
  - Relationship to existing theory (extend/revise/replace)
- Ranked list: including each explanation's plausibility score and ranking basis

## Yield Report

Report to the calling strategy after execution:
- Anomaly description completeness (whether it meets HARD-GATE requirements)
- Number of candidate explanations generated / number ranked
- Highest-plausibility explanation (for the strategy to prioritize for formalization)
- Discriminability: which explanations can be distinguished by a single experiment (for reference in subsequent experiment design)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| anomaly-characterization | SOP: Describe and classify anomalous phenomena that existing theory cannot explain |
| explanation-generation | SOP: generate a list of candidate explanations for an anomalous phenomenon |
| plausibility-ranking | SOP: rank candidate explanations by plausibility using multi-dimensional weighted scoring |

<!-- END available-tables (generated) -->
