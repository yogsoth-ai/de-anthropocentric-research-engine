import { describe, it, expect } from 'vitest';
import { parsePaperId, isKnownId } from '../src/id.js';

describe('parsePaperId', () => {
  it('detects prefixed ARXIV ID', () => {
    const r = parsePaperId('ARXIV:2005.14165');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
    expect(r.raw).toBe('ARXIV:2005.14165');
  });

  it('converts prefixed arXiv DOI to ARXIV kind', () => {
    const r = parsePaperId('DOI:10.48550/arXiv.2005.14165');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
    expect(r.raw).toBe('DOI:10.48550/arXiv.2005.14165');
  });

  it('keeps prefixed non-arXiv DOI as DOI kind', () => {
    const r = parsePaperId('DOI:10.1145/3292500.3330919');
    expect(r.kind).toBe('DOI');
    expect(r.formatted).toBe('DOI:10.1145/3292500.3330919');
  });

  it('detects prefixed PMID', () => {
    const r = parsePaperId('PMID:12345678');
    expect(r.kind).toBe('PMID');
    expect(r.formatted).toBe('PMID:12345678');
  });

  it('detects prefixed PMCID', () => {
    const r = parsePaperId('PMCID:PMC1234567');
    expect(r.kind).toBe('PMCID');
    expect(r.formatted).toBe('PMCID:PMC1234567');
  });

  it('detects prefixed ACL', () => {
    const r = parsePaperId('ACL:P18-1234');
    expect(r.kind).toBe('ACL');
    expect(r.formatted).toBe('ACL:P18-1234');
  });

  it('detects prefixed CorpusId', () => {
    const r = parsePaperId('CorpusId:215416146');
    expect(r.kind).toBe('CorpusId');
    expect(r.formatted).toBe('CorpusId:215416146');
  });

  it('detects prefixed URL', () => {
    const r = parsePaperId('URL:https://arxiv.org/abs/2005.14165');
    expect(r.kind).toBe('URL');
    expect(r.formatted).toBe('URL:https://arxiv.org/abs/2005.14165');
  });

  it('detects S2 ID (40-char hex)', () => {
    const hex = '649def34f8be52c8b66281af98ae884c09aef38b';
    const r = parsePaperId(hex);
    expect(r.kind).toBe('S2');
    expect(r.formatted).toBe(hex);
  });

  it('detects bare arXiv ID and adds prefix', () => {
    const r = parsePaperId('2005.14165');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
    expect(r.raw).toBe('2005.14165');
  });

  it('detects bare arXiv ID with version suffix', () => {
    const r = parsePaperId('2005.14165v3');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165v3');
  });

  it('converts bare arXiv DOI to ARXIV kind', () => {
    const r = parsePaperId('10.48550/arXiv.2005.14165');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
    expect(r.raw).toBe('10.48550/arXiv.2005.14165');
  });

  it('keeps bare non-arXiv DOI as DOI kind', () => {
    const r = parsePaperId('10.1145/3292500.3330919');
    expect(r.kind).toBe('DOI');
    expect(r.formatted).toBe('DOI:10.1145/3292500.3330919');
  });

  it('detects bare https URL and adds prefix', () => {
    const r = parsePaperId('https://arxiv.org/abs/2005.14165');
    expect(r.kind).toBe('URL');
    expect(r.formatted).toBe('URL:https://arxiv.org/abs/2005.14165');
  });

  it('detects bare http URL and adds prefix', () => {
    const r = parsePaperId('http://example.com/paper');
    expect(r.kind).toBe('URL');
    expect(r.formatted).toBe('URL:http://example.com/paper');
  });

  it('returns UNKNOWN for unrecognized input', () => {
    const r = parsePaperId('some-random-string');
    expect(r.kind).toBe('UNKNOWN');
    expect(r.formatted).toBe('some-random-string');
  });

  it('is case-insensitive for prefixes', () => {
    const r = parsePaperId('arxiv:2005.14165');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
  });

  it('trims whitespace from input', () => {
    const r = parsePaperId('  ARXIV:2005.14165  ');
    expect(r.kind).toBe('ARXIV');
    expect(r.formatted).toBe('ARXIV:2005.14165');
    expect(r.raw).toBe('ARXIV:2005.14165');
  });
});

describe('isKnownId', () => {
  it('returns true for known kinds', () => {
    expect(isKnownId(parsePaperId('ARXIV:2005.14165'))).toBe(true);
    expect(isKnownId(parsePaperId('a'.repeat(40)))).toBe(true);
  });

  it('returns false for UNKNOWN kind', () => {
    expect(isKnownId(parsePaperId('random'))).toBe(false);
  });
});
