# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7692](https://github.com/NVIDIA/cccl/pull/7692)
- Source page: `sources/prs/cccl-cub/PR-7692.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7692`
- Generated at: `2026-05-20T15:20:18.029784+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-17T02:20:42Z`
- Merged: `2026-04-21T00:58:56Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 54 (approved=2, changes_requested=2, commented=50)
- Inline review comments: 101
- Review threads observed: 60
- Resolved/outdated thread markers: resolved=53, outdated=37
- Human participants with discussion text: Jacobfaib, bernhardmgruber, elstehle, fbusato, miscco, oleksandr-pavlyk, pauleonix, wmaxey
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-16T09:37:13Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4119755187)
- `2026-04-16T13:50:13Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121387219)
- `2026-04-16T14:25:40Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121673740)
- `2026-04-16T14:26:00Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121676094)
- `2026-04-16T14:26:12Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121677499)
- `2026-04-16T14:29:06Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121699716)
- `2026-04-16T14:47:01Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121850295)
- `2026-04-16T14:53:11Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4121898277)
- `2026-04-17T01:19:24Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4125382309)
- `2026-04-17T11:47:22Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128469914)
- `2026-04-17T11:49:32Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128483576)
- `2026-04-17T12:02:47Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128561508)
- `2026-04-17T12:10:25Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128612035)
- `2026-04-17T12:14:40Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128642352)
- `2026-04-17T12:50:59Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4128895085)
- `2026-04-17T15:19:34Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4130003113)
- `2026-04-17T17:50:08Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4130946375)
- `2026-04-17T17:51:54Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4130958828)
- `2026-04-17T17:52:49Z` `COMMENTED` by `wmaxey` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4130964205)
- `2026-04-17T17:54:43Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4130974457)
- `2026-04-17T19:52:24Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4131707970)
- `2026-04-17T20:03:47Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4131712839)
- `2026-04-17T20:42:19Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4131977750)
- `2026-04-17T22:02:59Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7692#pullrequestreview-4132402623)
- ... 30 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cub/cub/warp/specializations/warp_reduce_batched_wspro.cuh`: 51 inline comment(s)
- `cub/cub/warp/warp_reduce_batched.cuh`: 34 inline comment(s)
- `cub/test/warp/catch2_test_warp_reduce_batched_api.cu`: 8 inline comment(s)
- `cub/benchmarks/bench/reduce/warp_reduce_batched_sum.cu`: 4 inline comment(s)
- `cub/benchmarks/bench/reduce/warp_reduce_batched_base.cuh`: 2 inline comment(s)
- `cub/test/warp/catch2_test_warp_reduce_batched.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-20T10:13:31Z` `inline` by `pauleonix` `cub/cub/warp/specializations/warp_reduce_batched_wspro.cuh`:50; signals: block, compile, kernel, perf, warp; excerpt: "For both warp- and block-primitives we tend to leave perf-tuning up to the user (up to some default choices as a starting point). Afaik ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3109875737)
- `2026-04-20T17:33:36Z` `inline` by `Jacobfaib` `cub/cub/warp/specializations/warp_reduce_batched_wspro.cuh`:56; signals: compile, cuda, hang, warp; excerpt: "requested it so heavily templated code does not have to do special handling. Right, for example suppose the user wants to use this algorithm ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3112533791)
- `2026-04-16T09:27:58Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/warp_reduce_batched_sum.cu`:6; signals: benchmark, compile, warp; excerpt: "Important: if this benchmark is ever intended for tuning, please only compile for TUNE T during benchmarking: However, I don't see any tuning parameters ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3092158292)
- `2026-04-16T14:53:11Z` `inline` by `pauleonix` `cub/cub/warp/warp_reduce_batched.cuh`:104; signals: hang, perf, warp; excerpt: "The other warp primitives have a smem implementation that is used for non-power-of-two logical warps. We decided not to support that at all b/c ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3094134578)
- `2026-04-17T19:52:24Z` `inline` by `fbusato` `cub/cub/warp/specializations/warp_reduce_batched_wspro.cuh`:72; signals: perf, performance, warp; excerpt: "no performance advantages. It improves readability because the variables are close to where they are used." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3102908041)
- `2026-04-20T17:19:21Z` `inline` by `pauleonix` `cub/cub/warp/specializations/warp_reduce_batched_wspro.cuh`:56; signals: block, compile, warp; excerpt: "@Jacobfaib requested it so heavily templated code does not have to do special handling. In contrast to C-arrays, other static ranges can be empty. ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3112451995)
- `2026-04-20T15:03:04Z` `inline` by `elstehle` `cub/test/warp/catch2_test_warp_reduce_batched_api.cu`:338; signals: block, kernel, warp; excerpt: "I assume this was supposed to test WarpReduceBatchedSumToBlockedApiKernel?" (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3111628170)
- `2026-04-20T15:49:14Z` `inline` by `elstehle` `cub/test/warp/catch2_test_warp_reduce_batched_api.cu`:338; signals: block, kernel, warp; excerpt: "...should be sufficient to rename SumToStriped to WarpReduceBatchedSumToBlockedApiKernel." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3111920577)
- `2026-04-16T14:25:40Z` `inline` by `pauleonix` `cub/benchmarks/bench/reduce/warp_reduce_batched_sum.cu`:6; signals: benchmark, warp; excerpt: "Afaik we do not tune warp primitives/just expose tuning knobs to the user? Benchmarking got removed from this PR. Will follow up in new ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3093934658)
- `2026-04-16T14:26:00Z` `inline` by `pauleonix` `cub/benchmarks/bench/reduce/warp_reduce_batched_base.cuh`:21; signals: benchmark, warp; excerpt: "Seems like there should be no Doxygen at all in benchmarks... Benchmarking got removed from this PR. Will follow up in new PR." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3093936881)
- `2026-04-17T12:10:23Z` `inline` by `pauleonix` `cub/cub/warp/warp_reduce_batched.cuh`:264; signals: block, warp; excerpt: "I kept it in line with other CUB warp/block primitves that return more than one element per thread. On the other hand it causes ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3100134573)
- `2026-04-17T12:14:38Z` `inline` by `pauleonix` `cub/cub/warp/warp_reduce_batched.cuh`:264; signals: cuda, warp; excerpt: "One (minor?) reason to keep it this way is that it allows the user to use a statically-sized range of their choice. If we ..." (https://github.com/NVIDIA/cccl/pull/7692#discussion_r3100164105)
