# Plan A — 远程环境从零搭(裸机 → 四身份可启动 + 纵向薄片 e2e)Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把租来的 RunPod 容器从裸机搭到「optimizer / sim / exec / loss 四个 CC 身份都能起来、各看到该看的 skill、重启不丢」,并用一条真实纵向薄片 e2e(1 run,全真 claude/codex)证明通路成立。

**Architecture:** 一切落持久盘 `/workspace`(`/` 仅 5G overlay,重启即抹)。四身份 = 四个独立 `CLAUDE_CONFIG_DIR`(技能靠复制进 config-dir,非 mount)+ 四个独立 cwd(产出隔离)。两组 API key 物理隔离(Claude 组给 optim/sim/exec,Codex 组给 loss)。父 CC 在自己 Bash 工具里直起子 CC(`IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<role> bash -lc 'cd <cwd> && claude'`),无驱动脚本、无 PTY,只有 optimizer 进 tmux。

**Tech Stack:** Ubuntu 22.04 · Python 3.11 · node(装到 /workspace)· claude-code CLI 2.1.x · codex CLI · tmux · 第三方代理 `api.ikuncode.cc`。

---

## 关键前置纪律(每个 Task 都适用,先读)

- **★铁律:一切落 `/workspace`,绝不进 `/` 或 `~`。** `/` 只有 5.0 GB overlay 且重启即抹;`/workspace` 是 851 TB 持久网络盘。任何装包、配置、产物落 `/` 都会在重启后消失或撑爆根盘。
- **两组 key 物理隔离**:Claude 组(`ANTHROPIC_API_KEY` + `ANTHROPIC_BASE_URL=https://api.ikuncode.cc` 无后缀 + `ANTHROPIC_MODEL=claude-opus-4-7`)给 optim/sim/exec;Codex 组(`OPENAI_API_KEY`/`IKUNCODE_KEY` + `OPENAI_BASE_URL=https://api.ikuncode.cc/v1` 带 `/v1` + `OPENAI_MODEL=gpt-5.5`,wire-api=`responses`)给 loss。混用会让 claude 报 `model_not_found`。
- **key 值绝不写进任何提交物**(脚本、spec、报告、commit、本 plan)。只按变量名引用;执行者在设备上手填。
- **从零搭**:设备上现存的 `env.sh` / `bootstrap.sh` / `home/` / `mounts/` / 旧 `2026-06-06-probe-pretrain/` 一律视为不存在,从零写。**不上去删**;若旧物碍事再清理,且 `env.sh` 是 key 唯一副本,清理前先救出 key。
- **DARE repo 保留**:`/workspace/De-Anthropocentric-Research-Engine` 是 771 skill 的复制源,不删。新代码做在 repo 子目录 `self-iteration/2026-06-07-probe-pretrain/`(下文简称 `<proj>`),push 到分支 `self-iteration/probe-pretrain`,**绝不推 main**。
- **顺序固定**:Task 1→8 是裸机到可启动的硬序(node 在前,其余依赖它);Task 9 是校验;Task 10 是薄片 e2e。前一步未验过不进下一步。
- **隐私红线**:CC log 绝对路径(`/workspace/home/<role>/.claude/projects/...`)绝不进任何提交物;读 log 只走 `--logs-dir` 必填的脚本。薄片产出落 `runs/`(设备本地、gitignore)。

---

## File Structure

本 plan 创建/修改的文件(全部在设备 `/workspace` 上,**不进 git 提交物**,key 由执行者手填):

- `/workspace/opt/node/` — node runtime(解包落点)
- `/workspace/home/.npm-global/` — claude + codex 可执行
- `/workspace/home/.hf/` — HF_HOME
- `/workspace/env.sh` — 持久环境变量 + 两组 key 隔离 + `IS_SANDBOX=1`
- `/workspace/bootstrap.sh` — 重启重连幂等脚本
- `/workspace/home/{optim,sim,exec}/.claude/` — 三个 claude config-dir(各含 `settings.local.json` + `.claude.json` + `skills/`)
- `/workspace/home/loss/.codex/` — codex config-dir(含 `config.toml` + `skills/`)
- `/workspace/work/{optim,sim,exec,loss}/` — 四身份独立 cwd
- `<proj>/fixtures/golden-slice/` — 黄金合成样例种子(1 PolicyCard + 1 topic),归档进 git

