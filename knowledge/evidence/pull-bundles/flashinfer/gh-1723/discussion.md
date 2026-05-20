# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1723](https://github.com/flashinfer-ai/flashinfer/pull/1723)
- Source page: `sources/prs/flashinfer/PR-1723.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1723`
- Generated at: `2026-05-20T15:23:19.818972+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-19T02:25:02Z`
- Merged: `2025-09-19T04:59:14Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: GordonGustafson, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-09-19T02:26:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a change to dynamically set MaxNumTopGroups based on model characteristics, addressing a ... (https://github.com/flashinfer-ai/flashinfer/pull/1723#pullrequestreview-3242592190)
- `2025-09-19T03:40:18Z` `APPROVED` by `zhyncs` (https://github.com/flashinfer-ai/flashinfer/pull/1723#pullrequestreview-3242759965)
- `2025-09-19T04:05:35Z` `COMMENTED` by `yzh119` - In our tests DeepSeek-V3 model quality was severely degraded when using MaxNumTopGroups = 16 MaxNumTopGroups will determine register ... (https://github.com/flashinfer-ai/flashinfer/pull/1723#pullrequestreview-3242797553)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_routing_deepseek.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-19T04:05:35Z` `review` `COMMENTED` by `yzh119`; signals: perf, performance, register; excerpt: "In our tests DeepSeek-V3 model quality was severely degraded when using MaxNumTopGroups = 16 MaxNumTopGroups will determine register usage thus influencing performance. Currently the ..." (https://github.com/flashinfer-ai/flashinfer/pull/1723#pullrequestreview-3242797553)
- `2025-09-19T04:16:37Z` `issue` by `GordonGustafson`; signals: general review; excerpt: "@yzh119 We have this check: Kimi's number of experts is 384, so MaxNumTopGroups for Kimi needs to be at least 12 (32 12 = ..." (https://github.com/flashinfer-ai/flashinfer/pull/1723#issuecomment-3310470666)
