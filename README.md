# academic-research-skills-opencode

OpenCode port of `Imbad0202/academic-research-skills` v3.23.1.

Based on Academic Research Skills by Cheng-I Wu — https://github.com/Imbad0202/academic-research-skills — licensed CC-BY-NC-4.0. Non-commercial only.

## What this is
5 OpenCode skills + 16 `/ars-*` commands covering research → write → review → revise → finalize, with mandatory human checkpoints and integrity gates.

Skills live in `.opencode/skills/` (also readable by OpenCode from `.claude/skills` and `.agents/skills` if you copy them there):

- `deep-research` v2.12.1 — 13 agents, 8 modes
- `academic-paper` v3.3.1 — 12 agents, 11 modes
- `academic-paper-reviewer` v1.11.1 — 7 agents, 6 modes
- `academic-pipeline` v3.23.1 — 10-stage orchestrator
- `sr-screener` v1.0.0 — dual blinded screening + adjudicator

Upstream commit pinned in `.upstream-version`. `MODE_REGISTRY.md` and `.opencode/shared/` vendored from upstream.

## Idioma: español + inglés (por defecto `es-en`)
Resúmenes bilingües ES+EN, guía APA en español, cribado y ejemplos en español. Detalle y excepciones: `docs/SPANISH_SUPPORT.md`.

## Flujo completo: de la idea al artículo
Guía paso a paso con comandos, checkpoints y qué esperar en cada stage: `docs/FLUJO_CREAR_ARTICULO.md`.

## Install (project-local, no global install)
```sh
git clone https://github.com/<you>/academic-research-skills-opencode.git
# copy into your project:
cp -R academic-research-skills-opencode/.opencode /path/to/project/.opencode
cp academic-research-skills-opencode/MODE_REGISTRY.md /path/to/project/MODE_REGISTRY.md
```
Then in OpenCode: `/ars-plan`, `/ars-full`, `/ars-reviewer`, `/ars-pdf`, `/ars-preview`, etc. Or invoke skill directly: `skill(name="academic-pipeline")`.

## PDF backend: tachyon-tex-cli (default)
PDF goes through vendored skill `.opencode/skills/tachyon-tex/` (from `srsergi0/tachyon-tex-cli`, Fair Source 0.9). No global install, needs Node.js 22+:
```sh
npx --yes github:srsergi0/tachyon-tex-cli main.tex --json
```
Details: `docs/PDF_BACKEND_TACHYON.md`. DOCX still via Pandoc path from upstream.

## OpenCode differences
- Frontmatter made OpenCode-compliant: `name` matches dir, `description` <=1024 chars, `metadata.opencode/slash: "true"`. Full trigger lists stay in body.
- `${CLAUDE_PLUGIN_ROOT}` → repo root / `.opencode/`. Claude hooks, plugin agents allowlist, SessionStart announce do NOT run in OpenCode.
- Subagent orchestration: use OpenCode subagents manually; `sr-screener` dual review needs two subagent calls + adjudication.
- Python scripts: only `scripts/validate_skills.py` ships here. Upstream `scripts/` verification cache etc. require the full upstream checkout.
- See `docs/OPENCODE_MAP.md` for control matrix.

## Integrity boundary
Same as upstream: checks manuscript and reported process, does NOT prove experiments were run or data are authentic. Human remains author. Advisory warnings can be acked with `/ars-mark-read`, reverted with `/ars-unmark-read`.

## License
CC-BY-NC-4.0, see `LICENSE.UPSTREAM`. Attribution required. No commercial use.
