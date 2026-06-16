# @yogsoth-ai/dare

One-command installer for the De-Anthropocentric Research Engine skill library.

## Usage

In your project directory:

```bash
npx @yogsoth-ai/dare install
```

This copies the full DARE skill body into `./.claude/skills/` (creating it if
needed) and writes a `.mcp.json` template if you don't already have one.

- Existing skills with the same name are **never overwritten** — re-running only
  adds what's missing.
- An existing `.mcp.json` is left untouched.

After installing, fill in your API keys in `.mcp.json`, then invoke
`/de-anthropocentric-research-engine` in Claude Code.

> Note: the `install` here is a subcommand of this CLI, not `npm install`.
