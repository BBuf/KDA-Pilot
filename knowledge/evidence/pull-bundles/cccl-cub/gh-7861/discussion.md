# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7861](https://github.com/NVIDIA/cccl/pull/7861)
- Source page: `sources/prs/cccl-cub/PR-7861.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7861`
- Generated at: `2026-05-20T15:20:20.227594+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-03T12:00:51Z`
- Merged: `2026-03-12T15:02:38Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T10:21:57Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7861#pullrequestreview-3935439984)
- `2026-03-12T10:27:06Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7861#pullrequestreview-3935474414)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_scan.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-12T10:15:51Z` `issue` by `bernhardmgruber`; signals: hang, regression, warp; excerpt: "Do I see Right. This is a regression we already accepted in 6811. The original PR was just not looking at cub.bench.scan.exclusive.custom.base, only at ..." (https://github.com/NVIDIA/cccl/pull/7861#issuecomment-4045537690)
- `2026-03-12T10:27:06Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:665; signals: warp; excerpt: "auto ipt = Policy1000::WarpspeedPolicy::items per thread; is defined as so if sizeof(InputValueT) is larger than 8, we would get values smaller than 127, which ..." (https://github.com/NVIDIA/cccl/pull/7861#discussion_r2923654509)
- `2026-03-12T10:21:50Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:665; signals: general review; excerpt: "Should this just be I assume we do not want to have more items per thread of they are even larger" (https://github.com/NVIDIA/cccl/pull/7861#discussion_r2923625941)
