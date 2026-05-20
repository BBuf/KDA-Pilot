# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7676](https://github.com/NVIDIA/cccl/pull/7676)
- Source page: `sources/prs/cccl-cub/PR-7676.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7676`
- Generated at: `2026-05-20T15:20:14.603411+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-13T23:23:10Z`
- Merged: `2026-03-17T21:40:40Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 38 (approved=1, commented=37)
- Inline review comments: 54
- Review threads observed: 30
- Resolved/outdated thread markers: resolved=28, outdated=20
- Human participants with discussion text: fbusato, miscco, oleksandr-pavlyk, pciolkosz
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-24T18:44:18Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3849883030)
- `2026-02-24T19:26:39Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3850084856)
- `2026-03-11T09:55:58Z` `COMMENTED` by `miscco` - Fiirst pass of comments. In general, please add a bit more spacing into the functions, so that different ... (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3928103556)
- `2026-03-11T13:16:38Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3929531584)
- `2026-03-11T14:14:08Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3929914319)
- `2026-03-11T14:14:22Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3929915882)
- `2026-03-11T14:26:50Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930008454)
- `2026-03-11T14:33:48Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930059616)
- `2026-03-11T14:39:25Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930102993)
- `2026-03-11T14:49:11Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930176230)
- `2026-03-11T14:49:53Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930181250)
- `2026-03-11T14:52:47Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930201309)
- `2026-03-11T15:06:32Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930315532)
- `2026-03-11T16:19:38Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3930837762)
- `2026-03-11T16:52:50Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931061634)
- `2026-03-11T18:54:53Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931781391)
- `2026-03-11T18:58:27Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931805808)
- `2026-03-11T19:02:18Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931830354)
- `2026-03-11T19:03:34Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931838951)
- `2026-03-11T19:14:47Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3931920600)
- `2026-03-11T19:43:03Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3932093293)
- `2026-03-11T19:51:20Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3932155228)
- `2026-03-11T20:05:39Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3932232591)
- `2026-03-11T20:05:53Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/7676#pullrequestreview-3932233879)
- ... 14 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`: 17 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/mdspan_to_raw_tensor.cuh`: 7 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/memcpy_batch_tiles.cuh`: 7 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/mdspan_d2h_h2d.cuh`: 6 inline comment(s)
- `libcudacxx/include/cuda/__driver/driver_api.h`: 6 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/simplify_paired.cuh`: 4 inline comment(s)
- `cudax/include/cuda/experimental/__copy/mdspan_d2h_h2d.cuh`: 2 inline comment(s)
- `libcudacxx/include/cuda/__mdspan/traits.h`: 2 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/types.cuh`: 2 inline comment(s)
- `cudax/include/cuda/experimental/__copy_bytes/abs_integer.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-24T18:44:18Z` `inline` by `oleksandr-pavlyk` `cudax/include/cuda/experimental/__copy/mdspan_d2h_h2d.cuh`:134; signals: coalesc, cuda, cute, layout; excerpt: "It appears src2 and dst2 are unused. I suspect everywhere from line 134 to the end of this functions src1 and dst1 should be ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2848941807)
- `2026-03-13T20:35:12Z` `inline` by `pciolkosz` `libcudacxx/include/cuda/__driver/driver_api.h`:354; signals: cuda, hang, perf, performance; excerpt: "I think we should pass the stream as is to the driver and then only if the call fails, we can check if this ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2933650003)
- `2026-03-11T16:52:50Z` `inline` by `oleksandr-pavlyk` `cudax/include/cuda/experimental/__copy_bytes/memcpy_batch_tiles.cuh`:84; signals: cuda, perf, tile; excerpt: "This code performs integral division and modular operation even for 1D arrays, where coord = static cast ( i); could be used. Can this ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2919679342)
- `2026-03-11T19:51:20Z` `inline` by `oleksandr-pavlyk` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:187; signals: compile, cuda, layout; excerpt: "I tried adding a test to cover such case. Test source code The test compiles when added at the bottom of "cudax/test/copy bytes/mdspan d2h ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2920641938)
- `2026-03-13T19:08:22Z` `inline` by `oleksandr-pavlyk` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:187; signals: cuda, layout, race; excerpt: "I meant the source mdspan needs to support overlapping mappings, but the destination mapping must be unique to avoid race condition. I did merge ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2933260055)
- `2026-03-11T09:50:34Z` `inline` by `miscco` `cudax/include/cuda/experimental/__copy_bytes/memcpy_batch_tiles.cuh`:171; signals: cuda, tile, vector; excerpt: "Nitpick: This is a heavy use for std::vector consider using ::cuda::std::get temporary buffer" (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2917175062)
- `2026-03-11T20:14:49Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy_bytes/simplify_paired.cuh`:82; signals: cuda, perf, performance; excerpt: "that's a good idea. Sorted strides of source tensors could improve performance" (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2920760291)
- `2026-03-11T14:39:25Z` `inline` by `oleksandr-pavlyk` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:109; signals: cuda, hang; excerpt: "The implementation check for strictly ascending ordering. Either update the comment, or change the implementation to use cudax:: abs integer( a) <= cudax:: abs ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2918820156)
- `2026-03-11T18:58:27Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:168; signals: compile, cuda; excerpt: "rank() 0 is important to avoid compile-time errors. Secondly, even without compile errors, it saves compile time" (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2920353000)
- `2026-03-11T20:26:29Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:187; signals: cuda, layout; excerpt: "I didn't know that this is possible in NumPy. The new condition makes sense. I will add the test case. Related to layout stride.h:308: ..." (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2920821986)
- `2026-03-11T20:34:54Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:187; signals: cuda, layout; excerpt: "@oleksandr-pavlyk do you think it makes sense to enable interleaved layouts for destination tensors? this implies overlapping" (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2920861227)
- `2026-03-13T19:13:26Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy_bytes/tensor_query.cuh`:187; signals: cuda, layout; excerpt: "uhmm, weird. The check is only on the destination. Anyway, I will open a new PR for layout stride relaxed + your test" (https://github.com/NVIDIA/cccl/pull/7676#discussion_r2933280760)
