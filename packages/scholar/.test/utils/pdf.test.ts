import { describe, it, before, after, mock } from "node:test";
import assert from "node:assert/strict";
import { writeFileSync, mkdirSync, rmSync } from "fs";
import { join } from "path";
import { tmpdir } from "os";
import { content, type ProgressCallback } from "../../src/utils/pdf.js";

describe("pdf (Apify)", () => {
  const originalFetch = globalThis.fetch;
  let originalEnv: string | undefined;
  let tempDir: string;
  let tempPdf: string;

  before(() => {
    originalEnv = process.env.APIFY_TOKEN;
    process.env.APIFY_TOKEN = "test-apify-token";
    tempDir = join(tmpdir(), `dare-scholar-pdf-test-${Date.now()}`);
    mkdirSync(tempDir, { recursive: true });
    tempPdf = join(tempDir, "sample.pdf");
    writeFileSync(tempPdf, Buffer.from("%PDF-1.4 fake content"));
  });

  after(() => {
    globalThis.fetch = originalFetch;
    if (originalEnv === undefined) delete process.env.APIFY_TOKEN;
    else process.env.APIFY_TOKEN = originalEnv;
    rmSync(tempDir, { recursive: true, force: true });
  });

  function mockApifyFlow(opts: {
    markdown?: string;
    pollsBeforeReady?: number;
    startOk?: boolean;
    runStatus?: string;
    emptyDataset?: boolean;
  }): void {
    const {
      markdown = "# Paper",
      pollsBeforeReady = 0,
      startOk = true,
      runStatus,
      emptyDataset = false,
    } = opts;
    let pollCount = 0;

    globalThis.fetch = (async (
      url: string | URL | Request,
      init?: RequestInit,
    ): Promise<Response> => {
      const urlStr = typeof url === "string" ? url : url.toString();

      if (
        urlStr.includes("/acts/clearpath~pdf-to-markdown-api/runs") &&
        init?.method === "POST"
      ) {
        return {
          ok: startOk,
          status: startOk ? 201 : 400,
          statusText: startOk ? "Created" : "Bad Request",
          json: async () => ({
            data: { id: "run_abc123", defaultDatasetId: "ds_xyz" },
          }),
        } as unknown as Response;
      }

      if (urlStr.includes("/actor-runs/run_abc123")) {
        pollCount++;
        const status =
          runStatus ??
          (pollCount > pollsBeforeReady ? "SUCCEEDED" : "RUNNING");
        return {
          ok: true,
          status: 200,
          json: async () => ({ data: { status } }),
        } as unknown as Response;
      }

      if (urlStr.includes("/datasets/ds_xyz/items")) {
        const items = emptyDataset ? [] : [{ markdown }];
        return {
          ok: true,
          status: 200,
          json: async () => items,
        } as unknown as Response;
      }

      throw new Error(`Unexpected fetch: ${urlStr}`);
    }) as typeof fetch;
  }

  // ── URL source ───────────────────────────────────────────

  it("converts URL source to markdown", async () => {
    mockApifyFlow({ markdown: "# From URL" });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, "# From URL");
  });

  it("sends pdfUrls for URL source", async () => {
    const calls: { url: string; body?: string }[] = [];
    const origMock = globalThis.fetch;
    mockApifyFlow({ markdown: "# Test" });
    const mockedFetch = globalThis.fetch;
    globalThis.fetch = (async (
      url: string | URL | Request,
      init?: RequestInit,
    ): Promise<Response> => {
      const urlStr = typeof url === "string" ? url : url.toString();
      calls.push({ url: urlStr, body: init?.body as string });
      return (mockedFetch as any)(url, init);
    }) as typeof fetch;

    await content("https://example.com/paper.pdf");
    const startCall = calls.find((c) =>
      c.url.includes("clearpath~pdf-to-markdown-api"),
    );
    assert.ok(startCall);
    const body = JSON.parse(startCall!.body!);
    assert.deepEqual(body.pdfUrls, ["https://example.com/paper.pdf"]);
    assert.equal(body.pdfBase64Items, undefined);
  });

  // ── Local file source ────────────────────────────────────

  it("converts local file via base64 encoding", async () => {
    mockApifyFlow({ markdown: "# From Local" });
    const result = await content(tempPdf);
    assert.equal(result, "# From Local");
  });

  it("sends pdfBase64Items for local file", async () => {
    const calls: { url: string; body?: string }[] = [];
    mockApifyFlow({ markdown: "# Test" });
    const mockedFetch = globalThis.fetch;
    globalThis.fetch = (async (
      url: string | URL | Request,
      init?: RequestInit,
    ): Promise<Response> => {
      const urlStr = typeof url === "string" ? url : url.toString();
      calls.push({ url: urlStr, body: init?.body as string });
      return (mockedFetch as any)(url, init);
    }) as typeof fetch;

    await content(tempPdf);
    const startCall = calls.find((c) =>
      c.url.includes("clearpath~pdf-to-markdown-api"),
    );
    assert.ok(startCall);
    const body = JSON.parse(startCall!.body!);
    assert.equal(body.pdfUrls, undefined);
    assert.equal(body.pdfBase64Items.length, 1);
    assert.equal(body.pdfBase64Items[0].filename, "sample.pdf");
    assert.equal(typeof body.pdfBase64Items[0].data, "string");
  });

  // ── Polling ──────────────────────────────────────────────

  it("polls until run succeeds", async () => {
    mockApifyFlow({ markdown: "# After Polls", pollsBeforeReady: 2 });
    const result = await content("https://example.com/poll.pdf");
    assert.equal(result, "# After Polls");
  });

  // ── Error cases (return null) ────────────────────────────

  it("returns null for nonexistent local file", async () => {
    const result = await content("/nonexistent/path/file.pdf");
    assert.equal(result, null);
  });

  it("returns null when Actor start fails", async () => {
    mockApifyFlow({ startOk: false });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, null);
  });

  it("returns null when run status is FAILED", async () => {
    mockApifyFlow({ runStatus: "FAILED" });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, null);
  });

  it("returns null when run status is ABORTED", async () => {
    mockApifyFlow({ runStatus: "ABORTED" });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, null);
  });

  it("returns null when run status is TIMED-OUT", async () => {
    mockApifyFlow({ runStatus: "TIMED-OUT" });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, null);
  });

  it("returns null when dataset is empty", async () => {
    mockApifyFlow({ emptyDataset: true });
    const result = await content("https://example.com/paper.pdf");
    assert.equal(result, null);
  });

  it("returns null when APIFY_TOKEN is not set", async () => {
    const saved = process.env.APIFY_TOKEN;
    delete process.env.APIFY_TOKEN;
    try {
      const result = await content("https://example.com/paper.pdf");
      assert.equal(result, null);
    } finally {
      process.env.APIFY_TOKEN = saved;
    }
  });

  // ── Progress callback ────────────────────────────────────

  it("invokes progress callback", async () => {
    mockApifyFlow({ markdown: "# Progress Test" });
    const messages: string[] = [];
    const onProgress: ProgressCallback = (info) => {
      messages.push(info.message);
    };
    await content("https://example.com/paper.pdf", onProgress);
    assert.ok(messages.length >= 2);
    assert.ok(messages.some((m) => m.includes("Starting")));
    assert.ok(messages.some((m) => m.includes("Done")));
  });

  // ── Simulation: realistic Apify dataset response ─────────

  describe("simulation: realistic paper conversion", () => {
    it("handles a realistic multi-section paper markdown", async () => {
      const paperMd = [
        "# Attention Is All You Need",
        "",
        "## Abstract",
        "",
        "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks...",
        "",
        "## 1 Introduction",
        "",
        "Recurrent neural networks, long short-term memory and gated recurrent neural networks...",
        "",
        "## 2 Background",
        "",
        "The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU...",
        "",
        "## References",
        "",
        '[1] Bahdanau, D. "Neural Machine Translation by Jointly Learning to Align and Translate." ICLR 2015.',
      ].join("\n");

      mockApifyFlow({ markdown: paperMd, pollsBeforeReady: 1 });
      const result = await content("https://arxiv.org/pdf/1706.03762");
      assert.ok(result);
      assert.ok(result.includes("# Attention Is All You Need"));
      assert.ok(result.includes("## Abstract"));
      assert.ok(result.includes("## References"));
      assert.ok(result.includes("Bahdanau"));
    });

    it("handles markdown with unicode content", async () => {
      const unicodeContent =
        "# 论文\n\n数学公式: ∑_{i=1}^{n} x_i = S\n\nÜber résumé";
      mockApifyFlow({ markdown: unicodeContent });
      const result = await content("https://example.com/unicode.pdf");
      assert.equal(result, unicodeContent);
    });
  });
});
