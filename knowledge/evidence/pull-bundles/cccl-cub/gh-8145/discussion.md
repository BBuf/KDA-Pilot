# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8145](https://github.com/NVIDIA/cccl/pull/8145)
- Source page: `sources/prs/cccl-cub/PR-8145.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8145`
- Generated at: `2026-05-20T15:20:30.186279+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T10:14:47Z`
- Merged: `2026-03-30T16:17:16Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 14 (approved=4, changes_requested=1, commented=9)
- Inline review comments: 19
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, fbusato, griwes, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T10:21:14Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-3997954941)
- `2026-03-24T10:22:17Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-3997961184)
- `2026-03-24T10:23:24Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-3997968837)
- `2026-03-24T10:24:38Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-3997977149)
- `2026-03-24T17:30:15Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4000894283)
- `2026-03-25T07:24:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004537273)
- `2026-03-25T07:46:01Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004638533)
- `2026-03-25T07:46:34Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004642475)
- `2026-03-25T07:47:09Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004646258)
- `2026-03-25T07:48:46Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004654453)
- `2026-03-25T07:53:14Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4004676819)
- `2026-03-26T03:49:36Z` `APPROVED` by `griwes` - I love the unification of the divergent constexpr/nonconstexpr paths. (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4011237926)
- `2026-03-30T14:34:33Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4031069827)
- `2026-03-30T15:55:37Z` `APPROVED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8145#pullrequestreview-4031618432)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_scan.cuh`: 10 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`: 4 inline comment(s)
- `cub/cub/device/dispatch/dispatch_scan.cuh`: 3 inline comment(s)
- `cub/test/catch2_test_device_scan_env.cu`: 1 inline comment(s)
- `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-24T10:21:14Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:644; signals: hang, warp; excerpt: "Note: I am entirely removing warpspeed scan from the old policy hub, since we have the new tuning API now and we did not ..." (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2980490318)
- `2026-03-24T17:14:02Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:74; signals: kernel, warp; excerpt: "could be constexpr?" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983100467)
- `2026-03-24T17:14:40Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:76; signals: kernel, warp; excerpt: "suggestion. replace 32 with a constant for warp size" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983103783)
- `2026-03-24T17:17:55Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:140; signals: kernel, warp; excerpt: "suggestion. rewrite as max(1, num stages - 1)" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983122097)
- `2026-03-24T17:20:36Z` `inline` by `fbusato` `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`:32; signals: kernel, warp; excerpt: "32 - warp size" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983140162)
- `2026-03-25T07:48:46Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:74; signals: kernel, warp; excerpt: "No, because policy is not constexpr." (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2986409119)
- `2026-03-24T10:22:17Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:1317; signals: kernel; excerpt: "Note: It's not the policy selector's job to handle the type erasure required for CCCL.C, that's what we have the kernel source for." (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2980496209)
- `2026-03-24T10:24:38Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_scan_env.cu`:67; signals: ptx; excerpt: "Note: It could be argued that we should not use a detail function in the unit tests, but we will probably expose ptx arch ..." (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2980509496)
- `2026-03-24T17:29:52Z` `inline` by `fbusato` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:654; signals: cuda; excerpt: "question. Do we really need this kind of dispatch instead of using a template type + cuda::std utilities?" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983196159)
- `2026-03-25T07:47:09Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:654; signals: compile; excerpt: "Unfortunately, yes. We need to be able to compile the entire dispatch and tuning without any types when coming from Python via CCCL.C." (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2986401739)
- `2026-03-24T17:21:56Z` `inline` by `fbusato` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:643; signals: hang; excerpt: "is this change expected?" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983147859)
- `2026-03-24T17:29:05Z` `inline` by `fbusato` `cub/cub/device/dispatch/dispatch_scan.cuh`:560; signals: compile; excerpt: "my understanding is that everything here is at compile-time" (https://github.com/NVIDIA/cccl/pull/8145#discussion_r2983191349)
