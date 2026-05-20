# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#2037](https://github.com/NVIDIA/cutlass/pull/2037)
- Source page: `sources/prs/cutlass/PR-2037.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-2037`
- Generated at: `2026-05-20T15:21:13.884115+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-13T07:26:59Z`
- Merged: `2025-01-31T18:51:28Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Hongbosherlock, Maximilianxu, ginowu, hwu36, ll2088, manishucsd, mnicely, soundOfDestiny, yizhang2077, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 12

## Review Decisions

- `2025-01-29T20:03:29Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/2037#pullrequestreview-2547127098)
- `2025-01-30T01:27:50Z` `COMMENTED` by `soundOfDestiny` (https://github.com/NVIDIA/cutlass/pull/2037#pullrequestreview-2582729671)
- `2025-01-31T18:51:21Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/2037#pullrequestreview-2587551259)

## Inline Comment Hotspots

- `examples/65_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/CMakeLists.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-01-30T01:27:50Z` `inline` by `soundOfDestiny` `examples/65_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/CMakeLists.txt`:36; signals: block, fp8, gemm, hang, hopper, warp; excerpt: "new example new example number? yeah I've changed it to example number 67" (https://github.com/NVIDIA/cutlass/pull/2037#discussion_r1934890769)
- `2025-01-13T16:10:32Z` `inline` by `manishucsd` `examples/65_hopper_fp8_warp_specialized_gemm_with_blockwise_scaling/CMakeLists.txt`:36; signals: block, fp8, gemm, hopper, warp; excerpt: "new example new example number?" (https://github.com/NVIDIA/cutlass/pull/2037#discussion_r1913444053)
- `2025-01-17T08:15:38Z` `issue` by `zhyncs`; signals: block, cutlass, fp8; excerpt: "Hi @hwu36 This PR is from the DeepSeek Team. Could you help review and merge it? The SGLang team wants to implement block-wise FP8 ..." (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2597667903)
- `2025-01-21T06:32:46Z` `issue` by `ll2088`; signals: block, cutlass, fp8; excerpt: "Hi @hwu36 This PR is from the DeepSeek Team. Could you help review and merge it? The SGLang team wants to implement block-wise FP8 ..." (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2603773361)
- `2025-01-21T14:41:31Z` `issue` by `soundOfDestiny`; signals: cutlass, memory, shared memory; excerpt: "returned error: invalid argument Got cutlass error: Error Internal at: 673 The issue of incorrect calculation of shared memory size has appeared since It ..." (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2604922501)
- `2025-01-21T06:44:26Z` `issue` by `zhyncs`; signals: block, cutlass; excerpt: "@ll2088 Our current open source version has been referenced and adapted by other projects, including vLLM and LightLLM. The version developed based on CUTLASS ..." (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2603787690)
- `2025-01-21T06:51:27Z` `issue` by `ll2088`; signals: block, cutlass; excerpt: "@ll2088 Our current open source version has been referenced and adapted by other projects, including vLLM and LightLLM. The version developed based on CUTLASS ..." (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2603796557)
- `2025-01-21T10:02:08Z` `issue` by `ll2088`; signals: compile, tile; excerpt: "![image]( @soundOfDestiny using TileShape = Shape ; why does it not work? compile problem occurs. And why does ScaleMsPerTile = 128 not work? @soundOfDestiny" (https://github.com/NVIDIA/cutlass/pull/2037#issuecomment-2604232750)
