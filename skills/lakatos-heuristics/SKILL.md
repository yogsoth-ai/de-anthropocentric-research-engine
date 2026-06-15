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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| contradiction-derivation | Negate a claim, derive logical consequences step by step, detect whether a genuine contradiction or absurdity emerges. |
| counterexample-heuristics | Generate counterexamples (monsters), attempt monster-barring, incorporate surviving counterexamples as lemma refinements (Lakatos method). |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| claim-refinement | Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation). |
| contradiction-detection | Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state. |
| counterexample-generation | Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies. |
| monster-barring-attempt | Attempt to exclude a counterexample as illegitimate by tightening definitions or preconditions (Lakatos monster-barring). |

<!-- END available-tables (generated) -->
