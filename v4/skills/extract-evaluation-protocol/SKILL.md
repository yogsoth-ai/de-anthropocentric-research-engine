---
name: extract-evaluation-protocol
description: "Extract evaluation-protocol elements from a source and mark unstated or ambiguous parameters."
---

# extract-evaluation-protocol

## Purpose

Extract evaluation-protocol elements from a source and mark unstated or ambiguous parameters.

## Input contract

```yaml
required: [source_record, protocol_schema]
optional: [supplementary_materials, domain_defaults]
constraints: [extracted values must distinguish stated, inferred, and missing]
```

## Procedure

1. Parse task, data, split, metric, baseline, budget, evaluator, and reporting elements.
2. Link each value to a source passage or record field.
3. Mark ambiguity, omission, and any inference made from context.
4. Emit a normalized protocol record with comparability notes.

## Output contract

```yaml
produces: [protocol_record, source_links, ambiguity_log, comparability_notes]
delta_fields: [evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Missing fields are explicit.
- Inferred defaults are never represented as stated facts.

## Failure and counterexamples

Do not fill omitted protocol values from common practice without an inference label.

## Provenance map

- `resolved: protocol-element-extraction`
