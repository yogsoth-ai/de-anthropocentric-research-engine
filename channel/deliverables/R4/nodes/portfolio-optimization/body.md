# portfolio-optimization

## Purpose

Formalize objectives/constraints, construct a Pareto frontier, stress across scenarios, and select a robust portfolio.

## Input contract

~~~yaml
required: [source_state, task_object]
optional: [constraints, prior_evidence]
constraints: [typed inputs, provenance-bearing evidence, explicit uncertainty]
~~~

## Execution protocol

1. Apply `define-objective` and record its typed result.
2. Apply `optimize-pareto-frontier` and record its typed result.
3. Apply `construct-scenario` and record its typed result.
4. Apply `evaluate-scenario-impact` and record its typed result.
5. Apply `select-from-frontier` and record its typed result.
6. Apply `measure-portfolio-diversity` and record its typed result.
7. Apply `map-dependencies` and record its typed result.
8. Apply `sequence-work` and record its typed result.
9. Apply `evaluate-optionality` and record its typed result.
10. Apply `evaluate-scenario-robustness` and record its typed result.

Deviation: Skip a step only when its artifact is already present or the decision objective excludes it; record the reason and uncertainty.

## Output contract

~~~yaml
produces: [analysis_artifact, decision_rationale]
delta_fields: [findings, evidence_updates, hypothesis_updates, assumption_updates, uncertainties, decisions, open_questions, recommended_jumps]
~~~

## Thresholds and quality gates

- Tie each conclusion to evidence, assumptions, or uncertainty.
- Coverage gates declare universe, numerator, denominator, batch increment, stopping reason, and source references.
- Fixed statistical values remain fixed where applicable, including α 0.05 and power 0.8.

## Failure and counterexamples

Reject unsupported, circular, untyped, or out-of-scope conclusions; preserve counterexamples.

## Provenance map

- concept: portfolio-optimization <- portfolio-optimization [campaign]
- concept: value-maximization <- value-maximization [strategy]
- concept: diversity-maximization <- diversity-maximization [strategy]
- concept: risk-balancing <- risk-balancing [strategy]
- concept: temporal-sequencing <- temporal-sequencing [strategy]
- concept: robustness-under-uncertainty <- robustness-under-uncertainty [strategy]
- concept: pareto-frontier-construction <- pareto-frontier-construction [tactic]
- concept: scenario-stress-testing <- scenario-stress-testing [tactic]
- concept: niche-coverage-analysis <- niche-coverage-analysis [tactic]

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| v3 refactory source | n/a | textual | Exact normalized provenance retained; unresolved entries remain marked. |

## Context checkpoint / Delta notes

Append artifacts, evidence updates, assumptions, uncertainties, decisions, open questions, and recommended jumps.
