# adjust-abstraction-scope

## Purpose
Move a scientific object up or down in abstraction, or narrow/broaden scope dimensions, until explanatory and experimental leverage improve.

## Input contract
```yaml
required: [research_object, current_scope, leverage_failure]
optional: [candidate_levels, context_constraints, target_use]
constraints: [retain object identity; change representation or declared scope explicitly]
```

## Procedure
1. Record object, current level, and scope dimensions (population, mechanism, context, outcome, timeframe, boundary).
2. Generate at least one upward and one downward abstraction candidate when leverage is unclear.
3. For each candidate, state what is gained, lost, and newly testable.
4. Select the narrowest or broadest level that supports the caller's stated use and record rationale.

## Output contract
```yaml
produces: [scoped_representations, selected_scope, leverage_rationale]
delta_fields: [findings, decisions, uncertainties]
```

## Quality gates
- Object identity is invariant across representations.
- Every changed dimension is named with before/after values.
- Selected scope has an explicit explanatory or experimental leverage claim.

## Parameterization
Caller supplies object schema, allowed abstraction dimensions, admissible scope bounds, target use, and selection rule.

## Failure and counterexamples
Reject a level that changes the object while appearing to change only scope; reject scope changes with no stated leverage test.

## Provenance map
- resolved: abstraction-laddering
- resolved: scope-assessment
- intermediate: question-reformulation
- intermediate: scope-calibration
- intermediate: Pass8/shift-abstraction-level
- intermediate: Pass8/adjust-question-scope

