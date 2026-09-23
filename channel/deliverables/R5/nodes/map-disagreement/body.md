# map-disagreement

## Purpose

Represent where perspectives or arguments agree, disagree, and why.

## Input contract

```yaml
required: [perspectives, claims_or_arguments, comparison_dimensions]
optional: [evidence, clustering_rule, convergence_measure]
constraints: [agreement and disagreement are tied to the same proposition and comparison dimension; preserve minority positions]
```

## Procedure

1. Normalize perspectives, propositions, and evidence.
2. Cluster equivalent positions and separate agreement from disagreement.
3. Attribute each disagreement to evidence, assumptions, scope, values, or definitions.
4. Report convergence trends and unresolved fault lines.

## Output contract

```yaml
produces: [agreement_map, disagreement_register, cluster_arguments, convergence_trends]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Preserve source thresholds when the divergence mode applies: consensus >70% and disagreement >50%.
- The map includes reasons and evidence for each fault line; percentages describe the supplied perspective set, not population truth.
- Collection, clustering, argument extraction, and visualization remain separable outputs.

## Parameterization

The caller must provide perspective schema, proposition identity, comparison dimensions, agreement rule, disagreement rule, evidence links, and the population represented by any percentages.

## Failure and counterexamples

Reject comparisons across different propositions or scopes, and reject consensus claims when the denominator of perspectives is absent.

## Provenance map

- resolved: convergence/disagreement-mapping
- resolved: stress-test/divergence-detection

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| stress-test/divergence-detection | 14 | percentage | Consensus is >70%; disagreement is >50%; identify convergence trends. |

