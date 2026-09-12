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
1. Surface load-bearing assumptions (`surface-assumptions`).
2. Classify vulnerability (`classify-assumption-vulnerability`).
3. Challenge each material assumption (`challenge-assumption`).
4. Apply bounded perturbations (`apply-perturbation`).
5. Re-check causal links (`validate-causal-link`).
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
