---
name: evidence-scout
description: Searches for external evidence supporting or opposing specific claims.
  Returns structured evidence with source assessment and relevance scoring.
execution: subagent
prompt: ./prompt.md
input: claims_to_evidence (string), stance (string), search_budget (string)
dependencies:
  sops:
  - spawn-agent
  - stress-test-paper-overview
  - stress-test-web-search
---

# Evidence Scout

Searches for external evidence supporting or opposing claims.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Evidence gathering requires web search and paper lookup in dedicated context. Isolated execution prevents search results from biasing ongoing debate reasoning.

## Input

- **claims_to_evidence**: Specific claims needing external evidence
- **stance**: Whether to search for supporting or opposing evidence (pro/con)
- **search_budget**: Number of searches allowed (2/5/10 based on campaign budget)

## Output

- **evidence_items**: List of evidence found (source, content, relevance score)
- **evidence_quality**: Assessment of each source's reliability
- **coverage**: Which claims have evidence vs. which remain unevidenced

## Budget

One unit = one evidence gathering pass (multiple searches within budget).
