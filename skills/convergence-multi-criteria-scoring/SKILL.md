---
name: multi-criteria-scoring
description: Multi-Criteria Scoring Campaign — evaluate and rank candidates against
  multiple weighted criteria using AHP, BWM, TOPSIS, VIKOR, ELECTRE, PROMETHEE, MAUT
  methods.
execution: campaign
dependencies:
  strategies:
  - best-option-selection
  - category-sorting
  - full-ranking
  - non-compensatory-screening
  - weight-elicitation
  campaigns:
  - pairwise-ranking
  sops:
  - context-checkpoint
  - context-init
  - convergence-paper-overview
  - convergence-paper-research
  - convergence-paper-search
  - convergence-saturation-detection
  - convergence-sensitivity-analysis
  - convergence-web-research
  - convergence-web-search
---

# Multi-Criteria Scoring

Evaluate and rank candidate alternatives using multi-criteria weighted assessment. Supports mainstream MCDA methods including AHP, BWM, TOPSIS, VIKOR, ELECTRE, PROMETHEE, and MAUT, covering the full workflow from criteria definition, weighting, scoring, to sensitivity analysis.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| "What criteria? How to score?" / select best option / rank by criteria | best-option-selection |
| "Full ranking" / full ranking / league table / priority list | full-ranking |
| "Categorize" / categorize / A/B/C grading / compliance sorting | category-sorting |
| "Eliminate non-qualifying" / go/no-go / safety screening / veto | non-compensatory-screening |
| "Determine weights" / weight negotiation / criteria importance | weight-elicitation |

## Manifest

### Strategies

| Strategy | Purpose | Budget |
|----------|---------|--------|
| best-option-selection | Select best option from candidates | M |
| full-ranking | Produce complete priority ranking | M |
| category-sorting | Classify candidates into predefined categories | M |
| non-compensatory-screening | Eliminate non-qualifying candidates | S |
| weight-elicitation | Determine criteria weights | S |

### Tactics

| Tactic | Purpose |
|--------|---------|
| scoring-matrix-construction | Define criteria → assign weights → score → aggregate → sensitivity check |
| screening-then-scoring | Non-compensatory elimination first → then fine-grained scoring of survivors |
| multi-method-triangulation | Multi-method comparison → identify method-sensitive options |

### Subagent SOPs

| SOP | Purpose |
|-----|---------|
| criterion-definition | Extract evaluation criteria from research goals and candidates |
| weight-elicitation-sop | Compute criteria weights using specified method |
| alternative-scoring | Score candidates against each criterion |
| normalization | Normalize the score matrix |
| dominance-check | Identify dominated and non-dominated alternatives |
| threshold-setting | Set minimum thresholds for each criterion |
| conjunctive-filter | Eliminate candidates failing thresholds |
| rank-comparison | Compare consistency of multiple ranking results |
| method-sensitivity-report | Analyze impact of method choice on rankings |
| scoring-synthesis | Synthesize scores, rankings, and sensitivity into final recommendation |

## Budget Table

| Metric | Target |
|--------|--------|
| Criteria count | 5-8 |
| Candidate count | 8-15 |
| Weight method comparison | >=2 methods |
| Sensitivity analysis | >=3 parameter perturbations |

## MCP Tools

| Tool | Usage |
|------|-------|
| vault_search | Retrieve existing evaluation criteria and historical scores |
| vault_query_graph | Query relationships and dependencies between alternatives |
| vault_add_edge | Record evaluation result relationships |

## Context Management

- Each SOP executes as a subagent with independent context
- Strategy layer maintains State Ledger to track progress
- Score matrix is passed between SOPs as structured data
- Sensitivity analysis results are aggregated into final synthesis
