---
description: ARS ars-full - Academic pipeline full: research to finalize
---

Load the skill `academic-pipeline` with the OpenCode `skill` tool, then run mode `full pipeline (10 stages: research, write, integrity 2.5, review, revise, re-review, final integrity 4.5, finalize)`.

User request: $ARGUMENTS

Instructions:
1. Use skill tool: skill(name="academic-pipeline").
2. Follow `.opencode/skills/academic-pipeline/SKILL.md` mode `full pipeline (10 stages: research, write, integrity 2.5, review, revise, re-review, final integrity 4.5, finalize)`. Mode registry: `MODE_REGISTRY.md`.
3. Shared contracts: `.opencode/shared/`.
4. Human-in-the-loop: stop at each checkpoint and ask user to confirm before advancing. Integrity gates 2.5/4.5 are mandatory.
5. If skill files cannot be loaded, report failure and stop. Do not substitute this summary for mode instructions.
6. Upstream: Imbad0202/academic-research-skills v3.23.1. This is an OpenCode port, CC-BY-NC-4.0, non-commercial only.
