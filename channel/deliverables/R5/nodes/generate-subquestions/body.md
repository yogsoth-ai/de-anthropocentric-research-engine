# generate-subquestions
## Purpose
Decompose a research question into MECE subquestions with coverage and independence arguments.
## Input contract
```yaml
required: [main_research_question, scope_statement]
optional: [evidence_map, dependency_constraints, desired_granularity]
constraints: [question must be scoped and complex enough to decompose]
```
## Procedure
1. Parse the main question into objects, mechanisms, conditions, and outcomes.
2. Generate candidate subquestions and assign coverage domains.
3. Remove overlap, test independence, and map dependencies.
4. Return the MECE set with unresolved gaps.
## Output contract
```yaml
produces: [subquestion_set, coverage_map, independence_arguments, dependency_notes]
delta_fields: [findings, open_questions, uncertainties]
```
## Quality gates
- Input contains one confirmed, appropriately scoped main question.
- Every subquestion maps to a distinct coverage domain.
- Overlap and uncovered regions are explicitly reported.
## Parameterization
Caller supplies question schema, scope test, MECE policy, granularity, and dependency representation.
## Failure and counterexamples
Reject decompositions that merely restate the main question or leave domains without a coverage rationale.
## Provenance map
- concept: hypothesis-formation/sub-question-generation
