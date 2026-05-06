export type PaperIdKind =
  | 'S2' | 'ARXIV' | 'DOI' | 'PMID' | 'PMCID'
  | 'ACL' | 'CorpusId' | 'URL' | 'UNKNOWN';

export interface ParsedPaperId {
  kind: PaperIdKind;
  raw: string;
  formatted: string;
}

const PREFIXES: PaperIdKind[] = [
  'ARXIV', 'DOI', 'PMID', 'PMCID', 'ACL', 'CorpusId', 'URL',
];

const S2_HEX = /^[0-9a-f]{40}$/i;
const BARE_ARXIV = /^\d{4}\.\d{4,5}(v\d+)?$/;
const BARE_DOI = /^10\.\d{4,}\//;
const BARE_URL = /^https?:\/\//i;
const ARXIV_DOI = /^10\.48550\/arXiv\.(.+)$/i;

export function parsePaperId(input: string): ParsedPaperId {
  const trimmed = input.trim();

  for (const prefix of PREFIXES) {
    if (trimmed.toLowerCase().startsWith(prefix.toLowerCase() + ':')) {
      const value = trimmed.slice(prefix.length + 1);
      if (prefix === 'DOI') {
        const m = value.match(ARXIV_DOI);
        if (m) return { kind: 'ARXIV', raw: trimmed, formatted: `ARXIV:${m[1]}` };
      }
      return { kind: prefix, raw: trimmed, formatted: `${prefix}:${value}` };
    }
  }

  if (S2_HEX.test(trimmed)) {
    return { kind: 'S2', raw: trimmed, formatted: trimmed };
  }

  if (BARE_ARXIV.test(trimmed)) {
    return { kind: 'ARXIV', raw: trimmed, formatted: `ARXIV:${trimmed}` };
  }

  if (BARE_DOI.test(trimmed)) {
    const m = trimmed.match(ARXIV_DOI);
    if (m) return { kind: 'ARXIV', raw: trimmed, formatted: `ARXIV:${m[1]}` };
    return { kind: 'DOI', raw: trimmed, formatted: `DOI:${trimmed}` };
  }

  if (BARE_URL.test(trimmed)) {
    return { kind: 'URL', raw: trimmed, formatted: `URL:${trimmed}` };
  }

  return { kind: 'UNKNOWN', raw: trimmed, formatted: trimmed };
}

export function isKnownId(id: ParsedPaperId): boolean {
  return id.kind !== 'UNKNOWN';
}
