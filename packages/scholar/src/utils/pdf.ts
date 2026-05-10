import { resolve, basename } from "path";
import { readFileSync, existsSync } from "fs";

const APIFY_BASE = "https://api.apify.com/v2";
const POLL_INTERVAL = 3000;
const POLL_TIMEOUT = 600_000;

export type ProgressCallback = (info: {
  message: string;
  current?: number;
  total?: number;
}) => void | Promise<void>;

function getToken(): string {
  const token = process.env.APIFY_TOKEN;
  if (!token) throw new Error("APIFY_TOKEN not set");
  return token;
}

export async function content(
  source: string,
  onProgress?: ProgressCallback,
): Promise<string | null> {
  try {
    const token = getToken();
    let input: Record<string, unknown>;

    if (source.startsWith("http://") || source.startsWith("https://")) {
      input = { pdfUrls: [source], outputMode: "markdown" };
    } else {
      const fullPath = resolve(source);
      if (!existsSync(fullPath)) return null;
      const pdfBuf = readFileSync(fullPath);
      const base64 = pdfBuf.toString("base64");
      input = {
        pdfBase64Items: [{ filename: basename(fullPath), data: base64 }],
        outputMode: "markdown",
      };
    }

    await onProgress?.({ message: "Starting conversion..." });

    const startRes = await fetch(
      `${APIFY_BASE}/acts/clearpath~pdf-to-markdown-api/runs?token=${token}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(input),
      },
    );
    if (!startRes.ok) return null;

    const startData = (await startRes.json()) as any;
    const runId: string = startData.data.id;
    const datasetId: string = startData.data.defaultDatasetId;

    await onProgress?.({ message: "Processing..." });
    const deadline = Date.now() + POLL_TIMEOUT;

    while (Date.now() < deadline) {
      await new Promise((r) => setTimeout(r, POLL_INTERVAL));
      const pollRes = await fetch(
        `${APIFY_BASE}/actor-runs/${runId}?token=${token}`,
      );
      const pollData = (await pollRes.json()) as any;
      const status: string = pollData.data.status;

      if (status === "SUCCEEDED") {
        const dsRes = await fetch(
          `${APIFY_BASE}/datasets/${datasetId}/items?token=${token}`,
        );
        const items = (await dsRes.json()) as any[];
        if (!items.length || !items[0].markdown) return null;
        await onProgress?.({ message: "Done" });
        return items[0].markdown;
      }

      if (status === "FAILED" || status === "ABORTED" || status === "TIMED-OUT")
        return null;
    }

    return null;
  } catch {
    return null;
  }
}
