---
name: select-experimental-baseline
description: "Select fair SOTA/simple/oracle/control baselines with provenance and rationale matched to the experimental claim."
---

# select-experimental-baseline

## Purpose

Select fair SOTA/simple/oracle/control baselines with provenance and rationale matched to the experimental claim.

## Input contract

```yaml
required: [experimental_claim, candidate_baselines, protocol_context]
optional: [evidence, assumptions, prior_results]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Validate the typed inputs and state the decision this operation must support.
2. Apply the declared operation to the named object; record intermediate values that affect interpretation.
3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.

## Output contract

```yaml
produces: [select_experimental_baseline_result, evidence_trace, uncertainties]
delta_fields: [evidence_updates, uncertainties]
```

## Quality gates

- Inputs are named scientific objects with compatible schemas.
- Every material result has a derivation or source reference.
- Fixed statistical criteria remain exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.

## Provenance map

- intermediate: experiment-execution/baseline-selection
