---
name: assumption-negation
description: "Classic reductio ad absurdum: negate the core claim, derive logical consequences, seek contradiction or absurdity."
type: strategy
used-by: [adversarial-stress-testing]
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
