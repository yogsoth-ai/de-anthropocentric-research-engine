'use strict';

const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { CODEX_ADAPTER_REL, SOURCE_ADAPTER_REL, installCodex, parseArgs } = require('./codex.js');

function tmp(prefix) {
  return fs.mkdtempSync(path.join(os.tmpdir(), prefix));
}

function seedRepo() {
  const repo = tmp('dare-repo-');
  fs.mkdirSync(path.join(repo, path.dirname(SOURCE_ADAPTER_REL)), { recursive: true });
  fs.writeFileSync(path.join(repo, SOURCE_ADAPTER_REL), 'adapter\n');
  fs.mkdirSync(path.join(repo, 'skills', 'de-anthropocentric-research-engine'), { recursive: true });
  fs.mkdirSync(path.join(repo, 'skills', 'research-catalog'), { recursive: true });
  fs.writeFileSync(path.join(repo, 'skills', 'de-anthropocentric-research-engine', 'SKILL.md'), 'root\n');
  fs.writeFileSync(path.join(repo, 'skills', 'research-catalog', 'SKILL.md'), 'catalog\n');
  return repo;
}

test('parseArgs defaults to copy mode', () => {
  const opts = parseArgs(['--target', 'project']);
  assert.strictEqual(opts.mode, 'copy');
  assert.ok(opts.targetDir.endsWith('project'));
});

test('parseArgs supports explicit link mode', () => {
  const opts = parseArgs(['--target', 'project', '--link']);
  assert.strictEqual(opts.mode, 'link');
});

test('installCodex installs adapter and copies skills into external target by default', () => {
  const repoRoot = seedRepo();
  const targetDir = tmp('dare-target-');

  const result = installCodex({ repoRoot, targetDir });

  assert.strictEqual(result.adapter.status, 'created');
  assert.strictEqual(result.skills.status, 'copied');
  assert.strictEqual(fs.readFileSync(path.join(targetDir, CODEX_ADAPTER_REL), 'utf8'), 'adapter\n');
  assert.strictEqual(
    fs.readFileSync(path.join(targetDir, '.dare', 'skills', 'research-catalog', 'SKILL.md'), 'utf8'),
    'catalog\n'
  );
});

test('installCodex links skills only when explicitly requested', () => {
  const repoRoot = seedRepo();
  const targetDir = tmp('dare-target-');

  const result = installCodex({ repoRoot, targetDir, mode: 'link' });

  assert.strictEqual(result.skills.status, 'linked');
  assert.strictEqual(fs.lstatSync(path.join(targetDir, '.dare', 'skills')).isSymbolicLink(), true);
});

test('installCodex is idempotent when files already match', () => {
  const repoRoot = seedRepo();
  const targetDir = tmp('dare-target-');

  installCodex({ repoRoot, targetDir, mode: 'copy' });
  const result = installCodex({ repoRoot, targetDir, mode: 'copy' });

  assert.strictEqual(result.adapter.status, 'unchanged');
  assert.strictEqual(result.skills.status, 'existing-dare-skills');
});

test('installCodex does not overwrite different adapter without force', () => {
  const repoRoot = seedRepo();
  const targetDir = tmp('dare-target-');
  fs.mkdirSync(path.join(targetDir, path.dirname(CODEX_ADAPTER_REL)), { recursive: true });
  fs.writeFileSync(path.join(targetDir, CODEX_ADAPTER_REL), 'custom\n');

  assert.throws(
    () => installCodex({ repoRoot, targetDir, mode: 'copy' }),
    /--force/
  );
});

test('installCodex creates Codex adapter but uses repo skills when target is repo root', () => {
  const repoRoot = seedRepo();

  const result = installCodex({ repoRoot, targetDir: repoRoot, mode: 'copy' });

  assert.strictEqual(result.adapter.status, 'created');
  assert.strictEqual(result.skills.status, 'using-repo-skills');
  assert.strictEqual(fs.readFileSync(path.join(repoRoot, CODEX_ADAPTER_REL), 'utf8'), 'adapter\n');
  assert.strictEqual(fs.existsSync(path.join(repoRoot, '.dare', 'skills')), false);
});
