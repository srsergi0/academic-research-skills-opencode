# OpenCode control map

Port of upstream `docs/CONTROL_AVAILABILITY.md` for OpenCode channel.

| Mechanism | OpenCode port status |
|---|---|
| Methodology layer (5 SKILL.md protocols) | Active, vendored in `.opencode/skills/` |
| Skill auto-routing | Conditional, via `skill` tool + descriptions |
| Cross-skill routing discipline | Prompt-level, in each SKILL.md |
| `/ars-*` commands | Active, in `.opencode/commands/` with `$ARGUMENTS` |
| SessionStart announce / auto-update | Absent |
| Write-scope guard hook | Absent (prompt-level only) |
| Plugin agents allowlist | Absent |
| Subagent orchestration | Conditional, manual via OpenCode subagents |
| Python verification cache / resolvers | Absent unless full upstream checkout present |
| Cross-model verification `ARS_CROSS_MODEL` | Absent in this port (needs API keys + upstream scripts) |
| Prompt checkpoints + integrity gates 2.5/4.5 | Active as instructions, human enforces |
| sr-screener dual blinded review | Conditional, run two subagents + adjudicate manually |
| Claim-audit `ARS_CLAIM_AUDIT=1` | Documented, not wired to formatter hard gate |

Upstream version: v3.23.1. No accuracy claim beyond upstream docs. See upstream `docs/RISK_REGISTER.md` and `docs/DATA_FLOWS.md` for risks.