> 这里的「测试」不是 pytest,而是**设备上可复跑的校验命令**(冒烟 S1–S4 + 薄片 E1–E5)。每个 Task 末给出确切校验命令 + 期望输出,验过才算完成。

---

### Task 1: 装 node 到 /workspace(Phase 0.1)

**Files:**
- Create: `/workspace/opt/node/` (解包 node linux-x64)

node 完全没装,`/` 仅 5G 装不下,codex 依赖它。必须落持久盘。

- [ ] **Step 1: 确认 node 缺失、确认在持久盘上操作**

Run:
```bash
command -v node || echo "NODE_ABSENT"
df -h /workspace | tail -1   # 确认 /workspace 是大盘(851T)
```
Expected: 打印 `NODE_ABSENT`;`/workspace` 容量为 TB 级。

- [ ] **Step 2: 下载并解包 node 到 /workspace/opt/node**

Run:
```bash
mkdir -p /workspace/opt
cd /workspace/opt
# 选 LTS linux-x64;版本号执行时取当前 LTS,此处用占位
curl -fsSL -o node.tar.xz https://nodejs.org/dist/v20.18.0/node-v20.18.0-linux-x64.tar.xz
tar -xJf node.tar.xz
mv node-v20.18.0-linux-x64 node
rm node.tar.xz
```
Expected: `/workspace/opt/node/bin/node` 存在。

- [ ] **Step 3: PATH 前置 node bin + 设 npm prefix 到持久盘**

Run:
```bash
export PATH=/workspace/opt/node/bin:$PATH
npm config set prefix /workspace/home/.npm-global
```
Expected: 无报错。

- [ ] **Step 4: 校验 node 起得来**

Run: `node -v && npm -v`
Expected: 打印 node 版本(如 `v20.18.0`)与 npm 版本,均无 "command not found"。

> 本 Task 的 PATH/prefix 是临时 export;持久化在 Task 4 的 `env.sh`。先临时通,验证 node 可用,再写进 env.sh。

---

### Task 2: 装 claude + codex(npm global 落 /workspace,Phase 0.2)

**Files:**
- Modify: `/workspace/home/.npm-global/` (npm 全局安装落点)

claude 自带 runtime(245MB 自包含二进制,不依赖 node);codex 需 Task 1 的 node。

- [ ] **Step 1: 确认 prefix 指向持久盘(承接 Task 1)**

Run: `npm config get prefix`
Expected: `/workspace/home/.npm-global`(若不是,重跑 Task 1 Step 3)。

- [ ] **Step 2: 全局装 claude-code + codex**

Run:
```bash
npm i -g @anthropic-ai/claude-code @openai/codex
export PATH=/workspace/home/.npm-global/bin:$PATH
```
Expected: 两个包装到 `/workspace/home/.npm-global`,无 EACCES(因落持久盘非系统目录)。

- [ ] **Step 3: 校验 claude 起得来**

Run: `claude --version`
Expected: 打印 `2.1.x`(实测 2.1.167 量级),无报错。

- [ ] **Step 4: 校验 codex 起得来(此时 node 已就位,应可跑)**

Run: `codex --version`
Expected: 打印 codex 版本,**不再**报 node 缺失(对比从前 `codex.js` 依赖 node 报错的坏状态)。

---

### Task 3: 装 tmux + huggingface-cli(Phase 0.3)

**Files:**
- Modify: 系统(apt)+ `/workspace/home/.hf/`(HF_HOME)

tmux 仅 optimizer 长驻用;huggingface-cli 是数据集上传备用。

- [ ] **Step 1: 装 tmux**

Run: `command -v tmux || apt install -y tmux`
Expected: `tmux` 可用(`apt` 在 RunPod root 容器内无需 sudo)。

- [ ] **Step 2: 装 huggingface_hub(pip,HF_HOME 落持久盘)**

Run:
```bash
export HF_HOME=/workspace/home/.hf
pip install huggingface_hub
```
Expected: 安装成功,无报错。

- [ ] **Step 3: 校验**

Run: `tmux -V && huggingface-cli --version`
Expected: 打印 tmux 版本与 huggingface-cli 版本,均无 "command not found"。

