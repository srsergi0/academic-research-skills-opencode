---
description: ARS compile paper to PDF via tachyon-tex
---

Load skills `academic-paper` then `tachyon-tex` with the OpenCode `skill` tool.

User request: $ARGUMENTS

Instructions:
1. skill(name="academic-paper"): produce/review the `.tex` source (format-convert / Phase 7). Keep the `.tex` as source of truth.
2. skill(name="tachyon-tex"): compile with `npx --yes github:srsergi0/tachyon-tex-cli <main.tex> --json` or `node .opencode/skills/tachyon-tex/scripts/cli.mjs <main.tex> --output <paper.pdf> --json --keep-logs`.
3. Default engine `auto` (Tectonic). Escalate to `--engine latexmk --tex-engine pdflatex|lualatex` only for biblatex/Biber, Lua, minted.
4. Report output PDF path, engine, duration_ms, warnings. On failure read first file/line diagnostic, fix source, recompile (max 3 tries).
5. Backend doc: `docs/PDF_BACKEND_TACHYON.md`.
