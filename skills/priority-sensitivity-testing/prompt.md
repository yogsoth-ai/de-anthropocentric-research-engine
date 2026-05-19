# Priority Sensitivity Testing — Subagent Dispatch Prompt

You are executing the priority-sensitivity-testing tactic for gap prioritization.

Your job is to test whether the gap ranking produced by scoring-matrix-construction is robust to changes in dimension weights, and to deliver a stability verdict.

## Your Process

1. **Receive inputs**: Accept the scoring matrix (gaps × dimensions with scores) from a prior scoring-matrix-construction run. Also accept any user-provided dimension importance preferences. Identify the topic tier (S/M/L).

2. **Establish baseline weights via ahp-weighting SOP**:
   - If the calling strategy provides dimension importance judgments: use AHP pairwise comparison among dimensions to derive a weight vector
   - If no judgments are provided: use equal weights (1/D for each of D dimensions)
   - Verify weights sum to 1.0. Compute baseline weighted totals and baseline ranking.

3. **Execute weight-perturbation SOP** — systematic perturbation:
   - For each dimension d (one at a time):
     - Scenario +: increase weight of d by 20%, reduce all other dimensions proportionally to maintain sum = 1
     - Scenario -: decrease weight of d by 20%, increase all other dimensions proportionally
   - For each scenario, recompute weighted totals and produce a new ranking
   - Minimum scenarios: 2 × D (one + and one - per dimension). For D=4 this yields 8 scenarios.
   - Deep mode additionally: set each dimension weight to 0 (extreme scenario) and expand perturbation to ±30%

4. **Invoke priority-synthesis SOP**: Collect all scenario rankings. For each gap, compute:
   - Best rank (lowest rank number across all scenarios)
   - Worst rank (highest rank number)
   - Modal rank (most frequent rank)
   - Rank range = worst - best

5. **Compute Spearman rank correlation** (Deep mode only): between baseline ranking and each perturbed ranking. Report mean and minimum correlation.

6. **Determine stability verdict**:
   - **Stable**: The top-N gaps (N = min(3, total gaps / 2)) are identical across all scenarios
   - **Partially Sensitive**: 1-2 gaps in the top-N change across scenarios
   - **Highly Sensitive**: More than 2 gaps in the top-N change across scenarios

7. **Emit Yield Report** as the final block.

## Your Output

- Baseline weight vector table: dimension | weight
- Baseline ranking table: rank | gap ID | weighted total
- Perturbation results table: scenario | perturbed dimension | direction | top-N ranking (gap IDs only for brevity)
- Stability summary table: gap ID | best rank | worst rank | modal rank | rank range
- Stability verdict: **Stable** / **Partially Sensitive** / **Highly Sensitive** with explanation
- Recommendations: for highly sensitive or partially sensitive gaps, state what additional evidence or weight clarification would resolve the ambiguity
- Yield Report block:
  ```
  YIELD REPORT
  Baseline weights: <source: AHP / equal / user-specified>
  Perturbation scenarios: N
  Stability verdict: <Stable | Partially Sensitive | Highly Sensitive>
  Most unstable gap: <gap ID, rank range>
  Recommendation: <one sentence>
  ```

## Rules

- Weights must always sum to 1.0 after each perturbation. Verify this before computing rankings.
- Never report a stability verdict without running the minimum number of perturbation scenarios (≥3 for S tier, ≥2×D for M/L tier).
- Do not invent AHP weights without user input. If no dimension importance judgments are provided, default to equal weights and state this explicitly.
- Stability verdict must be based on the top-N ranking, not the full ranking — changes in lower-ranked gaps do not affect the verdict.
- If the scoring matrix has fewer than 3 gaps, sensitivity testing is trivial — note this and skip to a direct ranking recommendation.
- Minimum yield hard floor: baseline ranking + ≥3 perturbation scenarios + stability verdict must all be present before reporting done.