> 注:python3 是 3.11.10(非 3.12;CLAUDE.md 旧记 3.12 以设备为准)。本 plan 不动系统 python;Spec B 的 venv 建在 /workspace。

---

### Task 4: 写 env.sh(持久环境 + 两组 key 隔离,Phase 0.4)

**Files:**
- Create: `/workspace/env.sh`

把 Task 1–3 临时 export 的环境持久化,核心是**两套互相隔离的 API 凭证**。**key 值由执行者在设备上手填,不进任何提交物。**

- [ ] **Step 1: 写 env.sh 骨架(key 留占位,执行者手填)**

Create `/workspace/env.sh`:
```bash
#!/usr/bin/env bash
# /workspace/env.sh — 持久环境。source 进每个新 shell。key 值执行者手填,绝不进 git。

# ---- 路径(node / npm-global / hf 全落持久盘)----
export PATH=/workspace/opt/node/bin:/workspace/home/.npm-global/bin:$PATH
export NPM_CONFIG_PREFIX=/workspace/home/.npm-global
export HF_HOME=/workspace/home/.hf

# ---- root 起 bypass REPL 必需 ----
export IS_SANDBOX=1

# ---- Claude 分组(给 optim / sim / exec 三层 CC)----
export ANTHROPIC_API_KEY="<在此填 Claude 组 key,x-api-key 鉴权>"
export ANTHROPIC_BASE_URL="https://api.ikuncode.cc"     # 无后缀,CLI 自拼 /v1/messages
export ANTHROPIC_MODEL="claude-opus-4-7"

# ---- Codex 分组(给两次 loss 计算的 codex)----
export OPENAI_API_KEY="<在此填 Codex 组 key>"
export IKUNCODE_KEY="$OPENAI_API_KEY"
export OPENAI_BASE_URL="https://api.ikuncode.cc/v1"      # 带 /v1
export OPENAI_MODEL="gpt-5.5"
```

- [ ] **Step 2: 执行者手填两组 key,确认两组不同**

Run(执行者编辑 env.sh 填 key 后):
```bash
grep -c '在此填' /workspace/env.sh   # 应为 0,确认占位都填了
```
Expected: `0`(两个占位都已替换为真 key)。⚠️ 红线:两组 key 必须是不同的两个分组值,曾因填成同一个 key 导致 claude 报 `model_not_found`。

- [ ] **Step 3: source 并校验环境生效**

Run:
```bash
source /workspace/env.sh
echo "$IS_SANDBOX | $ANTHROPIC_BASE_URL | $OPENAI_BASE_URL"
node -v && claude --version && codex --version
```
Expected: 打印 `1 | https://api.ikuncode.cc | https://api.ikuncode.cc/v1`;node/claude/codex 三个版本号全出。

---

### Task 5: 写 bootstrap.sh(重启重连,幂等,Phase 0.5)

**Files:**
- Create: `/workspace/bootstrap.sh`

`~` 重启即抹,必须可重跑。幂等:把 `source /workspace/env.sh` 挂进 `~/.bashrc`;首次检查 tmux。**不做 `~/.claude` symlink**(四身份各用独立 config-dir 经环境变量指向,软链脆弱且会让四身份串配置)。

- [ ] **Step 1: 写 bootstrap.sh**

Create `/workspace/bootstrap.sh`:
```bash
#!/usr/bin/env bash
# /workspace/bootstrap.sh — 重启/新 shell 恢复。幂等,重复 source 无副作用。

# 1. 把 env.sh 挂进 ~/.bashrc(去重:先删旧行再加)
LINE='source /workspace/env.sh'
grep -qF "$LINE" ~/.bashrc 2>/dev/null || echo "$LINE" >> ~/.bashrc

# 2. 当前 shell 立即生效
source /workspace/env.sh

# 3. 首次检查 tmux(optimizer 长驻 host)
command -v tmux >/dev/null 2>&1 || apt install -y tmux
```

- [ ] **Step 2: 校验幂等(连跑两次无报错、~/.bashrc 不重复加行)**

Run:
```bash
bash /workspace/bootstrap.sh && bash /workspace/bootstrap.sh
grep -c 'source /workspace/env.sh' ~/.bashrc   # 应为 1,不因跑两次变 2
```
Expected: 两次执行均无报错;grep 计数为 `1`(幂等去重成立)。

