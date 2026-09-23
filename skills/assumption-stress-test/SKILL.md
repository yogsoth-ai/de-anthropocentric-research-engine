---
name: assumption-stress-test
description: "Surface load-bearing assumptions, classify vulnerability, challenge or perturb them, and re-check causal logic."
---

# assumption-stress-test
## Purpose
Expose load-bearing assumptions, classify their vulnerability, perturb them, and re-check causal validity.
## Input contract
```yaml
required: [claim_or_model, assumptions]
optional: [evidence, causal_graph, perturbation_bounds]
constraints: [each assumption must be traceable to a claim or causal link]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `surface-assumptions` to surface load-bearing assumptions.
2. You MUST load skill `classify-assumption-vulnerability` to classify their vulnerability.
3. You MUST load skill `challenge-assumption` to challenge each material assumption.
4. You MUST load skill `apply-perturbation` to apply bounded perturbations.
5. You MUST load skill `validate-causal-link` to re-check affected causal links.
   If the surviving result requires broader model and scaling variants, consider `robustness-analysis` as the next tactic.
Deviation: omit perturbation only when the assumption is purely definitional; still record and classify it.
## Output contract
```yaml
produces: [assumption_register, vulnerability_map, perturbation_results, causal_recheck]
delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: all load-bearing assumptions are classified; every challenged assumption has a perturbation or explicit non-perturbability reason; causal links are rechecked.
## Failure and counterexamples
Do not call a model robust when an untested high-vulnerability assumption carries the conclusion or when perturbation bounds are unstated.
## Provenance map
- `assumption-audit`, `assumption-stress-test`, `assumption-criticality`, `assumption-perturbation`: resolved/concept according to exact v3 lookup; no near-name substitution.
- Status: `assumption-audit`, `assumption-stress-test`, `assumption-criticality` resolved; `assumption-perturbation` concept (only package-prefixed variants found).
## Preserved source criteria ledger
- Preserve assumption surfacing, vulnerability classification, perturbation, and causal-link validation.
## Context checkpoint / Delta notes
Append changed assumptions, perturbation deltas, causal failures, and unresolved questions.
