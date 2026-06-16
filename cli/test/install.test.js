const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { runInstall } = require('../src/install.js');

function tmp() {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'dare-inst-'));
}

function seedPayload(payloadDir) {
  const skills = path.join(payloadDir, 'skills');
  fs.mkdirSync(path.join(skills, 'alpha'), { recursive: true });
  fs.writeFileSync(path.join(skills, 'alpha', 'SKILL.md'), 'A');
  fs.writeFileSync(path.join(payloadDir, 'mcp.example.json'), '{"mcpServers":{}}');
}

test('runInstall populates .claude/skills and creates .mcp.json', () => {
  const cwd = tmp();
  const payloadDir = tmp();
  seedPayload(payloadDir);
  const r = runInstall({ cwd, payloadDir });
  assert.strictEqual(r.added, 1);
  assert.strictEqual(r.skipped, 0);
  assert.strictEqual(r.mcpResult, 'created');
  assert.ok(fs.existsSync(path.join(cwd, '.claude', 'skills', 'alpha', 'SKILL.md')));
  assert.ok(fs.existsSync(path.join(cwd, '.mcp.json')));
});

test('runInstall throws clear error when payload missing', () => {
  const cwd = tmp();
  const payloadDir = path.join(tmp(), 'nonexistent');
  assert.throws(() => runInstall({ cwd, payloadDir }), /payload/i);
});
