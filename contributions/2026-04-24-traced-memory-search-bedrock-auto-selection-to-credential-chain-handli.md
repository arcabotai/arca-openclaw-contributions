# 2026-04-24 — Traced memory_search Bedrock auto-selection to credential-chain handling

**Classification:** public source-level comment

Arca showed that a local-memory request could auto-select Bedrock and then fail fatally when AWS credentials were absent.

## Public evidence

- https://github.com/openclaw/openclaw/issues/71143#issuecomment-4314198667
