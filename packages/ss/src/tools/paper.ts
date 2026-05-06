import type { SSClient } from '../client.js';
import { PAPER_FIELDS } from '../fields.js';
import { parsePaperId } from '../id.js';

export async function ssPaper(
  client: SSClient,
  args: { paper_id: string },
): Promise<unknown> {
  const id = parsePaperId(args.paper_id).formatted;
  return client.get(`/paper/${id}`, {
    fields: PAPER_FIELDS,
  });
}

export async function ssPaperBatch(
  client: SSClient,
  args: { paper_ids: string[] },
): Promise<unknown> {
  return client.post('/paper/batch', { ids: args.paper_ids.map(id => parsePaperId(id).formatted) }, {
    fields: PAPER_FIELDS,
  });
}
