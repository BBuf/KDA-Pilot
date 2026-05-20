# PR Discussion Digest

- Source PR: [NVIDIA/cccl#3671](https://github.com/NVIDIA/cccl/pull/3671)
- Source page: `sources/prs/cccl-cub/PR-3671.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-3671`
- Generated at: `2026-05-20T15:19:37.483346+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-04T14:24:49Z`
- Merged: `2025-02-20T11:13:38Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 32 (approved=1, changes_requested=1, commented=30)
- Inline review comments: 60
- Review threads observed: 34
- Resolved/outdated thread markers: resolved=31, outdated=32
- Human participants with discussion text: bernhardmgruber, gonzalobg, jrhemstad, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-04T15:54:45Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593295895)
- `2025-02-04T15:59:18Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593324407)
- `2025-02-04T16:00:15Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593327293)
- `2025-02-04T16:04:43Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593343572)
- `2025-02-04T16:05:40Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593346121)
- `2025-02-04T16:08:41Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593358715)
- `2025-02-04T17:09:21Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593524120)
- `2025-02-04T17:33:44Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593578336)
- `2025-02-04T17:34:23Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2593579603)
- `2025-02-06T20:47:32Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2599890446)
- `2025-02-06T22:58:28Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2600214325)
- `2025-02-17T17:57:22Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2621699695)
- `2025-02-17T18:22:46Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2621731660)
- `2025-02-18T14:14:58Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2623717024)
- `2025-02-18T14:26:58Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2623763998)
- `2025-02-18T16:55:07Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2624279082)
- `2025-02-18T22:10:30Z` `COMMENTED` by `jrhemstad` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2625159278)
- `2025-02-19T08:26:15Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2625999052)
- `2025-02-19T09:15:36Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626126676)
- `2025-02-19T09:15:52Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626127670)
- `2025-02-19T10:45:26Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626293261)
- `2025-02-19T11:36:24Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626522728)
- `2025-02-19T11:38:03Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626526432)
- `2025-02-19T11:39:32Z` `COMMENTED` by `gonzalobg` (https://github.com/NVIDIA/cccl/pull/3671#pullrequestreview-2626530390)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `libcudacxx/include/cuda/try_cancel`: 26 inline comment(s)
- `docs/libcudacxx/extended_api/work_stealing.rst`: 16 inline comment(s)
- `libcudacxx/test/libcudacxx/cuda/for_each_canceled/for_each_canceled.pass.cpp`: 10 inline comment(s)
- `libcudacxx/test/libcudacxx/cuda/try_cancel/try_cancel.pass.cpp`: 6 inline comment(s)
- `libcudacxx/include/cuda/for_each_canceled`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-19T08:26:15Z` `inline` by `gonzalobg` `libcudacxx/include/cuda/try_cancel`:149; signals: block, cuda, hang; excerpt: "Ack, stabilizing API for now to not block on updating that agreement. If the agreement somehow changes before this is ready, we can re-unstabilize ..." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961191425)
- `2025-02-18T14:26:58Z` `inline` by `gonzalobg` `docs/libcudacxx/extended_api/work_stealing.rst`:43; signals: cuda, hang; excerpt: "I've slightly tweaked it and incorporated the suggestions. Leaving this open cause I have not incorporated the leading "or, .." change. The "otherwise" applies ..." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1959859798)
- `2025-02-19T10:36:00Z` `inline` by `bernhardmgruber` `docs/libcudacxx/extended_api/work_stealing.rst`:94; signals: block, cuda; excerpt: "I am a huge fan of const. Also, let's use slightly more descriptive names in examples: (I am not sure blocks per grid helps, ..." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961405512)
- `2025-02-19T10:42:01Z` `inline` by `bernhardmgruber` `libcudacxx/test/libcudacxx/cuda/for_each_canceled/for_each_canceled.pass.cpp`:50; signals: cuda, kernel; excerpt: "Consider a rename for clarification: Applies to the other kernels and the host-side test function as well." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961436822)
- `2025-02-04T15:53:35Z` `inline` by `miscco` `libcudacxx/include/cuda/try_cancel`:191; signals: cuda, ptx; excerpt: "This does not work for nvc++, I am wondering whether this should rather be in the PTX exposure" (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1941440934)
- `2025-02-17T17:52:25Z` `inline` by `bernhardmgruber` `docs/libcudacxx/extended_api/work_stealing.rst`:65; signals: block, cuda; excerpt: "Consider adding a note that blockIdx should not be accessed here." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1958633439)
- `2025-02-17T17:53:07Z` `inline` by `bernhardmgruber` `docs/libcudacxx/extended_api/work_stealing.rst`:90; signals: cuda, memory; excerpt: "Please free the allocated memory." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1958634485)
- `2025-02-17T18:15:34Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/try_cancel`:87; signals: block, cuda; excerpt: "Where is ThreadBlockRank defined? Do you mean ThreadBlockDim there?" (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1958653638)
- `2025-02-19T10:29:36Z` `inline` by `bernhardmgruber` `docs/libcudacxx/extended_api/work_stealing.rst`:22; signals: block, cuda; excerpt: "Remark: Can we consistently spell it thread blocks or thread-blocks?" (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961394875)
- `2025-02-19T10:38:22Z` `inline` by `bernhardmgruber` `libcudacxx/test/libcudacxx/cuda/for_each_canceled/for_each_canceled.pass.cpp`:11; signals: cuda, sm100; excerpt: "Given we have a fallback for before SM100, why can't we test on those architectures?" (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961411616)
- `2025-02-19T10:41:28Z` `inline` by `bernhardmgruber` `libcudacxx/test/libcudacxx/cuda/for_each_canceled/for_each_canceled.pass.cpp`:77; signals: cuda, kernel; excerpt: "Please remove this unused parameter: Applies to the following two kernels as well." (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961433859)
- `2025-02-19T14:24:35Z` `inline` by `gonzalobg` `libcudacxx/test/libcudacxx/cuda/for_each_canceled/for_each_canceled.pass.cpp`:114; signals: cuda, hang; excerpt: "This change dropped the if (c[i] != (1 + i)) @miscco ?" (https://github.com/NVIDIA/cccl/pull/3671#discussion_r1961778943)
