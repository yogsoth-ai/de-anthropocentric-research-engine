---
name: critical-case-design
description: 'Flyvbjerg critical case methodology: select most-likely and least-likely
  cases to maximize inferential power.'
type: strategy
dependencies:
  tactics:
  - boundary-probing
  - counterexample-heuristics
  sops:
  - breakpoint-detection
  - contradiction-detection
  - extreme-value-generation
  - parameter-space-mapping
---

# Critical Case Design

## Tactics

- boundary-probing
- counterexample-heuristics

## Method

1. Identify the claim's scope and conditions
2. Design most-likely case: conditions maximally favorable to claim
3. Design least-likely case: conditions maximally unfavorable
4. If claim fails in most-likely case: strong disconfirmation
5. If claim holds in least-likely case: strong confirmation
6. Report inferential power of each test

## Budget

| Size | Critical cases designed | Evaluation depth |
|---|---|---|
| S | 2 (one most-likely, one least-likely) | Surface |
| M | 4 (two each) | Moderate |
| L | 6 (three each) | Deep |

## Orchestration

1. Dispatch `parameter-space-mapping` to identify conditions
2. Dispatch `extreme-value-generation` for favorable/unfavorable extremes
3. Dispatch `breakpoint-detection` to test claim at critical cases
4. Dispatch `contradiction-detection` to evaluate outcomes

## Subagents

- parameter-space-mapping
- extreme-value-generation
- breakpoint-detection
- contradiction-detection

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| boundary-probing | Map parameter space, generate extreme values, test at boundaries, detect breakpoints, synthesize validity envelope. |
| counterexample-heuristics | Generate counterexamples (monsters), attempt monster-barring, incorporate surviving counterexamples as lemma refinements (Lakatos method). |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| breakpoint-detection | Test a claim at extreme parameter values and detect the precise point where it breaks down. |
| contradiction-detection | Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state. |
| extreme-value-generation | Generate boundary and extreme test values for a given parameter dimension to stress-test claims. |
| parameter-space-mapping | Identify all parameter dimensions along which a claim's validity might vary. |

<!-- END available-tables (generated) -->
