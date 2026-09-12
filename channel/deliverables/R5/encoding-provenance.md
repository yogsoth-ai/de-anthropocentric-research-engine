# Encoding damage provenance

The corruption entered during the 2026-09-12 historical-94 cleanup commit `8094292` (clean baseline `e78eefa`, damaged commit `8094292`). The damaged files gained cp936 mojibake (`≥` became `鈮?`, arrows/quotes became `鈥?`) and BOMs.

Cause: UTF-8 text was passed through a cp936/GBK decode/encode path while rewriting the pilot bodies. Three-byte UTF-8 sequences were paired as cp936 characters; the remaining byte was lost or merged with the following ASCII character. Because `≥`, `≤`, `≈`, and `≠` collapse to the same damaged prefix, character substitution is unsafe and can reverse a criterion.

Preventive rule: never pipe Markdown through the platform-default text encoding. Use Python or PowerShell with explicit UTF-8 read/write (`encoding='utf-8'`, `Set-Content -Encoding utf8`), preserve newline mode, and verify a byte-level diff plus a CJK/replacement scan after every rewrite. Recover ledger rows from v3 source coordinates rather than mapping mojibake characters.
