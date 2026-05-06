import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient } from '../../src/client.js';
import { ssPaper, ssPaperBatch } from '../../src/tools/paper.js';
import { PAPER_FIELDS } from '../../src/fields.js';

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

const REALISTIC_PAPER = {
  paperId: '649def34f8be52c8b66281af98ae884c09aef38b',
  title: 'Attention Is All You Need',
  abstract: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...',
  year: 2017,
  authors: [
    { authorId: '1234', name: 'Ashish Vaswani' },
    { authorId: '5678', name: 'Noam Shazeer' },
  ],
  citationCount: 120000,
  influentialCitationCount: 15000,
  referenceCount: 44,
  isOpenAccess: true,
  openAccessPdf: { url: 'https://arxiv.org/pdf/1706.03762', status: 'GREEN' },
  externalIds: { ArXiv: '1706.03762', DOI: '10.48550/arXiv.1706.03762' },
  fieldsOfStudy: ['Computer Science'],
  publicationTypes: ['JournalArticle', 'Conference'],
  publicationDate: '2017-06-12',
  venue: 'NeurIPS',
  tldr: { model: 'tldr@v2.0.0', text: 'A new simple network architecture based solely on attention mechanisms.' },
  url: 'https://www.semanticscholar.org/paper/649def34f8be52c8b66281af98ae884c09aef38b',
};

const PAPER_MISSING_ABSTRACT = {
  ...REALISTIC_PAPER,
  paperId: 'missing-abstract-id',
  title: 'Restricted Paper',
  abstract: null,
  tldr: null,
};

describe('ssPaper', () => {
  let originalFetch: typeof globalThis.fetch;

  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns full paper details for a valid S2 ID', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    const result = await ssPaper(client, { paper_id: '649def34f8be52c8b66281af98ae884c09aef38b' });

    expect(result).toEqual(REALISTIC_PAPER);
    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('fields=');
    expect(url).toContain('title');
    expect(url).toContain('abstract');
  });

  it('handles arXiv ID format', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    await ssPaper(client, { paper_id: 'ARXIV:1706.03762' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('ARXIV:1706.03762');
  });

  it('converts arXiv DOI to ARXIV format', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    await ssPaper(client, { paper_id: 'DOI:10.48550/arXiv.1706.03762' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/ARXIV:1706.03762');
  });

  it('handles non-arXiv DOI format', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    await ssPaper(client, { paper_id: 'DOI:10.1145/3292500.3330919' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('DOI:10.1145');
  });

  it('returns paper with null abstract gracefully', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: PAPER_MISSING_ABSTRACT }]);
    const client = new SSClient();
    const result = await ssPaper(client, { paper_id: 'missing-abstract-id' }) as any;

    expect(result.abstract).toBeNull();
    expect(result.title).toBe('Restricted Paper');
  });

  it('returns not_found error for nonexistent paper', async () => {
    globalThis.fetch = mockFetch([{ status: 404, body: { message: 'Paper not found' } }]);
    const client = new SSClient();
    const result = await ssPaper(client, { paper_id: 'nonexistent' }) as any;

    expect(result.error).toBe('not_found');
  });

  it('auto-prefixes bare arXiv ID', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    await ssPaper(client, { paper_id: '2005.14165' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/ARXIV:2005.14165');
  });

  it('converts bare arXiv DOI to ARXIV format', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_PAPER }]);
    const client = new SSClient();
    await ssPaper(client, { paper_id: '10.48550/arXiv.1706.03762' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/ARXIV:1706.03762');
  });
});

describe('ssPaperBatch', () => {
  let originalFetch: typeof globalThis.fetch;

  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns multiple papers in one call', async () => {
    const batch = [REALISTIC_PAPER, PAPER_MISSING_ABSTRACT];
    globalThis.fetch = mockFetch([{ status: 200, body: batch }]);
    const client = new SSClient();
    const result = await ssPaperBatch(client, {
      paper_ids: ['649def34f8be52c8b66281af98ae884c09aef38b', 'missing-abstract-id'],
    });

    expect(result).toEqual(batch);
    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[1].method).toBe('POST');
    const body = JSON.parse(call[1].body);
    expect(body.ids).toHaveLength(2);
  });

  it('handles mixed found/not-found papers (nulls in array)', async () => {
    const batch = [REALISTIC_PAPER, null, PAPER_MISSING_ABSTRACT];
    globalThis.fetch = mockFetch([{ status: 200, body: batch }]);
    const client = new SSClient();
    const result = await ssPaperBatch(client, {
      paper_ids: ['id1', 'nonexistent', 'id3'],
    }) as any[];

    expect(result).toHaveLength(3);
    expect(result[0]?.paperId).toBe(REALISTIC_PAPER.paperId);
    expect(result[1]).toBeNull();
    expect(result[2]?.paperId).toBe('missing-abstract-id');
  });

  it('sends correct fields parameter', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: [] }]);
    const client = new SSClient();
    await ssPaperBatch(client, { paper_ids: ['a'] });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain(`fields=${encodeURIComponent(PAPER_FIELDS)}`);
  });
});
