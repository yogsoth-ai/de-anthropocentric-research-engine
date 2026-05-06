import type { SSClient } from '../client.js';
import { PAPER_FIELDS_NO_TLDR } from '../fields.js';
import { isSSError } from '../client.js';
import { parsePaperId } from '../id.js';

interface RecsArgs {
  positive_paper_ids: string[];
  negative_paper_ids?: string[];
  limit?: number;
}

async function resolveToS2Id(client: SSClient, paperId: string): Promise<string | null> {
  const parsed = parsePaperId(paperId);
  if (parsed.kind === 'S2') return parsed.formatted;

  const result = await client.get<{ paperId: string }>(`/paper/${parsed.formatted}`, { fields: 'paperId' });
  if (isSSError(result)) return null;
  return result.paperId;
}

export async function ssRecommendations(
  client: SSClient,
  args: RecsArgs,
): Promise<unknown> {
  const positiveIds: string[] = [];
  for (const id of args.positive_paper_ids) {
    const s2Id = await resolveToS2Id(client, id);
    if (s2Id) positiveIds.push(s2Id);
  }
  if (positiveIds.length === 0) {
    return { error: 'no_valid_papers', message: 'None of the positive paper IDs could be resolved' };
  }

  const negativeIds: string[] = [];
  if (args.negative_paper_ids) {
    for (const id of args.negative_paper_ids) {
      const s2Id = await resolveToS2Id(client, id);
      if (s2Id) negativeIds.push(s2Id);
    }
  }

  const body: Record<string, unknown> = { positivePaperIds: positiveIds };
  if (negativeIds.length > 0) body.negativePaperIds = negativeIds;

  const limit = Math.min(args.limit ?? 100, 500);
  return client.post('/papers/', body, {
    fields: PAPER_FIELDS_NO_TLDR,
    limit: String(limit),
  }, true);
}
