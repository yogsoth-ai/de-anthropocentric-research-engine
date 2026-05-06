import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import { SSClient } from './client.js';
import { ssPaper, ssPaperBatch } from './tools/paper.js';
import { ssReferences, ssCitations } from './tools/references.js';
import { ssRecommendations } from './tools/recommendations.js';
import { ssAuthor, ssAuthorPapers } from './tools/author.js';
import { ssRelevanceSearch } from './tools/search.js';

const server = new McpServer({
  name: 'dare-ss',
  version: '0.2.0',
});

const client = new SSClient(process.env.SS_API_KEY);

// ── Tool 1: ss_paper ──────────────────────────────────────────

server.tool(
  'ss_paper',
  'Get details for a single paper from Semantic Scholar. Accepts S2 ID, ARXIV:xxx, DOI:xxx, PMID:xxx, URL:xxx formats. Bare arXiv IDs (e.g. 2005.14165) and DOIs (e.g. 10.xxx/...) are auto-prefixed.',
  {
    paper_id: z.string().describe('Paper ID (S2 ID, ARXIV:xxx, DOI:xxx, PMID:xxx, URL:xxx)'),
  },
  async (args) => {
    try {
      const result = await ssPaper(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_paper failed: ${e.message}` }] };
    }
  },
);

// ── Tool 2: ss_paper_batch ────────────────────────────────────

server.tool(
  'ss_paper_batch',
  'Get details for multiple papers in one call (max 500). Papers not found return null.',
  {
    paper_ids: z.array(z.string()).max(500).describe('Array of paper IDs (max 500)'),
  },
  async (args) => {
    try {
      const result = await ssPaperBatch(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_paper_batch failed: ${e.message}` }] };
    }
  },
);

// ── Tool 3: ss_references ─────────────────────────────────────

server.tool(
  'ss_references',
  'Get papers that this paper cites (outgoing references). Includes citation context, intent, and influence.',
  {
    paper_id: z.string().describe('Paper ID'),
    offset: z.number().optional().describe('Pagination offset (default 0)'),
    limit: z.number().optional().describe('Max results (default 100, max 1000)'),
  },
  async (args) => {
    try {
      const result = await ssReferences(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_references failed: ${e.message}` }] };
    }
  },
);

// ── Tool 4: ss_citations ──────────────────────────────────────

server.tool(
  'ss_citations',
  'Get papers that cite this paper (incoming citations). Includes citation context, intent, and influence.',
  {
    paper_id: z.string().describe('Paper ID'),
    offset: z.number().optional().describe('Pagination offset (default 0)'),
    limit: z.number().optional().describe('Max results (default 100, max 1000)'),
  },
  async (args) => {
    try {
      const result = await ssCitations(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_citations failed: ${e.message}` }] };
    }
  },
);

// ── Tool 5: ss_recommendations ────────────────────────────────

server.tool(
  'ss_recommendations',
  'Get recommended papers based on seed papers. Auto-resolves non-S2 IDs. Supports positive and negative seeds.',
  {
    positive_paper_ids: z.array(z.string()).min(1).describe('Papers to find similar ones to'),
    negative_paper_ids: z.array(z.string()).optional().describe('Papers to steer away from'),
    limit: z.number().optional().describe('Max results (default 100, max 500)'),
  },
  async (args) => {
    try {
      const result = await ssRecommendations(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_recommendations failed: ${e.message}` }] };
    }
  },
);

// ── Tool 6: ss_author ─────────────────────────────────────────

server.tool(
  'ss_author',
  'Get details for a single author (name, affiliations, h-index, paper/citation counts).',
  {
    author_id: z.string().describe('Semantic Scholar author ID (numeric)'),
  },
  async (args) => {
    try {
      const result = await ssAuthor(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_author failed: ${e.message}` }] };
    }
  },
);

// ── Tool 7: ss_author_papers ──────────────────────────────────

server.tool(
  'ss_author_papers',
  'Get papers by a specific author with full metadata.',
  {
    author_id: z.string().describe('Semantic Scholar author ID (numeric)'),
    offset: z.number().optional().describe('Pagination offset (default 0)'),
    limit: z.number().optional().describe('Max results (default 100, max 1000)'),
  },
  async (args) => {
    try {
      const result = await ssAuthorPapers(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_author_papers failed: ${e.message}` }] };
    }
  },
);

// ── Tool 8: ss_relevance_search ───────────────────────────────

server.tool(
  'ss_relevance_search',
  'Search for papers by relevance using keywords or title. Returns ranked results with metadata.',
  {
    query: z.string().describe('Search keywords or paper title'),
    limit: z.number().optional().describe('Max results (default 10, max 100)'),
    offset: z.number().optional().describe('Pagination offset (default 0)'),
    year: z.string().optional().describe('Year range filter (e.g. "2020-2024", "2020-", "-2023")'),
    fields_of_study: z.string().optional().describe('Field filter (e.g. "Computer Science")'),
    min_citation_count: z.number().optional().describe('Minimum citation count threshold'),
    open_access_only: z.boolean().optional().describe('Only return papers with open access PDF'),
  },
  async (args) => {
    try {
      const result = await ssRelevanceSearch(client, args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result, null, 2) }] };
    } catch (e: any) {
      return { isError: true, content: [{ type: 'text' as const, text: `ss_relevance_search failed: ${e.message}` }] };
    }
  },
);

// ── Start ───────────────────────────────────────────────────────

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
