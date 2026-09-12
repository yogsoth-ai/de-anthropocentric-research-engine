---
name: parse-patent-claim
description: "Parse independent/dependent claim structure, extract elements, and map claim features to technical functions/domains."
---

# parse-patent-claim

## Purpose

Parse independent and dependent claim structure, extract elements, and map claim features to technical functions or domains.

## Input contract

```yaml
required: [claim_text, claim_set]
optional: [technical_ontology, family_context, jurisdiction]
constraints: [element boundaries, dependency links, and source spans must be retained]
```

## Procedure

1. Identify independent claims and dependency relations.
2. Segment each claim into required elements, limitations, and functional language.
3. Map elements to technical functions and preserve alternative interpretations.
4. Emit a source-linked claim-element graph.

## Output contract

```yaml
produces: [claim_element_map, dependency_graph, function_map, interpretation_alternatives]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Every element points to a claim span.
- Dependency and optionality are not conflated.

## Failure and counterexamples

Do not paraphrase away limiting language or treat a dependent claim as independent coverage.

## Provenance map

- `resolved: claim-parsing`
- `resolved: knowledge-acquisition-claim-decomposition`
