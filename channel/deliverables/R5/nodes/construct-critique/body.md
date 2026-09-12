# construct-critique

## Purpose

Construct the strongest structured attack on a claim or artifact from an explicit perspective, grounded in reasons and evidence.

## Input contract

```yaml
required: [target_claim_or_artifact, critique_perspective, evidence_set]
optional: [argument_schema, known_assumptions, decision_context]
constraints: [separate claim, ground, warrant, rebuttal, and severity; critique must target the supplied artifact]
```

## Procedure

1. State the target claim and its intended scope.
2. Generate attacks from the supplied perspective using the argument schema.
3. Attach evidence and classify each attack as formal, empirical, scope, or implementation-related.
4. Rank severity, identify the strongest-point attack, and return rebuttal requirements.

## Output contract

```yaml
produces: [critique_set, evidence_links, severity_labels, strongest_attack, rebuttal_requirements]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates

- In critic-attack mode, produce at least 3 attacks, label each HIGH/MEDIUM/LOW, attach evidence, and include at least 1 attack against the strongest point.
- Toulmin critiques preserve claim, ground, warrant, and rebuttal fields.
- Perspective changes the attack lens, not the target claim or evidence standard.

## Parameterization

The caller must provide target schema, critique perspective(s), evidence set, argument model, severity scale, and whether the task is debate, convergence, or perspective review.

## Failure and counterexamples

Reject attacks that merely restate disagreement without a reason or evidence, and reject severity labels without a stated scale.

## Provenance map

- resolved: stress-test/debate-critic
- resolved: convergence/critic-attack
- resolved: stress-test/perspective-critic

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| convergence/critic-attack | 27 | numeric/gate | Must produce ≥3 attacks, each with HIGH/MEDIUM/LOW severity and evidence, including at least 1 attack against the strongest point. |

