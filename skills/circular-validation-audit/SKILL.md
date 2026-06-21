---
name: circular-validation-audit
description: "Strategy: Run BEFORE building any validator (sandbox/simulation/benchmark). Builds a non-circularity matrix of theory-claim × validator-assumption to detect when a validator would 'confirm' a theory only because it was built on the theory's own premises. A circular validator's PASS carries zero evidential weight. Methods: Cartwright nomological machines, Winsberg sanctioning-of-simulations, tautology detection."
type: strategy
produces: NonCircularityMatrix
---

# Circular Validation Audit

A pre-build gate for any validator we are about to construct — a sandbox, simulation, or benchmark that is supposed to verify a theory. The catastrophic failure mode: we build the validator using the theory's own assumptions as the validator's ground-truth machinery, run the theory's method on the validator's output, and celebrate when it "recovers" the truth — but the recovery was guaranteed by construction, not by the theory being right. The PASS carries zero evidential weight. This is the single most expensive mistake available, because a circular validator can burn enormous compute producing confident, meaningless confirmations. So this audit runs FIRST, on the validator DESIGN, before a line of it is built.

## The core risk, stated precisely

A validator V tests a theory T by: generating data D from a ground-truth generator G, running T's recovery method R on D, and checking if R(D) matches G's hidden truth. The test is non-circular only if G is NOT itself an instance of T's central assumptions. If G is built from the same functional factorization / the same noise law / the same mechanism that T claims to discover, then "R recovers G" is a tautology: we encoded the answer into the question. The audit's job is to find every place where G secretly contains T.

## Non-circularity matrix (the central artifact)

Rows = the theory's load-bearing claims/assumptions (the ones the validator is meant to test). Columns = the validator's ground-truth construction choices (how each mechanism is implemented, what functional forms or noise laws the generator uses, what intervention semantics the validator actually applies).

Each cell asks: **does this construction choice ASSUME this claim?**

| | validator: construction choice 1 | validator: construction choice 2 | validator: construction choice 3 | … |
|---|---|---|---|---|
| claim: load-bearing claim A | ? | ? | ? | ? |
| claim: load-bearing claim B | ? | ? | ? | ? |
| claim: load-bearing claim C | ? | ? | ? | ? |
| … | ? | ? | ? | ? |

Fill rows with each load-bearing claim the validator must test. Fill columns with each ground-truth construction choice in the validator. Cell verdicts:

- **CIRCULAR (red)** — the construction choice IS the claim. Testing it here proves nothing. Either the claim must be tested by a different validator, or the validator must implement that mechanism in a theory-AGNOSTIC way (see below).
- **INDEPENDENT (green)** — the construction choice is made on grounds the claim does not depend on (e.g. drawn from real empirical literature, or from a deliberately DIFFERENT functional form). A PASS here is real evidence.
- **PARTIAL (amber)** — shares some structure; the PASS is weak evidence, weight noted.

## The de-circularization moves (what to do with a red cell)

1. **Adversarial ground truth** — implement the validator's generator with a mechanism the theory does NOT predict (e.g. a noise law of a different family, a component that IS partly absorbable), and check the theory's method either still recovers correctly OR correctly reports "I cannot recover this." A theory that only works when the validator is built in its image is not a theory, it's a tautology. The strongest validator includes truths the theory should FAIL on — and we check it fails honestly.
2. **Held-out mechanism** — build the ground truth with a free parameter or structure the recovery method is not told about; success = recovering it blind.
3. **Different-formalism oracle** — generate ground truth in one formalism (e.g. an individual-based stochastic simulation), recover in another (the theory's preferred representation). If the theory claims they're equivalent, this doubles as a test of THAT claim — but only if the generating formalism itself was not derived from the theory's formalism.

## Execution

1. **Enumerate the validator's construction choices** — read the current validator design sketch and list every ground-truth construction choice: how each mechanism is implemented, what functional forms or noise laws the generator uses, what intervention semantics are assumed.
2. **Enumerate the claims the validator must test** — from the falsification ledger or the theory's load-bearing propositions.
3. **Fill the matrix** — one subagent per row is fine; each cell gets CIRCULAR/INDEPENDENT/PARTIAL + one sentence why.
4. **For every red cell, attach a de-circularization move** — or mark the claim "not testable in this validator; needs different validator/oracle."
5. **Compute the verdict** — the validator design is GREEN-LIGHT only if every load-bearing claim has at least one INDEPENDENT (or successfully de-circularized) test. Any claim with only CIRCULAR cells = the validator as designed cannot honestly test it → revise the design before building.

## Connection to compute-only constraint

This is where "compute-first, non-circular" bites. Some claims may be provably unrecoverable from observational data alone — for those, a validator that "recovers" them must be using a genuine intervention. The audit must verify the intervention is real (the validator actually applies a do-intervention and the recovery uses interventional data) and not a relabeled observational shortcut. An intervention that's free in the validator is legitimate; an observational method wearing an interventional costume is circular.

## Output

`NonCircularityMatrix`: the filled matrix + per-red-cell de-circularization move (or "untestable here") + overall GREEN/REVISE verdict on the validator design + the explicit list of "truths the validator should make the theory FAIL on" (the adversarial ground-truth set that turns the validator from a confirmation machine into a real test).
