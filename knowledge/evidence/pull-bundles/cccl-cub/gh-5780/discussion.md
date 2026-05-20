# PR Discussion Digest

- Source PR: [NVIDIA/cccl#5780](https://github.com/NVIDIA/cccl/pull/5780)
- Source page: `sources/prs/cccl-cub/PR-5780.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-5780`
- Generated at: `2026-05-20T15:19:51.025517+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-05T01:26:57Z`
- Merged: `2025-09-30T08:29:26Z`

## Discussion Counts

- Issue comments: 40
- Review submissions: 64 (approved=1, commented=63)
- Inline review comments: 92
- Review threads observed: 41
- Resolved/outdated thread markers: resolved=38, outdated=32
- Human participants with discussion text: bernhardmgruber, miscco, pauleonix
- Automation comments/reviews omitted from high-signal summary: 16
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-09-05T06:52:13Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3188205412)
- `2025-09-05T23:22:21Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3191038242)
- `2025-09-05T23:38:32Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3191093505)
- `2025-09-05T23:49:21Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3191120757)
- `2025-09-08T10:11:10Z` `COMMENTED` by `bernhardmgruber` - Good work so far! Let's add some unit test to cover the API and show how it's used. (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3195850540)
- `2025-09-08T15:28:05Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3197047505)
- `2025-09-08T15:30:12Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3197058205)
- `2025-09-08T16:24:59Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3197261143)
- `2025-09-15T08:23:41Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3223408695)
- `2025-09-15T14:43:59Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3225014882)
- `2025-09-15T14:50:43Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3225049505)
- `2025-09-15T14:52:35Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3225057566)
- `2025-09-16T17:18:09Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3230973735)
- `2025-09-16T17:35:12Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3231027866)
- `2025-09-16T19:57:21Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3231504593)
- `2025-09-16T22:38:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3231908971)
- `2025-09-19T00:30:00Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3242404901)
- `2025-09-19T09:35:42Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3243740184)
- `2025-09-19T09:42:34Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3244047767)
- `2025-09-19T09:51:15Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3244084900)
- `2025-09-20T04:16:12Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3248262404)
- `2025-09-20T04:34:27Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3248277667)
- `2025-09-20T04:38:15Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3248279613)
- `2025-09-20T04:39:49Z` `COMMENTED` by `pauleonix` (https://github.com/NVIDIA/cccl/pull/5780#pullrequestreview-3248282474)
- ... 38 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cub/cub/block/block_load_to_shared.cuh`: 72 inline comment(s)
- `cub/test/catch2_test_block_load_to_shared.cu`: 20 inline comment(s)

## High-Signal Discussion

- `2025-09-22T13:45:14Z` `inline` by `pauleonix` `cub/test/catch2_test_block_load_to_shared.cu`; signals: alignment, block, correctness, perf, performance; excerpt: "Ah yeah right, I was thinking of the higher alignment that you needed in transform, but that was only for performance, not for correctness." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2368487850)
- `2025-09-22T13:11:10Z` `inline` by `pauleonix` `cub/cub/block/block_load_to_shared.cuh`:211; signals: benchmark, block, hopper, tma; excerpt: "Do you have numbers that using LDGSTS is significantly better than UBLKCP on Hopper for relevant work loads? My understand is that UBLKCP is ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2368325055)
- `2025-09-29T16:28:00Z` `inline` by `pauleonix` `cub/cub/block/block_load_to_shared.cuh`:120; signals: block, perf, performance, warp; excerpt: "Yeah, it seems like this is problematic (previous implementation had this issue as well as I did not need 32 threads for peeling and ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2388565697)
- `2025-09-22T13:33:53Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_block_load_to_shared.cu`; signals: aligned, block, memory, shared memory; excerpt: "Dynamic shared memory is 16B aligned by default, nothing fancy needed I guess." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2368428927)
- `2025-09-15T14:43:59Z` `inline` by `pauleonix` `cub/test/catch2_test_block_load_to_shared.cu`:28; signals: block, memory, shared memory; excerpt: "But we want to support using dynamic shared memory like you do in DeviceTransform. Do we really want to have different constructors for that?" (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2349247440)
- `2025-09-16T17:18:09Z` `inline` by `pauleonix` `cub/test/catch2_test_block_load_to_shared.cu`:28; signals: block, memory, shared memory; excerpt: "Added it to avoid having to use the static member functions (with template) when using static shared memory." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2353161841)
- `2025-09-19T08:27:14Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load_to_shared.cuh`:61; signals: alignment, block, hopper; excerpt: "We may know that Hopper may benefit from 128 byte alignment, but the effect is minor and not worth putting in user side documentation ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2362163692)
- `2025-09-19T08:30:50Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load_to_shared.cuh`:68; signals: block, ptx, tma; excerpt: "I am a bit torn. I think that in public documentation we should rather refer to instructions in PTX, because that's well documented. I ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2362172181)
- `2025-09-19T08:53:09Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load_to_shared.cuh`:162; signals: block, compile, ptx; excerpt: "We have at least PTX 8.0 since CTK 12.0. Also, if we didn't, then the block load algorithm would compile and not work." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2362223328)
- `2025-09-19T09:30:22Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load_to_shared.cuh`:312; signals: aligned, block, hang; excerpt: "Critical: the src pointer needs to be aligned up, otherwise it goes out of bounds Requires further changes below and a peeling loop for ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2362311598)
- `2025-09-19T09:42:31Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_block_load_to_shared.cu`; signals: block, memory, shared memory; excerpt: "Please also add a test where the block load is used using dynamic shared memory. This way we can validate the design as well." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2362339253)
- `2025-09-20T06:08:07Z` `inline` by `pauleonix` `cub/test/catch2_test_block_load_to_shared.cu`:98; signals: block, cuda, kernel; excerpt: "Are you mixing up this PR with the one on DeviceMerge? Because we can't initialize a cuda::std::span with an iterator. I could get rid ..." (https://github.com/NVIDIA/cccl/pull/5780#discussion_r2365344224)
