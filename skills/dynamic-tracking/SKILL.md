---
name: dynamic-tracking
description: Strategy for continuous rating updates using Elo, Glicko-2, TrueSkill
  2, and Whole-History Rating for live ranking systems and A/B testing.
dependencies:
  tactics:
  - adaptive-pair-selection
  - consistency-audit-loop
  sops:
  - ranking-synthesis
---

# Dynamic Tracking

## Purpose

Maintain live rankings that update incrementally as new comparisons arrive. Suitable for ongoing evaluation, A/B testing, and systems where candidates enter/exit over time. Tracks rating uncertainty and temporal dynamics.

## When to use

- Continuous stream of comparisons (not batch)
- Candidates added/removed over time
- A/B testing or tournament-style evaluation
- Need to track rating trajectories and momentum

## Budget

| Resource | Allocation |
|----------|-----------|
| Comparisons per update | 1+ (online update) |
| Rating recalculation | After each comparison or micro-batch |
| Stability window | Last 20-50 comparisons for convergence check |
| Decay handling | Increase uncertainty for inactive candidates |

## State Ledger

```yaml
candidates: {}          # id → {mu, sigma, last_active, history: []}
comparison_log: []      # [{pair, winner, timestamp, context}]
method: ""              # elo | glicko2 | trueskill2 | whr
parameters: {}          # K-factor, tau, beta, etc.
iteration: 0
window_size: 30
convergence: {stable: false, score: 0.0}
```

## Available Tactics

- **adaptive-pair-selection** — select next matchup for maximum information
- **consistency-audit-loop** — periodic transitivity audit

## Available SOPs

- pair-selector
- comparison-executor
- rating-update
- convergence-check
- cycle-detection
- ranking-synthesis

## Execution Guidance

1. Initialize new candidates with default prior
2. For each incoming comparison:
   a. Run comparison-executor (or accept external result)
   b. Run rating-update with online method
   c. Every window_size comparisons, run convergence-check
3. Periodically run cycle-detection on recent window
4. Increase sigma for candidates inactive > threshold
5. On demand: run ranking-synthesis for current snapshot

## Output Format

```yaml
current_ranking:
  - {rank: 1, candidate: "...", mu: 1842, sigma: 45, games: 23}
  - {rank: 2, candidate: "...", mu: 1798, sigma: 52, games: 18}
method: glicko2
total_comparisons: 342
last_updated: "2026-05-19T14:30:00Z"
rating_period: 7
top_movers:
  - {candidate: "...", delta: +120, last_5: "WWWLW"}
stability_score: 0.88
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| adaptive-pair-selection | Iteratively select maximally informative pairs, execute comparisons, update ratings, and check convergence until ranking stabilizes. |
| consistency-audit-loop | Detect preference cycles, localize inconsistent judgments, request corrections, and recompute ratings until consistency threshold is met. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ranking-synthesis | Produce the final ranking artifact from converged ratings and consistency report. |

<!-- END available-tables (generated) -->
