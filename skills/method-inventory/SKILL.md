---
name: method-inventory
description: Comprehensively identify all relevant methods for a task — 50 methods, 60 web searches budget
used-by: baseline-establishment
---

# Method Inventory


## Purpose

Systematically discover and catalog every relevant method (published, preprint, industry) that has been evaluated on the target task. Combines leaderboard scraping, citation chain traversal, and keyword-based academic search to ensure no significant method is missed.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Methods discovered | 30 | 50 |
| Web searches | 40 | 60 |
| Papers consulted | 20 | 40 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Methods discovered | 0 | 50 | BLOCKED |
| Web searches used | 0 | 60 | — |
| Papers consulted | 0 | 40 | — |
| Leaderboard sources | 0 | 5 | — |
| Citation chains traced | 0 | 10 | — |
</HARD-GATE>
```

Cannot exit until methods_discovered >= 40 (80% of target).

## Available Tactics

- **leaderboard-harvesting** — Scrape Papers With Code, benchmark-specific leaderboards, survey papers

## Available SOPs

- **method-discovery** — Core method identification via literature, leaderboards, citation chains

## Execution Guidance

1. Start with leaderboard-harvesting tactic to get the well-known methods
2. Use method-discovery SOP with citation chaining to find less prominent methods
3. Search for survey papers and meta-analyses that enumerate methods
4. Check preprint servers for very recent unpublished methods
5. Verify each method has: name, year, authors, venue, key innovation
6. Deduplicate (same method with different names across papers)
7. Classify methods by family/approach (e.g., transformer-based, GNN-based, hybrid)

## Output Format

```json
{
  "task": "string",
  "domain": "string",
  "methods": [
    {
      "name": "string",
      "aliases": ["string"],
      "year": 2024,
      "authors": "string",
      "venue": "string",
      "family": "string",
      "key_innovation": "string",
      "paper_id": "string",
      "source": "leaderboard|paper|citation_chain|preprint"
    }
  ],
  "coverage_assessment": {
    "leaderboard_sources_checked": 0,
    "citation_chains_traced": 0,
    "survey_papers_consulted": 0,
    "confidence": "high|medium|low"
  }
}
```
