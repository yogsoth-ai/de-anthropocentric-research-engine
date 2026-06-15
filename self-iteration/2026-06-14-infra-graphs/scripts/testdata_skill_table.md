# test fixture — 2-column skill table

The original skill-index.md (the description source) was split into the 9
per-package ref files and removed. This tiny fixture preserves one example of
the `| skill | description |` two-column format that `parse_descriptions` is
contracted to parse, so the unit test stays meaningful without depending on the
deleted file.

| Skill | Description |
|-------|-------------|
| actor-profiling | Understand who the user is — background, resources, constraints, and deep motivations. |
| and-or-decompose | KAOS-style recursive goal decomposition. |
