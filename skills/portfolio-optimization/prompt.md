# Portfolio Optimization — Subagent Dispatch Prompt

You are executing the portfolio-optimization strategy for gap prioritization.

## Your Task

Treat the set of research gaps as an investment portfolio. Score each gap individually for return and risk, analyze correlations between gaps, then recommend the optimal gap combination that maximizes expected research output while managing risk and ensuring diversity.

## Process

1. **Normalize gaps**: Ensure each gap has a consistent format — ID, one-sentence description, domain tag, primary methods required, data dependencies.

2. **Score each gap on four dimensions** (1–5):
   - Importance, Feasibility, Novelty, Impact

3. **Compute per-gap return and risk**:
   - Return = (Importance + Impact) / 2
   - Risk = (6 − Feasibility) / 5  (higher feasibility → lower risk; normalized to 0–1)
   - Risk-adjusted return = Return × (1 − Risk × 0.5)

4. **Build correlation matrix**: For each pair of gaps, estimate their correlation (0 = independent, 1 = fully correlated) based on:
   - Method overlap: do they require the same algorithms, models, or techniques?
   - Data overlap: do they require the same datasets or data collection?
   - Prerequisite overlap: does solving one depend on solving the other?
   
   Correlation estimate: 0–0.3 (low), 0.3–0.6 (medium), 0.6–1.0 (high).

5. **Enumerate candidate combinations**: Generate combinations of K gaps (K = target portfolio size per budget tier). For each combination:
   - Portfolio return = mean(individual returns)
   - Portfolio risk = mean(individual risks) × (1 − 0.5 × mean(pairwise correlations))  [diversification discount]
   - Portfolio score = Portfolio return / Portfolio risk

6. **Identify efficient frontier**: Find combinations where no other combination has both higher return and lower risk. Present 3 points on the frontier: max return, min risk, and max risk-adjusted score.

7. **Apply diversity constraint**: The recommended combination must include at least one gap from each major sub-domain (if applicable) and must not have >2 gaps with pairwise correlation > 0.6.

8. **Synthesize output**: Recommend the combination at the max risk-adjusted score point on the efficient frontier. Provide backup recommendations for conservative (min risk) and aggressive (max return) preferences.

## Output Format

### Individual Gap Scores

| Gap ID | Return | Risk | Risk-Adj Return | Primary Methods | Data Dependencies |
|--------|--------|------|----------------|----------------|------------------|
| G-01   | …      | …    | …              | …              | …                |

### Correlation Matrix (high-correlation pairs only, ≥0.3)

| Gap A | Gap B | Correlation | Overlap Type |
|-------|-------|-------------|-------------|
| G-01  | G-03  | 0.7         | shared dataset |

### Efficient Frontier

| Point | Combination | Portfolio Return | Portfolio Risk | Score |
|-------|-------------|-----------------|----------------|-------|
| Max Return | [G-ids] | … | … | … |
| Balanced | [G-ids] | … | … | … |
| Min Risk | [G-ids] | … | … | … |

### Recommendation
Primary recommendation (balanced), conservative alternative, aggressive alternative. For each: the gap IDs, rationale for the combination, expected research timeline, and resource requirements.

## Rules

- Return and risk formulas are fixed — do not substitute without explicit instruction.
- Correlation estimates are qualitative; do not claim false precision. Use Low/Medium/High bands if numerical estimation is unreliable.
- The diversity constraint (no >2 gaps with correlation > 0.6) is a hard constraint on the final recommendation.
- If all gaps are highly correlated (unavoidable in a narrow sub-field), note this explicitly and explain why correlation cannot be reduced further.
- Portfolio size K: S tier = 3–5, M tier = 5–8, L tier = 8–12. Do not recommend fewer than 3 gaps.
