# identify-shared-priors
## Purpose
Trace supposedly independent paths to shared priors, datasets, models, prompts, framings, assumptions, or upstream sources.
## Input contract
```yaml
required: [evidence_paths, provenance_records]
optional: [prompt_records, model_records, upstream_sources]
constraints: [shared dependency identity and path membership must be explicit]
```
## Procedure
1. Inventory each path's inputs and assumptions.
2. Match shared priors, data, models, prompts, framing, and upstream evidence.
3. Produce dependency clusters and unresolved provenance.
## Output contract
```yaml
produces: [shared_prior_map, dependency_clusters, unresolved_links]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```
## Quality gates
- Similar conclusions alone are not evidence of shared priors; trace the dependency.
## Failure and counterexamples
Mark provenance unknown rather than inferring common origin from naming similarity.
## Provenance map
- resolved: independent-convergence-audit
