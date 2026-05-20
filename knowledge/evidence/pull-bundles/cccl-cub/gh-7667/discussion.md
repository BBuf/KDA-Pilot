# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7667](https://github.com/NVIDIA/cccl/pull/7667)
- Source page: `sources/prs/cccl-cub/PR-7667.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7667`
- Generated at: `2026-05-20T15:20:14.600664+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-13T12:49:15Z`
- Merged: `2026-02-27T19:02:27Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=2
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T21:31:15Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3843638749)
- `2026-02-26T07:37:37Z` `APPROVED` by `miscco` - Mostly nits and a policy question (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3858985015)
- `2026-02-26T08:28:53Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3859290157)
- `2026-02-26T08:29:26Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3859293705)
- `2026-02-26T08:33:06Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3859313531)
- `2026-02-27T17:37:22Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/7667#pullrequestreview-3868198579)

## Inline Comment Hotspots

- `cub/benchmarks/bench/run_length_encode/encode.cu`: 3 inline comment(s)
- `cub/benchmarks/bench/reduce/by_key.cu`: 2 inline comment(s)
- `cub/cub/device/dispatch/dispatch_streaming_reduce_by_key.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_reduce_by_key.cuh`: 1 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_rle_encode.cuh`: 1 inline comment(s)
- `cub/cub/device/dispatch/dispatch_reduce_by_key.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-26T08:28:53Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/by_key.cu`:39; signals: benchmark, hang; excerpt: "Maybe, but I didn't want to change the benchmark definition in this PR." (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857653707)
- `2026-02-26T07:33:13Z` `inline` by `miscco` `cub/benchmarks/bench/reduce/by_key.cu`:39; signals: benchmark; excerpt: "Question: should this be" (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857401836)
- `2026-02-26T07:33:39Z` `inline` by `miscco` `cub/benchmarks/bench/run_length_encode/encode.cu`:49; signals: benchmark; excerpt: "Ditto" (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857403389)
- `2026-02-26T08:29:26Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/run_length_encode/encode.cu`:49; signals: benchmark; excerpt: "Same." (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857656339)
- `2026-02-26T07:34:45Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_reduce_by_key.cuh`:32; signals: general review; excerpt: "We unconditionally provide concepts" (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857407107)
- `2026-02-26T07:37:03Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_streaming_reduce_by_key.cuh`:51; signals: general review; excerpt: "Question: I see a ton of transitive includes in here, What is the CUB policy here?" (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857416613)
- `2026-02-26T08:33:05Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_streaming_reduce_by_key.cuh`:51; signals: general review; excerpt: "We should include what we use. I added a bunch of includes." (https://github.com/NVIDIA/cccl/pull/7667#discussion_r2857671965)
