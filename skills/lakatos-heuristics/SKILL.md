---
name: lakatos-heuristics
description: 'Proofs and Refutations method: generate counterexamples, attempt monster-barring,
  incorporate surviving counterexamples as lemma refinements.'
type: strategy
dependencies:
  tactics:
  - contradiction-derivation
  - counterexample-heuristics
  sops:
  - claim-refinement
  - contradiction-detection
  - counterexample-generation
  - monster-barring-attempt
---

# Lakatos Heuristics

## Tactics

- counterexample-heuristics
- contradiction-derivation

## Method

1. Take the claim as a tentative theorem
2. Generate counterexamples systematically
3. For each counterexample, attempt monster-barring (exclude as illegitimate)
4. If monster-barring fails, incorporate as lemma (refine the claim)
5. Iterate until claim is robust or abandoned

## Budget

| Size | Counterexamples | Monster-barring rounds | Lemma incorporations |
|---|---|---|---|
| S | 5 | 2 | 2 |
| M | 12 | 4 | 4 |
| L | 25 | 8 | 8 |

## Orchestration

1. Dispatch `counterexample-generation` against the claim
2. For each counterexample, dispatch `monster-barring-attempt`
3. If barring fails, dispatch `claim-refinement` to incorporate lemma
4. Repeat until saturation or budget exhausted

## Subagents

- counterexample-generation
- monster-barring-attempt
- claim-refinement
- contradiction-detection
