---
name: cross-consistency-filtering
description: "Orchestrates pairwise consistency evaluation and narrative construction to filter the morphological field"
version: 1.0.0
category: experiment-execution
type: tactic
used-by: scenario-planning
orchestrates:
  - consistency-pair-evaluation
  - scenario-narrative-construction
---

# Tactic: Cross-Consistency Filtering

## Orchestration Pattern

1. **Spawn consistency evaluation** → `consistency-pair-evaluation`
   - Pass: Zwicky Box (full parameter space), evaluation criteria
   - Receive: CCA matrix with pairwise consistency scores

2. **Apply filtering rules**
   - Mark configurations with ANY inconsistent pair as eliminated
   - Mark configurations with conditionally consistent pairs as flagged
   - Retain configurations with all-consistent pairs as primary scenarios
   - If too few survive (< 3): relax to include conditionally consistent configs
   - If too many survive (> 10): tighten criteria or select representative subset

3. **Rank surviving configurations**
   - Score by: total consistency score (sum of pairwise ratings)
   - Score by: diversity (maximize coverage of parameter space)
   - Score by: relevance (proximity to current trajectory)
   - Select top N (typically 4-8) for narrative construction

4. **Spawn narrative construction** → `scenario-narrative-construction` (per selected config)
   - Pass: parameter configuration, consistency context, research approach
   - Receive: rich scenario narrative

5. **Validate narratives**
   - Check: Does narrative honor all parameter values in the configuration?
   - Check: Is the causal logic internally consistent?
   - Check: Is the scenario distinguishable from others?
   - If validation fails: re-spawn with specific correction guidance

## Quality Checks

- [ ] CCA matrix is complete (all pairs evaluated)
- [ ] Filtering produces 3-8 surviving configurations
- [ ] Surviving configs span the parameter space (not clustered)
- [ ] Each narrative is internally consistent with its configuration
- [ ] Narratives are qualitatively distinct from each other
