import type { SSClient } from '../client.js';
import { PAPER_FIELDS } from '../fields.js';

const SEARCH_FIELDS = PAPER_FIELDS;

interface SearchArgs {
  query: string;
  limit?: number;
  offset?: number;
  year?: string;
  fields_of_study?: string;
  min_citation_count?: number;
  open_access_only?: boolean;
}

export async function ssRelevanceSearch(
  client: SSClient,
  args: SearchArgs,
): Promise<unknown> {
  const params: Record<string, string> = {
    query: args.query,
    fields: SEARCH_FIELDS,
    offset: String(args.offset ?? 0),
    limit: String(Math.min(args.limit ?? 10, 100)),
  };

  if (args.year !== undefined) params.year = args.year;
  if (args.fields_of_study !== undefined) params.fieldsOfStudy = args.fields_of_study;
  if (args.min_citation_count !== undefined) params.minCitationCount = String(args.min_citation_count);
  if (args.open_access_only) params.openAccessPdf = '';

  return client.get('/paper/search', params);
}
