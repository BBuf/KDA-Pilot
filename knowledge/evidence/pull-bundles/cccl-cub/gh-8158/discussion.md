# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8158](https://github.com/NVIDIA/cccl/pull/8158)
- Source page: `sources/prs/cccl-cub/PR-8158.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8158`
- Generated at: `2026-05-20T15:20:30.188452+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T17:03:39Z`
- Merged: `2026-04-09T16:21:14Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-09T09:10:19Z` `APPROVED` by `miscco` - I shudder from the complexity of all that tuning (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4081015037)
- `2026-04-09T10:00:52Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4081382730)
- `2026-04-09T10:01:58Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4081388955)
- `2026-04-09T10:02:47Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4081393038)
- `2026-04-09T10:30:12Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4081542215)
- `2026-04-09T16:20:01Z` `APPROVED` by `NaderAlAwar` - C and benchmark parts look good (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4083820662)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_scan.cuh`: 3 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-09T10:01:58Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:115; signals: kernel, regression, warp; excerpt: "This fixed the SASS regression. The tuning policy was computed at runtime . We should be careful in the future to always put a ..." (https://github.com/NVIDIA/cccl/pull/8158#discussion_r3056985651)
- `2026-04-09T09:02:48Z` `issue` by `bernhardmgruber`; signals: sm100, sm120; excerpt: "I see SASS diffs for SM100 and SM120. Almost exclusively in the setup code around the SMEM allocator. More instructions are generated." (https://github.com/NVIDIA/cccl/pull/8158#issuecomment-4212935181)
- `2026-04-09T10:00:52Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_scan.cuh`:196; signals: kernel; excerpt: "The DeviceScanKernel entry point is also used for the old scan implementation, so yes, we still need that." (https://github.com/NVIDIA/cccl/pull/8158#discussion_r3056979698)
- `2026-04-09T09:02:09Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_scan.cuh`:196; signals: kernel; excerpt: "Are we sure this is still needed, I thought that CCCL GRID CONSTANT is only used above 12.8" (https://github.com/NVIDIA/cccl/pull/8158#discussion_r3056654653)
- `2026-04-09T10:02:47Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_scan.cuh`:196; signals: kernel; excerpt: "Oh I meant whether we need the conditional compilation" (https://github.com/NVIDIA/cccl/pull/8158#discussion_r3056989631)
- `2026-04-09T13:05:01Z` `issue` by `bernhardmgruber`; signals: warp; excerpt: "Found it. I selected the warpspeed tuning even on older architectures, which led to a division by zero in the host code. Fixed." (https://github.com/NVIDIA/cccl/pull/8158#issuecomment-4214435651)
- `2026-04-09T16:20:01Z` `review` `APPROVED` by `NaderAlAwar`; signals: benchmark; excerpt: "C and benchmark parts look good" (https://github.com/NVIDIA/cccl/pull/8158#pullrequestreview-4083820662)
