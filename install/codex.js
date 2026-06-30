#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');

const SOURCE_ADAPTER_REL = path.join('agents', 'skills', 'dare-research-engine', 'SKILL.md');
const CODEX_ADAPTER_REL = path.join('.agents', 'skills', 'dare-research-engine', 'SKILL.md');
const REQUIRED_SKILLS = [
  path.join('de-anthropocentric-research-engine', 'SKILL.md'),
  path.join('research-catalog', 'SKILL.md')
];

function usage() {
  return `Usage: node install/codex.js [options]

Install the DARE Codex adapter from this cloned repository into a target project.

Options:
  --target <dir>   Project directory to install into (default: current directory)
  --copy           Copy the DARE skills knowledge base into .dare/skills
  --link           Symlink .dare/skills to this clone's skills directory
  --force          Replace an existing adapter file
  --dry-run        Show what would change without writing files
  -h, --help       Show this help

Default behavior copies the knowledge base so the target still works if this clone is removed.
`;
}

function parseArgs(argv) {
  const opts = {
    targetDir: process.cwd(),
    mode: 'copy',
    force: false,
    dryRun: false,
    help: false
  };

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--target') {
      const value = argv[++i];
      if (!value) throw new Error('--target requires a directory');
      opts.targetDir = value;
    } else if (arg === '--copy') {
      opts.mode = 'copy';
    } else if (arg === '--link') {
      opts.mode = 'link';
    } else if (arg === '--force') {
      opts.force = true;
    } else if (arg === '--dry-run') {
      opts.dryRun = true;
    } else if (arg === '-h' || arg === '--help') {
      opts.help = true;
    } else {
      throw new Error(`Unknown option: ${arg}`);
    }
  }

  opts.targetDir = path.resolve(opts.targetDir);
  return opts;
}

function repoRootFromScript() {
  return path.resolve(__dirname, '..');
}

function fileExists(filePath) {
  try {
    return fs.statSync(filePath).isFile();
  } catch {
    return false;
  }
}

function dirExists(dirPath) {
  try {
    return fs.statSync(dirPath).isDirectory();
  } catch {
    return false;
  }
}

function realPathOrNull(p) {
  try {
    return fs.realpathSync.native(p);
  } catch {
    return null;
  }
}

function samePath(a, b) {
  const realA = realPathOrNull(a);
  const realB = realPathOrNull(b);
  return realA !== null && realB !== null && realA === realB;
}

function validateRepo(repoRoot) {
  const adapter = path.join(repoRoot, SOURCE_ADAPTER_REL);
  const skillsRoot = path.join(repoRoot, 'skills');
  if (!fileExists(adapter)) {
    throw new Error(`Codex adapter not found at ${adapter}`);
  }
  for (const skill of REQUIRED_SKILLS) {
    const required = path.join(skillsRoot, skill);
    if (!fileExists(required)) {
      throw new Error(`Required DARE skill not found at ${required}`);
    }
  }
}

function validateSkillsRoot(skillsRoot) {
  for (const skill of REQUIRED_SKILLS) {
    const required = path.join(skillsRoot, skill);
    if (!fileExists(required)) {
      throw new Error(`Existing skills root is not a DARE skills tree: missing ${required}`);
    }
  }
}

function readIfExists(filePath) {
  try {
    return fs.readFileSync(filePath, 'utf8');
  } catch (err) {
    if (err && err.code === 'ENOENT') return null;
    throw err;
  }
}

function installAdapter({ repoRoot, targetDir, force, dryRun }) {
  const source = path.join(repoRoot, SOURCE_ADAPTER_REL);
  const dest = path.join(targetDir, CODEX_ADAPTER_REL);

  if (samePath(source, dest)) {
    return { status: 'already-present', path: dest };
  }

  const sourceBody = fs.readFileSync(source, 'utf8');
  const existingBody = readIfExists(dest);
  if (existingBody !== null) {
    if (existingBody === sourceBody) {
      return { status: 'unchanged', path: dest };
    }
    if (!force) {
      throw new Error(`Adapter already exists and differs: ${dest}. Re-run with --force to replace it.`);
    }
  }

  if (!dryRun) {
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(source, dest);
  }

  if (dryRun) {
    return { status: existingBody === null ? 'would-create' : 'would-replace', path: dest };
  }
  return { status: existingBody === null ? 'created' : 'replaced', path: dest };
}

