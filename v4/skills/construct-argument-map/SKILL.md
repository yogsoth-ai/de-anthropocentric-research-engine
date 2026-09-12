---
name: construct-argument-map
description: "Atomize claims, expose premises and counterclaims, attach evidence/defeaters, score claim strength, and construct an inspectable argument graph independent of storage format."
---

# construct-argument-map

## Purpose

Atomize claims, expose premises and counterclaims, attach evidence/defeaters, score claim strength, and construct an inspectable argument graph independent of storage format.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Split compound claims into atomic propositions so every later relation can receive its own evidence and confidence judgment. (`atomize-claim`)
2. Register explicit and implicit assumptions, especially those whose failure would change the conclusion. (`surface-assumptions`)
3. Link source records to typed relations with directness, independence, consistency, and alternative-interpretation metadata. (`attach-evidence-to-relation`)
4. Add credible counterclaims with their supporting basis, scope, implications, and possible rebuttals. (`document-counterclaim`)
5. Score each typed object against the caller’s rubric without filling missing evidence with an unstated default. (`score-object`)
6. Attack the assembled argument from the supplied perspective and rank the strongest formal, empirical, scope, or implementation weakness. (`construct-critique`)
7. Compare opposing claims under shared scope, classify contradictions, and record the evidence needed to adjudicate them. (`detect-contradiction`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [argument_graph, evidence_links, counterclaims, strength_assessment]
delta_fields: [findings, evidence_updates]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: argument-mapping
- resolved: claim-extraction
- intermediate: premise-identification [strategy]
- intermediate: counterargument-mapping [strategy]
- resolved: evidence-linking-arg
- resolved: argument-synthesis
- intermediate: claim-decomposition [tactic]
- resolved: strength-assessment

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
