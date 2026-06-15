---
name: assumption-negation
description: 'Classic reductio ad absurdum: negate the core claim, derive logical
  consequences, seek contradiction or absurdity.'
type: strategy
dependencies:
  tactics:
  - contradiction-derivation
  - counterexample-heuristics
  sops:
  - claim-negation
  - claim-refinement
  - contradiction-detection
  - deductive-chain
---

# Assumption Negation

## Tactics

- contradiction-derivation
- counterexample-heuristics

## Method

1. Extract the core claim or assumption from the artifact
2. Formally negate it (produce ~P from P)
3. Derive logical consequences of ~P through deductive chains
4. Evaluate whether derivation reaches genuine contradiction
5. If contradiction found: original claim survives this test
6. If no contradiction: claim may be contingent, not necessary

## Budget

| Size | Negation chains | Max derivation depth |
|---|---|---|
| S | 3 | 5 steps |
| M | 6 | 8 steps |
| L | 10 | 12 steps |

## Orchestration

1. Dispatch `claim-negation` to produce formal negation
2. For each negation, dispatch `deductive-chain` to derive consequences
3. Dispatch `contradiction-detection` to evaluate results
4. If no contradiction, dispatch `claim-refinement` for weakened version

## Subagents

- claim-negation
- deductive-chain
- contradiction-detection
- claim-refinement

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
| claim-negation | Formally negate the core claim, producing the logical complement for reductio testing. |
| claim-refinement | Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation). |
| contradiction-detection | Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state. |
| deductive-chain | Derive logical consequences step by step from a given premise, building a traceable derivation chain. |

<!-- END available-tables (generated) -->
