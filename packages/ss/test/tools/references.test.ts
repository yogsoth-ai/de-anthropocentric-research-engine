import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient } from '../../src/client.js';
import { ssReferences, ssCitations } from '../../src/tools/references.js';

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

const REALISTIC_REFERENCES = {
  offset: 0,
  next: 100,
  data: [
    {
      contexts: ['We build on the transformer architecture [1].'],
      intents: ['methodology'],
      isInfluential: true,
      citedPaper: {
        paperId: 'ref-001',
        title: 'Attention Is All You Need',
        abstract: 'The dominant sequence transduction models...',
        year: 2017,
        authors: [{ authorId: '1234', name: 'Ashish Vaswani' }],
        citationCount: 120000,
        externalIds: { ArXiv: '1706.03762' },
        url: 'https://www.semanticscholar.org/paper/ref-001',
      },
    },
    {
      contexts: ['Following the approach of [2] for pre-training...'],
      intents: ['background'],
      isInfluential: false,
      citedPaper: {
        paperId: 'ref-002',
        title: 'BERT: Pre-training of Deep Bidirectional Transformers',
        abstract: 'We introduce a new language representation model...',
        year: 2019,
        authors: [{ authorId: '5678', name: 'Jacob Devlin' }],
        citationCount: 80000,
        externalIds: { ArXiv: '1810.04805' },
        url: 'https://www.semanticscholar.org/paper/ref-002',
      },
    },
  ],
};

const REALISTIC_CITATIONS = {
  offset: 0,
  next: 100,
  data: [
    {
      contexts: ['The transformer model [Vaswani et al., 2017] has been widely adopted.'],
      intents: ['background'],
      isInfluential: true,
      citingPaper: {
        paperId: 'cit-001',
        title: 'GPT-4 Technical Report',
        abstract: null,
        year: 2023,
        authors: [{ authorId: '9999', name: 'OpenAI' }],
        citationCount: 5000,
        externalIds: { ArXiv: '2303.08774' },
        url: 'https://www.semanticscholar.org/paper/cit-001',
      },
    },
  ],
};

describe('ssReferences', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns references with citation context and intents', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_REFERENCES }]);
    const client = new SSClient();
    const result = await ssReferences(client, { paper_id: 'test-paper' }) as any;

    expect(result.data).toHaveLength(2);
    expect(result.data[0].contexts[0]).toContain('transformer');
    expect(result.data[0].intents).toContain('methodology');
    expect(result.data[0].isInfluential).toBe(true);
    expect(result.data[0].citedPaper.title).toBe('Attention Is All You Need');
  });

  it('passes offset and limit parameters', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 50, data: [] } }]);
    const client = new SSClient();
    await ssReferences(client, { paper_id: 'test', offset: 50, limit: 200 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('offset=50');
    expect(url).toContain('limit=200');
  });

  it('clamps limit to 1000', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 0, data: [] } }]);
    const client = new SSClient();
    await ssReferences(client, { paper_id: 'test', limit: 5000 });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=1000');
  });

  it('defaults offset=0 and limit=100', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 0, data: [] } }]);
    const client = new SSClient();
    await ssReferences(client, { paper_id: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('offset=0');
    expect(url).toContain('limit=100');
  });

  it('includes citedPaper fields in request', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 0, data: [] } }]);
    const client = new SSClient();
    await ssReferences(client, { paper_id: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('citedPaper.title');
    expect(url).toContain('contexts');
    expect(url).toContain('intents');
  });

  it('auto-prefixes bare arXiv ID', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_REFERENCES }]);
    const client = new SSClient();
    await ssReferences(client, { paper_id: '1706.03762' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/ARXIV:1706.03762/references');
  });
});

describe('ssCitations', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns citations with citing paper details', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_CITATIONS }]);
    const client = new SSClient();
    const result = await ssCitations(client, { paper_id: 'test-paper' }) as any;

    expect(result.data).toHaveLength(1);
    expect(result.data[0].citingPaper.title).toBe('GPT-4 Technical Report');
    expect(result.data[0].citingPaper.abstract).toBeNull();
    expect(result.data[0].isInfluential).toBe(true);
  });

  it('includes citingPaper fields in request', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { offset: 0, data: [] } }]);
    const client = new SSClient();
    await ssCitations(client, { paper_id: 'test' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('citingPaper.title');
    expect(url).toContain('contexts');
  });

  it('auto-prefixes bare arXiv ID', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: REALISTIC_CITATIONS }]);
    const client = new SSClient();
    await ssCitations(client, { paper_id: '1706.03762' });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('/paper/ARXIV:1706.03762/citations');
  });
});
