---
name: robustness-analysis
description: "Generate plausible model variants and test whether conclusions converge across assumption/model choices."
---

# robustness-analysis
## Purpose
Generate plausible model variants and test whether conclusions converge across assumptions and model choices.
## Input contract
```yaml
required: [base_model, conclusion, load_bearing_assumptions]
optional: [evidence, alternative_models, sensitivity_dimensions]
constraints: [variants must preserve the declared target question]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `surface-assumptions` to surface assumptions.
2. You MUST load skill `generate-alternative-model` to generate plausible alternatives.
3. You MUST load skill `assess-sensitivity` to compare sensitivity across variants.
4. You MUST load skill `identify-load-bearing-factors` to identify load-bearing factors.
5. You MUST load skill `analyze-scaling-regime` to check scaling regimes.
   If the result needs explicit validity boundaries, consider `map-validity-envelope`. If apparent agreement may reuse evidence or priors, consider `audit-convergence-independence`.
Deviation: omit scaling analysis only when the model has no scale variable; document the reason.
## Output contract
```yaml
produces: [model_variant_set, convergence_assessment, fragility_flags, load_bearing_factors]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Thresholds and quality gates
- B: at least two plausible variants are compared; conclusion changes, invariants, and fragility drivers are explicit.
## Failure and counterexamples
Do not call a conclusion robust when all variants share the same unchallenged assumption.
## Provenance map
- `robustness-testing`, `multi-model-convergence`, `alternative-model-generation`, `convergence-assessment`, `fragility-flagging`: resolved.
- `assumption-enumeration`: intermediate (only package-prefixed variants exist).
## Preserved source criteria ledger
- Preserve multi-model convergence and explicit fragility reporting.
## Context checkpoint / Delta notes
Append variants, changed assumptions, convergence results, and fragility flags.
