# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8826](https://github.com/NVIDIA/cccl/pull/8826)
- Source page: `sources/prs/cccl-cub/PR-8826.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8826`
- Generated at: `2026-05-20T15:20:57.333329+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-05T15:08:48Z`
- Merged: `2026-05-12T10:02:11Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 16
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: NaderAlAwar, bernhardmgruber
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T13:08:59Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4252444539)
- `2026-05-08T14:07:57Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4252695392)
- `2026-05-08T15:08:39Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4253223826)
- `2026-05-08T15:18:13Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4253285916)
- `2026-05-11T08:43:02Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4261950838)
- `2026-05-11T08:46:09Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4261973342)
- `2026-05-11T08:46:54Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4261978820)
- `2026-05-11T14:59:10Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8826#pullrequestreview-4264760826)

## Inline Comment Hotspots

- `cub/benchmarks/bench/reduce/base.cuh`: 6 inline comment(s)
- `cub/test/catch2_test_device_reduce_env.cu`: 4 inline comment(s)
- `cub/benchmarks/bench/reduce/nondeterministic.cu`: 3 inline comment(s)
- `cub/benchmarks/bench/reduce/arg_extrema.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-08T15:18:13Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/base.cuh`:58; signals: benchmark, hang, perf, performance, regression; excerpt: "Right. I see I missed the SASS checks for this PR that would have revealed that issue. On a different note: I discussed this ..." (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3209605062)
- `2026-05-08T14:04:58Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/base.cuh`:58; signals: benchmark, cuda; excerpt: "Important: now that this benchmark calls the public DeviceReduce::Reduce API, the accumulator type may differ from T because cuda::std::plus might promote to a larger ..." (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3209181416)
- `2026-05-11T08:43:01Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/base.cuh`:58; signals: benchmark, hang; excerpt: "6576 is resolved now and I rebased the PR. We did change the meaning of the benchmark in 8884, so this PR no longer ..." (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3217436586)
- `2026-05-08T14:06:26Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/base.cuh`:21; signals: benchmark; excerpt: "Suggestion: might be worth a drive by fix since we no longer return the nondeterministic policy" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3209189779)
- `2026-05-08T14:07:39Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/nondeterministic.cu`:66; signals: benchmark; excerpt: "Important: same issue as base.cuh regarding the type" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3209196743)
- `2026-05-11T08:46:09Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/nondeterministic.cu`:66; signals: benchmark; excerpt: "Thx! Fixed." (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3217455551)
- `2026-05-11T08:46:53Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/reduce/base.cuh`:58; signals: benchmark; excerpt: "And I fixed the accumulator type passed here! Sorry, I missed that initially. Well spotted!" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3217460185)
- `2026-05-11T14:54:49Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/base.cuh`:52; signals: benchmark; excerpt: "Important: typo which will cause compilation failures" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3219877923)
- `2026-05-11T14:55:04Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/nondeterministic.cu`:66; signals: benchmark; excerpt: "Important: typo" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3219879841)
- `2026-05-11T14:56:15Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/arg_extrema.cu`:29; signals: benchmark; excerpt: "Suggestion: this is also worth a driveby fix to remove the nondeterministic policy" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3219888878)
- `2026-05-11T14:58:31Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/arg_extrema.cu`:38; signals: benchmark; excerpt: "Nit:" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3219905363)
- `2026-05-11T14:58:42Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/arg_extrema.cu`:66; signals: benchmark; excerpt: "Nit:" (https://github.com/NVIDIA/cccl/pull/8826#discussion_r3219906794)
