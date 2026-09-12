# evaluate-compatibility

## Purpose

Evaluate logical, empirical, and normative compatibility of a candidate combination and prune invalid regions.

## Input contract

```yaml
required: [candidate_combination, component_schema, compatibility_rules, evidence]
optional: [matrix, consistency_judgments, feasibility_criteria, novelty_criteria]
constraints: [each incompatibility is tied to an explicit rule or evidence item; preserve distinct logical, empirical, and normative judgments]
```

## Procedure

1. Normalize the combination and component schemas.
2. Apply each compatibility rule pairwise and at the full-combination level.
3. Record conflicts, supporting evidence, and unresolved judgments.
4. Prune only combinations that violate an explicit rule; retain near-boundary cases with rationale.
5. Return surviving combinations and a compatibility report.

## Output contract

```yaml
produces: [surviving_combinations, incompatibility_register, compatibility_judgments, pruning_rationale]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Every removed combination has an explicit incompatible pair or rule.
- CCA-style reduction covers the supplied matrix and consistency judgments; feasibility and novelty are reported separately when requested.
- No hidden veto or unstated preference is introduced during pruning.

## Parameterization

The caller must provide component/object schemas, the combination representation, compatibility dimensions and rules, evidence for each judgment, and whether the decision is logical, empirical, normative, or mixed. If CCA is used, provide the full matrix and pairwise consistency judgments.

## Failure and counterexamples

Reject when compatibility rules are absent, evidence is untraceable, or a normative preference is presented as a logical contradiction. Do not remove a combination solely because it is unfamiliar.

## Provenance map

- concept: creative-ideation/consistency-pair-evaluation
- resolved: creative-ideation/solution-space-reduction
- resolved: creative-ideation/combination-evaluation

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| creative-ideation/solution-space-reduction | 11 | gate | Apply CCA to remove inconsistent combinations from the supplied matrix using consistency judgments. |
| creative-ideation/combination-evaluation | 11 | gate | Evaluate proposed combinations for feasibility, novelty, and implementation difficulty. |

