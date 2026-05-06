import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient } from '../../src/client.js';
import { ssRelevanceSearch } from '../../src/tools/search.js';

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

const SEARCH_RESPONSE = {
  total: 1500,
  offset: 0,
  next: 10,
  data: [
    {
      paperId: '649def34f8be52c8b66281af98ae884c09aef38b',
      title: 'Attention Is All You Need',
      year: 2017,
      citationCount: 120000,
    },
    {
      paperId: 'abc123',
      title: 'BERT: Pre-training of Deep Bidirectional Transformers',
      year: 2018,
      citationCount: 80000,
    },
  ],
};

describe('ssRelevanceSearch', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('sends query to /paper/search with fields', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    const result = await ssRelevanceSearch(client, { query: 'attention mechanism' });

    expect(result).toEqual(SEARCH_RESPONSE);
    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/search');
    expect(url).toContain('query=attention+mechanism');
    expect(url).toContain('fields=');
  });

  it('passes limit and offset as query params', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'transformers', limit: 5, offset: 20 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=5');
    expect(url).toContain('offset=20');
  });

  it('clamps limit to 100', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test', limit: 999 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=100');
  });

  it('passes year filter when provided', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test', year: '2020-2024' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('year=2020-2024');
  });

  it('passes fieldsOfStudy filter when provided', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test', fields_of_study: 'Computer Science' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('fieldsOfStudy=Computer+Science');
  });

  it('passes minCitationCount when provided', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test', min_citation_count: 100 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('minCitationCount=100');
  });

  it('passes openAccessPdf filter when true', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test', open_access_only: true });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('openAccessPdf');
  });

  it('omits optional params when not provided', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).not.toContain('year=');
    expect(url).not.toContain('fieldsOfStudy=');
    expect(url).not.toContain('minCitationCount=');
    expect(url).not.toMatch(/[?&]openAccessPdf(&|$|=)/);
  });

  it('includes openAccessPdf in fields (not stripped)', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('fields=');
    const fieldsParam = new URL(url).searchParams.get('fields')!;
    expect(fieldsParam).toContain('openAccessPdf');
  });

  it('uses default limit=10 and offset=0', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: SEARCH_RESPONSE }]);
    const client = new SSClient();
    await ssRelevanceSearch(client, { query: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=10');
    expect(url).toContain('offset=0');
  });
});
