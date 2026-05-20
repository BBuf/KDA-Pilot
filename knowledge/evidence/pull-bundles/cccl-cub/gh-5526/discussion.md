# PR Discussion Digest

- Source PR: [NVIDIA/cccl#5526](https://github.com/NVIDIA/cccl/pull/5526)
- Source page: `sources/prs/cccl-cub/PR-5526.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-5526`
- Generated at: `2026-05-20T15:19:51.013373+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-13T15:57:03Z`
- Merged: `2025-08-18T09:33:24Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: bernhardmgruber, elstehle, miscco
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-14T19:18:08Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3121847882)
- `2025-08-14T19:18:14Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3121848112)
- `2025-08-18T06:24:09Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3126933691)
- `2025-08-18T06:55:11Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3126968528)
- `2025-08-18T07:16:27Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3127073444)
- `2025-08-18T07:26:38Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3127118253)
- `2025-08-18T07:30:58Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3127134141)
- `2025-08-18T07:31:09Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5526#pullrequestreview-3127134617)

## Inline Comment Hotspots

- `cub/benchmarks/bench/transform/fill.cu`: 5 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_transform.cuh`: 2 inline comment(s)
- `cub/cub/device/device_transform.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-18T07:26:38Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/transform/fill.cu`:7; signals: alignment, benchmark, blackwell, block, hopper, tile; excerpt: "Hopper and Blackwell use 256 and 128 which we determined by experimentation. A block size which is a multiple of 128 also has the ..." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281525161)
- `2025-08-18T06:55:07Z` `inline` by `elstehle` `cub/benchmarks/bench/transform/fill.cu`:7; signals: benchmark, perf, performance; excerpt: "question: I realized just now that for transform we're generally using a granularity of 128 threads. This seems quite coarse grained. Do we expect ..." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281460480)
- `2025-08-18T06:24:09Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_transform.cuh`:368; signals: vector; excerpt: "Not at all. We have two fallbacks now: we can fallback to the prefetch algorithm, which can handle everything, but in some cases we ..." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281405695)
- `2025-08-18T06:39:42Z` `inline` by `elstehle` `cub/cub/device/device_transform.cuh`:247; signals: hang; excerpt: "This breaks users that were previously explicitly passing the template arguments. Do we feel confident that the interface is new enough that this change ..." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281431640)
- `2025-08-18T07:30:57Z` `inline` by `elstehle` `cub/benchmarks/bench/transform/fill.cu`:7; signals: benchmark; excerpt: "Got it. Thanks for the elaborate answer! Agreed, let's keep it as is for now. We can still revisit whether evaluating intermediate values gives ..." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281534287)
- `2025-08-18T06:48:08Z` `inline` by `elstehle` `cub/benchmarks/bench/transform/fill.cu`:2; signals: benchmark; excerpt: "question: Shouldn't net new files be Apache 2?" (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281447889)
- `2025-08-18T07:16:27Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/transform/fill.cu`:2; signals: benchmark; excerpt: "Yes!" (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281502778)
- `2025-08-18T07:31:09Z` `inline` by `bernhardmgruber` `cub/cub/device/device_transform.cuh`:247; signals: general review; excerpt: "We added TransformIf last week in 5198. It's not on the CCCL 3.1 release branch, so we should be good." (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2281534635)
- `2025-08-14T19:18:08Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_transform.cuh`:368; signals: general review; excerpt: "Was that the fix that we shadowed the policy variable?" (https://github.com/NVIDIA/cccl/pull/5526#discussion_r2277520934)
