# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6069](https://github.com/NVIDIA/cccl/pull/6069)
- Source page: `sources/prs/cccl-cub/PR-6069.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6069`
- Generated at: `2026-05-20T15:19:53.092528+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T00:17:56Z`
- Merged: `2025-10-01T14:40:28Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 11
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-30T06:16:41Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3282753098)
- `2025-09-30T06:18:07Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3282766250)
- `2025-09-30T14:35:41Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3285310549)
- `2025-09-30T15:52:06Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3285699965)
- `2025-09-30T19:54:31Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3286503911)
- `2025-09-30T20:51:00Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3286676947)
- `2025-09-30T21:21:23Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3286750898)
- `2025-09-30T22:37:48Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3286920790)
- `2025-09-30T22:53:52Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3286952695)
- `2025-10-01T14:14:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3289427355)
- `2025-10-01T14:26:18Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6069#pullrequestreview-3289502630)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`: 11 inline comment(s)

## High-Signal Discussion

- `2025-09-30T21:28:20Z` `issue` by `bernhardmgruber`; signals: benchmark, hang, kernel, perf, performance, sm90; excerpt: "There are SASS differences for cub.bench.segmented sort.keys.base on sm89 and sm90 but performance is the same What kind of SASS differences do you observe? ..." (https://github.com/NVIDIA/cccl/pull/6069#issuecomment-3353865782)
- `2025-10-01T00:14:34Z` `issue` by `NaderAlAwar`; signals: benchmark, hang, kernel, perf, performance, sm90; excerpt: "There are SASS differences for cub.bench.segmented sort.keys.base on sm89 and sm90 but performance is the same What kind of SASS differences do you observe? ..." (https://github.com/NVIDIA/cccl/pull/6069#issuecomment-3354198711)
- `2025-10-01T14:21:38Z` `issue` by `bernhardmgruber`; signals: benchmark, hang, kernel, perf, performance, regression; excerpt: "@bernhardmgruber On further inspection there are no actual SASS differences. What I observed was that following my changes there were fewer kernels instantiated That ..." (https://github.com/NVIDIA/cccl/pull/6069#issuecomment-3356592016)
- `2025-09-30T15:30:43Z` `issue` by `NaderAlAwar`; signals: perf, performance, sm90; excerpt: "There are SASS differences for cub.bench.segmented sort.keys.base on sm89 and sm90 but performance is the same" (https://github.com/NVIDIA/cccl/pull/6069#issuecomment-3352759727)
- `2025-09-30T19:54:31Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:768; signals: compile, hang; excerpt: "@bernhardmgruber Before 4428 segmented reduce code used advance iterators if supported. This would call operator+ if iterator type implemented it on the host. Otherwise ..." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2392679994)
- `2025-10-01T00:15:54Z` `issue` by `NaderAlAwar`; signals: perf, performance; excerpt: "These are the performance numbers on sm89. There are a few that are slower but I think it is just noise. After rerunning those ..." (https://github.com/NVIDIA/cccl/pull/6069#issuecomment-3354203205)
- `2025-09-30T14:35:40Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:768; signals: kernel; excerpt: "I spent some time looking into this and I believe that iterators must support +=. From the c.parallel side, inside operator()+=, we throw an ..." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2391814564)
- `2025-09-30T20:51:00Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:768; signals: compile; excerpt: "Conceptually, iterators are supposed to behave like pointers, so they can be cheaply copied, moved, default constructed, etc. and it += n and it ..." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2392805042)
- `2025-09-30T21:20:35Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:204; signals: kernel; excerpt: "Question: Why do we need to pass a wrapped policy to a kernel? This is new. So far kernels always retained their ChainedPolicy parameter." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2392860040)
- `2025-09-30T22:53:51Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:204; signals: kernel; excerpt: "This is a special kernel used only to launch the segmented sort kernels when CDP is enabled. It is meant to be called with ..." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2393008396)
- `2025-10-01T14:14:12Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:768; signals: block; excerpt: "Yes. Let's not block the work here." (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2394769259)
- `2025-09-30T15:52:05Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_sort.cuh`:768; signals: general review; excerpt: "This was introduced in 4428. We have indirect iterator t in the meantime supporting operator+=. I think PR 4428 should be reverted. @oleksandr-pavlyk ?" (https://github.com/NVIDIA/cccl/pull/6069#discussion_r2392101327)
