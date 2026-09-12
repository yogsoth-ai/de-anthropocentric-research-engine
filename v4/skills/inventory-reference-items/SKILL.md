---
name: inventory-reference-items
description: "Build a structured inventory of externally established reference items under a parent-specified schema, preserving applicability/status, key attributes, limitations, and provenance. Typical schemas include benchmark or known-solution/method family."
---

# inventory-reference-items

## Purpose

Build a structured inventory of externally established reference items under a caller-specified schema.

## Input contract

```yaml
required: [reference_items, item_schema, applicability_rules]
optional: [known_solutions, benchmarks, source_scope, status_vocabulary]
constraints: [preserve applicability, status, limitations, key attributes, and provenance for every item]
```

## Procedure

1. Define the eligible reference universe and normalize item identifiers.
2. Extract schema fields, applicability, status, limitations, and provenance.
3. Deduplicate items without merging distinct benchmarks or methods.
4. Return the inventory with exclusions and unresolved provenance.

## Output contract

```yaml
produces: [reference_inventory, applicability_map, limitation_register, provenance_index]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- Every item has a stable identifier, source reference, applicability status, and limitation note.
- Benchmark and known-solution inventories remain schema-distinct when their fields differ.
- Missing fields are explicit; no benchmark or solution is inferred from a similar name.

## Parameterization

The caller must provide item type, schema, eligible source scope, inclusion/status rules, canonical identifier policy, and required provenance fields.

## Failure and counterexamples

Reject inventory entries with no provenance, mixed item types under one schema, or deduplication that removes a distinct reference item.

## Provenance map

- concept: knowledge-acquisition/benchmark-inventory
- intermediate: Pass4/inventory-benchmarks
- concept: creative-ideation/benchmark-inventory
- intermediate: Pass4/inventory-known-solutions

## Preserved source criteria ledger

No resolved v3 source node was present for these four entries; they remain explicitly marked concept/intermediate and are not replaced by a similarly named inventory.

