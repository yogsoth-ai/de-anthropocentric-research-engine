---
name: discrepancy-analysis
description: Identify discrepancies between reported and reproducible scores — 15
  methods, 45 data points, 30 web searches budget
dependencies:
  tactics:
  - leaderboard-harvesting
  sops:
  - discrepancy-identification
  - reproducibility-checklist-audit
---

# Discrepancy Analysis


## Purpose

Detect inconsistencies between scores reported in original papers versus third-party reproductions, leaderboard entries, and ablation studies. Flags methods with suspicious performance claims, identifies common sources of score inflation, and assesses the reliability of reported baselines.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Methods analyzed | 10 | 15 |
| Data points compared | 30 | 45 |
| Web searches | 20 | 30 |
| Reproduction studies consulted | 5 | 10 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Methods analyzed | 0 | 15 | BLOCKED |
| Score pairs compared | 0 | 45 | BLOCKED |
| Discrepancies flagged | 0 | — | — |
| Reproduction studies found | 0 | 10 | — |
| Reliability ratings assigned | 0 | 15 | — |
</HARD-GATE>
```

Cannot exit until score_pairs_compared >= 36 (80% of target).

## Available Tactics

- **leaderboard-harvesting** — Collect multiple sources for cross-validation

## Available SOPs

- **discrepancy-identification** — Compare same-method scores across sources
- **reproducibility-checklist-audit** — Assess paper reproducibility completeness

## Execution Guidance

1. For each method, collect scores from multiple independent sources
2. Use discrepancy-identification SOP to flag significant deviations
3. Search for reproduction studies, blog posts, and issue trackers
4. Apply reproducibility-checklist-audit to papers with large discrepancies
5. Categorize discrepancy sources (data leakage, cherry-picked seeds, unfair baselines)
6. Assign reliability ratings to each method's reported scores
7. Document which baselines in the field are trustworthy vs. inflated

## Output Format

```json
{
  "discrepancies": [
    {
      "method": "string",
      "dataset": "string",
      "metric": "string",
      "reported_score": 0.0,
      "reproduced_score": 0.0,
      "delta": 0.0,
      "delta_significant": true,
      "likely_cause": "string",
      "sources": ["string"]
    }
  ],
  "reliability_ratings": [
    {
      "method": "string",
      "rating": "high|medium|low|unreliable",
      "reproducibility_checklist_score": 0,
      "notes": "string"
    }
  ],
  "systematic_issues": [
    {
      "issue": "string",
      "affected_methods": ["string"],
      "prevalence": "string"
    }
  ]
}
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| leaderboard-harvesting | Systematically collect performance data from platforms and papers |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| discrepancy-identification | Compare same-method scores across sources, flag significant deviations |
| reproducibility-checklist-audit | Assess paper completeness against ML Reproducibility Checklist |

<!-- END available-tables (generated) -->
