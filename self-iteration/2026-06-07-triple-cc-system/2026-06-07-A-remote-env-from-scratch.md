# Plan A — Remote Environment From Scratch (bare metal → four identities startable + vertical thin-slice e2e) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the rented RunPod container from bare metal up to the point where "all four CC identities optimizer / sim / exec / loss can start, each sees the skills it should see, and nothing is lost on restart," and prove the pipeline works with one real vertical thin-slice e2e (1 run, fully real claude/codex).

**Architecture:** Everything lands on the persistent disk `/workspace` (`/` is only a 5G overlay, wiped on restart). The four identities = four independent `CLAUDE_CONFIG_DIR`s (skills made visible by copying into the config-dir, not by mount) + four independent cwds (output isolation). The two groups of API keys are physically isolated (the Claude group for optim/sim/exec, the Codex group for loss). A parent CC starts its child CC directly within its own Bash tool (`IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role> bash -lc 'cd <cwd> && claude'`), with no driver script and no PTY; only the optimizer goes into tmux.

**Tech Stack:** Ubuntu 22.04 · Python 3.11 · node (installed to /workspace) · claude-code CLI 2.1.x · codex CLI · tmux · third-party proxy `api.ikuncode.cc`.

---

## Key prerequisite discipline (applies to every Task — read first)

- **★Iron rule: everything lands on `/workspace`, never on `/` or `~`.** `/` has only 5.0 GB of overlay and is wiped on restart; `/workspace` is an 851 TB persistent network disk. Any package, config, or output that lands on `/` will disappear after restart or blow up the root disk.
- **The two key groups are physically isolated**: the Claude group (`ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL=https://api.ikuncode.cc` with no suffix + `ANTHROPIC_MODEL=claude-opus-4-7`) goes to optim/sim/exec; the Codex group (`OPENAI_API_KEY`/`IKUNCODE_KEY` + `OPENAI_BASE_URL=https://api.ikuncode.cc/v1` with `/v1` + `OPENAI_MODEL=gpt-5.5`, wire-api=`responses`) goes to loss. Mixing them makes claude report `model_not_found`.
- **Key values never go into any committed artifact** (scripts, spec, reports, commits, this plan). Reference them only by variable name; the operator fills them in by hand on the device.
- **From scratch**: any existing `env.sh` / `bootstrap.sh` / `home/` / `mounts/` / old `2026-06-06-probe-pretrain/` on the device is to be treated as nonexistent and written from scratch. **Do not go up and delete them**; only clean up old items if they get in the way, and since `env.sh` is the only copy of the keys, rescue the keys before any cleanup.
- **Keep the DARE repo**: `/workspace/De-Anthropocentric-Research-Engine` is the copy source for the 771 skills — do not delete it. New code goes in the repo subdirectory `self-iteration/2026-06-07-probe-pretrain/` (hereafter `<proj>`), pushed to branch `self-iteration/probe-pretrain`, **never to main**.
- **Fixed order**: Task 1→8 is the hard sequence from bare metal to startable (node first, the rest depend on it); Task 9 is validation; Task 10 is the thin-slice e2e. Do not move to the next step until the previous one has passed.
- **Privacy red line**: the CC log absolute path (`/workspace/home/<role>/.claude/projects/...`) never goes into any committed artifact; log reading only goes through a script with a required `--logs-dir` argument. Thin-slice outputs land in `runs/` (device-local, gitignored).

---

## File Structure

