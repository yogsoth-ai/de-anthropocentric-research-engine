const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { build } = require('../scripts/build.js');

function tmp() {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'dare-build-'));
}

test('build copies skills/ and mcp.example.json into outDir, wiping stale', () => {
  const repoRoot = tmp();
  fs.mkdirSync(path.join(repoRoot, 'skills', 'alpha'), { recursive: true });
  fs.writeFileSync(path.join(repoRoot, 'skills', 'alpha', 'SKILL.md'), 'A');
  fs.writeFileSync(path.join(repoRoot, 'mcp.example.json'), '{"mcpServers":{}}');
  const outDir = path.join(tmp(), 'payload');
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'STALE.txt'), 'old');

  build(repoRoot, outDir);

  assert.ok(fs.existsSync(path.join(outDir, 'skills', 'alpha', 'SKILL.md')));
  assert.ok(fs.existsSync(path.join(outDir, 'mcp.example.json')));
  assert.strictEqual(fs.existsSync(path.join(outDir, 'STALE.txt')), false);
});
