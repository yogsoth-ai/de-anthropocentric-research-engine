---
name: challenge-assumption
description: "Construct a strong countercase or alternative to an assumption and assess consequence if it fails."
---

# challenge-assumption

## Purpose
Construct a strong countercase or alternative to an assumption and assess the consequence if it fails.

## Input contract
```yaml
required: [assumption, claim_or_decision, supporting_evidence]
optional: [alternative_worlds, dependency_graph, challenge_mode]
constraints: [separate assumption, countercase, evidence, and impact]
```

## Procedure
1. State the assumption's role and dependencies in the target claim.
2. Build the strongest evidence-backed countercase and at least one alternative assumption.
3. Propagate consequences through dependent claims and identify discriminating observations.
4. Rate threat severity and confidence using the caller's scale.

## Output contract
```yaml
produces: [countercase, alternative_assumptions, consequence_analysis, discriminating_tests]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates
- Countercase attacks the assumption's strongest support, not a weak proxy.
- At least one alternative assumption and one impact path are explicit.
- Confidence distinguishes empirical threat from theoretical possibility.

## Parameterization
Caller supplies assumption schema, evidence standard, challenge mode, consequence model, severity/confidence scales, and test budget.

## Failure and counterexamples
Reject a challenge that merely negates the assumption without mechanism or evidence.

## Provenance map
- concept: convergence/assumption-challenge
- resolved: benchmark-challenge
- resolved: counter-assumption-generation
