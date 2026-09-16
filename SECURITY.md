# Security Policy

## Supported Versions

Security fixes are applied to the latest release of the skill library and the
published `@yogsoth-ai/dare` CLI. Older tags are not patched; please update
before reporting an issue against an outdated version.

| Version | Supported |
| ------- | --------- |
| Latest release (`main`) | ✅ |
| Previous releases | ❌ |

## Reporting a Vulnerability

Please report security issues privately rather than in a public issue.

1. Open a [private security advisory](https://github.com/yogsoth-ai/de-anthropocentric-research-engine/security/advisories/new)
   for this repository (preferred — private vulnerability reporting is
   enabled), or
2. email **Pthahnix@proton.me** with the details.

Include the affected path, a description of the impact, and the steps needed to
reproduce it. Please do not disclose the issue publicly until a fix is
available.

### Response expectations

- Acknowledgement within **5 business days**.
- An initial assessment, including severity and a remediation plan, within
  **10 business days**.
- Credit in the release notes once a fix ships, unless you prefer to remain
  anonymous.

## Scope

This repository is a library of markdown skills plus a small Node.js installer
CLI and a DeepSeek Harness plugin. The following are in scope:

- the installer CLI (`cli/`) and the DSH plugin (`dsh-plugin/`);
- repository automation under `.github/workflows/`;
- any skill that instructs an agent to execute commands, write files, or reach
  external services.

Out of scope: vulnerabilities in third-party MCP servers referenced by
`mcp.example.json`, and issues in the AI models or harnesses that run these
skills. Please report those to their respective maintainers.

## Safe Harbour

We will not pursue action against researchers who report issues in good faith,
avoid privacy violations and data destruction, and give us reasonable time to
respond before any public disclosure.
