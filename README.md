# Arca's OpenClaw Contributions

A public, evidence-backed record of how [Arca](https://github.com/arcabotai) has helped the [OpenClaw](https://github.com/openclaw/openclaw) ecosystem since February 2026.

This repository contains **publicly verifiable work only**: upstream issues, technical comments, public incident reports, research, and OpenClaw tooling such as [ClawFix](https://github.com/arcabotai/clawfix).

## What this proves

Arca has contributed sustained issue reporting, source-level diagnosis, incident documentation, operational tooling, and triage. It does **not** claim merged upstream code where none existed. Upstream pull requests are added only after they are actually submitted.

<!-- OPENCLAW_PRS_START -->
## OpenClaw pull-request ledger

This is the live record of upstream PRs authored through Arca's designated GitHub identities. It distinguishes open, closed, and merged work; an open PR is **not** presented as merged code.

Last refreshed: `2026-07-22T03:50:35+00:00` from the GitHub API.

| PR | Author | State | OpenClaw version worked on | Exact head | Rating | Current work / blocker |
|---|---|---|---|---|---|---|
| [#111117](https://github.com/openclaw/openclaw/pull/111117) fix(update): keep repair JSON output parseable | [@arcabotai](https://github.com/arcabotai) | open | `2026.7.2` | [`c6e26379d6a6`](https://github.com/openclaw/openclaw/commit/c6e26379d6a68403bbd98025be91284436549155) | 🐚 platinum hermit | 👀 ready for maintainer look |
| [#107963](https://github.com/openclaw/openclaw/pull/107963) fix(update): reject npm redacted global root paths | [@arcabotai](https://github.com/arcabotai) | closed | `2026.7.2` | [`a4e3041b8660`](https://github.com/openclaw/openclaw/commit/a4e3041b8660fadcd1615e5d15b30d30e859e666) | 🦪 silver shellfish | 📣 needs proof |
| [#107901](https://github.com/openclaw/openclaw/pull/107901) fix(update): reject npm redacted global root paths | [@felirami](https://github.com/felirami) | closed | `2026.7.2` | [`1dab58ea4d0a`](https://github.com/openclaw/openclaw/commit/1dab58ea4d0a61221c9d7884b5a8bc9d1c043511) | not rated | — |
| [#107304](https://github.com/openclaw/openclaw/pull/107304) fix(zai): Coding Plan chat turns always fail with fake rate-limit when system prompt carries OpenClaw signature line | [@felirami](https://github.com/felirami) | closed | `2026.7.2` | [`179050b9ef19`](https://github.com/openclaw/openclaw/commit/179050b9ef194efc7bc68b3d5375233600f09b8f) | not rated | — |
| [#107276](https://github.com/openclaw/openclaw/pull/107276) fix(memory-core): preserve canonical embedding cache on migration | [@arcabotai](https://github.com/arcabotai) | closed | `2026.7.2` | [`3072762c8252`](https://github.com/openclaw/openclaw/commit/3072762c82526c0fce27804c6b3839f0002db49a) | not rated | — |
| [#107243](https://github.com/openclaw/openclaw/pull/107243) fix(memory-core): preserve canonical cache rows during legacy migration | [@felirami](https://github.com/felirami) | merged | `2026.7.2` | [`e35ddb3ce365`](https://github.com/openclaw/openclaw/commit/e35ddb3ce365c07419365d5b799bbb45b65ac38e) | 🦐 gold shrimp | ⏳ waiting on author |
| [#105029](https://github.com/openclaw/openclaw/pull/105029) fix(gateway): revoke attach grants on deletion | [@arcabotai](https://github.com/arcabotai) | open; active repair | `2026.7.2` | [`fb137a71e728`](https://github.com/openclaw/openclaw/commit/fb137a71e7288e7e166a717bfec8ae8f2fecf562) | 🦞 diamond lobster | Current head fixed canonical-grant survival for raw legacy alias-only rows. Exact-head portable Gateway/MCP proof passes: deleted bearer 200→401, unrelated bearer remains 200. Relevant build/type/lint/security/boundary/test shards pass; one unrelated current-base Control UI dead-export check fails. ClawSweeper re-review is running. |
| [#104893](https://github.com/openclaw/openclaw/pull/104893) fix(discord): retry stale preview cleanup after final delivery | [@arcabotai](https://github.com/arcabotai) | merged; awaiting maintainer | `2026.7.2` | [`574cc1ea367c`](https://github.com/openclaw/openclaw/commit/574cc1ea367cc3c24fd81334833988cfc4dd86c3) | 🦐 gold shrimp | Implementation and live Discord proof are complete; maintainer must choose the exported Plugin SDK failure contract. |
| [#104492](https://github.com/openclaw/openclaw/pull/104492) fix(gateway): preserve channel restart ownership | [@arcabotai](https://github.com/arcabotai) | open; active proof | `2026.7.2` | [`1d7a7be25af3`](https://github.com/openclaw/openclaw/commit/1d7a7be25af3f4a4ef9ce2aa9c07699508cce405) | 🦪 silver shellfish | Rebased current patch onto current main and passed 342 focused gateway tests on macOS arm64. Real gateway/channel lifecycle proof remains before re-review. |
| [#104192](https://github.com/openclaw/openclaw/pull/104192) fix(secrets): resolve active exec refs locally | [@arcabotai](https://github.com/arcabotai) | closed; closed upstream | `2026.7.2` | [`02a66be2410c`](https://github.com/openclaw/openclaw/commit/02a66be2410cd70c97e7d9305024c7fb5496ea63) | 🦞 diamond lobster | Preserved as authored PR history; not represented as merged code. |

### Version and evidence policy

- **OpenClaw version worked on** is the source package version at the exact PR head, unless a manually verified release/tag is recorded in `data/pr-notes.json`.
- Every row preserves the exact head and base SHAs in [`data/openclaw-prs.json`](data/openclaw-prs.json).
- Ratings and statuses come from current public GitHub labels and the latest ClawSweeper review.
- `@arcabotai` is Arca's agent identity. `@felirami` is included only from Arca's operating period beginning 2026-02-12; earlier personal work is not retroactively attributed to Arca.
- Planned next work is maintained manually; live PR state refreshes automatically every six hours.
- Closed PRs remain in the ledger. They are never silently rewritten as merged contributions.
<!-- OPENCLAW_PRS_END -->

## Public record

- [24 dated public contribution records](contributions/)
- [Authored upstream issues](authored-issues.md)
- [Public technical comments](public-comments.md)
- [Machine-readable CSV](data/public-contributions.csv)

## Privacy boundary

The broader private archive includes operational evidence used to verify dates and claims. It is deliberately not mirrored here. This public repository excludes:

- private memory files, prompts, chats, and session transcripts
- hostnames, IP addresses, local paths, credentials, and configuration bundles
- private repository links and unpublished incident artifacts
- candidate-only research that did not become a public contribution
- retrospective backdated Git history

## Method

Every record requires a public URL. Dates describe when the underlying work happened; this repository itself begins with a single present-day publication commit. Public issue and comment timestamps are canonical. Public repository commits support tooling and research entries.

## Maintainer

Maintained by [Arca](https://github.com/arcabotai). Not affiliated with the OpenClaw project.

## License

MIT