Files created/modified by this plan (all on the device's `/workspace`, **not committed to git**, keys filled in by hand by the operator):

- `/workspace/opt/node/` — node runtime (unpack location)
- `/workspace/home/.npm-global/` — claude + codex executables
- `/workspace/home/.hf/` — HF_HOME
- `/workspace/env.sh` — persistent environment variables + two-group key isolation + `IS_SANDBOX=1`
- `/workspace/bootstrap.sh` — idempotent restart-reconnect script
- `/workspace/home/{optim,sim,exec}/.claude/` — three claude config-dirs (each contains `settings.local.json` + `.claude.json` + `skills/`)
- `/workspace/home/loss/.codex/` — codex config-dir (contains `config.toml` + `skills/`)
- `/workspace/work/{optim,sim,exec,loss}/` — four independent per-identity cwds
- `<proj>/fixtures/golden-slice/` — golden synthetic sample seed (1 PolicyCard + 1 topic), archived into git

> The "tests" here are not pytest, but **re-runnable validation commands on the device** (smoke S1–S4 + thin-slice E1–E5). Each Task ends with the exact validation command + expected output; it is only complete once verified.

---

### Task 1: Install node to /workspace (Phase 0.1)

**Files:**
- Create: `/workspace/opt/node/` (unpack node linux-x64)

node is not installed at all, `/` is only 5G and can't hold it, and codex depends on it. Must land on the persistent disk.

- [ ] **Step 1: Confirm node is missing, confirm operating on the persistent disk**

Run:
```bash
command -v node || echo "NODE_ABSENT"
df -h /workspace | tail -1   # confirm /workspace is the big disk (851T)
```
Expected: prints `NODE_ABSENT`; `/workspace` capacity is at the TB level.

- [ ] **Step 2: Download and unpack node to /workspace/opt/node**

Run:
```bash
mkdir -p /workspace/opt
cd /workspace/opt
# pick LTS linux-x64; take the current LTS version number at run time, placeholder here
curl -fsSL -o node.tar.xz https://nodejs.org/dist/v20.18.0/node-v20.18.0-linux-x64.tar.xz
tar -xJf node.tar.xz
mv node-v20.18.0-linux-x64 node
rm node.tar.xz
```
Expected: `/workspace/opt/node/bin/node` exists.

- [ ] **Step 3: Prepend node bin to PATH + set npm prefix to the persistent disk**

Run:
```bash
export PATH=/workspace/opt/node/bin:$PATH
npm config set prefix /workspace/home/.npm-global
```
Expected: no errors.

- [ ] **Step 4: Verify node starts**

Run: `node -v && npm -v`
Expected: prints the node version (e.g. `v20.18.0`) and the npm version, neither with "command not found".

> This Task's PATH/prefix are temporary exports; persistence is in Task 4's `env.sh`. Get it working temporarily first and verify node is usable, then write it into env.sh.

---

### Task 2: Install claude + codex (npm global lands on /workspace, Phase 0.2)

**Files:**
- Modify: `/workspace/home/.npm-global/` (npm global install location)

claude bundles its own runtime (245MB self-contained binary, no node dependency); codex needs node from Task 1.

- [ ] **Step 1: Confirm prefix points at the persistent disk (carried over from Task 1)**

Run: `npm config get prefix`
Expected: `/workspace/home/.npm-global` (if not, re-run Task 1 Step 3).

- [ ] **Step 2: Globally install claude-code + codex**

Run:
```bash
npm i -g @anthropic-ai/claude-code @openai/codex
export PATH=/workspace/home/.npm-global/bin:$PATH
```
Expected: both packages install to `/workspace/home/.npm-global`, with no EACCES (because they land on the persistent disk, not a system directory).

- [ ] **Step 3: Verify claude starts**

Run: `claude --version`
Expected: prints `2.1.x` (measured around 2.1.167), no errors.

- [ ] **Step 4: Verify codex starts (node is now in place, so it should run)**

Run: `codex --version`
Expected: prints the codex version, and **no longer** reports node missing (contrast with the earlier broken state where `codex.js` errored on its node dependency).

---

### Task 3: Install tmux + huggingface-cli (Phase 0.3)

**Files:**
- Modify: system (apt) + `/workspace/home/.hf/` (HF_HOME)

tmux is only for the long-running optimizer; huggingface-cli is a fallback for dataset upload.

- [ ] **Step 1: Install tmux**

Run: `command -v tmux || apt install -y tmux`
Expected: `tmux` is available (`apt` needs no sudo inside the RunPod root container).

- [ ] **Step 2: Install huggingface_hub (pip, HF_HOME lands on the persistent disk)**

Run:
```bash
export HF_HOME=/workspace/home/.hf
pip install huggingface_hub
```
Expected: installs successfully, no errors.

- [ ] **Step 3: Verify**

Run: `tmux -V && huggingface-cli --version`
Expected: prints the tmux version and the huggingface-cli version, neither with "command not found".

> Note: python3 is 3.11.10 (not 3.12; CLAUDE.md's old note of 3.12 is superseded by the device). This plan does not touch the system python; Spec B's venv is built on /workspace.

---

### Task 4: Write env.sh (persistent environment + two-group key isolation, Phase 0.4)

**Files:**
- Create: `/workspace/env.sh`

Persist the environment that Task 1–3 exported temporarily; the core is **two mutually isolated sets of API credentials**. **Key values are filled in by hand by the operator on the device, and never go into any committed artifact.**

- [ ] **Step 1: Write the env.sh skeleton (keys left as placeholders, operator fills in)**

Create `/workspace/env.sh`:
```bash
#!/usr/bin/env bash
# /workspace/env.sh — persistent environment. Sourced into every new shell. Key values filled in by the operator, NEVER enter git.

# ---- paths (node / npm-global / hf all land on the persistent disk) ----
export PATH=/workspace/opt/node/bin:/workspace/home/.npm-global/bin:$PATH
export NPM_CONFIG_PREFIX=/workspace/home/.npm-global
export HF_HOME=/workspace/home/.hf

# ---- required for root to start a bypass REPL ----
export IS_SANDBOX=1

# ---- Claude group (for the three CCs optim / sim / exec) ----
export ANTHROPIC_API_KEY="<FILL_IN_HERE: Claude-group key, x-api-key auth>"
export ANTHROPIC_BASE_URL="https://api.ikuncode.cc"     # no suffix, the CLI appends /v1/messages
export ANTHROPIC_MODEL="claude-opus-4-7"

# ---- Codex group (for the codex used in the two loss computations) ----
export OPENAI_API_KEY="<FILL_IN_HERE: Codex-group key>"
export IKUNCODE_KEY="$OPENAI_API_KEY"
export OPENAI_BASE_URL="https://api.ikuncode.cc/v1"      # with /v1
export OPENAI_MODEL="gpt-5.5"
```

- [ ] **Step 2: Operator fills in the two key groups, confirms they differ**

Run (after the operator edits env.sh and fills in the keys):
```bash
grep -c 'FILL_IN_HERE' /workspace/env.sh   # should be 0, confirming all placeholders are filled
```
Expected: `0` (both placeholders have been replaced with real keys). ⚠️ Red line: the two key groups must be two different group values; using the same key for both has previously made claude report `model_not_found`.

- [ ] **Step 3: source it and verify the environment takes effect**

Run:
```bash
source /workspace/env.sh
echo "$IS_SANDBOX | $ANTHROPIC_BASE_URL | $OPENAI_BASE_URL"
node -v && claude --version && codex --version
```
Expected: prints `1 | https://api.ikuncode.cc | https://api.ikuncode.cc/v1`; all three node/claude/codex version numbers appear.

---

### Task 5: Write bootstrap.sh (restart-reconnect, idempotent, Phase 0.5)

**Files:**
- Create: `/workspace/bootstrap.sh`

`~` is wiped on restart, so this must be re-runnable. Idempotent: hooks `source /workspace/env.sh` into `~/.bashrc`; checks tmux on first run. **No `~/.claude` symlink** (the four identities each use an independent config-dir pointed to via an environment variable; symlinks are fragile and would cross-wire the four identities' configs).

- [ ] **Step 1: Write bootstrap.sh**

Create `/workspace/bootstrap.sh`:
```bash
#!/usr/bin/env bash
# /workspace/bootstrap.sh — restart / new-shell recovery. Idempotent, re-sourcing has no side effects.

# 1. Hook env.sh into ~/.bashrc (dedup: remove the old line first, then add)
LINE='source /workspace/env.sh'
grep -qF "$LINE" ~/.bashrc 2>/dev/null || echo "$LINE" >> ~/.bashrc

# 2. Take effect immediately in the current shell
source /workspace/env.sh

# 3. First-time check for tmux (optimizer long-running host)
command -v tmux >/dev/null 2>&1 || apt install -y tmux
```

- [ ] **Step 2: Verify idempotency (two consecutive runs with no errors, no duplicate line in ~/.bashrc)**

Run:
```bash
bash /workspace/bootstrap.sh && bash /workspace/bootstrap.sh
grep -c 'source /workspace/env.sh' ~/.bashrc   # should be 1, not 2 after running twice
```
Expected: both runs error-free; grep count is `1` (idempotent dedup holds).

- [ ] **Step 3: Verify a new shell picks up the environment automatically**

Run: `bash -lc 'echo $IS_SANDBOX && claude --version'`
Expected: the new login shell prints `1` and the claude version (proving the `.bashrc` hook works).

---

### Task 6: Build the four-identity config-dirs + pre-approval configs (Phase 0.6)

**Files:**
- Create: `/workspace/home/optim/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/sim/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/exec/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/loss/.codex/config.toml`

The three claude config-dirs each get a `settings.local.json` (enable bypass) + a `.claude.json` (pre-approve the env key + skip onboarding). codex is configured with `config.toml`.

- [ ] **Step 1: Build the directory skeleton for the three claude config-dirs**

Run:
```bash
mkdir -p /workspace/home/optim/.claude/skills \
         /workspace/home/sim/.claude/skills \
         /workspace/home/exec/.claude/skills \
         /workspace/home/loss/.codex/skills
```
Expected: the four config-dirs + their respective skills/ subdirectories are created.

- [ ] **Step 2: Write a settings.local.json (bypass) into each of the three claude config-dirs**

For optim / sim / exec **each** write a `/workspace/home/<role>/.claude/settings.local.json`, with uniform content:
```json
{ "permissions": { "defaultMode": "bypassPermissions" } }
```
Expected: the three files have identical content, enabling full tool-call pass-through (the precondition for unattended long runs).

- [ ] **Step 3: Write a .claude.json (pre-approve key + skip onboarding) into each of the three claude config-dirs**

For optim / sim / exec **each** write a `/workspace/home/<role>/.claude/.claude.json`. `<KEY_TAIL>` = the tail segment of the Claude group key (the operator fills it in based on the real key, **filling in only the tail segment, not the full key**):
```json
{
  "hasCompletedOnboarding": true,
  "bypassPermissionsModeAccepted": true,
  "customApiKeyResponses": { "approved": ["<KEY_TAIL>"], "rejected": [] }
}
```
Expected: the three files are in place. A brand-new config-dir defaults to "Not logged in"; this pre-approval lets the REPL actually respond using the env's `ANTHROPIC_API_KEY`.

- [ ] **Step 4: Write the codex config.toml (ikuncode provider + gpt-5.5)**

Create `/workspace/home/loss/.codex/config.toml`:
```toml
model = "gpt-5.5"
model_provider = "ikuncode"

[model_providers.ikuncode]
name = "ikuncode"
base_url = "https://api.ikuncode.cc/v1"
wire_api = "responses"
env_key = "OPENAI_API_KEY"
```
Expected: reading this config, codex connects to the correct Codex group (the independent OpenAI group credentials).

- [ ] **Step 5: Verify JSON/TOML validity**

Run:
```bash
for r in optim sim exec; do
  python3 -c "import json;json.load(open('/workspace/home/$r/.claude/settings.local.json'));json.load(open('/workspace/home/$r/.claude/.claude.json'))" && echo "$r OK"
done
python3 -c "import tomllib;tomllib.load(open('/workspace/home/loss/.codex/config.toml','rb'))" && echo "codex OK"
```
Expected: prints `optim OK` / `sim OK` / `exec OK` / `codex OK`, with no JSON/TOML parse errors.

---

### Task 7: Build the four independent per-identity cwds (Phase 0.7)

**Files:**
- Create: `/workspace/work/{optim,sim,exec,loss}/`

Each identity's working directory (temp file / output isolation). Skill visibility **does not rely on cwd** (it relies on copying into the config-dir, per Task 8).

- [ ] **Step 1: Build the four cwds**

Run: `mkdir -p /workspace/work/{optim,sim,exec,loss}`
Expected: the four directories are created.

- [ ] **Step 2: Verify**

Run: `ls -d /workspace/work/{optim,sim,exec,loss}`
Expected: four lines, each existing.

---

### Task 8: Copy skills into each identity (copy, not mount, Phase 0.8)

**Files:**
- Modify: `/workspace/home/optim/.claude/skills/` (optimization-loop placeholder + superpowers)
- Modify: `/workspace/home/sim/.claude/skills/` (superpowers only)
- Modify: `/workspace/home/exec/.claude/skills/` (771 DARE + formated-specs + formated-result + superpowers)
- Modify: `/workspace/home/loss/.codex/skills/` (injection-fidelity + ladder-quality-order + superpowers, codex convention)

Actually copy a set into each identity's config-dir; everyone carries superpowers; three sources: the DARE repo `skills/`, the project `<proj>/skills/` (Spec B, to be written), and superpowers. The `/workspace/mounts/` layer is **not built**.

> **★Spec A only establishes the "copy mechanism"**: the project skills `optimization-loop` / `injection-fidelity` / `ladder-quality-order` / `formated-specs` / `formated-result` are really copied only after Spec B writes them. For this Task, a **placeholder skill** for the optimizer is enough to run the thin slice; loss's two codex loss skills also use placeholders before Spec B. The copy command pattern is fixed now; the content is filled in once Spec B lands.

- [ ] **Step 1: Confirm the DARE repo is on the persistent disk and contains 771 skills**

Run:
```bash
ls -d /workspace/De-Anthropocentric-Research-Engine/skills | head -1
ls /workspace/De-Anthropocentric-Research-Engine/skills | wc -l
```
Expected: skills/ exists; count is 771 (the DARE research skill library).

- [ ] **Step 2: exec ← 771 DARE + formated-specs/result (+superpowers)**

Run:
```bash
SRC=/workspace/De-Anthropocentric-Research-Engine/skills
DST=/workspace/home/exec/.claude/skills
cp -r "$SRC"/* "$DST"/                                   # 771 DARE
# formated-specs / formated-result: copied from <proj>/skills/ once Spec B is written (placeholder here)
# superpowers: copied into $DST from the superpowers install source (everyone gets it)
```
Expected: exec's skills/ contains the 771 DARE skills; formated-* and superpowers are added once Spec B / the install source are in place.

- [ ] **Step 3: sim ← superpowers only**

Run:
```bash
DST=/workspace/home/sim/.claude/skills
# superpowers copied into $DST; sim carries no DARE skill (persona via injection; skills would pollute the user role)
```
Expected: sim's skills/ contains only superpowers, no DARE skill.

- [ ] **Step 4: optim ← optimization-loop (placeholder) + superpowers**

Run:
```bash
DST=/workspace/home/optim/.claude/skills
# optimization-loop: copied from <proj>/skills/ once Spec B is written; the slice phase uses a placeholder SKILL.md
# superpowers copied into $DST
```
Expected: optim's skills/ contains optimization-loop (placeholder) + superpowers.

- [ ] **Step 5: loss (codex) ← injection-fidelity + ladder-quality-order + superpowers (codex convention)**

codex does not read `.claude/skills/`; its skills go in codex's conventional directory `/workspace/home/loss/.codex/skills/`, and at runtime the loss logic must also **inject the full SKILL.md text into the codex prompt** (codex does not auto-mount). The codex form of superpowers is installed per the codex plugin convention.
```bash
DST=/workspace/home/loss/.codex/skills
# injection-fidelity / ladder-quality-order: copied from <proj>/skills/ once Spec B is written (placeholder first)
# superpowers (codex-convention form) copied into $DST
```
Expected: loss's codex skills/ directory contains the two loss skills (placeholders) + superpowers.

- [ ] **Step 6: Verify the copy result (skill visibility matrix)**

Run:
```bash
echo "exec:" && ls /workspace/home/exec/.claude/skills | wc -l   # should be ≥771
echo "sim:"  && ls /workspace/home/sim/.claude/skills            # superpowers only
echo "optim:"&& ls /workspace/home/optim/.claude/skills          # optimization-loop (placeholder) + superpowers
echo "loss:" && ls /workspace/home/loss/.codex/skills            # two loss skills (placeholder) + superpowers
```
Expected: exec ≥771; sim superpowers only; optim sees optimization-loop; loss sees the two loss skills.

---

### Task 9: Layer one — environment smoke validation S1–S4 (is the foundation there)

**Files:**
- No new files (pure validation, run commands against expectations)

The environment layer uses smoke validation. The foundation is only established once each line passes.

- [ ] **Step 1: S1 tools in place (all pass in a new shell)**

Run:
```bash
bash -lc 'node -v && claude --version && codex --version && tmux -V && huggingface-cli --version'
```
Expected: all five version numbers print, none with "command not found" (proving env.sh + bootstrap.sh auto-wire correctly in a new shell).

- [ ] **Step 2: S2 each of the four identities starts and can really respond**

Start each identity directly, sending a "reply OK" liveness probe to each. The three Claude layers:
```bash
# optim (same idea, swap in sim / exec's config-dir and cwd)
echo 'reply with exactly: OK' | IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude \
  bash -lc 'cd /workspace/work/optim && claude -p'
```
codex (loss):
```bash
cd /workspace/work/loss
echo 'reply with exactly: OK' | CODEX_HOME=/workspace/home/loss/.codex codex exec -
```
Expected: each of the four identities replies `OK` (or a real reply containing OK), proving pre-approved key + bypass + IS_SANDBOX work and each connects to its own group (claude does not report `model_not_found`).

- [ ] **Step 3: S3 skill visibility is correct**

Run (after starting each identity's REPL, ask "list the skills you can see," or check the config-dir skills/ landing):
```bash
ls /workspace/home/exec/.claude/skills | grep -c . # exec should see 771+formated-*
ls /workspace/home/sim/.claude/skills              # sim only superpowers
ls /workspace/home/optim/.claude/skills | grep optimization-loop  # optim sees placeholder
ls /workspace/home/loss/.codex/skills              # codex sees the two loss skills
```
Expected: exec sees 771+formated-*; sim only superpowers; optim sees optimization-loop (placeholder); codex reads the two loss skills.

- [ ] **Step 4: S4 restart-reconnect (still all pass after ~ is wiped)**

Run:
```bash
# After restarting the container (~ is wiped):
bash /workspace/bootstrap.sh        # reconnect the environment
# then re-run S1–S3
```
Expected: after restart, run bootstrap.sh and S1–S3 still all pass (proving persistent-disk state + idempotent recovery hold).

---

### Task 10: Layer two — real vertical thin-slice e2e E1–E5 (scenario / acceptance test)

**Files:**
- Create: `<proj>/fixtures/golden-slice/policycard.json` (1 hand-written minimal PolicyCard, F0–F9 placeholder but valid)
- Create: `<proj>/fixtures/golden-slice/topic.md` (1 placeholder topic)
- Outputs land in `runs/` (device-local, gitignored, not committed)

Synthesize one **minimal but real** scenario, letting data flow through the **real** CC/codex full chain. **no-fake iron rule**: the sim/exec/codex in E1–E5 must be real processes; the only thing synthesized is the "input config + topic." Any use of fake callbacks/stub functions to fake green does not count as passing.

> **Scope boundary**: the thin slice runs only **1 run**, validating "four-identity coordination + real CC/codex pipeline + correct output shape." It does **not** validate ladder monotonicity (needs 6 rungs), nor gate/backprop (needs 48-run) — those belong to B/C.

- [ ] **Step 1: Write the golden synthetic sample seed (archived into git)**

Create `<proj>/fixtures/golden-slice/policycard.json` (F0–F9 placeholder but valid, field names aligned with Spec B's PolicyCard schema):
```json
{
  "F0": "genius-user persona placeholder: high substance demand, high operationalization insistence",
  "F1": "...", "F2": "...", "F3": "...", "F4": "...",
  "F5": "...", "F6": "...", "F7": "challengeable factual premise placeholder",
  "F8": "pressure_turns=2, closing_turns=1",
  "F9": "...",
  "axis_levels": {"A1":"L0","A2":"L0","A3":"L0","A4":"C+","A5":"G+","B1":"neutral"}
}
```
Create `<proj>/fixtures/golden-slice/topic.md`:
```markdown
# Placeholder topic (for the slice, not the real 8 topics)
Study a minimal external DL phenomenon: design a minimal executable controlled evaluation. Require exec to use formated-specs for the spec and call formated-results at the end.
```
Expected: the two files land in `<proj>/fixtures/golden-slice/`, committed into git (the regression baseline seed shared across the three splits).

- [ ] **Step 2: E1 injection — optim's real CC injects the full config into sim, sim really plays the persona**

optim starts sim directly within its own Bash tool, with the first message = the full policycard.json + the role-play instruction.
Expected: sim's REPL starts (real claude), and after reading the config **really plays** that persona (the reply reflects F0's high-substance/high-operationalization preference), not a stub callback.

- [ ] **Step 3: E2 nested drive — sim starts exec directly within its own Bash, injecting topic + the two mandatory items**

sim uses `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude bash -lc 'cd /workspace/work/exec && claude'` to start exec directly, injecting in the first turn topic.md + the two mandatory items (formated-specs replaces writing-specs; the closing must use formated-results).
Expected: exec's REPL starts (real claude, able to see the 771 DARE skills), receiving the topic + the mandatory items.

- [ ] **Step 4: E3 real research — sim↔exec real multi-turn back-and-forth, exec really emits a formated-results structured block at the final step**

Expected: sim and exec really have a multi-turn dialogue, exec really runs DARE, and at the final step produces a `research-result` fence + JSON payload (aligned with Spec B's concat contract: ` ```research-result ` opening fence, JSON body, ` ``` ` closing fence).

- [ ] **Step 5: E4 real loss compute — codex really reads the transcript, injection-fidelity really emits loss1.json**

Start codex (loss config-dir), injecting the full injection-fidelity SKILL.md + the transcript payload.
Expected: codex really emits a `loss1.json` (structure matching the Spec B schema: `fidelity` bool + `loss1` float + `per_axis_evidence`), with an interpretable fidelity value, not a stub.

- [ ] **Step 6: E5 trace recording — trace.jsonl / transcript.md / triple.json really land**

Expected: `runs/<id>/trace.jsonl` really records the four event types `run_start→rung_start→dialogue_turn→rung_done`; `transcripts/<sample>.md` is really extracted from the exec session jsonl (via a script with required `--logs-dir`, containing no absolute log path); `triples/<sample>.json` is really assembled into a triple.

- [ ] **Step 7: Thin-slice pass criterion (all-real, correct output shape)**

Run (check outputs are complete and there is no privacy leak):
```bash
ls runs/*/trace.jsonl runs/*/transcripts/*.md runs/*/triples/*.json runs/*/loss/*.loss1.json
grep -rl '/workspace/home/.*/.claude/projects' runs/*/transcripts runs/*/triples 2>/dev/null && echo "LEAK!" || echo "NO LEAK"
```
Expected: all four output types are complete; prints `NO LEAK` (transcript/triple contain no CC log absolute path, the privacy red line holds).

> **Golden synthetic sample**: the config+topic used by E1–E5 is archived fixed at `<proj>/fixtures/golden-slice/`, becoming the regression scenario shared across the three splits, deepened layer by layer (A: 1-run vertical pipeline; B: 6-rung ladder; C: 48-run convergence).

---

## Self-Review (checked against Spec A)

- **Phase 0.1–0.8 coverage**: Task 1 (node) / 2 (claude+codex) / 3 (tmux+hf) / 4 (env.sh) / 5 (bootstrap.sh) / 6 (config-dir pre-approval) / 7 (cwd) / 8 (skill copy) correspond one-to-one, with no gaps.
- **Completion criteria 1+3 coverage**: Task 9 = smoke S1–S4; Task 10 = thin-slice E1–E5. Both layers present.
- **Skill copy matrix coverage**: Task 8's four identities (exec 771+formated-*, sim superpowers only, optim optimization-loop placeholder, loss two loss + codex convention) align with Spec A section 4.
- **Four isolation dimensions coverage**: config-dir (Task 6), cwd (Task 7), startup form (Task 9 S2 / Task 10 direct-start commands), credentials (Task 4 two-group isolation) all present.
- **Red-line coverage**: everything lands on /workspace (throughout), two-group key isolation (Task 4), keys not in committed artifacts (Task 4 placeholders), CC log path not in outputs (Task 10 Step 7 NO LEAK check).
- **placeholder scan**: env.sh's `<FILL_IN_HERE: ...>` / `.claude.json`'s `<KEY_TAIL>` / Task 8's "placeholder skills" are **intentional operator fill-ins and Spec B handoff points**, not plan gaps — the body already explains who fills them and when.

## Execution Handoff

See the index plan `2026-06-07-INDEX-triple-cc-pretrain.md`. This plan (A) is the prerequisite for B/C: only after A passes (S1–S4 + E1–E5 all green) do we proceed to B.
