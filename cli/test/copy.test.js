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
