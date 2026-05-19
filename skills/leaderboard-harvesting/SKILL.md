---
name: leaderboard-harvesting
description: Systematically collect performance data from platforms and papers
execution: tactic
used-by: baseline-establishment
---

# Leaderboard Harvesting


## Purpose

Harvest structured performance data from leaderboard platforms (Papers With Code, benchmark-specific sites), survey papers, and official benchmark repositories. Produces deduplicated, provenance-tracked score collections.

## Stages

### Stage 1: Platform Scan

Identify and scrape all relevant leaderboard sources:
- Papers With Code task pages
- Benchmark-specific leaderboards (e.g., GLUE, ImageNet, WMT)
- GitHub benchmark repositories
- Survey papers with comprehensive comparison tables

**Yield**: List of leaderboard URLs + initial method counts per source.

### Stage 2: Paper Extraction

For methods not covered by leaderboards, extract scores directly from papers:
- Original method papers (primary source)
- Ablation studies and follow-up papers
- Reproduction studies and benchmarking papers

**Yield**: Raw score tuples with paper provenance.

### Stage 3: Cross-Validation

Compare scores across sources for the same method-dataset-metric triple:
- Flag discrepancies > 1 standard deviation
- Prefer primary sources when conflicts exist
- Note which scores come from official vs. unofficial implementations

**Yield**: Validated score set with confidence annotations.

### Stage 4: Dedup and Merge

Consolidate all sources into a single canonical dataset:
- Resolve method name aliases
- Merge duplicate entries with provenance tracking
- Assign confidence levels based on source agreement

**Yield**: Unified performance dataset ready for analysis.

## Minimum Yield

| Metric | Floor |
|--------|-------|
| Leaderboard sources checked | 3 |
| Methods with scores | 15 |
| Cross-validated score pairs | 10 |
| Deduplication conflicts resolved | 5 |

## SOPs Used

- method-discovery (for finding methods on leaderboards)
- score-extraction (for paper-based extraction)
- discrepancy-identification (for cross-validation)
