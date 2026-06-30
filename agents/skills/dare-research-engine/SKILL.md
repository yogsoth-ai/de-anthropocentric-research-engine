---
name: dare-research-engine
description: Use the DARE research engine to crystallize research goals, write executable research specs, and execute staged research workflows.
---

# DARE Codex Adapter

You are running the Codex port of DARE.

When this skill is invoked:

1. Treat "CC" and "Claude Code" in upstream DARE documents as "Codex".
2. Resolve the DARE skill root from the first existing path:
   - `.dare/skills/` when this adapter was installed into another repository
   - `skills/` when running from the DARE repository clone itself
3. Read `<skill-root>/de-anthropocentric-research-engine/SKILL.md` first.
4. Read `<skill-root>/research-catalog/SKILL.md` before selecting research packages.
5. Treat YAML `dependencies` in each upstream `SKILL.md` as the authoritative call graph.
6. Open dependency skills from `<skill-root>/<skill-name>/SKILL.md` only when needed.
7. Use Codex-style invocation names such as `$dare-research-engine`, not Claude slash commands.
8. Preserve runtime context in `context/INDEX.md` and related context files.
9. Never write API keys or secrets into specs, context files, or committed config.

Do not load every upstream skill up front. The upstream `skills/` tree is the DARE knowledge base, not a Codex skill registry.
