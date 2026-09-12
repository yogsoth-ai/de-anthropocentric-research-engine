# construct-argument-map

## Purpose

Coordinate construct argument map with explicit dependencies, evidence, uncertainty, and decision boundaries.

## Input contract

```yaml
required: [research_object, evidence_records, decision_objective]
optional: [constraints, prior_artifacts, uncertainty_register]
constraints: [typed fields, traceable provenance, no unsupported post hoc changes]
```

## Execution protocol

1. Freeze the declared inputs and establish the decision target. (`atomize-claim`)
2. Transform the current artifact while preserving its provenance and uncertainty. (`attach-evidence-to-relation`)
3. Transform the current artifact while preserving its provenance and uncertainty. (`document-counterclaim`)
4. Integrate the preceding artifacts and state the stopping rationale. (`detect-contradiction`)

Deviation: Skip only a step whose artifact is already present or outside the declared objective; record the reason and residual uncertainty.

## Output contract

```yaml
produces: [structured_artifact, decision_record]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Thresholds and quality gates

- Every claim is linked to evidence or a named assumption.
- Coverage gates state universe, numerator, denominator, batch increment, stopping reason, and source references.
- Statistical nodes retain fixed α 0.05 and power 0.8 where applicable.
- Stop only when the declared decision criterion is met or an unresolved blocker is recorded.

## Failure and counterexamples

Preserve contradictory evidence, null results, boundary cases, and out-of-scope inputs; do not silently convert them into support.

## Provenance map

- resolved: construct-argument-map <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: construct/argument/map <- architecture semantic consolidation

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory_source.json | nodes[].name | textual | Preserve source transformation and its stated decision boundaries. |

## Context checkpoint / Delta notes

Append findings, evidence updates, uncertainties, decisions, and recommended jumps.