- [ ] **Step 3: 校验新 shell 自动带环境**

Run: `bash -lc 'echo $IS_SANDBOX && claude --version'`
Expected: 新登录 shell 打印 `1` 与 claude 版本(证明 `.bashrc` 钩子生效)。

---

### Task 6: 建四身份 config-dir + 预批配置(Phase 0.6)

**Files:**
- Create: `/workspace/home/optim/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/sim/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/exec/.claude/{settings.local.json,.claude.json}`
- Create: `/workspace/home/loss/.codex/config.toml`

三个 claude config-dir 各放 `settings.local.json`(开 bypass)+ `.claude.json`(预批 env key + 跳过 onboarding)。codex 配 `config.toml`。

- [ ] **Step 1: 建三个 claude config-dir 的目录骨架**

Run:
```bash
mkdir -p /workspace/home/optim/.claude/skills \
         /workspace/home/sim/.claude/skills \
         /workspace/home/exec/.claude/skills \
         /workspace/home/loss/.codex/skills
```
Expected: 四个 config-dir + 各自 skills/ 子目录建好。

- [ ] **Step 2: 三个 claude config-dir 各写 settings.local.json(bypass)**

为 optim / sim / exec **各**写一份 `/workspace/home/<role>/.claude/settings.local.json`,内容统一:
```json
{ "permissions": { "defaultMode": "bypassPermissions" } }
```
Expected: 三份文件内容一致,开启工具调用全程放行(无人值守长跑前提)。

- [ ] **Step 3: 三个 claude config-dir 各写 .claude.json(预批 key + 跳 onboarding)**

为 optim / sim / exec **各**写一份 `/workspace/home/<role>/.claude/.claude.json`。`<KEY_TAIL>` = Claude 组 key 的尾段(执行者据真 key 填,**只填尾段不填全 key**):
```json
{
  "hasCompletedOnboarding": true,
  "bypassPermissionsModeAccepted": true,
  "customApiKeyResponses": { "approved": ["<KEY_TAIL>"], "rejected": [] }
}
```
Expected: 三份文件就位。全新 config-dir 默认 "Not logged in",此预批让 REPL 用 env 的 `ANTHROPIC_API_KEY` 真正回话。

- [ ] **Step 4: 写 codex config.toml(ikuncode provider + gpt-5.5)**

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
Expected: codex 读此配置即连对 Codex 分组(独立 OpenAI 组凭证)。

- [ ] **Step 5: 校验 JSON/TOML 合法**

Run:
```bash
for r in optim sim exec; do
  python3 -c "import json;json.load(open('/workspace/home/$r/.claude/settings.local.json'));json.load(open('/workspace/home/$r/.claude/.claude.json'))" && echo "$r OK"
done
python3 -c "import tomllib;tomllib.load(open('/workspace/home/loss/.codex/config.toml','rb'))" && echo "codex OK"
```
Expected: 打印 `optim OK` / `sim OK` / `exec OK` / `codex OK`,无 JSON/TOML 解析异常。

---

### Task 7: 建四身份独立 cwd(Phase 0.7)

**Files:**
- Create: `/workspace/work/{optim,sim,exec,loss}/`

各身份工作目录(临时文件/产出隔离)。技能可见性**不靠 cwd**(靠 Task 8 复制进 config-dir)。

- [ ] **Step 1: 建四个 cwd**

Run: `mkdir -p /workspace/work/{optim,sim,exec,loss}`
Expected: 四目录建好。

- [ ] **Step 2: 校验**

Run: `ls -d /workspace/work/{optim,sim,exec,loss}`
Expected: 四行,逐一存在。

---

### Task 8: 复制 skill 进各身份(复制,非 mount,Phase 0.8)

**Files:**
- Modify: `/workspace/home/optim/.claude/skills/` (optimization-loop 占位 + superpowers)
- Modify: `/workspace/home/sim/.claude/skills/` (仅 superpowers)
- Modify: `/workspace/home/exec/.claude/skills/` (771 DARE + formated-specs + formated-result + superpowers)
- Modify: `/workspace/home/loss/.codex/skills/` (injection-fidelity + ladder-quality-order + superpowers,codex 规范)

