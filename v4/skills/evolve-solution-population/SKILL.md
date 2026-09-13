---
name: evolve-solution-population
description: "Maintain a diverse population of candidate solutions, mutate/recombine variants, select under explicit fitness and novelty criteria, and iterate while preserving useful niches rather than collapsing prematurely to one winner."
---

# evolve-solution-population
## Purpose
Maintain diverse candidate solutions, mutate/recombine them, select under fitness and novelty criteria, and avoid premature convergence.
## Input contract
```yaml
mode_contracts:
  mutation-selection: &evolution_input
    required: [initial_solution_population, fitness_criteria]
    optional: [mutation_operators, novelty_criteria, iteration_budget]
    constraints: [population_members_must_be_comparable_under_declared_criteria]
  novelty-preserving-evolution: *evolution_input
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
mode_contracts:
  mutation-selection: &evolution_output
    produces: [evolved_population, selected_variants, diversity_report, sensitivity_report]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
  novelty-preserving-evolution: *evolution_output
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