function installSkillsPointer({ repoRoot, targetDir, mode, dryRun }) {
  const source = path.join(repoRoot, 'skills');

  if (samePath(repoRoot, targetDir)) {
    return { status: 'using-repo-skills', path: source };
  }

  const dest = path.join(targetDir, '.dare', 'skills');
  if (fs.existsSync(dest)) {
    validateSkillsRoot(dest);
    if (samePath(source, dest)) {
      return { status: 'linked-existing', path: dest };
    }
    return { status: 'existing-dare-skills', path: dest };
  }

  if (dryRun) {
    return { status: mode === 'link' ? 'would-link' : 'would-copy', path: dest };
  }

  fs.mkdirSync(path.dirname(dest), { recursive: true });

  if (mode === 'copy') {
    fs.cpSync(source, dest, { recursive: true });
    return { status: 'copied', path: dest };
  }

  try {
    const linkType = process.platform === 'win32' ? 'junction' : 'dir';
    fs.symlinkSync(source, dest, linkType);
    return { status: 'linked', path: dest, source };
  } catch (err) {
    if (mode === 'link') {
      throw new Error(`Could not create symlink ${dest} -> ${source}: ${err.message}`);
    }
    fs.cpSync(source, dest, { recursive: true });
    return { status: 'copied-fallback', path: dest, linkError: err.message };
  }
}

function installCodex(options = {}) {
  const repoRoot = path.resolve(options.repoRoot || repoRootFromScript());
  const targetDir = path.resolve(options.targetDir || process.cwd());
  const mode = options.mode || 'copy';
  const force = Boolean(options.force);
  const dryRun = Boolean(options.dryRun);

  if (!['copy', 'link'].includes(mode)) {
    throw new Error(`Invalid mode: ${mode}`);
  }
  if (!dirExists(targetDir)) {
    throw new Error(`Target directory does not exist: ${targetDir}`);
  }

  validateRepo(repoRoot);

  const adapter = installAdapter({ repoRoot, targetDir, force, dryRun });
  const skills = installSkillsPointer({ repoRoot, targetDir, mode, dryRun });

  return { repoRoot, targetDir, adapter, skills, dryRun };
}

function formatResult(result) {
  const lines = [
    'dare-codex-install:',
    `  repo: ${result.repoRoot}`,
    `  target: ${result.targetDir}`,
    `  adapter: ${result.adapter.status} ${result.adapter.path}`,
    `  skills: ${result.skills.status} ${result.skills.path}`,
    '  invoke: $dare-research-engine',
    '  mcp: not configured by this installer'
  ];
  if (result.skills.source) {
    lines.splice(5, 0, `  skills_source: ${result.skills.source}`);
  }
  if (result.skills.linkError) {
    lines.splice(5, 0, `  link_fallback_reason: ${result.skills.linkError}`);
  }
  if (result.dryRun) {
    lines.splice(1, 0, '  dry_run: true');
  }
  return `${lines.join('\n')}\n`;
}

function main(argv) {
  let opts;
  try {
    opts = parseArgs(argv);
    if (opts.help) {
      process.stdout.write(usage());
      return 0;
    }
    const result = installCodex(opts);
    process.stdout.write(formatResult(result));
    return 0;
  } catch (err) {
    process.stderr.write(`dare-codex-install: ${err.message}\n\n${usage()}`);
    return 1;
  }
}

if (require.main === module) {
  process.exitCode = main(process.argv.slice(2));
}

module.exports = {
  CODEX_ADAPTER_REL,
  SOURCE_ADAPTER_REL,
  parseArgs,
  installCodex,
  formatResult
};
