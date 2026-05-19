---
name: performance-extraction
description: Systematically extract performance data and conditions from papers — 30 methods, 150 data points, 40 web searches budget
used-by: baseline-establishment
---

# Performance Extraction


## Purpose

Extract structured performance data from papers, leaderboards, and reproducibility studies. Each data point is a (Task, Dataset, Metric, Score, Conditions) tuple with full provenance. Prioritizes primary sources (original papers) but cross-references against leaderboards and third-party reproductions.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Methods covered | 20 | 30 |
| Data points extracted | 100 | 150 |
| Web searches | 25 | 40 |
| Papers read | 15 | 30 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Methods covered | 0 | 30 | BLOCKED |
| Data points extracted | 0 | 150 | BLOCKED |
| Web searches used | 0 | 40 | — |
| Papers read | 0 | 30 | — |
| Datasets covered | 0 | 5 | — |
| Metrics tracked | 0 | 3 | — |
</HARD-GATE>
```

Cannot exit until data_points >= 120 (80% of target).

## Available Tactics

- **leaderboard-harvesting** — Bulk data collection from structured platforms

## Available SOPs

- **score-extraction** — Extract tuples from individual papers
- **condition-cataloging** — Record conditions alongside scores

## Execution Guidance

1. For each method in the inventory, locate the original paper
2. Use score-extraction SOP on each paper to pull all reported results
3. Cross-reference against Papers With Code / benchmark leaderboards
4. Use condition-cataloging to record experimental setup for each score
5. Flag scores that lack essential condition information
6. Track provenance: which table/figure in which paper
7. Prefer results from official implementations over third-party

## Output Format

```json
{
  "data_points": [
    {
      "method": "string",
      "task": "string",
      "dataset": "string",
      "split": "test|val|dev",
      "metric": "string",
      "score": 0.0,
      "confidence_interval": [0.0, 0.0],
      "conditions": {
        "hardware": "string",
        "training_data_size": "string",
        "hyperparams_reported": true,
        "seeds_reported": true,
        "compute_budget": "string"
      },
      "provenance": {
        "paper_id": "string",
        "table_or_figure": "string",
        "is_primary_source": true
      }
    }
  ],
  "coverage_summary": {
    "methods_covered": 0,
    "datasets_covered": 0,
    "metrics_tracked": [],
    "missing_data_flags": []
  }
}
```
