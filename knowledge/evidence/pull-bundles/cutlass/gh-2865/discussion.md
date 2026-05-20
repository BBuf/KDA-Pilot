# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2865](https://github.com/NVIDIA/cutlass/pull/2865)
- Source page: `sources/prs/cutlass/PR-2865.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2865`
- Generated at: `2026-05-20T15:21:22.874571+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T11:48:34Z`
- Merged: `2025-12-18T00:51:39Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 19
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=11, outdated=11
- Human participants with discussion text: HydraQYH, Junkai-Wu
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-10T05:15:16Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3560748281)
- `2025-12-10T05:20:12Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3560759993)
- `2025-12-10T05:25:02Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3560772558)
- `2025-12-10T14:28:39Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3562832869)
- `2025-12-10T14:34:21Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3562860359)
- `2025-12-11T00:44:15Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3565146887)
- `2025-12-11T00:49:59Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3565175364)
- `2025-12-11T00:50:10Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3565175769)
- `2025-12-11T01:27:53Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3565246178)
- `2025-12-11T01:28:01Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3565246365)
- `2025-12-17T09:37:17Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3586800721)
- `2025-12-17T15:26:42Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3588285832)
- `2025-12-18T00:51:12Z` `APPROVED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2865#pullrequestreview-3590242051)

## Inline Comment Hotspots

- `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`: 10 inline comment(s)
- `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_cooperative.hpp`: 5 inline comment(s)
- `include/cutlass/gemm/kernel/sm100_tile_scheduler.hpp`: 2 inline comment(s)
- `include/cutlass/gemm/kernel/sm100_tile_scheduler_stream_k.hpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-10T05:20:11Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:156; signals: block, cutlass, gemm, kernel, sm120, sm90, tile, tma; excerpt: "I'm worried that MainloopSm120TmaWarpSpecializedBlockScaled is not the only dispatch policy that needs to be excluded in above is last tile. For example, there is ..." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2605234652)
- `2025-12-10T05:25:02Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:153; signals: block, cutlass, gemm, kernel, sm120, sm90, tma, warp; excerpt: "Also the meaning of the struct name is not very clear. If it needs to bypass sm120 blockscaled kernel, it should be named at ..." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2605245261)
- `2025-12-10T14:34:21Z` `inline` by `HydraQYH` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:156; signals: block, cutlass, gemm, kernel, sm120, sm90, tile, tma; excerpt: "MainloopSm120ArrayTmaWarpSpecializedBlockScaled will use the following two Mainloops: - - These two Mainloops use GroupScheduler and do not call is last tile. So it doesn't ..." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2606910324)
- `2025-12-10T05:15:15Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:153; signals: aligned, cutlass, gemm, kernel, sm90, tma, warp; excerpt: "The struct name here is not aligned with the coding style of cutlass. Please use camel case naming convention." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2605226145)
- `2025-12-17T09:36:42Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:803; signals: cutlass, gemm, kernel, sm120, sm90, tma, warp; excerpt: "Add if constexpr (!IsSm120Family) condition here." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2626294562)
- `2025-12-10T14:28:39Z` `inline` by `HydraQYH` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:153; signals: cutlass, gemm, kernel, sm90, tma, warp; excerpt: "This code is copied from: So the code of the main branch also has this typo, and I think you need to fix it ..." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2606888949)
- `2025-12-11T00:44:15Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:153; signals: cutlass, gemm, kernel, sm90, tma, warp; excerpt: "Thanks for catching this. Will try to refactor it in future." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2608729712)
- `2025-12-17T15:26:42Z` `inline` by `HydraQYH` `include/cutlass/gemm/kernel/sm90_gemm_tma_warpspecialized_pingpong.hpp`:803; signals: cutlass, gemm, kernel, sm90, tma, warp; excerpt: "Done." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2627513112)
- `2025-12-16T09:29:25Z` `issue` by `Junkai-Wu`; signals: block, hang, kernel, pipeline, sm120, tile; excerpt: "@HydraQYH The internal pipeline still fails. After checking, I found all sm120 kernels should not call the is last tile function, not just sm120 ..." (https://github.com/NVIDIA/cutlass/pull/2865#issuecomment-3659602772)
- `2025-12-11T00:49:59Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm100_tile_scheduler.hpp`:454; signals: cutlass, gemm, kernel, sm100, tile; excerpt: "Please remove this TODO comment. We are trying to avoid adding TODO comment in the public codes. Besides, there is nothing else to do ..." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2608747243)
- `2025-12-11T00:50:09Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/kernel/sm100_tile_scheduler_stream_k.hpp`:233; signals: cutlass, gemm, kernel, sm100, tile; excerpt: "Same as above." (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2608747606)
- `2025-12-11T01:27:53Z` `inline` by `HydraQYH` `include/cutlass/gemm/kernel/sm100_tile_scheduler.hpp`:454; signals: cutlass, gemm, kernel, sm100, tile; excerpt: "Done" (https://github.com/NVIDIA/cutlass/pull/2865#discussion_r2608806080)
