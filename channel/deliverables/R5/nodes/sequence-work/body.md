# sequence-work
## Purpose
Topologically sequence dependent work while prioritizing fail-fast and high-risk branches.
## Input contract
```yaml
required: [work_items, dependency_graph, prioritization_policy]
optional: [resource_limits, risk_scores, parallelism_rules]
constraints: [dependencies must be acyclic or cycles explicitly reported]
```
## Procedure
1. Validate nodes and dependency edges.
2. Detect cycles and compute available roots.
3. Rank ready items by fail-fast, risk, and policy priorities.
4. Emit ordered batches and parallelizable branches.
## Output contract
```yaml
produces: [work_sequence, parallel_batches, cycle_report, priority_rationale]
delta_fields: [decisions, uncertainties, open_questions]
```
## Quality gates
- Input contains a subquestion list and dependency graph.
- No item precedes an unmet prerequisite.
- Every priority change has a stated policy reason.
## Parameterization
Caller supplies work schema, dependency semantics, priority policy, cycle handling, and resource constraints.
## Failure and counterexamples
Reject sequences that hide cycles, violate prerequisites, or claim parallelism across dependent items.
## Provenance map
- concept: hypothesis-formation/answering-sequence-design
