# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1573](https://github.com/flashinfer-ai/flashinfer/pull/1573)
- Source page: `sources/prs/flashinfer/PR-1573.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1573`
- Generated at: `2026-05-20T15:22:59.729008+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-25T22:15:55Z`
- Merged: `2025-08-27T07:48:06Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: IwakuraRein, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-26T16:14:06Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1573#pullrequestreview-3156385055)
- `2025-08-26T16:54:49Z` `COMMENTED` by `IwakuraRein` (https://github.com/flashinfer-ai/flashinfer/pull/1573#pullrequestreview-3156530073)
- `2025-08-27T06:32:52Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1573#pullrequestreview-3158490972)

## Inline Comment Hotspots

- `flashinfer/fused_moe/core.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-26T16:12:00Z` `inline` by `yzh119` `flashinfer/fused_moe/core.py`:1145; signals: flashinfer, memory, moe; excerpt: "remove .to(torch.bfloat16) which causes illegal memory access when using deepseek v3 routing. could you explain why?" (https://github.com/flashinfer-ai/flashinfer/pull/1573#discussion_r2301491179)
- `2025-08-26T16:54:49Z` `inline` by `IwakuraRein` `flashinfer/fused_moe/core.py`:1145; signals: flashinfer, moe; excerpt: "@yzh119 Currently DeepSeek V3 requires fp32 routing logits:" (https://github.com/flashinfer-ai/flashinfer/pull/1573#discussion_r2301592209)
