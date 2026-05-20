# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7575](https://github.com/NVIDIA/cccl/pull/7575)
- Source page: `sources/prs/cccl-cub/PR-7575.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7575`
- Generated at: `2026-05-20T15:20:14.595997+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-09T14:04:46Z`
- Merged: `2026-02-25T09:07:52Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 18 (approved=3, changes_requested=1, commented=14)
- Inline review comments: 20
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=5, outdated=8
- Human participants with discussion text: bernhardmgruber, fbusato, miscco, pauleonix
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-11T17:08:03Z` `APPROVED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3786113892)
- `2026-02-11T20:25:14Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3787250035)
- `2026-02-11T20:25:56Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3787254483)
- `2026-02-11T20:29:33Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3787277283)
- `2026-02-12T11:08:09Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3790305608)
- `2026-02-12T11:12:55Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3790337080)
- `2026-02-12T12:22:22Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3790707640)
- `2026-02-13T07:33:35Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3795526830)
- `2026-02-13T10:55:07Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3796624599)
- `2026-02-14T00:31:23Z` `APPROVED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3800301204)
- `2026-02-22T18:32:58Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3838455480)
- `2026-02-23T07:38:28Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3839529779)
- `2026-02-23T07:38:36Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3839530162)
- `2026-02-23T14:12:54Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3841286575)
- `2026-02-23T21:39:05Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3843669929)
- `2026-02-23T21:39:45Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3843672557)
- `2026-02-23T21:40:36Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3843675575)
- `2026-02-25T06:35:07Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7575#pullrequestreview-3852214359)

## Inline Comment Hotspots

- `cub/cub/util_arch.cuh`: 10 inline comment(s)
- `cub/cub/agent/single_pass_scan_operators.cuh`: 6 inline comment(s)
- `cub/test/catch2_test_device_scan_invalid.cu`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-23T21:39:04Z` `inline` by `bernhardmgruber` `cub/cub/util_arch.cuh`:120; signals: compile, ptx, warp; excerpt: "we need the same workaround as for the warpspeed scan No. warpspeed scan uses the compiler built-in atomics, whereas the classical decoupled lookback relies ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2843215646)
- `2026-02-12T11:12:55Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_scan_invalid.cu`:60; signals: hang; excerpt: "The changes in this PR make segment take the primitive path now, because it's trivially copyable. So I guess segment must be made non-trivially ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2798273720)
- `2026-02-13T07:33:35Z` `inline` by `miscco` `cub/cub/util_arch.cuh`:119; signals: sm90; excerpt: "I believe this requires SM90 otherwise its only 8" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2802731752)
- `2026-02-23T07:38:28Z` `inline` by `miscco` `cub/cub/util_arch.cuh`:120; signals: warp; excerpt: "This will break NVHPC, we need the same workaround as for the warpspeed scan" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2839444044)
- `2026-02-11T17:07:27Z` `inline` by `fbusato` `cub/cub/agent/single_pass_scan_operators.cuh`:561; signals: general review; excerpt: "(sizeof(ValueT) + sizeof(KeyT) < largest atomic word size) or (sizeof(ValueT) + sizeof(KeyT) <= largest atomic word size)?" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2794463630)
- `2026-02-11T20:25:14Z` `inline` by `bernhardmgruber` `cub/cub/util_arch.cuh`:119; signals: general review; excerpt: "I don't know TBH. We hardcoded 16 in the past and I know the build-in atomics like nv atomic load support up to 16 ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2795348911)
- `2026-02-11T20:29:29Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_scan_invalid.cu`:60; signals: general review; excerpt: "@pauleonix I need your input here please. Why does segment need to be a non-primitive type and what should this mean here? Because it ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2795368817)
- `2026-02-13T10:55:07Z` `inline` by `bernhardmgruber` `cub/cub/util_arch.cuh`:119; signals: general review; excerpt: "I think the name of the variable may not be accurate then. We have ld.acquire.gpu.v2.u64 on SM70, and ld.cg.v2.u64+ threadfence() before that. (I am ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2803611931)
- `2026-02-23T14:12:54Z` `inline` by `pauleonix` `cub/cub/util_arch.cuh`:120; signals: general review; excerpt: "I think the inline here does nothing (static wins and makes more sense?). Looking at other constants in this header we do not seem ..." (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2841077940)
- `2026-02-11T17:03:46Z` `inline` by `fbusato` `cub/cub/agent/single_pass_scan_operators.cuh`:658; signals: general review; excerpt: "I would avoid macro style here" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2794446279)
- `2026-02-11T17:05:21Z` `inline` by `fbusato` `cub/cub/util_arch.cuh`:119; signals: general review; excerpt: "I don't think this is true for all architectures" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2794453613)
- `2026-02-11T17:07:42Z` `inline` by `fbusato` `cub/cub/agent/single_pass_scan_operators.cuh`:560; signals: general review; excerpt: "conditional t?" (https://github.com/NVIDIA/cccl/pull/7575#discussion_r2794464750)
