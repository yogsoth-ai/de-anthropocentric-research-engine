---
name: source-gathering
description: SOP for gathering source material relevant to the ontology domain — fetch
  papers and web pages into source pages.
execution: sop
dependencies:
  sops:
  - wiki-ingest-source
---

# Source Gathering

Gather source material (papers, web pages) relevant to the ontology domain and ingest as source pages.

## Tool

`wiki-ingest-source` (SOP) + web/paper search tools

## Protocol

1. Search for relevant sources using brave-search, apify, semantic-scholar
2. For each relevant source, call wiki-ingest-source SOP to create a source page
3. Return list of ingested source paths

## HARD-GATE

<HARD-GATE>
Must ingest ≥2 source pages per invocation.
</HARD-GATE>

## Yield

Returns: `{ sources_ingested: number, paths: string[] }`
