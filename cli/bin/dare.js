#!/usr/bin/env node
'use strict';
const path = require('node:path');
const { runInstall } = require('../src/install.js');

const USAGE = `Usage: dare <command>

Commands:
  install    Copy DARE skills into ./.claude/skills and create .mcp.json
`;

function main(argv) {
  const cmd = argv[2];
  if (cmd !== 'install') {
    process.stderr.write(USAGE);
    process.exit(1);
  }
  const payloadDir = path.join(__dirname, '..', 'payload');
  try {
    const r = runInstall({ cwd: process.cwd(), payloadDir });
    process.stdout.write(
      `dare: added ${r.added}, skipped ${r.skipped} skills` +
      (r.failed ? `, ${r.failed} failed` : '') +
      `; .mcp.json ${r.mcpResult}\n`
    );
    if (r.failed) {
      for (const f of r.failures) {
        process.stderr.write(`  failed: ${f.skill} — ${f.error}\n`);
      }
    }
    if (r.mcpResult === 'created') {
      process.stdout.write('dare: fill in your API keys in .mcp.json\n');
    }
    process.exit(0);
  } catch (err) {
    process.stderr.write(`dare: ${err.message}\n`);
    process.exit(1);
  }
}

main(process.argv);
