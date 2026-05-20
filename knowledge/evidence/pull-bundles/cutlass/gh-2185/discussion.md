# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2185](https://github.com/NVIDIA/cutlass/pull/2185)
- Source page: `sources/prs/cutlass/PR-2185.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2185`
- Generated at: `2026-05-20T15:21:17.191344+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-20T04:19:29Z`
- Merged: `2025-03-21T05:52:24Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 14
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=0
- Human participants with discussion text: IonThruster, hwu36, manishucsd, thakkarV, yzhaiustc
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-03-21T03:35:42Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704629904)
- `2025-03-21T03:43:43Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704650874)
- `2025-03-21T03:51:30Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704657903)
- `2025-03-21T03:54:32Z` `COMMENTED` by `yzhaiustc` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704660364)
- `2025-03-21T03:55:44Z` `COMMENTED` by `yzhaiustc` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704662243)
- `2025-03-21T03:56:29Z` `COMMENTED` by `yzhaiustc` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704662806)
- `2025-03-21T05:01:54Z` `COMMENTED` by `thakkarV` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704743285)
- `2025-03-21T05:06:28Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704748464)
- `2025-03-21T05:45:23Z` `COMMENTED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704793391)
- `2025-03-21T05:46:39Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704794879)
- `2025-03-21T05:51:20Z` `COMMENTED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2185#pullrequestreview-2704800571)

## Inline Comment Hotspots

- `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`: 8 inline comment(s)
- `include/cutlass/gemm/collective/sm100_mma_warpspecialized.hpp`: 4 inline comment(s)
- `include/cutlass/gemm/collective/sm100_mma_array_warpspecialized_emulated.hpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-21T03:43:39Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm100_mma_warpspecialized.hpp`:697; signals: block, cutlass, gemm, sm100, tmem, warp; excerpt: "I am trying to to think this through, in the absence of this for the first iteration what could go wrong where accumulators are ..." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006795841)
- `2025-03-21T03:22:53Z` `inline` by `manishucsd` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:341; signals: block, gemm, hang, layout, tile; excerpt: "Can you elaborate what these numbers mean? For eg. I understand what 128B, 64B, 32B swizzle mean. Does this change the TileK for the ..." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006782832)
- `2025-03-21T03:51:26Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm100_mma_array_warpspecialized_emulated.hpp`:1095; signals: bf16, cutlass, gemm, sm100, warp; excerpt: "Does this file only emulates F32-precision with 9xBF16 or does emulate any other computation too?" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006800357)
- `2025-03-21T05:45:23Z` `inline` by `hwu36` `include/cutlass/gemm/collective/sm100_mma_array_warpspecialized_emulated.hpp`:1095; signals: bf16, cutlass, gemm, sm100, warp; excerpt: "just bf16x9" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006887293)
- `2025-03-21T03:26:16Z` `inline` by `manishucsd` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:740; signals: block, gemm, perf, performance; excerpt: "how is enable deep profiling different from exhaustive performance search? I will just use the same name enable exhaustive search. This should be a ..." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006784825)
- `2025-03-21T05:51:20Z` `inline` by `hwu36` `include/cutlass/gemm/collective/sm100_mma_warpspecialized.hpp`:697; signals: cutlass, gemm, sm100, warp; excerpt: "@mihir-awatramani" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006891999)
- `2025-03-21T03:56:29Z` `inline` by `yzhaiustc` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:740; signals: block, gemm, hang; excerpt: "Thanks for suggestions :-) We can change the variable naming in next version." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006803559)
- `2025-03-21T03:24:18Z` `inline` by `manishucsd` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:344; signals: block, gemm; excerpt: "Is there a reason to not have {1, 2, 1}, {1, 4, 1}, {2, 4, 1}, {1, 8, 1} in this list, give that ..." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006783602)
- `2025-03-21T03:55:44Z` `inline` by `yzhaiustc` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:344; signals: block, gemm; excerpt: "there's no specific reason. we just don't want to make the search time too long in the current version." (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006803144)
- `2025-03-21T03:54:32Z` `inline` by `yzhaiustc` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:341; signals: block, gemm; excerpt: "@jackkosaian would you please help to elaborate the meaning of swizzle sizes?" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006801969)
- `2025-03-21T05:01:54Z` `inline` by `thakkarV` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:341; signals: block, gemm; excerpt: "@manishucsd this is the L2 swizzle count in terms of number of CTAs" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006856037)
- `2025-03-21T05:06:28Z` `inline` by `manishucsd` `tools/profiler/src/block_scaled_gemm_operation_profiler.cu`:341; signals: block, gemm; excerpt: "ok. that makes sense now. thanks!" (https://github.com/NVIDIA/cutlass/pull/2185#discussion_r2006859250)
