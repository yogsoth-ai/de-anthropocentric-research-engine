---
name: evaluate-scenario-robustness
description: "Aggregate a candidate, strategy, or portfolio across explicit scenarios under a declared robust-decision rule such as worst-case score, minimax regret, maximin, threshold survival, or pivot-trigger analysis."
---

# evaluate-scenario-robustness

## Purpose

Aggregate a candidate, strategy, or portfolio across explicit scenarios under a declared robust-decision rule such as worst-case score, minimax regret, maximin, threshold survival, or pivot-trigger analysis.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [parameters name the scientific object being transformed; preserve provenance and missingness]
```

## Procedure

1. Identify the typed target, decision question, and eligible evidence.
2. Transform the target using the declared rule and attach each material choice to an input or source.
3. Inspect scope, missingness, and counterexamples, then emit the typed result with uncertainty.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The operation applies to a named scientific object, not a generic placeholder.
- Every non-trivial value has a source, derivation, or explicit missing marker.
- The output remains within scope and records uncertainty.

## Failure and counterexamples

Fail closed when the target schema is incomplete, evidence is incompatible, or a counterexample breaks the interpretation.

## Provenance map

- intermediate: experiment-execution/robustness-scoring
- intermediate: experiment-execution/strategy-robustness-testing [tactic]
- intermediate: convergence/portfolio-optimization/robustness-under-uncertainty [strategy]
- intermediate: Pass8/score-scenario-robustness
- intermediate: Pass8/evaluate-regret-robustness
