# PR Discussion Digest

- Source PR: [NVIDIA/cccl#2944](https://github.com/NVIDIA/cccl/pull/2944)
- Source page: `sources/prs/cccl-cub/PR-2944.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-2944`
- Generated at: `2026-05-20T15:19:32.082763+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-11-22T22:14:47Z`
- Merged: `2024-11-27T00:42:47Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: bernhardmgruber, fbusato, gevtushenko
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-11-23T07:54:43Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/2944#pullrequestreview-2456365120)
- `2024-11-27T00:42:46Z` `APPROVED` by `gevtushenko` (https://github.com/NVIDIA/cccl/pull/2944#pullrequestreview-2463142544)

## Inline Comment Hotspots

- `cub/cub/thread/thread_reduce.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2024-11-23T08:03:25Z` `issue` by `bernhardmgruber`; signals: benchmark, regression; excerpt: "Thx for reporting the benchmarks. Looks good except for Reduce Max on I8, I32, 2^28. A 14% slowdown is unfortunately below @gevtushenko's rule of ..." (https://github.com/NVIDIA/cccl/pull/2944#issuecomment-2495391408)
- `2024-11-23T07:53:24Z` `inline` by `bernhardmgruber` `cub/cub/thread/thread_reduce.cuh`:555; signals: cuda; excerpt: "Suggestion: Sadly, we may want to include more operators here: We may also just test whether ReductionOp is any instantiation of ::cuda::std::plus. Technically, this ..." (https://github.com/NVIDIA/cccl/pull/2944#discussion_r1855144632)
- `2024-11-22T22:31:32Z` `issue` by `bernhardmgruber`; signals: benchmark; excerpt: "Could you please show a benchmark diff of the three algorithms before 2756 and after this PR? We should see a net benefit then. ..." (https://github.com/NVIDIA/cccl/pull/2944#issuecomment-2494980614)
- `2024-11-22T23:16:39Z` `issue` by `fbusato`; signals: h100; excerpt: "Reduce Max [0] NVIDIA H100 80GB HBM3 T{ct} OffsetT{ct} Elements{io} Ref Time Ref Noise Cmp Time Cmp Noise Diff %Diff Status --------- --------------- ---------------- ..." (https://github.com/NVIDIA/cccl/pull/2944#issuecomment-2495078351)
- `2024-11-25T21:07:04Z` `issue` by `fbusato`; signals: regression; excerpt: "@bernhardmgruber (and @gevtushenko) All routines that show regressions here have been "artificially" improved by the following problem. Non-standard binary operators were recognized as operators ..." (https://github.com/NVIDIA/cccl/pull/2944#issuecomment-2499034764)
