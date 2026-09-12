# evolve-solution-population
## Purpose
Maintain diverse candidate solutions, mutate/recombine them, select under fitness and novelty criteria, and avoid premature convergence.
## Input contract
```yaml
required: [initial_solution_population, fitness_criteria]
optional: [mutation_operators, novelty_criteria, iteration_budget]
constraints: [population members must be comparable under declared criteria]
```
## Execution protocol
1. Mutate or recombine the population (`mutate-solution-population`).
2. Select solution variants (`select-solution-variants`).
3. Measure portfolio diversity (`measure-portfolio-diversity`).
4. Assess sensitivity (`assess-sensitivity`).
5. Synthesize the retained set (`synthesize-idea`).
Deviation: stop when added variation no longer changes the frontier or diversity objective; retain niche candidates when explicitly protected.
## Mode branches
- `mutation-selection`: mutate/recombine, score, and select across iterations.
- `novelty-preserving-evolution`: apply diversity pressure and protect useful niches before convergence.
## Output contract
```yaml
produces: [evolved_population, selected_variants, diversity_report, sensitivity_report]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: mutation/recombination lineage is traceable; selection criteria are explicit; diversity is measured before convergence.
## Failure and counterexamples
Reject a single-winner result when novelty or niche preservation was required, and reject variants with untracked mutations.
## Provenance map
- `creative-ideation/systematic-enumeration`, `evolution-strategy`, `variation-selection`: resolved/concept according to exact v3 lookup.
- Status: `creative-ideation/systematic-enumeration`, `evolution-strategy` resolved; `variation-selection` concept.
## Preserved source criteria ledger
- Preserve mutation, recombination, selection, diversity pressure, and niche preservation.
## Context checkpoint / Delta notes
Append population lineage, fitness changes, diversity deltas, and retained niches.
