# generate-alternative-model
## Purpose
Generate a plausible model variant by relaxing, replacing, or generalizing assumptions.
## Input contract
```yaml
required: [base_model, load_bearing_assumptions]
optional: [observations, model_constraints, variant_operations]
constraints: [each variant names the changed assumption and retained predictions]
```
## Procedure
1. Identify assumptions that constrain the base model.
2. Relax, replace, or generalize one assumption at a time.
3. Re-derive the model structure and compare predictions or implications.
## Output contract
```yaml
produces: [model_variants, changed_assumptions, prediction_comparison]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Every variant is traceable to an operation and remains internally coherent.
## Failure and counterexamples
Reject variants that change multiple assumptions without attribution or that cannot produce testable implications.
## Provenance map
- `deep-insight/alternative-model-generation`: resolved.
