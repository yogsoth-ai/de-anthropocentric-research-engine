---
name: apply-question-framework
description: "Select and instantiate a research-question schema appropriate to study type."
---

# apply-question-framework

## Purpose

Structure an underspecified research question with a declared question framework.

## Input contract

```yaml
required: [question, research_context, framework]
optional: [population, intervention, comparator, outcome, time_horizon]
constraints: [framework fields must be instantiated or marked unknown]
```

## Procedure

1. Select the framework matching the question type.
2. Map the question into its required fields.
3. Mark missing, ambiguous, and non-applicable fields.
4. Emit the structured question and scope decisions.

## Output contract

```yaml
produces: [structured_question, field_map, missing_fields, scope_decisions]
delta_fields: [findings, decisions, uncertainties, open_questions]
```

## Quality gates

- Every populated field traces to the input question or context.
- Framework choice is justified.

## Failure and counterexamples

Do not force a causal question into a descriptive framework or fill absent fields from convention.

## Provenance map

- `resolved: apply-question-framework`

