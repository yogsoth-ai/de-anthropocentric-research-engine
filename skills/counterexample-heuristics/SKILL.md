---
name: counterexample-heuristics
description: Generate counterexamples (monsters), attempt monster-barring, incorporate
  surviving counterexamples as lemma refinements (Lakatos method).
type: tactic
strategies:
- lakatos-heuristics
- assumption-negation
- critical-case-design
dependencies:
  sops:
  - claim-refinement
  - counterexample-generation
  - monster-barring-attempt
---

# Counterexample Heuristics

## Orchestration Steps

1. Receive claim/theorem from strategy
2. Dispatch `counterexample-generation` to produce candidate monsters
3. For each counterexample:
   a. Dispatch `monster-barring-attempt` — can it be excluded legitimately?
   b. If barring succeeds: record as excluded, note narrowed scope
   c. If barring fails: counterexample is genuine
4. For genuine counterexamples, dispatch `claim-refinement`:
   - Incorporate as lemma (add condition to claim)
   - Or weaken claim scope
5. Report: original claim, counterexamples found, refined claim

## Subagents

- counterexample-generation
- monster-barring-attempt
- claim-refinement

## Termination Conditions

- All generated counterexamples resolved (barred or incorporated)
- Claim refined to survive all counterexamples (success)
- Claim collapses entirely under counterexamples (falsified)
- Budget exhausted (report current state)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| claim-refinement | Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation). |
| counterexample-generation | Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies. |
| monster-barring-attempt | Attempt to exclude a counterexample as illegitimate by tightening definitions or preconditions (Lakatos monster-barring). |

<!-- END available-tables (generated) -->
