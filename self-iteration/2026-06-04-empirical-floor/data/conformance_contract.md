# DARE Conformance Contract (Study 1a)

What any runtime must satisfy to execute the skill body.

## `subagent` — 363 skills
**Requirement:** Runtime MUST spawn an isolated sub-agent and recover its structured output.

## `tactic` — 70 skills
**Requirement:** Runtime MUST sequence multiple SOPs and aggregate their outputs.

## `strategy` — 50 skills
**Requirement:** Runtime MUST orchestrate nested tactics with budget/gate tracking.

## `campaign` — 25 skills
**Requirement:** Runtime MUST drive an end-to-end multi-strategy pipeline with phase state.

## `dialogue` — 10 skills
**Requirement:** Runtime MUST support multi-turn interactive Q&A with the user.

## `import` — 5 skills
**Requirement:** Runtime MUST resolve and inline an external/source skill by reference.

## `sequential` — 7 skills
**Requirement:** Runtime MUST execute ordered steps in-process without sub-agent spawn.

## `entry` — 0 skills
**Requirement:** Runtime MUST treat this as a pipeline entry point / router.

## `reference` — 1 skills
**Requirement:** Runtime MUST treat this as read-only reference material, not executable.

## `other` — 0 skills
**Requirement:** (no runtime requirement — uncategorized / not declared)

## `missing` — 225 skills
**Requirement:** (no runtime requirement — uncategorized / not declared)
