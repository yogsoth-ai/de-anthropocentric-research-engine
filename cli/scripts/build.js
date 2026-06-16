'use strict';
const fs = require('node:fs');
const path = require('node:path');

function build(repoRoot, outDir) {
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });
  fs.cpSync(path.join(repoRoot, 'skills'), path.join(outDir, 'skills'), { recursive: true });
  fs.copyFileSync(
    path.join(repoRoot, 'mcp.example.json'),
    path.join(outDir, 'mcp.example.json')
  );
}

if (require.main === module) {
  const repoRoot = path.join(__dirname, '..', '..');
  const outDir = path.join(__dirname, '..', 'payload');
  build(repoRoot, outDir);
  process.stdout.write(`build: payload regenerated at ${outDir}\n`);
}

module.exports = { build };
