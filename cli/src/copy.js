'use strict';
const fs = require('node:fs');
const path = require('node:path');

function ensureMcpJson(templatePath, destPath) {
  if (fs.existsSync(destPath)) return 'skipped';
  fs.copyFileSync(templatePath, destPath);
  return 'created';
}

function copySkills(srcSkillsDir, destSkillsDir) {
  fs.mkdirSync(destSkillsDir, { recursive: true });
  let added = 0, skipped = 0, failed = 0;
  const failures = [];
  const entries = fs.readdirSync(srcSkillsDir, { withFileTypes: true });
  for (const e of entries) {
    if (!e.isDirectory()) continue;
    const dest = path.join(destSkillsDir, e.name);
    if (fs.existsSync(dest)) { skipped++; continue; }
    try {
      fs.cpSync(path.join(srcSkillsDir, e.name), dest, { recursive: true });
      added++;
    } catch (err) {
      failed++;
      failures.push({ skill: e.name, error: err.message });
    }
  }
  return { added, skipped, failed, failures };
}

module.exports = { ensureMcpJson, copySkills };
