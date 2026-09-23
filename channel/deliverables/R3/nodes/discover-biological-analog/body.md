# discover-biological-analog
## Purpose
Identify biological systems that achieve a target function under comparable constraints.
## Input contract
```yaml
required: [biological_function, biological_constraints]
optional: [search_terms, candidate_taxa, environment]
constraints: [candidate must demonstrate the function, not merely resemble the target]
```
## Procedure
1. Search across organism, process, and ecosystem levels using the function formulation.
2. Verify the candidate's observed function and environmental constraints.
3. Rank candidates by mechanism evidence and transfer relevance.
## Output contract
```yaml
produces: [biological_candidate_set, function_evidence, relevance_ranking]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```
## Quality gates
- Each candidate has function evidence, constraint match, and a stated uncertainty; surface similarity is not a ranking criterion.
## Failure and counterexamples
Exclude candidates supported only by analogy language, stock imagery, or incompatible conditions.
## Provenance map
- `biomimicry/discover`: concept (no exact pool entry).
- `biological-analogy`: concept (no exact pool entry).
