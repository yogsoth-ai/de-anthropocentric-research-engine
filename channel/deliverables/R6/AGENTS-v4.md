<!-- BEGIN DARE RESEARCH ENGINE -->
## DARE Research Engine

Use DARE for AI Research tasks and whenever the user explicitly asks for DARE.

1. Treat `CC` and `Claude Code` in upstream DARE documents as `Codex`.
2. Resolve the DARE v4 skill root from the first existing path:
   - `.dare/skills/` in a project where DARE v4 was installed
   - `v4/skills/` in the DARE source repository
   DARE v4 replaces v3. Do not combine it with or fall back to a v3 skill root; the renamed v4 entry skills have the same names as v3, but are not a v3 fallback.
3. Read `<skill-root>/de-anthropocentric-research-engine/SKILL.md` first.
4. Read `<skill-root>/research-catalog/SKILL.md` before selecting research tactics.
5. Treat `You MUST load skill X` statements in each `SKILL.md` body as the authoritative call relations. `registry/graph.json` is a machine index, not an agent runtime read.
6. When a DARE document says to load a skill, open `<skill-root>/<skill-name>/SKILL.md` and follow it as the operative workflow.
7. Load called skills only when needed; do not load the entire DARE skill tree.
8. Preserve runtime context in `context/INDEX.md` and its related context files.
9. Never write API keys or secrets into specs, context files, or committed configuration.

The DARE skill tree is an on-demand research knowledge base, not a Codex skill-discovery directory.
<!-- END DARE RESEARCH ENGINE -->
