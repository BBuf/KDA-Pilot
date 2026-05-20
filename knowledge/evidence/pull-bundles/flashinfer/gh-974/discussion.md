# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#974](https://github.com/flashinfer-ai/flashinfer/pull/974)
- Source page: `sources/prs/flashinfer/PR-974.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-974`
- Generated at: `2026-05-20T15:26:50.220766+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-26T16:54:08Z`
- Merged: `2025-03-27T09:04:55Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-26T20:05:01Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/974#pullrequestreview-2718118835)
- `2025-03-26T23:39:05Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/974#pullrequestreview-2718848910)
- `2025-03-27T09:04:49Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/974#pullrequestreview-2720414210)

## Inline Comment Hotspots

- `include/flashinfer/sampling.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2025-03-26T17:40:29Z` `inline` by `yzh119` `include/flashinfer/sampling.cuh`:1343; signals: block, flashinfer; excerpt: "Please do not hardcode the BLOCK THREADS here because sm75 (T4 GPUs) do not support 1024, use DISPATCH COMPUTE CAP NUM THREADS instead." (https://github.com/flashinfer-ai/flashinfer/pull/974#discussion_r2014697357)
- `2025-03-26T23:38:52Z` `inline` by `yzh119` `include/flashinfer/sampling.cuh`:948; signals: block, flashinfer; excerpt: "You don't have to name this struct, just leave it as: and you can access them by temp storage.block aggregate.value0, temp storage.block aggregate.value1. Or ..." (https://github.com/flashinfer-ai/flashinfer/pull/974#discussion_r2015134330)
- `2025-03-26T17:40:33Z` `inline` by `yzh119` `include/flashinfer/sampling.cuh`:1364; signals: flashinfer; excerpt: "ditto." (https://github.com/flashinfer-ai/flashinfer/pull/974#discussion_r2014697537)
- `2025-03-26T23:38:57Z` `inline` by `yzh119` `include/flashinfer/sampling.cuh`:951; signals: flashinfer; excerpt: "ditto." (https://github.com/flashinfer-ai/flashinfer/pull/974#discussion_r2015134383)
- `2025-03-26T23:39:02Z` `inline` by `yzh119` `include/flashinfer/sampling.cuh`:954; signals: flashinfer; excerpt: "ditto." (https://github.com/flashinfer-ai/flashinfer/pull/974#discussion_r2015134424)
