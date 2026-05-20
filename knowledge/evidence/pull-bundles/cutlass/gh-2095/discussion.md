# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2095](https://github.com/NVIDIA/cutlass/pull/2095)
- Source page: `sources/prs/cutlass/PR-2095.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2095`
- Generated at: `2026-05-20T15:21:13.885890+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-10T05:30:35Z`
- Merged: `2025-02-28T03:39:29Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 17
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: LucasWilkinson, ProphetPeng, Skylion007, hwu36, manishucsd, qijiaxing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-02-25T09:41:44Z` `COMMENTED` by `ProphetPeng` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2640342919)
- `2025-02-25T15:16:33Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2641468831)
- `2025-02-25T21:50:52Z` `COMMENTED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2642549070)
- `2025-02-26T04:48:17Z` `COMMENTED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643064205)
- `2025-02-26T04:49:47Z` `COMMENTED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643065845)
- `2025-02-26T05:13:56Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643091893)
- `2025-02-26T05:18:43Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643096982)
- `2025-02-26T05:19:00Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643097256)
- `2025-02-26T06:12:56Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643152029)
- `2025-02-26T08:40:34Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643603303)
- `2025-02-26T08:43:44Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643612898)
- `2025-02-26T08:44:09Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643614176)
- `2025-02-26T08:54:17Z` `COMMENTED` by `LucasWilkinson` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2643645707)
- `2025-02-28T03:39:17Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2095#pullrequestreview-2649636210)

## Inline Comment Hotspots

- `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`: 14 inline comment(s)
- `examples/67_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/reference/host/gemm_with_groupwise_scaling.h`: 2 inline comment(s)
- `examples/67_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/67_hopper_fp8_warp_specialized_gemm_with_groupwise_scaling.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-25T15:16:33Z` `inline` by `LucasWilkinson` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:283; signals: block, cutlass, fp8, gemm, sm90, tile, tma, vector; excerpt: "currently this assumes full tiles in N and K so if using this for inference where activations may have partial tiles if you transpose ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1969993260)
- `2025-02-26T04:49:47Z` `inline` by `hwu36` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:610; signals: block, cutlass, fp8, gemm, sm90, tile, tma, warp; excerpt: "Maybe still using ScalePromotionInterval here, and move size (TileShape{}) / size (typename TiledMma::AtomShape MNK{} to can implement check?" (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970902445)
- `2025-02-26T05:13:56Z` `inline` by `LucasWilkinson` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:610; signals: block, compile, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "Hmm im not sure I see ScalePromotionInterval, what would be the motivation to not have this determined at compile time? it seems a bit ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970919816)
- `2025-02-26T05:54:02Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:150; signals: bf16, block, cutlass, fp8, gemm, kernel, perf, performance; excerpt: "Why is this restriction only for M and not for N? dim-M usually maps to batch count while dim-N will be model dimension, a ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970949776)
- `2025-02-26T06:07:27Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:492; signals: block, cutlass, fp8, gemm, layout, sm90, tile, tma; excerpt: "can you make sure that this copy if is issued by only 32 threads? The thread layout of shape 32 (created above) won't be ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970965605)
- `2025-02-26T06:12:52Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:610; signals: block, cutlass, fp8, gemm, sm90, tile, tma, warp; excerpt: "In anycase moving this as constexpr somewhere on the top will better for readability. static constexpr int ScalePromotionInterval = size (TileShape{}) / size (typename ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970971107)
- `2025-02-26T08:40:34Z` `inline` by `LucasWilkinson` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:372; signals: block, cutlass, fp8, gemm, hang, sm90, tma, warp; excerpt: "Im not sure, I didn't think this was a big deal since if you look at the in include/cutlass/gemm/collective/sm90 mma tma gmma rs warpspecialized ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1971162003)
- `2025-02-26T08:43:44Z` `inline` by `LucasWilkinson` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:150; signals: block, cutlass, fp8, gemm, perf, regression, sm90, tma; excerpt: "I was mostly just trying to keep it as close to the original as possible to minimize the chances of perf regressions, but I ..." (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1971166573)
- `2025-02-26T08:44:09Z` `inline` by `LucasWilkinson` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:150; signals: block, cutlass, fp8, gemm, sm90, tile, tma, warp; excerpt: "pushed an update that enables partial tiles in N" (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1971167250)
- `2025-02-26T06:08:40Z` `inline` by `manishucsd` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:372; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "Should TMA related tensor constructions be in lane predicate as before, no need for all the threads to construct this even in this implementation?" (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970966799)
- `2025-02-25T09:41:44Z` `inline` by `ProphetPeng` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:283; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "Is there any promblems when transpose A and transpose B?" (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1969382846)
- `2025-02-25T21:50:39Z` `inline` by `hwu36` `include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:444; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "wouldn't this be size(tBpB ScaleB) ?" (https://github.com/NVIDIA/cutlass/pull/2095#discussion_r1970593471)
