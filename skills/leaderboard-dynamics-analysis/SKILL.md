---
name: leaderboard-dynamics-analysis
description: Analyze leaderboard score distributions, compression, selective reporting
execution: subagent
prompt: ./prompt.md
input: leaderboard_data (model, score, date)
used-by: benchmark-archaeology
---

# Leaderboard Dynamics Analysis SOP

Analyze the dynamics of benchmark leaderboards: score distributions, compression over time, selective reporting patterns, and statistical artifacts.

## Input

- **leaderboard_data**: Structured data with (model_name, score, date, optional: model_size, paper_reference)

## Procedure

1. Compute score distribution statistics over time
2. Detect score compression (shrinking gap between top models)
3. Identify selective reporting patterns (cherry-picking, subset selection)
4. Analyze relationship between model size and score
5. Detect anomalies (withdrawn results, unreplicated claims)

## Output

Leaderboard health assessment with statistical evidence.
