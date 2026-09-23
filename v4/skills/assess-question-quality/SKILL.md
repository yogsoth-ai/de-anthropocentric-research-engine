---
name: assess-question-quality
description: "Audit a research question for scope and FINER-style quality; return targeted repairs."
---

# assess-question-quality

## Purpose

Assess whether a research question is clear, focused, answerable, relevant, and appropriately scoped.

## Input contract

```yaml
required: [research_question, intended_use]
optional: [constraints, evidence_context, stakeholder_needs]
constraints: [each quality judgment requires a criterion and textual evidence]
```

## Procedure

1. Evaluate clarity, focus, answerability, relevance, and scope fit.
2. Identify ambiguity, hidden assumptions, and unbounded terms.
3. Propose the smallest wording changes that resolve material defects.
4. Return a scored or categorical assessment with unresolved issues.

## Output contract

```yaml
produces: [quality_assessment, criterion_evidence, revision_candidates, unresolved_issues]
delta_fields: [findings, decisions, uncertainties, open_questions]
```

## Quality gates

- Judgments cite exact question terms.
- Revision candidates preserve the intended decision or outcome.

## Failure and counterexamples

Do not reward complexity as rigor or call a question answerable when its outcome cannot be observed.

## Provenance map

- `resolved: assess-question-quality`

