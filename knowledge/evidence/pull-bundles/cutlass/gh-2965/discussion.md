# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2965](https://github.com/NVIDIA/cutlass/pull/2965)
- Source page: `sources/prs/cutlass/PR-2965.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2965`
- Generated at: `2026-05-20T15:21:24.368639+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-19T08:13:22Z`
- Merged: `2026-01-23T07:56:53Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: HydraQYH, Junkai-Wu
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-20T01:42:39Z` `APPROVED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2965#pullrequestreview-3680014061)
- `2026-01-22T07:12:21Z` `COMMENTED` by `Junkai-Wu` (https://github.com/NVIDIA/cutlass/pull/2965#pullrequestreview-3690953931)
- `2026-01-22T07:22:48Z` `COMMENTED` by `HydraQYH` (https://github.com/NVIDIA/cutlass/pull/2965#pullrequestreview-3690985330)

## Inline Comment Hotspots

- `include/cutlass/gemm/collective/sm90_mma_array_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-22T07:12:21Z` `inline` by `Junkai-Wu` `include/cutlass/gemm/collective/sm90_mma_array_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:216; signals: block, cute, cutlass, fp8, gemm, pipeline, sm90, tma; excerpt: "Please use cute::conditional t here since using std:: here will break one of our internal pipelines." (https://github.com/NVIDIA/cutlass/pull/2965#discussion_r2715609841)
- `2026-01-22T07:22:48Z` `inline` by `HydraQYH` `include/cutlass/gemm/collective/sm90_mma_array_tma_gmma_ss_warpspecialized_fp8_blockwise_scaling.hpp`:216; signals: block, cutlass, fp8, gemm, sm90, tma, warp; excerpt: "Done." (https://github.com/NVIDIA/cutlass/pull/2965#discussion_r2715638363)
