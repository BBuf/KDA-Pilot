# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6202](https://github.com/NVIDIA/cccl/pull/6202)
- Source page: `sources/prs/cccl-cub/PR-6202.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6202`
- Generated at: `2026-05-20T15:19:54.985929+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-13T13:11:08Z`
- Merged: `2025-10-14T04:23:35Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=3, changes_requested=1, commented=1)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bernhardmgruber, elstehle, fbusato, miscco, wmaxey
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-13T13:19:20Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6202#pullrequestreview-3331612340)
- `2025-10-13T13:21:03Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/6202#pullrequestreview-3331618232)
- `2025-10-13T16:58:34Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6202#pullrequestreview-3332338068)
- `2025-10-13T17:16:21Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6202#pullrequestreview-3332432796)
- `2025-10-13T21:24:41Z` `APPROVED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6202#pullrequestreview-3333074592)

## Inline Comment Hotspots

- `cub/cub/block/block_radix_rank.cuh`: 2 inline comment(s)
- `thrust/thrust/detail/integer_math.h`: 1 inline comment(s)
- `cub/cub/warp/specializations/warp_scan_shfl.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-13T14:04:29Z` `issue` by `bernhardmgruber`; signals: hang, perf, performance; excerpt: "6099, the source of this backport, omitted a performance analysis of the change. Let's wait with merging this until we know that it does ..." (https://github.com/NVIDIA/cccl/pull/6202#issuecomment-3397677840)
- `2025-10-13T17:16:10Z` `inline` by `miscco` `cub/cub/block/block_radix_rank.cuh`:55; signals: block, cuda; excerpt: "We use cuda::std:: If AFAIK" (https://github.com/NVIDIA/cccl/pull/6202#discussion_r2426904449)
- `2025-10-13T16:56:04Z` `inline` by `fbusato` `cub/cub/warp/specializations/warp_scan_shfl.cuh`:53; signals: warp; excerpt: "these two headers are never used if I'm not wrong" (https://github.com/NVIDIA/cccl/pull/6202#discussion_r2426862011)
- `2025-10-13T16:58:05Z` `inline` by `fbusato` `cub/cub/block/block_radix_rank.cuh`:55; signals: block; excerpt: "looks unused" (https://github.com/NVIDIA/cccl/pull/6202#discussion_r2426867111)
- `2025-10-13T20:59:30Z` `issue` by `wmaxey`; signals: hang; excerpt: "We shouldn't be addressing review comments in the backport unless there are material conflicts with the old branch. We should fix these issues in ..." (https://github.com/NVIDIA/cccl/pull/6202#issuecomment-3399057196)
- `2025-10-13T16:52:58Z` `inline` by `fbusato` `thrust/thrust/detail/integer_math.h`:88; signals: general review; excerpt: "thrust::detail::log2 will be deleted in" (https://github.com/NVIDIA/cccl/pull/6202#discussion_r2426854027)
