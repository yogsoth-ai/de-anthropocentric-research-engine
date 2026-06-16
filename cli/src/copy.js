'use strict';
const fs = require('node:fs');

function ensureMcpJson(templatePath, destPath) {
  if (fs.existsSync(destPath)) return 'skipped';
  fs.copyFileSync(templatePath, destPath);
  return 'created';
}

module.exports = { ensureMcpJson };
