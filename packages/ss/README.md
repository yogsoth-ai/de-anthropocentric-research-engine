# dare-ss

Lightweight MCP server wrapping the [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/graph/v1).

## Tools

| Tool | Description |
|------|-------------|
| `ss_paper` | Get full metadata for a single paper (S2 ID, ARXIV:xxx, DOI:xxx, PMID:xxx, URL:xxx) |
| `ss_paper_batch` | Batch fetch up to 500 papers in one call |
| `ss_references` | Outgoing references with citation context, intent, and influence flag |
| `ss_citations` | Incoming citations with citation context, intent, and influence flag |
| `ss_recommendations` | Recommended papers based on positive/negative seed papers |
| `ss_author` | Author profile (name, affiliations, h-index, paper/citation counts) |
| `ss_author_papers` | All papers by an author with full metadata |

## Setup

```bash
npm install
```

## Running

```bash
npm run mcp
```

Set `SS_API_KEY` environment variable for higher rate limits (100 req/s vs 1 req/s unauthenticated).

## MCP Config

```json
{
  "mcpServers": {
    "dare-ss": {
      "command": "npx",
      "args": ["tsx", "G:/DARE-EXTENSION/DARE-SS/src/server.ts"],
      "env": {
        "SS_API_KEY": "<your-key>"
      }
    }
  }
}
```

## Testing

```bash
npm test                                                    # unit tests (39)
SS_API_KEY=<key> npx vitest run .test/integration.test.ts  # live API tests
```
