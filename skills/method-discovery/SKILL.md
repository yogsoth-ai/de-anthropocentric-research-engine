---
name: method-discovery
description: Identify all relevant methods via literature, leaderboards, citation chains
execution: subagent
prompt: ./prompt.md
input: task_name, domain, known_methods
used-by: baseline-establishment
---

# Method Discovery


## Purpose

Discover the complete set of methods that have been proposed and evaluated for a given task. Uses a multi-pronged search strategy combining leaderboard scraping, academic search, citation chain traversal, and survey paper mining.

## Input Schema

| Field | Type | Description |
|-------|------|-------------|
| task_name | string | The target task (e.g., "text summarization", "node classification") |
| domain | string | Research domain (e.g., "NLP", "graph learning", "computer vision") |
| known_methods | string[] | Already-known methods to seed citation chain traversal |

## Output Schema

```json
{
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
      "source": "leaderboard|paper|citation_chain|preprint|survey"
    }
  ],
  "search_log": {
    "leaderboards_checked": ["string"],
    "queries_issued": ["string"],
    "citation_chains_from": ["string"],
    "surveys_consulted": ["string"]
  }
}
```
