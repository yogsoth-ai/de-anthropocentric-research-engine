---
name: wiki-lint-fix
description: SOP wrapping vault_lint — run batch validation, report issues, optionally
  auto-fix safe problems.
execution: sop
---

# Wiki Lint Fix

Run batch validation on the vault and optionally auto-fix safe issues.

## HARD-GATE

<HARD-GATE>
Always run in report mode first. Review the issue list before enabling fix mode.
Never auto-fix without first presenting the issue summary to the calling tactic.
</HARD-GATE>

## Tool

`vault_lint`

## Parameters

| Param | Required | Description |
|-------|----------|-------------|
| fix | no | Auto-fix safe issues (default false) |

## Protocol

1. Call `vault_lint` with `fix: false` (report mode)
2. Categorize issues:
   - **Auto-fixable:** duplicate edges, stale index entries
   - **Manual:** broken wikilinks, orphan pages, missing frontmatter
3. Report issue summary to calling tactic
4. If calling tactic approves fix: call `vault_lint` with `fix: true`
5. Report what was fixed and what remains

## Auto-Fix Scope

Safe to auto-fix:
- Duplicate edges → deduplicate (keep first occurrence)
- Stale index entries → remove from _index.json

Requires manual resolution:
- Broken wikilinks → need to determine correct target or remove link
- Orphan pages → need to find appropriate connections
- Missing frontmatter → need to determine correct values

## Yield

Returns: `{ total_issues: number, errors: number, warnings: number, fixed: number }`
