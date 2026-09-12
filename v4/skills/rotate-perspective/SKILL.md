---
name: rotate-perspective
description: "Apply one perspective at a time to reinterpret the same target while holding the underlying evidence/object fixed; record changed assumptions, objectives, risks, and opportunities."
---

# rotate-perspective

## Purpose

Apply one perspective at a time to reinterpret the same target while holding the underlying evidence/object fixed; record changed assumptions, objectives, risks, and opportunities.

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

- intermediate: perspective-rotation [tactic]
- intermediate: six-thinking-hats [strategy]
- resolved: personal-analogy
