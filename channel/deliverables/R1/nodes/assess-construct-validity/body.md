# assess-construct-validity

## Purpose

Assess whether a benchmark or evaluation construct measures the claimed capability rather than content cues, confounds, or unrelated skill.

## Input contract

```yaml
required: [construct_claim, benchmark_specification, evaluation_records]
optional: [content_analysis, convergent_measures, discriminant_measures, confound_hypotheses]
constraints: [each validity judgment requires an observable indicator, comparison basis, and provenance]
```

## Procedure

1. State the target construct and map benchmark tasks, labels, and metrics to its intended components.
2. Check content coverage and plausible construct-irrelevant cues against the benchmark specification.
3. Compare convergent and discriminant evidence where available, preserving missing comparisons.
4. Test confound hypotheses with controlled contrasts or artifact probes and record residual uncertainty.

## Output contract

```yaml
produces: [construct_map, content_validity_assessment, convergent_discriminant_evidence, confound_report, validity_judgment]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Every validity claim cites a task, measure, contrast, or artifact observation.
- Content coverage, convergence, discrimination, and confounds are reported separately.
- A missing diagnostic is marked unresolved rather than treated as evidence of validity.

## Failure and counterexamples

Do not infer construct validity from a high score, face validity, or agreement with another measure that shares the same confound.

## Provenance map

- `concept: knowledge-acquisition/construct-validity-assessment`

