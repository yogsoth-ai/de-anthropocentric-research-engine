# trace-causal-chain
## Purpose
Trace ordered causal chains with intermediate nodes, branches, loops, mechanisms, and boundary conditions.
## Input contract
```yaml
required: [causal_question, evidence_set, chain_granularity]
optional: [candidate_graph, time_order, loop_policy]
constraints: [every edge has a because/mechanism statement]
```
## Procedure
1. Identify start and endpoint variables from the question.
2. Expand intermediate mediators and mechanism links.
3. Mark branches, feedback loops, temporal order, and unsupported edges.
4. Return complete chains with evidence and boundary conditions.
## Output contract
```yaml
produces: [causal_chains, intermediate_nodes, branch_loop_map, evidence_links, boundary_conditions]
delta_fields: [findings, hypothesis_updates, uncertainties]
```
## Quality gates
- Full chains, not endpoints alone, are reported.
- Each edge has an explicit mechanism or is labeled unresolved.
- Loops and alternative paths are retained rather than flattened.
## Parameterization
Caller supplies variable schema, evidence-link schema, granularity, temporal semantics, and loop policy.
## Failure and counterexamples
Reject endpoint-only summaries, circular edges without loop evidence, or implied mechanisms.
## Provenance map
- concept: knowledge-structuring/causal-chain-query
- concept: experiment-execution/causal-chain-tracing