每身份 config-dir 下实打实 copy 一份;superpowers 全员带;来源三处:DARE repo `skills/`、项目 `<proj>/skills/`(Spec B 待写)、superpowers。`/workspace/mounts/` 层**不建**。

> **★Spec A 只建立"复制机制"**:`optimization-loop` / `injection-fidelity` / `ladder-quality-order` / `formated-specs` / `formated-result` 这些项目 skill 由 Spec B 写好后再真复制。本 Task 对 optimizer 用**占位 skill**即可跑通薄片;loss 的两个 codex loss skill 在 Spec B 前也用占位。复制命令模式现在定死,内容随 Spec B 落地填。

- [ ] **Step 1: 确认 DARE repo 在持久盘、含 771 skill**

Run:
```bash
ls -d /workspace/De-Anthropocentric-Research-Engine/skills | head -1
ls /workspace/De-Anthropocentric-Research-Engine/skills | wc -l
```
Expected: skills/ 存在;计数为 771(DARE 研究技能库)。

- [ ] **Step 2: exec ← 771 DARE + formated-specs/result(+superpowers)**

Run:
```bash
SRC=/workspace/De-Anthropocentric-Research-Engine/skills
DST=/workspace/home/exec/.claude/skills
cp -r "$SRC"/* "$DST"/                                   # 771 DARE
# formated-specs / formated-result:Spec B 写好后从 <proj>/skills/ 复制(此处占位)
# superpowers:从 superpowers 安装源复制进 $DST(全员带)
```
Expected: exec 的 skills/ 含 771 DARE skill;formated-* 与 superpowers 待 Spec B/安装源就位后补。

- [ ] **Step 3: sim ← 仅 superpowers**

Run:
```bash
DST=/workspace/home/sim/.claude/skills
# superpowers 复制进 $DST;sim 不带任何 DARE skill(人设靠注入,技能会污染用户角色)
```
Expected: sim 的 skills/ 只含 superpowers,无 DARE skill。

- [ ] **Step 4: optim ← optimization-loop(占位)+ superpowers**

Run:
```bash
DST=/workspace/home/optim/.claude/skills
# optimization-loop:Spec B 写好后从 <proj>/skills/ 复制;薄片阶段放占位 SKILL.md
# superpowers 复制进 $DST
```
Expected: optim 的 skills/ 含 optimization-loop(占位)+ superpowers。

- [ ] **Step 5: loss(codex) ← injection-fidelity + ladder-quality-order + superpowers(codex 规范)**

codex 不读 `.claude/skills/`,其 skill 放 codex 约定目录 `/workspace/home/loss/.codex/skills/`,且运行时 loss 逻辑还要**把 SKILL.md 全文注入进 codex prompt**(codex 不自动挂载)。superpowers 给 codex 的形态按 codex 插件规范装。
```bash
DST=/workspace/home/loss/.codex/skills
# injection-fidelity / ladder-quality-order:Spec B 写好后从 <proj>/skills/ 复制(占位先行)
# superpowers(codex 规范形态)复制进 $DST
```
Expected: loss 的 codex skills/ 目录含两个 loss skill(占位)+ superpowers。

- [ ] **Step 6: 校验复制结果(技能可见性矩阵)**

Run:
```bash
echo "exec:" && ls /workspace/home/exec/.claude/skills | wc -l   # 应 ≥771
echo "sim:"  && ls /workspace/home/sim/.claude/skills            # 只 superpowers
echo "optim:"&& ls /workspace/home/optim/.claude/skills          # optimization-loop(占位)+superpowers
echo "loss:" && ls /workspace/home/loss/.codex/skills            # 两 loss(占位)+superpowers
```
Expected: exec ≥771;sim 仅 superpowers;optim 见 optimization-loop;loss 见两个 loss skill。

---

### Task 9: 第一层 — 环境冒烟校验 S1–S4(地基在不在)

**Files:**
- 无新文件(纯校验,跑命令对期望)

环境层用冒烟校验。每条验过才算地基成立。

- [ ] **Step 1: S1 工具就位(新 shell 全过)**

Run:
```bash
bash -lc 'node -v && claude --version && codex --version && tmux -V && huggingface-cli --version'
```
Expected: 五个版本号全打印,无一 "command not found"(证明 env.sh + bootstrap.sh 在新 shell 自动接好)。

