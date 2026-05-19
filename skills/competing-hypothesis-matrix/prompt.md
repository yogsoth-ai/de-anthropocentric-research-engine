# Competing Hypothesis Matrix — Subagent Dispatch Prompt

You are executing the competing-hypothesis-matrix tactic for hypothesis formulation.

Your job is to orchestrate three SOPs in strict sequence — competing-hypothesis-generation → discriminating-prediction-design → hypothesis-comparison-matrix — and produce a structured matrix that maps competing hypotheses against discriminating predictions, enabling rigorous experimental design.

## Your Process

1. **Generate competing hypotheses** (competing-hypothesis-generation SOP): Given one or more primary hypotheses, generate ≥3 competing alternatives. A competing hypothesis must:
   - Explain the same phenomenon or observation as the primary hypothesis
   - Propose a different causal mechanism (not just a rephrasing)
   - Be independently falsifiable

   For each competing hypothesis, provide:
   - **Statement**: "If X then Y because Z" form
   - **Mechanism**: The causal process that produces the predicted outcome
   - **Theoretical basis**: Which theory or prior work supports this alternative?
   - **Key difference from primary**: What is the core mechanistic difference?
   - **Shared predictions**: What does this hypothesis predict in common with the primary? (these cannot discriminate)
   - **Unique predictions**: What does this hypothesis predict that the primary does not?

   Generation rules: at least one competing hypothesis must come from a different theoretical tradition than the primary. Do not generate "straw man" alternatives that are obviously implausible — all competing hypotheses must be scientifically defensible.

2. **Design discriminating predictions** (discriminating-prediction-design SOP): For each pair of hypotheses (primary vs. each competing), design at least one discriminating prediction — an observation or experimental result that the two hypotheses predict differently.

   For each discriminating prediction, specify:
   - **Prediction statement**: "If we observe X under condition Y, then hypothesis H-A predicts [result 1] while hypothesis H-B predicts [result 2]."
   - **Hypotheses discriminated**: Which pair (or set) of hypotheses does this prediction separate?
   - **Experimental design sketch**: What study design would produce this observation? (1-3 sentences)
   - **Feasibility**: Is this experiment feasible with current methods and resources? (high / medium / low)
   - **Discriminating power**: How cleanly does this prediction separate the hypotheses? (clean = mutually exclusive predictions; noisy = overlapping predictions with different magnitudes)

   Aim for ≥2 discriminating predictions total. Prefer predictions with high discriminating power and high feasibility.

3. **Build comparison matrix** (hypothesis-comparison-matrix SOP): Assemble all hypotheses (primary + competing) and all discriminating predictions into a structured matrix.

   Matrix structure:
   - Rows: hypotheses (H-primary, H-C1, H-C2, ...)
   - Columns: discriminating predictions (DP-1, DP-2, ...)
   - Each cell: the expected result if this hypothesis is true and this prediction is tested
     - Use: "+" (supports), "−" (contradicts), "0" (neutral/no prediction), or a brief directional description

   After the matrix, add:
   - **Most discriminating prediction**: Which DP separates the most hypothesis pairs?
   - **Hardest-to-distinguish pair**: Which two hypotheses have the most similar prediction profiles?
   - **Recommended test sequence**: If you could run only one experiment, which DP should it be and why?

## Your Output

### Competing Hypotheses

For each competing hypothesis (H-C1, H-C2, ...): statement, mechanism, theoretical basis, key difference from primary, shared predictions, unique predictions.

### Discriminating Predictions

For each prediction (DP-1, DP-2, ...): prediction statement, hypotheses discriminated, experimental design sketch, feasibility, discriminating power.

### Comparison Matrix

| Hypothesis | DP-1 | DP-2 | ... |
|------------|------|------|-----|
| H-primary  | +    | 0    | ... |
| H-C1       | −    | +    | ... |
| H-C2       | 0    | −    | ... |

Followed by: most discriminating prediction, hardest-to-distinguish pair, recommended test sequence.

### Yield Report

```
YIELD REPORT
Primary hypotheses: N | Competing hypotheses generated: N
Discriminating predictions designed: N
Most discriminating prediction: [DP-N — separates N hypothesis pairs]
Hardest-to-distinguish pair: [H-X vs H-Y — reason]
Recommended first experiment: [DP-N — rationale]
Feasibility distribution: high=N, medium=N, low=N
```

## Rules

- Competing hypotheses must be scientifically defensible — do not generate obvious straw men.
- At least one competing hypothesis must come from a different theoretical tradition than the primary hypothesis.
- Every discriminating prediction must produce different expected results for at least two hypotheses — a prediction that all hypotheses agree on is not discriminating.
- Matrix cells must not be left empty — if a hypothesis makes no prediction about a DP, mark it "0" (neutral).
- Do not recommend a "winner" hypothesis — the goal is to design experiments that could distinguish them, not to pre-judge the outcome.
- Minimum yield hard floor: ≥3 competing hypotheses + ≥2 discriminating predictions + complete comparison matrix before reporting done.
