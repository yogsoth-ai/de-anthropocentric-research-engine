# derive-consequences
## Purpose
Trace valid consequences from an altered premise, provocation, or negated claim.
## Input contract
```yaml
required: [premise_change, base_model, inference_rules]
optional: [time_horizon, boundary_conditions, contradiction_policy]
constraints: [each consequence links to an explicit inference step]
```
## Procedure
1. State the altered premise and preserve unaffected assumptions.
2. Apply inference rules stepwise, recording intermediates and branches.
3. Mark contradictions, uncertainty, and boundary violations.
4. Return consequences with dependency paths and testable implications.
## Output contract
```yaml
produces: [consequence_chain, intermediate_steps, contradictions, testable_implications]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- No endpoint is emitted without its intermediate derivation.
- Premise changes are distinguished from downstream assumptions.
- Contradictory branches are retained and labeled.
## Parameterization
Caller supplies premise schema, model graph, inference calculus, depth limit, and contradiction policy.
## Failure and counterexamples
Reject leaps that omit mechanisms, circular derivations, or consequences outside declared scope.
## Provenance map
- concept: stress-test/deductive-chain
- concept: deep-insight/consequence-following
