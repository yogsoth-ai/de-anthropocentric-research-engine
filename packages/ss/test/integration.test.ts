/**
 * Integration tests — require live Semantic Scholar API access.
 * Run manually: SS_API_KEY=<key> npx vitest run .test/integration.test.ts
 *
 * These tests are excluded from the default `npm test` run.
 */
import { describe, it, expect } from 'vitest';
import { SSClient } from '../src/client.js';
import { ssPaper, ssPaperBatch } from '../src/tools/paper.js';
import { ssReferences, ssCitations } from '../src/tools/references.js';
import { ssRecommendations } from '../src/tools/recommendations.js';
import { ssAuthor, ssAuthorPapers } from '../src/tools/author.js';
import { isSSError } from '../src/client.js';

const ATTENTION_ARXIV = 'ARXIV:1706.03762';
const ATTENTION_S2 = '204e3073870fae3d05bcbc2f6a8e263d9b72e776';
const VASWANI_AUTHOR_ID = '1741101';

describe('Integration: ssPaper', () => {
  it('fetches Attention Is All You Need by arXiv ID', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssPaper(client, { paper_id: ATTENTION_ARXIV }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.title).toContain('Attention');
    expect(result.year).toBe(2017);
    expect(result.citationCount).toBeGreaterThan(50000);
    expect(result.isOpenAccess).toBe(true);
  });

  it('fetches paper by S2 ID', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssPaper(client, { paper_id: ATTENTION_S2 }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.paperId).toBe(ATTENTION_S2);
  });
});

describe('Integration: ssPaperBatch', () => {
  it('fetches multiple papers at once', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssPaperBatch(client, {
      paper_ids: [ATTENTION_ARXIV, 'ARXIV:1810.04805'],
    }) as any[];

    expect(Array.isArray(result)).toBe(true);
    expect(result).toHaveLength(2);
    expect(result[0]?.title).toContain('Attention');
    expect(result[1]?.title).toContain('BERT');
  });
});

describe('Integration: ssReferences', () => {
  it('returns references for Attention paper', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssReferences(client, { paper_id: ATTENTION_ARXIV, limit: 10 }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.data.length).toBeGreaterThan(0);
    expect(result.data[0]).toHaveProperty('citedPaper');
    expect(result.data[0]).toHaveProperty('contexts');
  });
});

describe('Integration: ssCitations', () => {
  it('returns citations for Attention paper', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssCitations(client, { paper_id: ATTENTION_ARXIV, limit: 10 }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.data.length).toBeGreaterThan(0);
    expect(result.data[0]).toHaveProperty('citingPaper');
  });
});

describe('Integration: ssRecommendations', () => {
  it('returns recommendations for Attention paper', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssRecommendations(client, {
      positive_paper_ids: [ATTENTION_ARXIV],
      limit: 10,
    }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.recommendedPapers.length).toBeGreaterThan(0);
  });
});

describe('Integration: ssAuthor', () => {
  it('returns Vaswani author details', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssAuthor(client, { author_id: VASWANI_AUTHOR_ID }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.name).toContain('Vaswani');
    expect(result.hIndex).toBeGreaterThan(10);
  });
});

describe('Integration: ssAuthorPapers', () => {
  it('returns papers by Vaswani', async () => {
    const client = new SSClient(process.env.SS_API_KEY);
    const result = await ssAuthorPapers(client, { author_id: VASWANI_AUTHOR_ID, limit: 10 }) as any;

    expect(isSSError(result)).toBe(false);
    expect(result.data.length).toBeGreaterThan(0);
    expect(result.data[0]).toHaveProperty('title');
  });
});
