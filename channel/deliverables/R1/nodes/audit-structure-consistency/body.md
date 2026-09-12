# audit-structure-consistency

## Purpose

Audit whether a concept, argument, or graph preserves its declared structural relations and constraints.

## Input contract

```yaml
required: [structure, relation_schema, consistency_rules]
optional: [source_structure, version_history, exception_rules]
constraints: [each inconsistency identifies nodes, relation, and violated rule]
```

## Procedure

1. Validate node types, relation types, direction, and required fields.
2. Check hierarchy, dependency, cardinality, and cycle constraints.
3. Compare versions or source structure where supplied.
4. Emit inconsistencies, valid exceptions, and repair questions.

## Output contract

```yaml
produces: [consistency_report, violated_rules, valid_exceptions, repair_questions]
delta_fields: [findings, uncertainties, open_questions]
```

## Quality gates

- Rules and exception policy are declared before checking.
- Structural validity is separated from semantic truth.

## Failure and counterexamples

Do not repair a graph silently or call a semantically weak structure consistent merely because it parses.

## Provenance map

- `resolved: audit-structure-consistency`

