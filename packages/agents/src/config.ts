// packages/agents/src/config.ts
import { getModel, type Model, type Api } from '@mariozechner/pi-ai';

/**
 * Bridge DARE env vars → pi-ai model.
 *
 * Primary env vars (set in .mcp.json dare-agents entry):
 * - DARE_AGENTS_PROVIDER  → pi-ai provider name (default: 'openrouter')
 *                           Supported: 'openrouter', 'anthropic', 'openai', etc.
 * - DARE_AGENTS_MODEL     → model ID (default depends on provider)
 * - DARE_AGENTS_API_KEY   → API key (falls back to provider-specific env vars)
 * - DARE_AGENTS_BASE_URL  → overrides model.baseUrl (for custom endpoints)
 *
 * Legacy env vars (fallbacks for backward compatibility):
 * - ANTHROPIC_MODEL       → model ID fallback
 * - ANTHROPIC_BASE_URL    → base URL fallback
 * - ANTHROPIC_AUTH_TOKEN   → API key fallback
 * - ANTHROPIC_API_KEY      → API key fallback
 * - OPENROUTER_API_KEY     → API key fallback (for openrouter provider)
 */

const PROVIDER_DEFAULTS: Record<string, string> = {
  openrouter: 'z-ai/glm-5',
  anthropic: 'claude-sonnet-4-20250514',
  openai: 'gpt-4o-mini',
};

export function getConfiguredModel(): Model<Api> {
  const provider = process.env.DARE_AGENTS_PROVIDER || 'openrouter';
  const modelId = process.env.DARE_AGENTS_MODEL
    || process.env.ANTHROPIC_MODEL
    || PROVIDER_DEFAULTS[provider]
    || 'z-ai/glm-5';
  let model = getModel(provider as any, modelId as any);
  if (!model) {
    const apiMap: Record<string, Api> = {
      openai: 'openai-completions',
      openrouter: 'openai-completions',
      anthropic: 'anthropic-messages',
      groq: 'openai-completions',
      cerebras: 'openai-completions',
      mistral: 'openai-completions',
    };
    model = {
      id: modelId,
      name: modelId,
      api: apiMap[provider] || 'openai-completions',
      provider,
      baseUrl: '',
      reasoning: false,
      input: ['text', 'image'],
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
      contextWindow: 128000,
      maxTokens: 16384,
    } as Model<Api>;
  }
  const baseUrl = process.env.DARE_AGENTS_BASE_URL
    || (provider === 'anthropic' ? process.env.ANTHROPIC_BASE_URL : undefined);
  if (baseUrl) {
    model.baseUrl = baseUrl;
  }
  const maxTokensOverride = process.env.DARE_AGENTS_MAX_TOKENS;
  if (maxTokensOverride) {
    model.maxTokens = parseInt(maxTokensOverride, 10);
  } else if (model.reasoning && model.maxTokens < 16384) {
    model.maxTokens = 16384;
  }
  return model;
}

export function getApiKey(): string {
  return process.env.DARE_AGENTS_API_KEY
    || process.env.OPENROUTER_API_KEY
    || process.env.ANTHROPIC_AUTH_TOKEN
    || process.env.ANTHROPIC_API_KEY
    || '';
}

/**
 * Build options object for pi-ai `complete()` / `stream()` calls.
 * Includes apiKey and maxTokens so the underlying provider sends
 * the right parameters to the API.
 *
 * Accepts an optional model to read maxTokens from (avoids calling
 * getConfiguredModel() again when the caller already has it).
 */
export function getCompleteOptions(model?: Model<Api>): { apiKey: string; maxTokens: number } {
  const maxTokens = model?.maxTokens ?? 16384;
  return {
    apiKey: getApiKey(),
    maxTokens,
  };
}
