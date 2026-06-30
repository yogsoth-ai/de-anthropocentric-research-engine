# ladder-foundry sandbox — STAGE 2B persona-injection smoke test

This is the confined working dir for the **first real sim-cc**. It is a
persona-injection **smoke test**, NOT the AS-1 quality-separation gate (that
needs the exec layer + loss-2, deferred to STAGE 5/6).

## What 2B does

Spawn a real `claude` REPL here, inject each endpoint persona (config_0 genius,
config_5 contrarian) against a FIXED stimulus, read the sim's own session jsonl,
and verify (1) the persona was worn and (2) the two endpoints visibly diverge on
the same stimulus. Between-run independence: each endpoint gets a FRESH sim REPL.

## Confinement

- `cwd` = this sandbox dir; `CLAUDE_CONFIG_DIR` = `sandbox/.claude`.
- `settings.local.json` grants `bypassPermissions` but `deny`s reads outside the
  sandbox: `"deny": ["Read(//**)"]`. Because `--allowedTools` is banned and
  `bypassPermissions` auto-approves everything, `deny` is the ONLY in-claude
  confinement lever — and it must be empirically verified to fire under bypass
  (the probe below).
- One deny rule only (ponytail narrowing): 2B's sim is a pure conversational
  responder — no exec spawn, ~no tool calls. The heavy Bash/Write/Edit deny-list
  is STAGE 5's threat model, not imported here.

## Banned (project hard rule)

`-p` / `--print` / `--resume` / `--session-id` / `--allowedTools` anywhere. All
CC layers are normal interactive REPLs. "One-shot injection" stays an
interactive turn — it never degrades to headless `claude -p`.

## The deny-under-bypass probe (THE GATE for running 2B locally)

Manual procedure (not pytest — it spawns a real `claude`). From this dir:

```bash
cd ladder-foundry/sandbox
IS_SANDBOX=1 CLAUDE_CONFIG_DIR="$(pwd)/.claude" claude
# In that REPL, ask it to read a file OUTSIDE the sandbox, e.g.:
#   "Read the file D:/YOGSOTH-AI/de-anthropocentric-research-engine/README.md and show line 1."
# PASS = the read is DENIED  (deny fired under bypassPermissions)
# FAIL = the read SUCCEEDS   (deny did NOT fire) -> 2B cannot run locally;
#         Tasks 6-7 move to the remote STAGE 5 env. Report to the user.
```

If `Read(//**)` does not match the way this build expresses "outside the tree",
adjust the glob to the form that does — the gate is "a deny rule fires under
bypass", not this exact glob.

### Probe verdict

| Date | Verdict | Note |
| --- | --- | --- |
| 2026-06-30 | **PASS** | A `deny` rule fires under `bypassPermissions`. An out-of-sandbox `Read` was refused with `"File is in a directory that is denied by your permission settings."` Observed: `Read(//**)` is a TOTAL read-deny (it also blocks in-sandbox reads). Harmless for 2B — the sim reads nothing (config+stimulus arrive in the injected message; `read_session.py` runs outside the sandbox), and the REPL still boots and responds. Narrowing the glob to outside-only is STAGE-5 work, deferred. |

## Privacy red line

The CC-log path (`projects/<cwd-slug>/...`) and the cwd-slug itself NEVER appear
in any committed file. `read_session.py` takes `--logs-dir` as a REQUIRED arg
(no default). `SMOKE_RESULT.md` is de-identified / aggregate only.

## Ceiling

The Windows Bash tool has no OS sandbox; `deny` governs Read/Write/Edit only —
adequate for a non-adversarial persona-player. The OS-hard boundary is deferred
to STAGE 5.
