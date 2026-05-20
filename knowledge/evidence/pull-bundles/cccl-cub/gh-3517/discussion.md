# PR Discussion Digest

- Source PR: [NVIDIA/cccl#3517](https://github.com/NVIDIA/cccl/pull/3517)
- Source page: `sources/prs/cccl-cub/PR-3517.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-3517`
- Generated at: `2026-05-20T15:19:32.097458+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-24T03:13:31Z`
- Merged: `2025-02-04T10:48:22Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 13 (approved=3, changes_requested=1, commented=9)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: ChristinaZ, bernhardmgruber, elstehle, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-01-24T07:05:51Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2571798878)
- `2025-01-24T08:55:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2572061574)
- `2025-01-24T09:10:19Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2572092858)
- `2025-01-24T13:09:49Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2572610196)
- `2025-01-24T14:21:37Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2572777216)
- `2025-01-25T05:50:35Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2573941621)
- `2025-01-25T05:57:51Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2573942514)
- `2025-01-25T06:30:49Z` `COMMENTED` by `elstehle` - Could you please also add a small test to test/catch2 test block load.cu that loads from an {aligned,unaligned} ... (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2573946930)
- `2025-01-26T07:05:59Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2574150820)
- `2025-02-03T08:37:16Z` `APPROVED` by `elstehle` - That's great. Thanks a lot for your contribution! (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2589229758)
- `2025-02-03T09:07:16Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2589301188)
- `2025-02-03T09:10:27Z` `COMMENTED` by `bernhardmgruber` - @elstehle Do we need a before/after benchmark? AFAIK, we don't have one for block load. I expect the ... (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2589307021)
- `2025-02-03T09:19:34Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2589331001)

## Inline Comment Hotspots

- `cub/cub/block/block_load.cuh`: 8 inline comment(s)
- `cub/test/catch2_test_block_load.cu`: 4 inline comment(s)

## High-Signal Discussion

- `2025-01-24T05:38:06Z` `issue` by `elstehle`; signals: aligned, alignment, block, compile, cuda, perf, performance, vector; excerpt: "Thank you @ChristinaZ for looking into this. It seems that the root cause is that we do have a superfluous template parameter that prevents ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2611643092)
- `2025-01-25T06:30:49Z` `review` `COMMENTED` by `elstehle`; signals: aligned, alignment, block, perf, performance, vector; excerpt: "Could you please also add a small test to test/catch2 test block load.cu that loads from an {aligned,unaligned} x {ptr-to-const,ptr-to-non-const}? Regarding performance concerns: I ..." (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2573946930)
- `2025-01-25T07:25:28Z` `issue` by `ChristinaZ`; signals: aligned, alignment, benchmark, block, perf, performance, vector; excerpt: "Could you please also add a small test to test/catch2 test block load.cu that loads from an {aligned,unaligned} x {ptr-to-const,ptr-to-non-const}? No problem. Let me ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2613823984)
- `2025-02-03T09:17:22Z` `issue` by `elstehle`; signals: alignment, benchmark, block, hang, perf, performance, vector; excerpt: "@elstehle Do we need a before/after benchmark? AFAIK, we don't have one for block load. I expect the SASS to change (for good!). My ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2630378259)
- `2025-02-03T09:19:24Z` `issue` by `bernhardmgruber`; signals: benchmark, block, hang, perf, performance; excerpt: "@elstehle Do we need a before/after benchmark? AFAIK, we don't have one for block load. I expect the SASS to change (for good!). My ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2630383021)
- `2025-02-03T09:10:27Z` `review` `COMMENTED` by `bernhardmgruber`; signals: benchmark, block, hang; excerpt: "@elstehle Do we need a before/after benchmark? AFAIK, we don't have one for block load. I expect the SASS to change (for good!)." (https://github.com/NVIDIA/cccl/pull/3517#pullrequestreview-2589307021)
- `2025-01-25T05:57:49Z` `inline` by `elstehle` `cub/cub/block/block_load.cuh`:214; signals: alignment, block, vector; excerpt: "I think, we actually want to make sure the pointer meets the alignment requirements of vector t." (https://github.com/NVIDIA/cccl/pull/3517#discussion_r1929482764)
- `2025-01-26T07:46:39Z` `issue` by `elstehle`; signals: block, compile, perf; excerpt: "Note, we have the following line in the block load test: Which means, the source file will be compiled twice: (1) once with define ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2614258762)
- `2025-01-24T14:21:09Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load.cuh`:211; signals: block, vector; excerpt: "Q: I don't understand this test. Shouldn't this test the address to be a multiple of sizeof(vector t) (which should be sizeof(T) vector size)" (https://github.com/NVIDIA/cccl/pull/3517#discussion_r1928756254)
- `2025-01-24T07:59:13Z` `issue` by `ChristinaZ`; signals: block, vector; excerpt: "Is this something you could take on? Yes, I think so. We can use a similar check within function Load(RandomAccessIterator block src it, T ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2611891968)
- `2025-01-24T09:16:17Z` `issue` by `elstehle`; signals: aligned, vector; excerpt: "Just to summarize the findings from the offline discussion with @miscco and @ChristinaZ: We have this overload that is supposed to be chosen when ..." (https://github.com/NVIDIA/cccl/pull/3517#issuecomment-2612035631)
- `2025-01-24T08:55:12Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load.cuh`:899; signals: block; excerpt: "We should probably use thrust::is contiguous iterator because that also considers all proclaimed iterators." (https://github.com/NVIDIA/cccl/pull/3517#discussion_r1928346279)
