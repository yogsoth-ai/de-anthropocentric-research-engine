import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient } from '../../src/client.js';
import { ssRecommendations } from '../../src/tools/recommendations.js';

function mockFetchSequence(responses: Array<{ status: number; body: unknown }>) {
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

const RECS_RESPONSE = {
  recommendedPapers: [
    { paperId: 'rec-001', title: 'Recommended Paper 1', year: 2023, citationCount: 500 },
    { paperId: 'rec-002', title: 'Recommended Paper 2', year: 2024, citationCount: 200 },
  ],
};

describe('ssRecommendations', () => {
  let originalFetch: typeof globalThis.fetch;
  beforeEach(() => { originalFetch = globalThis.fetch; });
  afterEach(() => { globalThis.fetch = originalFetch; });

  it('returns recommendations for S2 IDs (no resolution needed)', async () => {
    const s2Id = 'a'.repeat(40);
    globalThis.fetch = mockFetchSequence([
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    const result = await ssRecommendations(client, {
      positive_paper_ids: [s2Id],
    }) as any;

    expect(result.recommendedPapers).toHaveLength(2);
    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[1].method).toBe('POST');
    const body = JSON.parse(call[1].body);
    expect(body.positivePaperIds).toEqual([s2Id]);
  });

  it('auto-resolves arXiv IDs to S2 IDs before calling recommendations', async () => {
    globalThis.fetch = mockFetchSequence([
      { status: 200, body: { paperId: 'resolved-s2-id' } },
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    const result = await ssRecommendations(client, {
      positive_paper_ids: ['ARXIV:2106.15928'],
    }) as any;

    expect(result.recommendedPapers).toHaveLength(2);
    expect(globalThis.fetch).toHaveBeenCalledTimes(2);
    const recsCall = (globalThis.fetch as any).mock.calls[1];
    const body = JSON.parse(recsCall[1].body);
    expect(body.positivePaperIds).toEqual(['resolved-s2-id']);
  });

  it('includes negative paper IDs when provided', async () => {
    const posId = 'a'.repeat(40);
    const negId = 'b'.repeat(40);
    globalThis.fetch = mockFetchSequence([
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    await ssRecommendations(client, {
      positive_paper_ids: [posId],
      negative_paper_ids: [negId],
    });

    const call = (globalThis.fetch as any).mock.calls[0];
    const body = JSON.parse(call[1].body);
    expect(body.negativePaperIds).toEqual([negId]);
  });

  it('returns error when no positive IDs can be resolved', async () => {
    globalThis.fetch = mockFetchSequence([
      { status: 404, body: { message: 'Not found' } },
    ]);
    const client = new SSClient();
    const result = await ssRecommendations(client, {
      positive_paper_ids: ['ARXIV:nonexistent'],
    }) as any;

    expect(result.error).toBe('no_valid_papers');
  });

  it('skips unresolvable IDs but proceeds with valid ones', async () => {
    const validId = 'c'.repeat(40);
    globalThis.fetch = mockFetchSequence([
      { status: 404, body: {} },
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    const result = await ssRecommendations(client, {
      positive_paper_ids: ['ARXIV:bad', validId],
    }) as any;

    expect(result.recommendedPapers).toHaveLength(2);
  });

  it('auto-resolves bare arXiv ID (without ARXIV: prefix)', async () => {
    globalThis.fetch = mockFetchSequence([
      { status: 200, body: { paperId: 'resolved-bare-id' } },
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    const result = await ssRecommendations(client, {
      positive_paper_ids: ['2005.14165'],
    }) as any;

    expect(result.recommendedPapers).toHaveLength(2);
    const resolveUrl = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(resolveUrl).toContain('/paper/ARXIV:2005.14165');
  });

  it('clamps limit to 500', async () => {
    const s2Id = 'd'.repeat(40);
    globalThis.fetch = mockFetchSequence([
      { status: 200, body: RECS_RESPONSE },
    ]);
    const client = new SSClient();
    await ssRecommendations(client, {
      positive_paper_ids: [s2Id],
      limit: 9999,
    });

    const url = (globalThis.fetch as any).mock.calls[0][0] as string;
    expect(url).toContain('limit=500');
  });
});
