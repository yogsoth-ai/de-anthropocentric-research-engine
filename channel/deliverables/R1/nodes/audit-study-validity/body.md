# audit-study-validity

## Purpose

Audit a study against an appropriate methodological-quality and risk-of-bias rubric and return domain judgments with evidence and confidence.

## Input contract

```yaml
required: [study_record, validity_rubric]
optional: [protocol, analysis_plan, supplementary_materials]
constraints: [rubric applicability and judgment rationale must be explicit]
```

## Procedure

1. Select and scope the rubric for the study design.
2. Judge each domain from reported methods and supporting material.
3. Record signaling evidence, uncertainty, and direction of likely bias.
4. Aggregate domain judgments without hiding critical domain failures.

## Output contract

```yaml
produces: [domain_judgments, risk_of_bias_profile, evidence_basis, overall_confidence, applicability_notes]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- No overall label is emitted without domain-level evidence.
- Rubric choice and missing-data handling are recorded.

## Failure and counterexamples

Do not average incompatible domains into a false precision score or treat unreported methods as low risk.

## Provenance map

- `resolved: knowledge-acquisition-quality-assessment`
- `resolved: knowledge-acquisition-risk-of-bias-assessment`
- `resolved: knowledge-acquisition-quality-assessment-protocol`
- `intermediate: Pass3/assess-study-quality`
- `intermediate: Pass3/assess-risk-of-bias`

