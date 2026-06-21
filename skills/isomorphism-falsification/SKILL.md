---
name: isomorphism-falsification
description: "Strategy: Attack an isomorphism claim by demanding an explicit structure-preserving map and trying to break it. Targets any multi-language claim of the form 'X ≅ Y ≅ … across N mathematical languages'. Forces the claim to either earn the word 'isomorphism' or be demoted to 'analogy'. Methods: category theory (functor/natural-iso criteria), model theory, Lakatos monster-barring."
type: strategy
produces: IsomorphismVerdict
---

# Isomorphism Falsification

A dedicated attacker for the single most suspicious kind of claim an artifact can make: **"X = Y = Z = W"** asserted across multiple mathematical languages. "Isomorphism" is a precise mathematical word with a heavy burden of proof. "These things rhyme" is an analogy with almost none. The danger is that a pleasing analogy gets promoted to "isomorphism" because it FEELS unifying — pure elegance-trap. This strategy forces the claim to pay its burden or be demoted.

## Why this needs its own strategy

Generic debate/red-team will poke at it, but they don't know the specific bar an isomorphism must clear. This strategy encodes that bar. The burden of proof for "A ≅ B" is NOT "A and B share some features." It is: a map Φ: A → B that is (1) well-defined on all of A, (2) preserves the relevant structure (the operations/relations that matter — the composition of symmetries, the action of the generator, or whatever structure the artifact asserts is shared), (3) is invertible (or at least: the claimed correspondence is bijective on the objects we care about — the kernel/null/zero sets). Anything less is a homomorphism, a functor, an embedding, a loose analogy — each strictly weaker, and we must say which.

## The ladder of strength (assign the claim its true rung)

From strongest to weakest. The attack's job is to find the highest rung the claim can actually defend, then demote our wording to match:

1. **Isomorphism** — bijective, structure-preserving both ways. The full claim.
2. **Isomorphism on a substructure** — true only for the kernel/zero-mode sets, not the whole spaces. (Plausibly where many multi-language claims actually land — and that would still be a real, strong result if stated honestly.)
3. **Homomorphism / functor** — structure-preserving one way, not invertible. Maps objects to objects but loses information.
4. **Shared invariant** — all claimed sides have a quantity that coincides (e.g. all "zero sets" have the same dimension) but no map is exhibited. Numerical coincidence, not identity.
5. **Analogy** — suggestive parallel, no formal correspondence. The honest label if 1–4 all fail.

## Execution

### 1. Pin each claimed side precisely
For each language in which the artifact claims the same object lives, write down EXACTLY what that object is: its ambient space, what "zero/null/kernel/curl" means there, and what structure (group action, vector space, operator) it carries. Vagueness here is itself a finding — you cannot have an isomorphism between two things you cannot define.

### 2. Dimension/counting sanity check (cheap — run before any map-construction)
With each side now pinned: do all the claimed "zero sets" even have the same dimension / cardinality / number of generators? If the counts disagree, the isomorphism is dead at rung 4 immediately and cheaply — stop here, before the expensive map-construction below.

### 3. Demand the maps (pairwise, or a common target)
An isomorphism among N objects = either all pairwise isomorphisms or a common object all N map to iso-ally. For at least the load-bearing pairs (the boldest claimed equivalence and the most checkable one), attempt to WRITE the map explicitly. If we can only gesture ("they correspond"), drop to rung 4.

### 4. Try to break each map (monster-hunting)
For each exhibited map, hunt a monster: an element of A with no well-defined image in B; two distinct elements of A with the same image (non-injective → not iso); an element of B not hit (non-surjective); an operation preserved in A but not in B (structure not preserved). One surviving monster knocks the claim down a rung.

### 5. Assign the rung, demote the wording
Output the highest defended rung. If < 1, REWRITE every place the artifact says "isomorphism" to the honest word. This is not a defeat — "isomorphism on the kernel substructure" or even "shared invariant" is a strong true statement; "isomorphism" when it's really an analogy is self-deception.

## Anti-patterns to catch

- **Hand-wavy functoriality** — "obviously these are the same up to the right dictionary." Demand the dictionary entry for the specific monster.
- **Borrowed authority** — "it's well known that these two fields are connected." Connection ≠ this specific identity of THESE objects.
- **Retroactive rung-claiming** — if forced to rung 2, do not then re-narrate as if rung 1 were intended all along.

## Output

`IsomorphismVerdict`: per claimed equality (and overall) → {each claimed side pinned | maps attempted (explicit / gestured / none) | monsters found | dimension-count result | highest defended rung 1–5 | required wording change}. If rung 2 (iso on substructure): state exactly which substructure — that becomes a sharp, true claim for the next round.
