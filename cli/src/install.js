'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { copySkills, ensureMcpJson } = require('./copy.js');

function runInstall({ cwd, payloadDir }) {
  const srcSkills = path.join(payloadDir, 'skills');
  const tpl = path.join(payloadDir, 'mcp.example.json');
  if (!fs.existsSync(srcSkills) || !fs.existsSync(tpl)) {
    throw new Error(
      `Bundled payload not found at ${payloadDir}. The package may be corrupt — reinstall @yogsoth-ai/dare.`
    );
  }
  const destSkills = path.join(cwd, '.claude', 'skills');
  const { added, skipped, failed, failures } = copySkills(srcSkills, destSkills);
  const mcpResult = ensureMcpJson(tpl, path.join(cwd, '.mcp.json'));
  return { added, skipped, failed, failures, mcpResult };
}

module.exports = { runInstall };
