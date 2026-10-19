# PDF backend: tachyon-tex-cli

Default PDF renderer for this port. Replaces manual tectonic/Pandoc setup in upstream Stage 5 FINALIZE / academic-paper Phase 7.

## Skill
`.opencode/skills/tachyon-tex/` vendored from `srsergi0/tachyon-tex-cli` `skills/tachyon-tex` (Fair Source 0.9, see skill LICENSE). Load via OpenCode skill tool: `skill(name="tachyon-tex")`.

## No global install
Requires Node.js 22+ only:
```sh
npx --yes github:srsergi0/tachyon-tex-cli --help
npx --yes github:srsergi0/tachyon-tex-cli main.tex --json
npx --yes github:srsergi0/tachyon-tex-cli ./project --main main.tex --output ./build/paper.pdf --json
```
Or self-contained: `node .opencode/skills/tachyon-tex/scripts/cli.mjs main.tex --json`.

Binary auto-downloads per OS/CPU with SHA-256 verify into user cache. First build downloads LaTeX packages; later builds reuse cache. `--offline` needs cached binary+packages.

## Pipeline wiring
- `academic-paper` Phase 7 / `format-convert`: Markdown → `.tex` (existing templates), then compile with tachyon-tex. Keep `.tex` source; PDF is a build artifact.
- `academic-pipeline` Stage 5: user picks MD / PDF / LaTeX source. PDF path always goes through tachyon-tex.
- Engine: default `auto` (= embedded Tectonic 0.17 for ordinary LaTeX/math/TikZ/BibTeX). Escalate to `--engine latexmk --tex-engine pdflatex|lualatex` for biblatex/Biber, Lua code, minted (`--shell-escape`, trusted docs only).

## Verify (as tested 2026-10-19)
Multi-file article (main + 4 inputs + .bib, TikZ/PGFPlots, theorems, TOC) compiled `ok:true`, engine `tectonic`, PDF 48,989 bytes `%PDF-1.5`. Only `Overfull hbox` warnings.

## Live preview
```sh
npx --yes github:srsergi0/tachyon-tex-cli background ./project --main main.tex --open
npx --yes github:srsergi0/tachyon-tex-cli status --json
npx --yes github:srsergi0/tachyon-tex-cli logs ./project
npx --yes github:srsergi0/tachyon-tex-cli stop ./project
```
Binds `127.0.0.1`, keeps last good PDF on error.

## DOCX
Unchanged: Pandoc path from upstream when needed. This doc covers PDF only.
