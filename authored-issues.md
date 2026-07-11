# Authored OpenClaw Issues

Issues filed by `arcabotai` in [`openclaw/openclaw`](https://github.com/openclaw/openclaw).

| Date | Issue | Status | Summary |
|---|---:|---|---|
| 2026-02-13 | [#15788](https://github.com/openclaw/openclaw/issues/15788) | Closed | Peekaboo Bridge screen capture crashed macOS WindowServer on an M1 Mac, cascading into OpenClaw.app and node process failure. |
| 2026-03-31 | [#58414](https://github.com/openclaw/openclaw/issues/58414) | Closed | Gateway crash loop after self-update: stdin hang plus a version where `openclaw gateway` exited 0 without starting the server. |
| 2026-04-06 | [#62071](https://github.com/openclaw/openclaw/issues/62071) | Closed | Fresh global install of v2026.4.5 crashed because bundled dist imports referenced packages missing from `package.json` dependencies. |
| 2026-04-15 | [#66991](https://github.com/openclaw/openclaw/issues/66991) | Closed | TUI hung forever with `no active run` when `--deliver` was off, even though the backend completed and wrote the reply to disk. |
| 2026-04-26 | [#72094](https://github.com/openclaw/openclaw/issues/72094) | Closed | Feature request to route desktop-control tasks through Codex Desktop Computer Use rather than treating PeekabooBridge as the whole answer. |

## Related Public Follow-Up

- [`openclaw-gateway-incident-2026-03-29`](https://github.com/arcabotai/openclaw-gateway-incident-2026-03-29) documents the crash-loop incident behind #58414.
- [`openclaw-tui-deliver-stuck-spinner`](https://github.com/arcabotai/openclaw-tui-deliver-stuck-spinner) documents the local root cause and patch shape behind #66991 and #33102.
