---
name: assess-patent-claim-scope
description: "Assess protection breadth, limiting elements, support, overlap, design-around vulnerability, and likely scope uncertainty for a patent claim without making legal conclusions beyond the evidence."
---

# assess-patent-claim-scope

## Purpose

Assess claim breadth, limiting elements, support, overlap, design-around vulnerability, and scope uncertainty without making a legal conclusion beyond the evidence.

## Input contract

```yaml
required: [parsed_claim, cited_support, jurisdiction_scope]
optional: [related_claims, family_map, prior_art_records]
constraints: [each scope judgment must identify claim language, support, jurisdiction, and uncertainty]
```

## Procedure

1. Separate mandatory, optional, functional, and contextual claim elements.
2. Map each element to disclosed support and identify limiting combinations.
3. Compare overlap and distinction against related claims and declared prior-art records.
4. Record design-around paths and unresolved interpretation questions.

## Output contract

```yaml
produces: [element_scope_map, support_map, overlap_assessment, design_around_options, scope_uncertainties]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Mandatory elements and jurisdiction are explicit.
- Overlap claims cite the compared claim language.
- Unclear terms remain uncertainty markers.

## Failure and counterexamples

Do not infer broad protection from a title or abstract, and do not treat technical similarity as claim overlap.

## Provenance map

- `resolved: knowledge-acquisition-claim-analysis`
- `resolved: quality-scoring`
