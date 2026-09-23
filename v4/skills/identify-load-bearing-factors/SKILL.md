---
name: identify-load-bearing-factors
description: "Identify factors/assumptions/uncertainties whose change most strongly controls the conclusion."
---

# identify-load-bearing-factors

## Purpose

Identify factors or assumptions whose change most strongly controls the conclusion.

## Input contract

```yaml
required: [conclusion, factor_or_assumption_set, perturbation_evidence]
optional: [necessity_sufficiency_results, uncertainty_contributions, critical_path]
constraints: [load-bearing status is tied to observed or reasoned conclusion change; preserve factor identity]
```

## Procedure

1. Assemble ablation, necessity/sufficiency, fragility, and uncertainty evidence.
2. Compare conclusion changes attributable to each factor.
3. Classify factors as necessary, sufficient, jointly necessary, or decorative where supported.
4. Rank load-bearing factors and state the evidence gap for each uncertain ranking.

## Output contract

```yaml
produces: [load_bearing_register, necessity_sufficiency_map, fragility_ranking, evidence_gaps]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Every factor receives a role classification and evidence-backed importance assessment.
- Fragility severity and alternative credibility are reported separately.
- EVPI or uncertainty-contribution results retain the caller's units and are not treated as causal proof.

## Parameterization

The caller must provide conclusion schema, factor/assumption list, perturbation results, classification ontology, importance metric, and uncertainty representation.

## Failure and counterexamples

Reject a load-bearing claim based only on correlation, an untested factor, or a perturbation that changes multiple undeclared inputs.

## Provenance map

- resolved: stress-test/load-bearing-identification
- resolved: deep-insight/fragility-flagging
- resolved: deep-insight/critical-path-identification

## Preserved source criteria ledger

No numeric source gate was present in the resolved source nodes; the role and evidence requirements above preserve their qualitative constraints.

