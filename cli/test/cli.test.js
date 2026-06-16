const { test } = require('node:test');
const assert = require('node:assert');
const { execFileSync } = require('node:child_process');
const path = require('node:path');

const BIN = path.join(__dirname, '..', 'bin', 'dare.js');

function run(args) {
  try {
    const out = execFileSync('node', [BIN, ...args], { encoding: 'utf8' });
    return { code: 0, out };
  } catch (e) {
    return { code: e.status, out: (e.stdout || '') + (e.stderr || '') };
  }
}

test('no subcommand prints usage and exits non-zero', () => {
  const r = run([]);
  assert.notStrictEqual(r.code, 0);
  assert.match(r.out, /usage/i);
});

test('unknown subcommand prints usage and exits non-zero', () => {
  const r = run(['frobnicate']);
  assert.notStrictEqual(r.code, 0);
  assert.match(r.out, /usage/i);
});
