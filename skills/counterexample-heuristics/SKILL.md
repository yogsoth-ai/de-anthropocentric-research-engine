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
