---
name: independent-convergence-audit
description: "Strategy: Attack the evidential weight of an 'independent convergence' claim. When N reasoning paths all reach the same conclusion, the confidence boost is real only if the paths were actually independent. Measures shared-prior / shared-blindspot contamination and corrects the over-counted confidence. Methods: Bayesian agreement-as-evidence, correlated-error analysis, jury theorem assumptions."
type: strategy
produces: ConvergenceIndependenceReport
---

# Independent Convergence Audit

A dedicated attacker for one specific piece of evidence artifacts often lean on heavily: N reasoning paths "independently" converged on the same conclusion, and that triple- (or N-fold) convergence is treated as strong corroboration. It IS strong — IF the paths were independent. But paths run by the same model, from the same context, under the same prompts, may carry the same blind spot and the same priors. Correlated agreement is weak evidence dressed as strong evidence. This strategy measures how independent the convergence really was and corrects the confidence we should draw from it.

## Why agreement is only sometimes evidence

The logic "many paths agree → likely true" is the Condorcet/jury intuition, and it has a hard precondition: the paths' errors must be (at least partly) INDEPENDENT. If three jurors all read the same biased newspaper, their unanimous verdict carries roughly the weight of one juror, not three. The "newspaper" candidates are: (1) the same base model with the same training priors, (2) the same conversation context seen by all subagents, (3) the same prompt framing imposed by the orchestrator, (4) the same source literature feeding all paths, (5) a shared aesthetic pull toward unification (the elegance-trap acting on all paths at once). Each shared source collapses N effective-independent-paths toward 1.

## The independence ledger (central artifact)

For the convergence claim, score each potential shared-source channel:

| Shared channel | Present? | How much it correlates the paths | Effect on effective N |
|---|---|---|---|
| same base model / priors | yes (structural) | high — same inductive biases | large collapse |
| same conversation context | depends — were subagents isolated? | medium-high | medium collapse |
| same prompt framing | depends — did orchestrator steer toward "find the unifier"? | medium | medium collapse |
| same source literature | depends — did all paths cite the same sources? | medium | medium collapse |
| shared elegance pull | likely | medium — all drawn to the pretty answer | medium collapse |

Effective independence N_eff = (naive N) discounted by the collapse factors. If N_eff ≈ 1, the convergence is essentially ONE observation and our confidence must drop accordingly.

## Execution

### 1. Reconstruct each path's actual inputs
From the convergence checkpoint, recover for each path: what context it was given, whether it ran in an isolated subagent, what literature or seeds it had, and crucially whether the prompt already named or hinted at the target answer. A path that was TOLD to find a particular kind of unifier did not independently discover one.

### 2. Hunt the common cause
The killer question: is there a single upstream framing that MADE all paths converge? E.g. if the setup framed every input as "a symptom of a missing dynamical object," then all paths were pre-aimed at a dynamical unifier. That would make the convergence an artifact of the framing, not a property of the problem. Look specifically for the orchestrator's fingerprints.

### 3. The discriminating test: would an independent path have DIVERGED?
Design (and if cheap, run) a genuinely independent additional path — different framing, blind to the conclusion the other paths reached, ideally a different reasoning mode (e.g. purely empirical / bottom-up from data rather than top-down from theory). If it ALSO lands on the same conclusion, that's real independent corroboration. If it lands somewhere else, the original convergence was framing-induced.

### 4. Correlated-error check
Even if the conclusion is right, do the N paths share the SAME potential error? If all paths would be wrong in the same way under some condition, their agreement provides no protection against that error. List the errors the convergence does NOT rule out.

### 5. Correct the confidence
State the corrected evidential weight: e.g. "N-fold convergence, discounted for shared model and framing, is worth approximately one-and-a-half independent observations, not N." Adjust any downstream confidence that cited the convergence.

## What a healthy result looks like

This audit is NOT trying to prove the conclusion wrong — the conclusion may be entirely correct. It is trying to prevent us from being MORE confident than the evidence warrants. A good outcome is honest recalibration: "the convergence is partly framing-induced, so we should treat the conclusion as a strong hypothesis requiring a real test, not as already-established." That keeps us from skipping the real test because we felt too sure.

## Output

`ConvergenceIndependenceReport`: the independence ledger with N_eff estimate | identified common-cause framing (orchestrator fingerprints, if any) | result of the independent additional path (if run) or its design | correlated errors the convergence does not rule out | corrected confidence statement for the conclusion.
