---
name: competing-hypothesis-matrix
description: 'Tactic: Multi-hypothesis management — generate competing hypotheses,
  design discriminating predictions, build a structured comparison matrix'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- competing-hypothesis-generation
- discriminating-prediction-design
- hypothesis-comparison-matrix
dependencies:
  sops:
  - competing-hypothesis-generation
  - discriminating-prediction-design
  - hypothesis-comparison-matrix
---

# Competing Hypothesis Matrix

Multi-hypothesis management — systematically generate alternative explanations competing with the primary hypothesis, design key predictions that can distinguish them, and build a structured comparison matrix to avoid confirmation bias.

## Orchestration Intent

The most dangerous bias in scientific reasoning is holding only one hypothesis. This tactic forces CC to first systematically construct competing hypotheses before settling on the "best" hypothesis, then design predictions that can distinguish them.

The three steps cannot be reordered: first generate competing hypotheses (skipping not allowed), then design discriminating predictions (not allowed to only compare without testing), and finally build the comparison matrix (not allowed to only enumerate without quantifying). The final output is not "which hypothesis is correct" but "what experiment can distinguish them."

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| competing-hypothesis-generation | Based on the primary hypothesis, generate ≥3 alternative hypotheses competing with it (different mechanisms, same or similar phenomenon prediction range) | Required in all modes, execute first |
| discriminating-prediction-design | Design discriminating predictions for each pair of competing hypotheses — find an observable result for which the two hypotheses predict differently | Required in all modes, after competing-hypothesis-generation |
| hypothesis-comparison-matrix | Assemble all hypotheses and discriminating predictions into a structured comparison matrix, annotating each hypothesis's expected outcome for each prediction | Required in all modes, execute last |

## Orchestration Pattern

**Simplified (S tier, 1 primary hypothesis)**
- Sequentially execute all 3 SOPs; generate ≥3 competing hypotheses; design ≥2 discriminating predictions; build comparison matrix
- Applicable: a single primary hypothesis requiring competitive-thinking scrutiny

**Standard (M tier, 2-3 primary hypotheses)**
- competing-hypothesis-generation generates competing hypotheses independently for each primary hypothesis; discriminating-prediction-design designs discriminating predictions across primary and competing hypotheses; hypothesis-comparison-matrix includes all hypotheses (primary + competing)
- Applicable: multiple candidate hypotheses already exist, requiring unified management and comparison

**Deep (L tier, complex hypothesis set)**
- All 3 SOPs execute; competing-hypothesis-generation additional requirement: at least 1 competing hypothesis comes from a completely different theoretical framework; discriminating-prediction-design additional requirement: each discriminating prediction annotates the required experiment scale and difficulty; hypothesis-comparison-matrix additional output: recommended experiment priority (most discriminating predictions ranked first)
- Applicable: a complex hypothesis space requiring direct input to experiment design

## Minimum Yield

- ≥3 competing hypotheses (explaining the same phenomenon as the primary hypothesis but with different mechanisms)
- ≥2 discriminating predictions (each prediction produces different expected outcomes for at least 2 hypotheses)
- Structured comparison matrix: hypotheses × predictions, each cell annotating expected outcome direction (support/contradict/irrelevant)

## Yield Report

Report to the calling strategy after execution:
- Number of competing hypotheses / number of discriminating predictions
- Most discriminating prediction (distinguishing the most hypothesis pairs at once)
- Hardest-to-distinguish hypothesis pair (predictions nearly identical, requiring extremely fine experiment design)
- Recommended hypothesis to test first (most easily falsified + most discriminating)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| competing-hypothesis-generation | SOP: Generate mechanistically distinct competing hypotheses for the same phenomenon |
| discriminating-prediction-design | SOP: design key predictions and observation plans that can distinguish competing hypotheses |
| hypothesis-comparison-matrix | SOP: Build a multi-dimensional comparison matrix of competing hypotheses |

<!-- END available-tables (generated) -->
