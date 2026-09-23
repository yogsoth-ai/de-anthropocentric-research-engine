# define-evidence-protocol

## Purpose

Define research questions, eligible evidence scope, query concepts, inclusion/exclusion rules, provenance requirements, and stopping evidence.

## Input contract

```yaml
required: [research_question, evidence_scope, inclusion_rules]
optional: [exclusion_rules, query_concepts, quality_rubric, stopping_policy]
constraints: [eligible universe, provenance fields, and stopping evidence must be explicit]
```

## Procedure

1. State the question, target population or domain, comparison, outcomes, and time boundaries.
2. Define eligible evidence, exclusion rules, source-independence requirements, and extraction fields.
3. Specify batch boundaries, novelty dimensions, and relative stopping evidence.
4. Record unresolved scope choices before acquisition begins.

## Output contract

```yaml
produces: [evidence_protocol, eligible_universe, query_concepts, screening_rules, provenance_requirements, stopping_evidence]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- The eligible universe and exclusion rules are operational.
- Stopping evidence names numerator, denominator, batch increment, source references, direction, threshold, and rationale when relative quantities apply.

## Failure and counterexamples

Do not use provider names as a protocol, and do not declare coverage from search volume without a defined eligible universe.

## Provenance map

- `resolved: define-search-protocol`
- `resolved: inclusion-criteria-design`
