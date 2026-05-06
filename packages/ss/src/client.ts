const GRAPH_BASE = 'https://api.semanticscholar.org/graph/v1';
const RECS_BASE = 'https://api.semanticscholar.org/recommendations/v1';

export interface SSError {
  error: string;
  status?: number;
  message?: string;
  paperId?: string;
}

export class SSClient {
  private apiKey: string | undefined;
  private lastRequestTime = 0;
  private minInterval: number;

  constructor(apiKey?: string) {
    this.apiKey = apiKey;
    this.minInterval = apiKey ? 1000 : 100;
  }

  private async rateLimit(): Promise<void> {
    const now = Date.now();
    const elapsed = now - this.lastRequestTime;
    if (elapsed < this.minInterval) {
      await new Promise(r => setTimeout(r, this.minInterval - elapsed));
    }
    this.lastRequestTime = Date.now();
  }

  private headers(): Record<string, string> {
    const h: Record<string, string> = { 'Accept': 'application/json' };
    if (this.apiKey) h['x-api-key'] = this.apiKey;
    return h;
  }

  async get<T = unknown>(path: string, params?: Record<string, string>, useRecsBase = false): Promise<T | SSError> {
    const base = useRecsBase ? RECS_BASE : GRAPH_BASE;
    const url = new URL(base + path);
    if (params) {
      for (const [k, v] of Object.entries(params)) {
        url.searchParams.set(k, v);
      }
    }
    return this.request<T>(url.toString(), { method: 'GET' });
  }

  async post<T = unknown>(path: string, body: unknown, params?: Record<string, string>, useRecsBase = false): Promise<T | SSError> {
    const base = useRecsBase ? RECS_BASE : GRAPH_BASE;
    const url = new URL(base + path);
    if (params) {
      for (const [k, v] of Object.entries(params)) {
        url.searchParams.set(k, v);
      }
    }
    return this.request<T>(url.toString(), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
  }

  private async request<T>(url: string, init: RequestInit, retries = 3): Promise<T | SSError> {
    await this.rateLimit();
    const mergedHeaders = { ...this.headers(), ...(init.headers as Record<string, string> ?? {}) };

    let lastError: SSError = { error: 'unknown' };
    for (let attempt = 0; attempt < retries; attempt++) {
      try {
        const res = await fetch(url, { ...init, headers: mergedHeaders });

        if (res.ok) return await res.json() as T;

        if (res.status === 404) {
          return { error: 'not_found', status: 404, message: `Not found: ${url}` };
        }

        if (res.status === 429) {
          lastError = { error: 'rate_limited', status: 429 };
          const backoff = Math.pow(2, attempt) * 1000;
          await new Promise(r => setTimeout(r, backoff));
          continue;
        }

        if (res.status >= 500) {
          lastError = { error: 'api_error', status: res.status, message: await res.text().catch(() => '') };
          if (attempt < retries - 1) {
            await new Promise(r => setTimeout(r, 1000));
            continue;
          }
          return lastError;
        }

        return { error: 'api_error', status: res.status, message: await res.text().catch(() => '') };
      } catch (e: any) {
        lastError = { error: 'network_error', message: e.message };
        if (attempt < retries - 1) {
          await new Promise(r => setTimeout(r, 1000));
          continue;
        }
      }
    }
    return lastError;
  }
}

export function isSSError(v: unknown): v is SSError {
  return typeof v === 'object' && v !== null && 'error' in v && typeof (v as any).error === 'string';
}
