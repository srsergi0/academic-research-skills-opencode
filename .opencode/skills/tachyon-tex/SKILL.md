---
name: tachyon-tex
description: "Portable LaTeX to PDF via tachyon-tex-cli: Tectonic default, latexmk fallback, live preview. Use for .tex compile, engine choice, diagnostics."
license: Fair-Source-0.9
compatibility: opencode
metadata:
  upstream: "srsergi0/tachyon-tex-cli skills/tachyon-tex"
  opencode/slash: "true"
---
> **OpenCode port note.** Vendored from `srsergi0/tachyon-tex-cli` `skills/tachyon-tex`. Requires Node.js 22+. Preferred invocation here: `npx --yes github:srsergi0/tachyon-tex-cli <input> --json` (no global install) or `node .opencode/skills/tachyon-tex/scripts/cli.mjs`. Default PDF backend for Stage 5 FINALIZE / academic-paper Phase 7 in this repo. See `docs/PDF_BACKEND_TACHYON.md`.

# Tachyon TeX

Requires Node.js 22+ and network for initial binary/package installation; cached compilation supports offline use.

Run `node <this-skill-directory>/scripts/cli.mjs --help` to inspect commands. Resolve the script relative to this loaded SKILL.md; it needs no checkout or npm dependencies. Use argument arrays or quote paths with spaces. The helper detects OS/CPU, downloads the matching release, verifies SHA-256, and caches it automatically. Do not invent an installed executable path or ask the user to download a platform manually.

## Compile and diagnose

- Inspect the project to identify the main document and required assets. Pass a `.tex` file directly, or a directory/ZIP with `--main` when several documents exist. Keep includes, graphics, bibliographies, and local classes beside their source project.
- Run `node <skill-directory>/scripts/cli.mjs <input> --output <desired.pdf> --json --keep-logs`. Read the exit status and JSON on stdout; diagnostics/update messages appear on stderr. Report the actual output path after success. Failed compilation preserves the last successful PDF.
- Use embedded Tectonic for ordinary LaTeX/XeTeX and BibTeX. For pdfLaTeX, LuaLaTeX, biblatex/Biber, or external programs, use `--engine latexmk` and the appropriate `--tex-engine`. Portable full TeX installs automatically for recognized requirements. Read [engine guidance](references/engines.md) for advanced projects or package/tool failures.
- Read the first meaningful file/line diagnostic before changing anything. Distinguish invalid source from missing files, fonts, packages, external programs, and unavailable network/cache. Fix source only within the user's editing scope. Do not silently remove features or repeatedly rerun an unchanged failure. Recompile after a concrete correction; stop after three unsuccessful correction attempts and report the remaining cause and log path.
- Use `--offline` after the binary and required packages are cached. `--no-auto-update` keeps the installed binary; `--no-update-check` skips release checks. Normal use checks hourly and automatically installs verified new releases.

## Live preview

Run `node <skill-directory>/scripts/cli.mjs background <file-or-directory> --main main.tex --json` for a preview that survives the calling terminal. Omit `--main` for a direct file or unambiguous project. Add `--open` if the user wants the browser opened. Return the `http://127.0.0.1:...` preview URL.

Check `status <input> --json` until the session is `ready` or `error`; startup may be `starting`/`compiling`. A returned URL alone does not prove compilation succeeded. Poll at a reasonable interval (for example 2 seconds) with a bounded wait, then inspect `logs <input>` if still compiling or in error. Avoid `logs --follow` for a finite diagnostic because it stays attached until interrupted.

Source changes recompile and refresh the browser. Includes, packages, bibliographies, graphics, and data under the root are watched; files outside it and symlinks are not. Extract ZIP projects before watching. Errors appear in the preview/logs while retaining the last good PDF.

Use `status`, `logs`, and `stop` with the same input path. `stop --all` affects every session and should only be used when the user intends that. Leave a requested preview running; stop temporary verification sessions when finished. Read [session guidance](references/sessions.md) for multiple sessions and shutdown failures.
