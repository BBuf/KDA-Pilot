# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8172](https://github.com/NVIDIA/cccl/pull/8172)
- Source page: `sources/prs/cccl-cub/PR-8172.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8172`
- Generated at: `2026-05-20T15:20:32.179032+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T15:29:20Z`
- Merged: `2026-05-07T07:03:14Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 13 (approved=3, changes_requested=3, commented=7)
- Inline review comments: 30
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=18, outdated=24
- Human participants with discussion text: bernhardmgruber, charan-003, fbusato, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T17:17:10Z` `CHANGES_REQUESTED` by `miscco` - Thanks a lot for the interest. I agree with @bernhardmgruber that we want to move this into libcu++ ... (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4008328620)
- `2026-03-25T23:46:00Z` `COMMENTED` by `charan-003` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4010594344)
- `2026-03-26T00:00:23Z` `COMMENTED` by `charan-003` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4010634595)
- `2026-03-26T00:35:44Z` `COMMENTED` by `charan-003` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4010735551)
- `2026-03-26T18:17:53Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4016395674)
- `2026-03-30T07:44:00Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4028647331)
- `2026-03-31T15:51:30Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4038395194)
- `2026-04-23T15:02:26Z` `COMMENTED` by `bernhardmgruber` - @miscco can you please review the libcu++ changes? I also want to see a SASS diff for the ... (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4163532155)
- `2026-04-23T16:16:35Z` `COMMENTED` by `charan-003` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4164083439)
- `2026-05-06T12:40:41Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4236091666)
- `2026-05-06T13:31:21Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4236461476)
- `2026-05-06T13:33:26Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4236479331)
- `2026-05-07T07:01:59Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4241787069)

## Inline Comment Hotspots

- `cub/cub/detail/uninitialized_array.cuh`: 17 inline comment(s)
- `cub/test/catch2_test_detail_uninitialized_array.cu`: 5 inline comment(s)
- `libcudacxx/test/libcudacxx/libcxx/memory/uninitialized_array.pass.cpp`: 2 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_transform.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/tuning/common.cuh`: 2 inline comment(s)
- `libcudacxx/include/cuda/__memory/uninitialized_array.h`: 1 inline comment(s)
- `thrust/thrust/system/cuda/detail/core/util.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-06T13:33:21Z` `inline` by `miscco` `libcudacxx/test/libcudacxx/libcxx/memory/uninitialized_array.pass.cpp`:84; signals: cuda, memory, tile; excerpt: "Final comment: We need to replace open coded host device with TEST FUNC because of future tile support." (https://github.com/NVIDIA/cccl/pull/8172#discussion_r3195809313)
- `2026-04-23T15:02:26Z` `review` `COMMENTED` by `bernhardmgruber`; signals: benchmark, hang; excerpt: "@miscco can you please review the libcu++ changes? I also want to see a SASS diff for the fill benchmark of device transform. I ..." (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4163532155)
- `2026-03-26T22:32:46Z` `issue` by `charan-003`; signals: cuda, hang, kernel; excerpt: "before making further changes I want to make sure the implementation of uninitialized array in the libcu++ is correct. Based on searching for all ..." (https://github.com/NVIDIA/cccl/pull/8172#issuecomment-4138754519)
- `2026-03-25T17:01:59Z` `inline` by `miscco` `cub/cub/detail/uninitialized_array.cuh`:37; signals: compile, cuda; excerpt: "This is missing cuda::std::launder to tell the compiler we really know that there is an object in here See" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r2989699074)
- `2026-03-25T17:04:27Z` `inline` by `miscco` `cub/cub/detail/uninitialized_array.cuh`:7; signals: cuda, memory; excerpt: "Please move this file into libcudacxx/include/cuda/ memory/uninitialized array Also please adopt the license and the config accoringly" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r2989711785)
- `2026-03-25T17:11:44Z` `inline` by `miscco` `cub/test/catch2_test_detail_uninitialized_array.cu`; signals: cuda, memory; excerpt: "This is an internal CCCL API, please move the test into libcudacxx/test/libcudacxx/libcxx/memory/uninitialized array.pass.cpp" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r2989750017)
- `2026-03-30T07:41:53Z` `inline` by `miscco` `libcudacxx/include/cuda/__memory/uninitialized_array.h`:34; signals: cuda, memory; excerpt: "We do not want this to be publicly available, because it is a very dangerous feature. Please rename to" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r3008092415)
- `2026-03-30T07:43:39Z` `inline` by `miscco` `libcudacxx/test/libcudacxx/libcxx/memory/uninitialized_array.pass.cpp`; signals: cuda, memory; excerpt: "I believe this is an internal only feature we use. We should move this test to the other internal only tests, aka ‎libcudacxx/test/libcudacxx/libcxx/memory/uninitialized array.pass.cpp" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r3008099921)
- `2026-03-25T17:17:10Z` `review` `CHANGES_REQUESTED` by `miscco`; signals: hang; excerpt: "Thanks a lot for the interest. I agree with @bernhardmgruber that we want to move this into libcu++ unfortunately that requires a certain amount ..." (https://github.com/NVIDIA/cccl/pull/8172#pullrequestreview-4008328620)
- `2026-03-25T17:22:18Z` `issue` by `charan-003`; signals: cuda, hang; excerpt: "Thanks a lot for the interest. I agree with @bernhardmgruber that we want to move this into libcu++ unfortunately that requires a certain amount ..." (https://github.com/NVIDIA/cccl/pull/8172#issuecomment-4128366386)
- `2026-03-25T23:46:00Z` `inline` by `charan-003` `cub/cub/detail/uninitialized_array.cuh`:29; signals: cuda; excerpt: "i was following the [cccl/thrust/thrust/system/cuda/detail/core/util.h]( well i removed it, we can get the size from the template parameter Size directly if needed" (https://github.com/NVIDIA/cccl/pull/8172#discussion_r2991701311)
- `2026-03-26T00:35:44Z` `inline` by `charan-003` `cub/test/catch2_test_detail_uninitialized_array.cu`:43; signals: compile; excerpt: "@miscco for the non-trivial type tests should these be .fail.cpp tests that verify the static assert which complain at compile time, or would you ..." (https://github.com/NVIDIA/cccl/pull/8172#discussion_r2991834365)
