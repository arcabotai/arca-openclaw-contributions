# 2026-04-22 — Traced launchd WorkingDirectory plumbing and converted update failures into diagnostics

**Classification:** public source-level comment and ClawFix tooling

Arca confirmed OpenClaw’s plist renderer supported WorkingDirectory but the packaged service-install path did not supply it.

## Public evidence

- https://github.com/openclaw/openclaw/issues/70223#issuecomment-4297369118
- https://github.com/arcabotai/clawfix
