---
name: weight-perturbation
description: 'SOP: Perturb weights to test gap-ranking stability, output a stability verdict'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: Baseline weight vector + gap scoring matrix (gap × dimension)
output: PerturbationReport — perturbation scenarios, ranking change magnitude, and stability verdict
dependencies:
  skills:
  - subagent-spawning
---

# Weight Perturbation

Perturb weights to test gap-ranking stability, output a stability verdict.

## HARD-GATE

<HARD-GATE>
- The elements of the input weight vector must sum to 1.0 (±0.001 tolerance allowed)
- The number of rows in the scoring matrix (number of gaps) must be ≥ 2
- At least 4 perturbation scenarios must be generated (±20% per dimension)
- stability_verdict must be one of "stable" | "sensitive" | "unstable"
</HARD-GATE>

## Pipeline

1. **Precheck**: Verify the weight vector is normalized; verify the scoring matrix dimensions match the weight vector length
2. **Baseline ranking computation**: Weight-sum the scoring matrix with the baseline weights to obtain the baseline ranking
3. **Perturbation scenario generation**: Apply +20% and -20% perturbations to each dimension separately (re-normalizing afterward), generating 2×n perturbation scenarios
4. **Re-compute rankings**: Compute a new ranking for each perturbation scenario
5. **Compare change magnitude**: Count the number of gaps whose ranking changed in each scenario; compute Kendall τ correlation against the baseline ranking
6. **Stability verdict**: stable (all scenarios τ ≥ 0.8) / sensitive (any scenario 0.5 ≤ τ < 0.8) / unstable (any scenario τ < 0.5)
7. **Output**: Return a PerturbationReport object

## Output Format

```json
{
  "baseline_ranking": ["gap_003", "gap_001", "gap_002"],
  "perturbation_scenarios": [
    {
      "scenario_id": "importance_+20%",
      "perturbed_weights": { "importance": 0.48, "feasibility": 0.18, "novelty": 0.17, "impact": 0.17 },
      "ranking": ["gap_003", "gap_001", "gap_002"],
      "kendall_tau": 1.0,
      "rank_changes": 0
    }
  ],
  "min_kendall_tau": 0.87,
  "stability_verdict": "stable",
  "sensitive_dimensions": [],
  "summary": "Stability summary (2-3 sentences)"
}
```
