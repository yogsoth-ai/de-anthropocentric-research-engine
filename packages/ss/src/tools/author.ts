import type { SSClient } from '../client.js';
import { AUTHOR_FIELDS, PAPER_FIELDS_NO_TLDR } from '../fields.js';

export async function ssAuthor(
  client: SSClient,
  args: { author_id: string },
): Promise<unknown> {
  return client.get(`/author/${encodeURIComponent(args.author_id)}`, {
    fields: AUTHOR_FIELDS,
  });
}

export async function ssAuthorPapers(
  client: SSClient,
  args: { author_id: string; offset?: number; limit?: number },
): Promise<unknown> {
  const params: Record<string, string> = {
    fields: PAPER_FIELDS_NO_TLDR,
    offset: String(args.offset ?? 0),
    limit: String(Math.min(args.limit ?? 100, 1000)),
  };
  return client.get(`/author/${encodeURIComponent(args.author_id)}/papers`, params);
}
