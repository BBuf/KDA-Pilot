# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6362](https://github.com/NVIDIA/cccl/pull/6362)
- Source page: `sources/prs/cccl-cub/PR-6362.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6362`
- Generated at: `2026-05-20T15:19:57.089323+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-28T13:57:14Z`
- Merged: `2025-11-03T12:02:48Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: bernhardmgruber, elstehle, fbusato, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-28T14:35:07Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3389128153)
- `2025-10-30T19:02:50Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401205322)
- `2025-10-30T19:04:30Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401210212)
- `2025-10-30T21:12:03Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401672904)
- `2025-10-30T21:16:51Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401694253)
- `2025-10-30T21:20:37Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401707772)
- `2025-10-30T21:23:35Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3401719000)
- `2025-11-01T22:13:45Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3407804135)
- `2025-11-03T07:21:41Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3409712608)
- `2025-11-03T07:29:16Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6362#pullrequestreview-3409731435)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/transform.cuh`: 5 inline comment(s)
- `libcudacxx/include/cuda/__memcpy_async/cp_async_bulk_shared_global.h`: 2 inline comment(s)
- `libcudacxx/include/cuda/__memcpy_async/memcpy_async_tx.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-30T19:02:46Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/transform.cuh`:657; signals: hang, kernel, perf, performance, sm120; excerpt: "the original issue only describes slow performance for SM120. What are the implications of this change for other archs?" (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479215499)
- `2025-10-30T21:16:51Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/transform.cuh`:657; signals: cuda, kernel, ptx, sm100, sm90; excerpt: "Trying that with the codegen is identical on sm90 and sm100 for ::cuda::ptx::space shared and ::cuda::ptx::space cluster. I would still go with ::cuda::ptx::space shared ..." (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479551169)
- `2025-11-03T07:29:15Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/transform.cuh`:799; signals: compile, kernel; excerpt: "I considered and thought that the preprocessor might compile faster. But I don't mind. Chaning to conditional t." (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2485543204)
- `2025-10-30T21:23:35Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/transform.cuh`:657; signals: kernel, perf; excerpt: "perfect" (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479566193)
- `2025-11-01T22:13:45Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/__memcpy_async/memcpy_async_tx.h`:79; signals: cuda; excerpt: "I think the small duplication is fine for the two occurences here. Also, I would not know where to put the global variable except ..." (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2483974037)
- `2025-10-30T19:04:27Z` `inline` by `miscco` `libcudacxx/include/cuda/__memcpy_async/cp_async_bulk_shared_global.h`:57; signals: cuda; excerpt: "I believe we should move that out to a define that we can use in all places" (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479219081)
- `2025-10-30T21:12:03Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/__memcpy_async/cp_async_bulk_shared_global.h`:57; signals: cuda; excerpt: "Found a better way. Using conditional t now." (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479537888)
- `2025-10-30T21:20:37Z` `inline` by `fbusato` `libcudacxx/include/cuda/__memcpy_async/memcpy_async_tx.h`:79; signals: cuda; excerpt: "would not be better to use a global constexpr variable?" (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2479560015)
- `2025-11-03T07:21:22Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/transform.cuh`:799; signals: kernel; excerpt: "Nitpick: those two should also use the conditional t" (https://github.com/NVIDIA/cccl/pull/6362#discussion_r2485530074)
