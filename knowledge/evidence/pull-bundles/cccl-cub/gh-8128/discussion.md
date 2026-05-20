# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8128](https://github.com/NVIDIA/cccl/pull/8128)
- Source page: `sources/prs/cccl-cub/PR-8128.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8128`
- Generated at: `2026-05-20T15:20:30.184590+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T23:56:58Z`
- Merged: `2026-03-24T14:14:56Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 9 (approved=3, commented=6)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-03-20T23:59:32Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3984647898)
- `2026-03-24T10:01:15Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3997789757)
- `2026-03-24T11:02:39Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3998218200)
- `2026-03-24T11:03:59Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3998225931)
- `2026-03-24T11:05:50Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3998237040)
- `2026-03-24T12:33:14Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3998783061)
- `2026-03-24T14:14:53Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8128#pullrequestreview-3999562258)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/dispatch_merge_sort.cuh`: 9 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_merge_sort.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-20T23:59:33Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:106; signals: hang; excerpt: "We could consider this a breaking change, but this parameter was never intended to be customized by the user. It was only intended for ..." (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2968454841)
- `2026-03-24T14:13:50Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:485; signals: general review; excerpt: "Important: I think that this should be at least 1. I know existing behavior sets it to 0, but in general, even when we ..." (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2981904503)
- `2026-03-24T09:55:47Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_merge_sort.cuh`:24; signals: general review; excerpt: "Is that really needed?" (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980347907)
- `2026-03-24T09:59:40Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:212; signals: general review; excerpt: "Could that be constexpr or is that restricted due to CCCL.C" (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980370596)
- `2026-03-24T10:00:27Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:245; signals: general review; excerpt: "Could we pull that out into a variable?" (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980375120)
- `2026-03-24T11:02:39Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:212; signals: general review; excerpt: "It can I think." (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980729327)
- `2026-03-24T11:03:59Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_merge_sort.cuh`:24; signals: general review; excerpt: "We don't need I think, since CCCL HAS CONCEPTS() should be available regardless" (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980735922)
- `2026-03-24T11:05:50Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_merge_sort.cuh`:245; signals: general review; excerpt: "Refactored." (https://github.com/NVIDIA/cccl/pull/8128#discussion_r2980745443)
