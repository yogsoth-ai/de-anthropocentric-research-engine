import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient } from '../../src/client.js';
import { ssAuthor, ssAuthorPapers } from '../../src/tools/author.js';

function mockFetch(responses: Array<{ status: number; body: unknown }>) {
  let callIndex = 0;
  return vi.fn(async () => {
    const r = responses[callIndex++] ?? responses[responses.length - 1];
    return {
      ok: r.status >= 200 && r.status < 300,
      status: r.status,
      json: async () => r.body,
      text: async () => JSON.stringify(r.body),
    } as Response;
  });
}

const REALISTIC_AUTHOR = {
  authorId: '1741101',
  name: 'Ashish Vaswani',
  affiliations: ['Google Brain'],
  homepage: null,
  paperCount: 45,
  citationCount: 180000,
  hIndex: 30,
  externalIds: { DBLP: ['v/AshishVaswani'] },
  url: 'https://www.semanticscholar.org/author/1741101',
};

const AUTHOR_PAPERS_RESPONSE = {
  offset: 0,
  next: 100,
  data: [
    {
      paperId: 'paper-001',
      title: 'Attention Is All You Need',
      year: 2017,
      citationCount: 120000,
    },
    {
      paperId: 'paper-002',
      title: 'Tensor2Tensor for Neural Machine Translation',
      year: 2018,
      citationCount: 3000,
    },
  ],
};

describe('ssAuthor', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns author details', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_AUTHOR }]);
    const client = new SSClient();
    const result = await ssAuthor(client, { author_id: '1741101' }) as any;

    expect(result.name).toBe('Ashish Vaswani');
    expect(result.hIndex).toBe(30);
    expect(result.affiliations).toContain('Google Brain');
  });

  it('returns not_found for invalid author ID', async () => {
    globalThis.fetch = mockFetch([{ status: 404, body: {} }]);
    const client = new SSClient();
    const result = await ssAuthor(client, { author_id: '0' }) as any;

    expect(result.error).toBe('not_found');
  });

  it('requests correct author fields', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_AUTHOR }]);
    const client = new SSClient();
    await ssAuthor(client, { author_id: '1741101' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('name');
    expect(url).toContain('hIndex');
    expect(url).toContain('affiliations');
  });
});

describe('ssAuthorPapers', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns author papers with pagination', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: AUTHOR_PAPERS_RESPONSE }]);
    const client = new SSClient();
    const result = await ssAuthorPapers(client, { author_id: '1741101' }) as any;

    expect(result.data).toHaveLength(2);
    expect(result.data[0].title).toBe('Attention Is All You Need');
  });

  it('passes offset and limit', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 10, data: [] } }]);
    const client = new SSClient();
    await ssAuthorPapers(client, { author_id: '1741101', offset: 10, limit: 50 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('offset=10');
    expect(url).toContain('limit=50');
  });

  it('clamps limit to 1000', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 0, data: [] } }]);
    const client = new SSClient();
    await ssAuthorPapers(client, { author_id: '1741101', limit: 5000 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=1000');
  });
});
