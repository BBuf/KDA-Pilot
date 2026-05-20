# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8332](https://github.com/NVIDIA/cccl/pull/8332)
- Source page: `sources/prs/cccl-cub/PR-8332.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8332`
- Generated at: `2026-05-20T15:20:39.745331+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T21:45:09Z`
- Merged: `2026-04-24T19:14:03Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 12 (approved=3, commented=9)
- Inline review comments: 17
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=14, outdated=12
- Human participants with discussion text: bernhardmgruber, miscco, srinivasyadav18
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-09T07:16:29Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4080314481)
- `2026-04-13T20:25:20Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4101686213)
- `2026-04-13T20:49:48Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4101861536)
- `2026-04-21T15:56:20Z` `COMMENTED` by `srinivasyadav18` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4149120527)
- `2026-04-21T16:10:53Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4149166116)
- `2026-04-21T21:05:33Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4150770683)
- `2026-04-21T21:27:44Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4150852254)
- `2026-04-22T05:51:10Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4152324585)
- `2026-04-22T07:58:57Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4152958134)
- `2026-04-22T08:00:01Z` `APPROVED` by `bernhardmgruber` - Please address the two remaining nits. Otherwise, LGTM (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4152963753)
- `2026-04-24T13:10:45Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4170660599)
- `2026-04-24T17:27:29Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8332#pullrequestreview-4172310622)

## Inline Comment Hotspots

- `cub/cub/device/device_segmented_reduce.cuh`: 6 inline comment(s)
- `cub/benchmarks/bench/segmented_reduce/base.cuh`: 3 inline comment(s)
- `cub/benchmarks/bench/segmented_reduce/argmin.cu`: 3 inline comment(s)
- `cub/cub/device/dispatch/dispatch_segmented_reduce.cuh`: 2 inline comment(s)
- `cub/cub/agent/agent_reduce.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_segmented_reduce.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-21T16:10:16Z` `inline` by `bernhardmgruber` `cub/cub/agent/agent_reduce.cuh`:125; signals: compile, hang, warp; excerpt: "Critical: this is a breaking change, since cub::AgentWarpReducePolicy is part of the public API. Consider a "hack" like: where you would skip scaling if ..." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3118818032)
- `2026-04-13T20:23:27Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_reduce/base.cuh`:28; signals: benchmark, warp; excerpt: "Critical: TUNE S NOMINAL 4B ITEMS PER THREAD are nominal items and must be scaled before populating the tuning policy. This was also done ..." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3075596698)
- `2026-04-13T20:49:48Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_reduce.cuh`:355; signals: kernel, warp; excerpt: "As discussed offline, please extend AgentWarpReducePolicy to not apply scaling and pass the actual items per thread here." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3075740555)
- `2026-04-09T07:16:24Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_reduce/base.cuh`:39; signals: benchmark; excerpt: "Important: The previous policy hub made use of a lot more tuning variables than the new policy selector. Inside the sum.cu benchmark I see: ..." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3056108711)
- `2026-04-21T16:03:33Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_reduce/argmin.cu`:12; signals: benchmark; excerpt: "Important: Please retain the term NOMINAL 4B inside tuning parameters that are scaled later. It helps with understanding the code." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3118780091)
- `2026-04-21T21:23:37Z` `inline` by `bernhardmgruber` `cub/cub/device/device_segmented_reduce.cuh`:117; signals: hang; excerpt: "Suggestion: since we rely on deduction now instead of passing offset t explicitly as template parameter, let's add a cast in case we ever ..." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3120381904)
- `2026-04-21T15:56:20Z` `inline` by `srinivasyadav18` `cub/benchmarks/bench/segmented_reduce/base.cuh`:28; signals: benchmark; excerpt: "Resolved in [c5e465f](" (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3118737917)
- `2026-04-21T16:06:04Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_reduce/argmin.cu`:8; signals: benchmark; excerpt: "Important: Please also add the term NOMINAL 4B to those parameters since they are scaled as well." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3118794570)
- `2026-04-21T21:05:33Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_reduce/argmin.cu`:8; signals: benchmark; excerpt: "Discussed offline, not necessary." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3120303959)
- `2026-04-14T10:15:57Z` `issue` by `bernhardmgruber`; signals: hang; excerpt: "@srinivasyadav18 I just merged 8097, which adds the environment overloads for your changes here. Can you please rebase your work and make sure the ..." (https://github.com/NVIDIA/cccl/pull/8332#issuecomment-4243109108)
- `2026-04-22T05:51:03Z` `inline` by `miscco` `cub/cub/device/device_segmented_reduce.cuh`:1037; signals: general review; excerpt: "Question: can we not pass offset t explicitly? That requires us to keep the alias and the function declaration in sync. It should be ..." (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3121829358)
- `2026-04-09T07:04:47Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_reduce.cuh`:767; signals: general review; excerpt: "Important: Please add error handling here:" (https://github.com/NVIDIA/cccl/pull/8332#discussion_r3056037995)