- [ ] **Step 2: S2 四身份各起得来、能回真话**

逐身份直起,各发一句"回我 OK"探活。Claude 三层:
```bash
# optim(同理换 sim / exec 的 config-dir 与 cwd)
echo 'reply with exactly: OK' | IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude \
  bash -lc 'cd /workspace/work/optim && claude -p'
```
codex(loss):
```bash
cd /workspace/work/loss
echo 'reply with exactly: OK' | CODEX_HOME=/workspace/home/loss/.codex codex exec -
```
Expected: 四身份各回 `OK`(或含 OK 的真回复),证明预批 key + bypass + IS_SANDBOX 生效、各连对自己分组(claude 不报 `model_not_found`)。

- [ ] **Step 3: S3 技能可见性正确**

Run(每身份起 REPL 后问"列出你能看到的 skill",或检查 config-dir skills/ 落地):
```bash
ls /workspace/home/exec/.claude/skills | grep -c . # exec 应见 771+formated-*
ls /workspace/home/sim/.claude/skills              # sim 只 superpowers
ls /workspace/home/optim/.claude/skills | grep optimization-loop  # optim 见占位
ls /workspace/home/loss/.codex/skills              # codex 见两 loss skill
```
Expected: exec 看到 771+formated-*;sim 只 superpowers;optim 看到 optimization-loop(占位);codex 读到两 loss skill。

- [ ] **Step 4: S4 重启重连(~ 被抹后仍全过)**

Run:
```bash
# 重启容器(~ 被抹)后:
bash /workspace/bootstrap.sh        # 重新接好环境
# 然后重跑 S1–S3
```
Expected: 重启后跑 bootstrap.sh,S1–S3 仍全过(证明持久盘状态 + 幂等恢复成立)。

---

### Task 10: 第二层 — 真实纵向薄片 e2e E1–E5(scenario / acceptance test)

**Files:**
- Create: `<proj>/fixtures/golden-slice/policycard.json` (1 张手写极小 PolicyCard,F0–F9 占位但合法)
- Create: `<proj>/fixtures/golden-slice/topic.md` (1 个占位 topic)
- 产物落 `runs/`(设备本地、gitignore,不进提交物)

合成一条**极小但真实**的场景,让数据流过**真** CC/codex 全链。**no-fake 铁律**:E1–E5 的 sim/exec/codex 必须是真进程,合成的只有"输入 config + topic"。任何用假回调/桩函数凑绿一律不算通过。

> **范围界**:薄片只跑 **1 run**,验"四身份协同 + 真 CC/codex 通路 + 产物形态正确"。**不**验阶梯单调(需 6 档)、**不**验门控/backprop(需 48-run)——那是 B/C 的事。

- [ ] **Step 1: 写黄金合成样例种子(归档进 git)**

Create `<proj>/fixtures/golden-slice/policycard.json`(F0–F9 占位但合法,字段名对齐 Spec B 的 PolicyCard schema):
```json
{
  "F0": "天才用户人设占位:高实质要求、高操作化坚持",
  "F1": "...", "F2": "...", "F3": "...", "F4": "...",
  "F5": "...", "F6": "...", "F7": "可被挑战的事实前提占位",
  "F8": "pressure_turns=2, closing_turns=1",
  "F9": "...",
  "axis_levels": {"A1":"L0","A2":"L0","A3":"L0","A4":"C+","A5":"G+","B1":"neutral"}
}
```
Create `<proj>/fixtures/golden-slice/topic.md`:
```markdown
# 占位 topic(薄片用,非真 8 题)
研究一个极小的外部 DL 现象:设计一项最小可执行的对照评估。要求 exec 用 formated-specs 做规格、收尾调 formated-results。
```
Expected: 两文件落 `<proj>/fixtures/golden-slice/`,提交进 git(三拆共用回归基线种子)。

- [ ] **Step 2: E1 注入 — optim 真 CC 把 config 全文注入 sim,sim 真扮人设**

optim 在自己 Bash 工具里直起 sim,首轮消息 = policycard.json 全文 + 扮演指令。
Expected: sim REPL 起来(真 claude),读 config 后**真扮**该人设(回复体现 F0 的高实质/高操作化偏好),非桩回调。

