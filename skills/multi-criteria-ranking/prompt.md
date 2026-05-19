# Multi-Criteria Ranking — Subagent Dispatch Prompt

You are executing the multi-criteria-ranking strategy for gap prioritization.

## Your Task

Evaluate and rank a set of research gaps (5–20) using a weighted multi-criteria scoring framework. Decompose the ranking problem into independent dimensions, score each gap per dimension, then synthesize a final priority order.

## Process

1. **Normalize gaps**: Ensure each gap has a consistent format — ID, one-sentence description, domain tag. If gaps are missing these, infer them from context.

2. **Determine weights**: Use the default weight vector unless the user has specified otherwise:
   - Importance: 0.35
   - Feasibility: 0.25
   - Novelty: 0.20
   - Impact: 0.20
   Adjust weights if the research context clearly favors a different balance (e.g., applied engineering context → raise feasibility weight).

3. **Score each dimension independently**: For each gap, assign a score of 1–5 per dimension. Score one dimension across all gaps before moving to the next — this prevents anchoring bias.
   - Importance (1–5): How much would filling this gap advance the field?
   - Feasibility (1–5): Can this be solved with available methods and resources in a reasonable timeframe?
   - Novelty (1–5): How underexplored is this gap? (5 = no prior work; 1 = heavily studied)
   - Impact (1–5): How broad are the downstream effects of solving this gap?

4. **Build scoring matrix**: Compile all scores into a gap × dimension table.

5. **Compute weighted scores**: For each gap, compute: Score = 0.35×Importance + 0.25×Feasibility + 0.20×Novelty + 0.20×Impact.

6. **Sensitivity check**: Perturb each weight by ±20% and recompute rankings. Identify any gaps whose rank changes by more than 2 positions — flag these as "weight-sensitive."

7. **Synthesize output**: Produce the final ranked list with scores, flag weight-sensitive gaps, and write a 2–3 sentence attack recommendation for the top-N gaps.

## Output Format

### Scoring Matrix

| Gap ID | Importance | Feasibility | Novelty | Impact | Weighted Score | Rank |
|--------|-----------|-------------|---------|--------|---------------|------|
| G-01   | ...        | ...         | ...     | ...    | ...           | ...  |

### Weight Vector Used
- Importance: X | Feasibility: X | Novelty: X | Impact: X

### Sensitivity Analysis
- Stable rankings: [list]
- Weight-sensitive gaps: [list with note on which weight flip causes rank change]

### Top-N Attack Recommendations
For each top gap: gap ID, one-sentence rationale, suggested method direction, estimated difficulty (Low/Medium/High).

## Rules

- Score dimensions independently — do not let your overall impression of a gap bleed into individual dimension scores.
- If you cannot score a dimension due to insufficient information, assign 3 (neutral) and flag it.
- Do not skip the sensitivity check for M and L tier inputs.
- The final ranking must be deterministic — same inputs must produce same outputs.
- Do not add new gaps or modify gap descriptions. Your job is ranking, not discovery.
