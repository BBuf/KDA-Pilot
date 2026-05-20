# PR Discussion Digest

- Source PR: [NVIDIA/cccl#3691](https://github.com/NVIDIA/cccl/pull/3691)
- Source page: `sources/prs/cccl-cub/PR-3691.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-3691`
- Generated at: `2026-05-20T15:19:37.487591+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-05T11:17:10Z`
- Merged: `2025-02-06T21:56:39Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 2 (approved=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bernhardmgruber, elstehle, gonidelis, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-02-05T11:25:04Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3691#pullrequestreview-2595389775)
- `2025-02-06T15:30:42Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/3691#pullrequestreview-2599033148)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-02-06T09:07:38Z` `issue` by `bernhardmgruber`; signals: benchmark, hang; excerpt: "preliminary histogram.range results. I don't like that only I8,I32 workloads are getting picked. Why are not the other tunings manifesting? Investigating... From the benchmark ..." (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2639222798)
- `2025-02-06T09:04:30Z` `issue` by `bernhardmgruber`; signals: regression; excerpt: "histogram.even (tbh I consider it great and exactly what we expected. The sole provided tuning does great for 2^28 problem sizes). We should maybe ..." (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2639215810)
- `2025-02-05T13:58:13Z` `issue` by `bernhardmgruber`; signals: perf; excerpt: "Please don't merge until we have a perf diff from @gonidelis" (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2636927336)
- `2025-02-06T11:00:01Z` `issue` by `bernhardmgruber`; signals: benchmark; excerpt: "@gonidelis please provide multi histogram benchmarks as well. Thx!" (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2639496968)
- `2025-02-06T01:27:17Z` `issue` by `gonidelis`; signals: general review; excerpt: "histogram.even (tbh I consider it great and exactly what we expected. The sole provided tuning does great for 2^28 problem sizes). We should maybe ..." (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2638396966)
- `2025-02-06T01:37:55Z` `issue` by `gonidelis`; signals: general review; excerpt: "preliminary histogram.range results. I don't like that only I8,I32 workloads are getting picked. Why are not the other tunings manifesting? Investigating..." (https://github.com/NVIDIA/cccl/pull/3691#issuecomment-2638431311)
