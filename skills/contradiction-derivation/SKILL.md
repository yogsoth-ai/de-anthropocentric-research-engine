---
name: contradiction-derivation
description: Negate a claim, derive logical consequences step by step, detect whether
  a genuine contradiction or absurdity emerges.
type: tactic
strategies:
- assumption-negation
- validity-envelope-mapping
dependencies:
  sops:
  - claim-negation
  - contradiction-detection
  - deductive-chain
---

# Contradiction Derivation

## Orchestration Steps

1. Receive claim P from strategy
2. Dispatch `claim-negation` to produce ~P
3. Dispatch `deductive-chain` with ~P as premise, derive consequences
4. At each derivation step, dispatch `contradiction-detection` to check for:
   - Formal contradiction (Q and ~Q)
   - Absurd consequence (violates known facts)
   - Infinite regress or vacuous truth
5. If contradiction found: report with derivation trace
6. If chain exhausts without contradiction: report claim as contingent

## Subagents

- claim-negation
- deductive-chain
- contradiction-detection

## Termination Conditions

- Genuine contradiction detected (success)
- Maximum derivation depth reached (inconclusive)
- Circular reasoning detected (abort with warning)
- Budget exhausted (report partial results)
