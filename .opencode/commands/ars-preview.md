---
description: ARS live PDF preview via tachyon-tex watch
---

Load skill `tachyon-tex` with the OpenCode `skill` tool.

User request: $ARGUMENTS

Instructions:
1. skill(name="tachyon-tex").
2. Start: `npx --yes github:srsergi0/tachyon-tex-cli background <project> --main main.tex --open --json`.
3. Poll `status <project> --json` until `ready`/`error`, then `logs <project>` on error.
4. Return the `http://127.0.0.1:...` URL. Leave session running if user asked; else `stop <project>` when done.
