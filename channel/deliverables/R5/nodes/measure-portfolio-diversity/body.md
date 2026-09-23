# measure-portfolio-diversity
## Purpose
Quantify portfolio diversity and coverage across declared feature, mechanism, domain, or failure-mode dimensions.
## Input contract
```yaml
required: [portfolio, diversity_dimensions, feature_assignments]
optional: [niche_universe, strength_threshold, concentration_measure]
constraints: [niche definitions and distance/overlap rules are explicit]
```
## Procedure
1. Define niches and assign each portfolio member to them.
2. Compute coverage, concentration, and duplication using the supplied measure.
3. Identify empty niches and collapse risks.
4. Return diversity results with sensitivity to assignment uncertainty.
## Output contract
```yaml
produces: [diversity_metrics, niche_coverage, concentration_risks, empty_niches]
delta_fields: [findings, uncertainties, decisions]
```
## Quality gates
- Coverage is reported as a fraction of a declared niche universe.
- A caller-supplied strong-candidate threshold is applied consistently.
- Concentration and niche collapse are disclosed, not hidden by aggregate diversity.
## Parameterization
Caller supplies portfolio schema, niche universe, assignment rules, strength threshold, and concentration metric.
## Failure and counterexamples
Reject diversity scores without niche definitions or portfolios assessed on incompatible dimensions.
## Provenance map
- concept: convergence/diversity-maximization
- concept: convergence/niche-coverage-analysis
## Preserved source criteria ledger
| source | criterion |
|---|---|
| convergence/diversity-maximization | Coverage threshold may be caller-supplied; preserve declared threshold verbatim. |
