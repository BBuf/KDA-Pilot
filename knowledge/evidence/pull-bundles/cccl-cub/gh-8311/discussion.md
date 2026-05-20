# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8311](https://github.com/NVIDIA/cccl/pull/8311)
- Source page: `sources/prs/cccl-cub/PR-8311.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8311`
- Generated at: `2026-05-20T15:20:39.741133+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-07T15:29:57Z`
- Merged: `2026-04-09T11:47:41Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 14
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-09T07:28:40Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080284784)
- `2026-04-09T07:37:18Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080518371)
- `2026-04-09T07:40:56Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080545887)
- `2026-04-09T07:41:44Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080551018)
- `2026-04-09T07:42:19Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080554223)
- `2026-04-09T07:43:35Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080562316)
- `2026-04-09T08:26:48Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4080816202)
- `2026-04-09T11:13:46Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8311#pullrequestreview-4081794987)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`: 10 inline comment(s)
- `cub/cub/device/dispatch/dispatch_select_if.cuh`: 4 inline comment(s)

## High-Signal Discussion

- `2026-04-09T07:26:07Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_select_if.cuh`:902; signals: perf; excerpt: "Question: What is the purpose of this alias, it feels like OffsetT is perfectly fine" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056155195)
- `2026-04-09T07:42:18Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_select_if.cuh`:901; signals: cuda; excerpt: "It's ::cuda::std::int32 t." (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056235753)
- `2026-04-09T07:20:15Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:1670; signals: general review; excerpt: "Suggestion: the flags are really error prone because it is easy to miss whether there is a ! or not. We should consider introducing ..." (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056126814)
- `2026-04-09T07:21:36Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:2101; signals: general review; excerpt: "What is the meaning of no tuning, will we then fall back into the one from the previous architecture?" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056133382)
- `2026-04-09T07:37:18Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:1706; signals: general review; excerpt: "It shouldn't. The conditions are: so basically all combinations. We would really need pattern matching here :)" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056208422)
- `2026-04-09T07:00:46Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:28; signals: general review; excerpt: "probably unused" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056012770)
- `2026-04-09T07:15:47Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:1661; signals: general review; excerpt: "Nitpick: above this is named" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056104465)
- `2026-04-09T07:17:17Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:1706; signals: general review; excerpt: "Question: This is the same as the above condition, is that intentional?" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056113186)
- `2026-04-09T07:25:06Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_select_if.cuh`:901; signals: general review; excerpt: "Question is this an signed integer?" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056149863)
- `2026-04-09T07:40:56Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:1670; signals: general review; excerpt: "How about not?" (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056229011)
- `2026-04-09T07:41:43Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_select_if.cuh`:2101; signals: general review; excerpt: "Yes, added a comment." (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056232936)
- `2026-04-09T07:43:35Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_select_if.cuh`:902; signals: general review; excerpt: "There is none, I just retained it from the old dispatcher. Refactored it out." (https://github.com/NVIDIA/cccl/pull/8311#discussion_r3056242114)