- [ ] **Step 3: E2 嵌套驱动 — sim 在自己 Bash 里直起 exec,注入 topic + 两条强制**

sim 用 `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude bash -lc 'cd /workspace/work/exec && claude'` 直起 exec,首轮注入 topic.md + 两条强制(formated-specs 替代 writing-specs;收尾必须 formated-results)。
Expected: exec REPL 起来(真 claude,能看到 771 DARE skill),接收 topic + 强制项。

- [ ] **Step 4: E3 真研究 — sim↔exec 真来回多轮,exec 末步真出 formated-results 结构块**

Expected: sim 与 exec 真多轮对话,exec 真跑 DARE,末步产出一个 `research-result` 围栏 + JSON payload(对齐 Spec B 的 concat 契约:` ```research-result ` 开栏、JSON body、` ``` ` 闭栏)。

- [ ] **Step 5: E4 真算 loss — codex 真读 transcript,injection-fidelity 真吐 loss1.json**

起 codex(loss config-dir),注入 injection-fidelity SKILL.md 全文 + transcript payload。
Expected: codex 真吐一个 `loss1.json`(结构合 Spec B schema:`fidelity` bool + `loss1` float + `per_axis_evidence`),保真值可解释,非桩。

- [ ] **Step 6: E5 留痕 — trace.jsonl / transcript.md / triple.json 真落**

Expected: `runs/<id>/trace.jsonl` 真落 `run_start→rung_start→dialogue_turn→rung_done` 四类事件;`transcripts/<sample>.md` 真从 exec session jsonl 提取(走 `--logs-dir` 必填脚本,不含绝对 log 路径);`triples/<sample>.json` 真拼成三元组。

- [ ] **Step 7: 薄片通过判定(全真、产物形态对)**

Run(检查产物齐全且无隐私泄漏):
```bash
ls runs/*/trace.jsonl runs/*/transcripts/*.md runs/*/triples/*.json runs/*/loss/*.loss1.json
grep -rl '/workspace/home/.*/.claude/projects' runs/*/transcripts runs/*/triples 2>/dev/null && echo "LEAK!" || echo "NO LEAK"
```
Expected: 四类产物齐全;打印 `NO LEAK`(transcript/triple 不含 CC log 绝对路径,隐私红线成立)。

> **黄金合成样例**:E1–E5 用的这条 config+topic 固定存档 `<proj>/fixtures/golden-slice/`,成为三拆共用回归场景,逐层加深(A:1 run 纵向通路;B:6 档阶梯;C:48-run 收敛)。

---

## Self-Review(对照 Spec A 检查)

- **Phase 0.1–0.8 覆盖**:Task 1(node)/ 2(claude+codex)/ 3(tmux+hf)/ 4(env.sh)/ 5(bootstrap.sh)/ 6(config-dir 预批)/ 7(cwd)/ 8(skill 复制)逐一对应,无缺。
- **完成判定 1+3 覆盖**:Task 9 = 冒烟 S1–S4;Task 10 = 薄片 E1–E5。两层齐。
- **skill 复制矩阵覆盖**:Task 8 四身份(exec 771+formated-*、sim 仅 sp、optim optimization-loop 占位、loss 两 loss + codex 规范)对齐 Spec A 第 4 节。
- **隔离四维度覆盖**:config-dir(Task 6)、cwd(Task 7)、启动式(Task 9 S2 / Task 10 直起命令)、凭证(Task 4 两组隔离)齐。
- **红线覆盖**:一切落 /workspace(全程)、两组 key 隔离(Task 4)、key 不进提交物(Task 4 占位)、CC log 路径不进产物(Task 10 Step 7 NO LEAK 校验)。
- **placeholder 扫描**:env.sh 的 `<在此填...>` / `.claude.json` 的 `<KEY_TAIL>` / Task 8 的"占位 skill"是**有意的执行者填空与 Spec B 衔接点**,非计划缺口——已在正文说明谁来填、何时填。

## Execution Handoff

见索引 plan `2026-06-07-INDEX-triple-cc-pretrain.md`。本 plan(A)是 B/C 的前置:A 验过(S1–S4 + E1–E5 全绿)才进 B。
