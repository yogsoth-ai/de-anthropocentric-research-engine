---
name: construct-argument-map
description: "Atomize claims, expose premises and counterclaims, attach evidence/defeaters, score claim strength, and construct an inspectable argument graph independent of storage format."
---

# construct-argument-map

## Purpose

Atomize claims, expose premises and counterclaims, attach evidence/defeaters, score claim strength, and construct an inspectable argument graph independent of storage format.

## Input contract

```yaml
required: [claim_records, premise_records, evidence_records]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `atomize-claim` to split compound claims into atomic propositions.
2. You MUST load skill `surface-assumptions` to register explicit and implicit load-bearing assumptions.
3. You MUST load skill `attach-evidence-to-relation` to link source records to typed relations with directness, independence, consistency, and alternative interpretations.
4. You MUST load skill `document-counterclaim` to add credible counterclaims with their basis, scope, implications, and possible rebuttals.
5. You MUST load skill `score-object` to score each typed object against the supplied rubric without inventing missing evidence.
6. You MUST load skill `construct-critique` to attack the assembled argument and rank its strongest weakness.
7. You MUST load skill `detect-contradiction` to compare opposing claims under shared scope and record the evidence needed to adjudicate them.
   If the argument requires a balanced attack-defense exchange, consider `adversarial-deliberation`. If its apparent simplicity may hide unsupported relabeling, consider `audit-explanatory-compression`.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [argument_graph, evidence_links, counterclaims, strength_assessment]
delta_fields: [evidence_updates]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: knowledge-structuring/argument-mapping [campaign]
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
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
