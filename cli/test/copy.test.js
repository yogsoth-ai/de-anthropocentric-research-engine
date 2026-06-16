const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { ensureMcpJson } = require('../src/copy.js');

function tmp() {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'dare-test-'));
}

test('ensureMcpJson creates file when absent', () => {
  const dir = tmp();
  const tpl = path.join(dir, 'mcp.example.json');
  const dest = path.join(dir, '.mcp.json');
  fs.writeFileSync(tpl, '{"mcpServers":{}}');
  const result = ensureMcpJson(tpl, dest);
  assert.strictEqual(result, 'created');
  assert.strictEqual(fs.readFileSync(dest, 'utf8'), '{"mcpServers":{}}');
});

test('ensureMcpJson skips when dest exists', () => {
  const dir = tmp();
  const tpl = path.join(dir, 'mcp.example.json');
  const dest = path.join(dir, '.mcp.json');
  fs.writeFileSync(tpl, '{"mcpServers":{"a":1}}');
  fs.writeFileSync(dest, '{"user":"kept"}');
  const result = ensureMcpJson(tpl, dest);
  assert.strictEqual(result, 'skipped');
  assert.strictEqual(fs.readFileSync(dest, 'utf8'), '{"user":"kept"}');
});

const { copySkills } = require('../src/copy.js');

function seedSkill(root, name, files) {
  const d = path.join(root, name);
  fs.mkdirSync(d, { recursive: true });
  for (const [f, content] of Object.entries(files)) {
    fs.writeFileSync(path.join(d, f), content);
  }
}

test('copySkills fresh install copies all, dest auto-created', () => {
  const dir = tmp();
  const src = path.join(dir, 'skills');
  const dest = path.join(dir, '.claude', 'skills');
  seedSkill(src, 'alpha', { 'SKILL.md': 'A' });
  seedSkill(src, 'beta', { 'SKILL.md': 'B' });
  const r = copySkills(src, dest);
  assert.strictEqual(r.added, 2);
  assert.strictEqual(r.skipped, 0);
  assert.strictEqual(r.failed, 0);
  assert.strictEqual(fs.readFileSync(path.join(dest, 'alpha', 'SKILL.md'), 'utf8'), 'A');
});

test('copySkills skips same-named dir, never overwrites', () => {
  const dir = tmp();
  const src = path.join(dir, 'skills');
  const dest = path.join(dir, '.claude', 'skills');
  seedSkill(src, 'alpha', { 'SKILL.md': 'NEW' });
  seedSkill(src, 'beta', { 'SKILL.md': 'B' });
  seedSkill(dest, 'alpha', { 'SKILL.md': 'USER-EDIT' });
  const r = copySkills(src, dest);
  assert.strictEqual(r.added, 1);
  assert.strictEqual(r.skipped, 1);
  assert.strictEqual(fs.readFileSync(path.join(dest, 'alpha', 'SKILL.md'), 'utf8'), 'USER-EDIT');
  assert.strictEqual(fs.readFileSync(path.join(dest, 'beta', 'SKILL.md'), 'utf8'), 'B');
});
