import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { SSClient, isSSError } from '../src/client.js';

function mockFetch(responses: Array<{ status: number; body: unknown; delay?: number }>) {
  let callIndex = 0;
  return vi.fn(async () => {
    const r = responses[callIndex++] ?? responses[responses.length - 1];
    if (r.delay) await new Promise(res => setTimeout(res, r.delay));
    return {
      ok: r.status >= 200 && r.status < 300,
      status: r.status,
      json: async () => r.body,
      text: async () => JSON.stringify(r.body),
    } as Response;
  });
}

describe('SSClient', () => {
  let originalFetch: typeof globalThis.fetch;

  beforeEach(() => {
    originalFetch = globalThis.fetch;
  });

  afterEach(() => {
    globalThis.fetch = originalFetch;
  });

  it('makes a successful GET request', async () => {
    const paper = { paperId: 'abc123', title: 'Test Paper' };
    globalThis.fetch = mockFetch([{ status: 200, body: paper }]);

    const client = new SSClient();
    const result = await client.get('/paper/abc123', { fields: 'title' });

    expect(result).toEqual(paper);
    expect(globalThis.fetch).toHaveBeenCalledOnce();
  });

  it('makes a successful POST request', async () => {
    const papers = [{ paperId: 'a' }, { paperId: 'b' }];
    globalThis.fetch = mockFetch([{ status: 200, body: papers }]);

    const client = new SSClient();
    const result = await client.post('/paper/batch', { ids: ['a', 'b'] }, { fields: 'title' });

    expect(result).toEqual(papers);
    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[1].method).toBe('POST');
    expect(call[1].body).toBe(JSON.stringify({ ids: ['a', 'b'] }));
  });

  it('includes x-api-key header when API key is provided', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: {} }]);

    const client = new SSClient('my-secret-key');
    await client.get('/paper/abc123');

    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[1].headers['x-api-key']).toBe('my-secret-key');
  });

  it('does not include x-api-key header when no API key', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: {} }]);

    const client = new SSClient();
    await client.get('/paper/abc123');

    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[1].headers['x-api-key']).toBeUndefined();
  });

  it('returns structured error on 404', async () => {
    globalThis.fetch = mockFetch([{ status: 404, body: { message: 'Paper not found' } }]);

    const client = new SSClient();
    const result = await client.get('/paper/nonexistent');

    expect(isSSError(result)).toBe(true);
    if (isSSError(result)) {
      expect(result.error).toBe('not_found');
      expect(result.status).toBe(404);
    }
  });

  it('retries on 429 with exponential backoff', async () => {
    globalThis.fetch = mockFetch([
      { status: 429, body: {} },
      { status: 429, body: {} },
      { status: 200, body: { paperId: 'recovered' } },
    ]);

    const client = new SSClient();
    const result = await client.get('/paper/busy');

    expect(result).toEqual({ paperId: 'recovered' });
    expect(globalThis.fetch).toHaveBeenCalledTimes(3);
  });

  it('returns rate_limited error after max retries on 429', async () => {
    globalThis.fetch = mockFetch([
      { status: 429, body: {} },
      { status: 429, body: {} },
      { status: 429, body: {} },
    ]);

    const client = new SSClient();
    const result = await client.get('/paper/overloaded');

    expect(isSSError(result)).toBe(true);
    if (isSSError(result)) {
      expect(result.error).toBe('rate_limited');
    }
  });

  it('retries once on 500 then returns api_error', async () => {
    globalThis.fetch = mockFetch([
      { status: 500, body: 'Internal Server Error' },
      { status: 500, body: 'Internal Server Error' },
      { status: 500, body: 'Internal Server Error' },
    ]);

    const client = new SSClient();
    const result = await client.get('/paper/broken');

    expect(isSSError(result)).toBe(true);
    if (isSSError(result)) {
      expect(result.error).toBe('api_error');
      expect(result.status).toBe(500);
    }
  });

  it('returns network_error on fetch failure', async () => {
    globalThis.fetch = vi.fn(async () => { throw new Error('ECONNREFUSED'); });

    const client = new SSClient();
    const result = await client.get('/paper/offline');

    expect(isSSError(result)).toBe(true);
    if (isSSError(result)) {
      expect(result.error).toBe('network_error');
      expect(result.message).toBe('ECONNREFUSED');
    }
  });

  it('uses recommendations base URL for /recommendations paths', async () => {
    globalThis.fetch = mockFetch([{ status: 200, body: { recommendedPapers: [] } }]);

    const client = new SSClient();
    await client.get('/recommendations/v1/papers/abc123');

    const call = (globalThis.fetch as any).mock.calls[0];
    expect(call[0]).toContain('/recommendations/v1/papers/abc123');
  });
});

describe('isSSError', () => {
  it('returns true for SSError objects', () => {
    expect(isSSError({ error: 'not_found', status: 404 })).toBe(true);
  });

  it('returns false for non-error objects', () => {
    expect(isSSError({ paperId: 'abc', title: 'Test' })).toBe(false);
    expect(isSSError(null)).toBe(false);
    expect(isSSError('string')).toBe(false);
  });
});
