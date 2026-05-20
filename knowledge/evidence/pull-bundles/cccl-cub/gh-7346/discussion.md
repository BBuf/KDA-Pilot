# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7346](https://github.com/NVIDIA/cccl/pull/7346)
- Source page: `sources/prs/cccl-cub/PR-7346.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7346`
- Generated at: `2026-05-20T15:20:10.002502+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-25T23:52:46Z`
- Merged: `2026-02-25T16:44:49Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 12 (approved=3, commented=9)
- Inline review comments: 22
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=7, outdated=3
- Human participants with discussion text: bernhardmgruber, davebayer, fbusato, miscco, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-03T22:14:56Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3747870059)
- `2026-02-03T22:18:45Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3747880763)
- `2026-02-03T22:45:10Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3747991683)
- `2026-02-04T13:25:18Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3751059871)
- `2026-02-13T17:06:58Z` `APPROVED` by `fbusato` - a few minor comments. Looks good. It's a bit hard to review because some files have been moved ... (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3798333647)
- `2026-02-21T22:26:10Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3836143992)
- `2026-02-21T22:27:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3836144450)
- `2026-02-21T23:19:14Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3836145683)
- `2026-02-21T23:28:17Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3836205982)
- `2026-02-25T15:51:57Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3855145940)
- `2026-02-25T16:31:29Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3855390766)
- `2026-02-25T16:42:45Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/7346#pullrequestreview-3855453777)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_reduce_deterministic.cuh`: 10 inline comment(s)
- `cub/benchmarks/bench/reduce/deterministic.cu`: 7 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_reduce_deterministic.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2026-02-21T22:26:10Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/deterministic.cu`:17; signals: benchmark, compile, kernel; excerpt: "It's only used in host code at runtime (by the CUB dispatch) and by the kernel at compile-time. However, adding CCCL API does not ..." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2836742617)
- `2026-02-21T22:29:01Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_reduce_deterministic.cuh`:78; signals: hang, kernel; excerpt: "I did not change any code in this file, just moved it from kernel reduce.cuh. So I don't know. I guess it's fine." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2836744872)
- `2026-02-25T16:31:29Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_reduce_deterministic.cuh`:92; signals: hang, tile; excerpt: "Currently yes, but we could change this. It comes from the old policy hub, where we had using SingleTilePolicy = ReducePolicy; everywhere." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2854082103)
- `2026-02-03T22:14:56Z` `inline` by `oleksandr-pavlyk` `cub/benchmarks/bench/reduce/deterministic.cu`:20; signals: benchmark; excerpt: "Perhaps use struct field names to indicate which list applies to what sub-policy. If values start to differ, it would make it easier on ..." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2761223850)
- `2026-02-03T22:18:45Z` `inline` by `oleksandr-pavlyk` `cub/benchmarks/bench/reduce/deterministic.cu`:53; signals: benchmark; excerpt: "Perhaps is preprocessor to define auto rfa dispatch differently based on TUNE BASE and use that throughout to reduce branching? ` Then similarly for ..." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2761233261)
- `2026-02-04T13:25:18Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/deterministic.cu`:53; signals: benchmark; excerpt: "That's an interesting suggestion, but if I take the address of the template instantiation of dispatch when I need to later provide all function ..." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2764012844)
- `2026-02-21T22:27:12Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_reduce_deterministic.cuh`:1; signals: kernel; excerpt: "I did not add any new original content to this file, so the old copyright year should still apply to what is present in ..." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2836743306)
- `2026-02-21T23:18:22Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_reduce_deterministic.cuh`:134; signals: kernel; excerpt: "Because ReproducibleFloatingAccumulator does not implement operator+. We could add it, but I don't want to mess with the kernel." (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2836798906)
- `2026-02-03T22:45:09Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/deterministic.cu`:20; signals: benchmark; excerpt: "Sadly, this requires C++20 and I was told we won't upgrade the benchmarks yet :S" (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2761329492)
- `2026-02-13T16:49:25Z` `inline` by `fbusato` `cub/benchmarks/bench/reduce/deterministic.cu`:17; signals: benchmark; excerpt: "question for my knowledge. Why this function is not marked with CCCL ?" (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2805146254)
- `2026-02-13T16:50:26Z` `inline` by `fbusato` `cub/benchmarks/bench/reduce/deterministic.cu`:49; signals: benchmark; excerpt: "I prefer nullptr because it is a pointer" (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2805150940)
- `2026-02-13T16:53:21Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/kernel_reduce_deterministic.cuh`:78; signals: kernel; excerpt: "do we need to handle large input?" (https://github.com/NVIDIA/cccl/pull/7346#discussion_r2805162689)
