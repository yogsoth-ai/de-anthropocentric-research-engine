---
name: elegance-trap-probe
description: "Strategy: Attack a beautiful unified result on the suspicion that its beauty is the bug. Distinguishes EARNED simplicity (forbids/predicts/subsumes) from DECORATIVE simplicity (re-describes/relabels/accommodates). Directly serves the Occam aesthetic by making it a falsifiable bar, not a vibe. Methods: Sober parsimony-as-evidence, MDL, Meehl risky prediction, accommodation-vs-prediction."
type: strategy
produces: EleganceVerdict
---

# Elegance Trap Probe

The counter-intuitive attacker. Every other strategy attacks weaknesses; this one attacks a STRENGTH — the artifact's beauty. A common guiding aesthetic is Occam: a good result should be simple and elegant (LLM scaling laws replacing linguistics-inspired CNN/RNN; one principle of natural selection explaining all species). When we produce a beautiful unified result — one generator, a small number of projections, the key object as a symmetry — that is exactly what we hoped for. Which is precisely why it's dangerous. The same aesthetic that signals truth also seduces: a pretty story is easy to believe because it's pretty, not because it's right. This strategy interrogates whether the elegance was EARNED or is DECORATIVE, turning the aesthetic from a feeling into a falsifiable bar.

## The distinction that does all the work

**Earned simplicity** buys its compression by FORBIDDING and PREDICTING more. Natural selection is elegant because it forbids vast swaths of observation (no species improves for its own sake; no inheritance of un-selected acquired traits at the population level) and predicts specifics (fossils in strata order, antibiotic resistance dynamics). Scaling laws are elegant because they PREDICT loss at unseen scale — risky, falsifiable, and they held. Earned simplicity is a compression of MANY constraints into ONE generator that then GENERATES those constraints back, plus new ones.

**Decorative simplicity** achieves its prettiness by RE-DESCRIBING what we already knew in a unifying vocabulary, forbidding nothing new. It "explains" every existing observation because it was fitted to them; it makes no risky prediction; remove it and we lose a nice story but no predictive content. Freud's framework "explained" every behavior — and forbade none. A unification that says "everything is a projection of one generator" is decorative IF, for any conceivable observation, it can always find SOME projection to call it — i.e. if it cannot say what it would look like for the unification to be FALSE.

## The core test: what does the beautiful unification FORBID?

Apply Meehl/Popper directly to the artifact. A theory's content = what it forbids. So:
- **List what the unification forbids.** What patterns of data are IMPOSSIBLE if the unification is true? If the answer is "none — it can accommodate anything by choosing the right projection," the elegance is decorative and the unification is (so far) empty.
- **List the risky predictions.** What does it predict that the pre-unification picture does NOT, that we could check? A pretty theory that makes the same predictions as the collection of pieces it replaced has bought elegance with zero evidential currency (Meehl: it merely accommodates).
- **The deletion test (MDL flavor).** If we delete the unification and keep only the components as independent tools, do we LOSE predictive power, or only narrative tidiness? Earned simplicity loses power on deletion (the generator was doing work). Decorative simplicity loses only the story.

## Execution

### 1. Forbidden-set construction
One subagent: enumerate concrete observations the unification forbids. Push hard for SPECIFICS (a data pattern, a sandbox outcome). If the unification cannot be made to forbid anything checkable, that is the headline finding → unification is currently decorative, route to UNFALSIFIABLE.

### 2. Risky-prediction hunt
One subagent: find at least one prediction the unification makes that (a) differs from the pre-unification picture and (b) we could check in a sandbox or empirically. This prediction becomes a prime test target. If none exists, the unification is not yet earning its place.

### 3. Accommodation audit
Did the unification PREDICT the components it subsumes, or were the components found first and the unification fitted around them to look unified? (History matters here: if we found the pieces first and then sought a unifier, suspicion is high that the unification accommodates rather than predicts.) Honestly classify each component as predicted-by vs accommodated-into the unification.

### 4. The deletion test
Reason through: keep the components as standalone methods, delete the unifying narrative. What predictive or identifiability content is lost? List it. If nothing concrete is lost, the unification is (so far) decorative — still possibly a useful organizing frame, but it must be LABELED as organizing-frame, not as a discovered law.

### 5. Verdict + the path to earning it
Assign: EARNED (forbids + predicts, deletion loses power), DECORATIVE (re-describes, deletion loses only story), or PROMISING-BUT-UNEARNED (could be earned IF prediction P is checked and holds — name P). Crucially, this strategy does NOT demand we discard a decorative-so-far unification; it demands we either (a) find its forbidden-set/risky-prediction and check it, or (b) demote its status to "organizing frame" honestly. The Occam aesthetic is satisfied only by EARNED elegance — decorative elegance is the patchwork-in-disguise it was meant to avoid (a single pretty patch over everything forbids nothing).

## Relationship to the Occam aesthetic

This strategy is the aesthetic's enforcement arm. "Simple and elegant" is the GOAL, but the test of real elegance is not "does it feel unified" — it is "does the unification forbid and predict more than the pieces did." That is the difference between Darwin (earned) and a just-so story (decorative). By making the artifact state what it forbids, we either confirm the elegance is the real, earned kind — or we catch ourselves having fallen in love with a pretty re-description, which is the exact failure this strategy guards against.

## Output

`EleganceVerdict`: {forbidden-set (concrete, or "empty → decorative") | risky predictions distinct from pre-unification picture | accommodation audit per component (predicted vs fitted) | deletion-test result (power lost vs story lost) | verdict EARNED/DECORATIVE/PROMISING-BUT-UNEARNED | if unearned: the named prediction P whose check would earn it}.
