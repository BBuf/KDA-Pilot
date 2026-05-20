# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#1413](https://github.com/NVIDIA/cutlass/pull/1413)
- Source page: `sources/prs/cutlass/PR-1413.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-1413`
- Generated at: `2026-05-20T15:21:10.042936+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-03-19T14:49:39Z`
- Merged: `2024-08-30T03:11:06Z`

## Discussion Counts

- Issue comments: 37
- Review submissions: 17 (approved=2, commented=15)
- Inline review comments: 16
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Hongbosherlock, alexsamardzic, andrewor14, hwu36, lezcano, manishucsd, zkf331
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2024-03-21T09:33:30Z` `COMMENTED` by `lezcano` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-1951436943)
- `2024-03-21T09:52:06Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-1951509342)
- `2024-08-14T06:47:54Z` `APPROVED` by `manishucsd` - Thank you for working on this. Apologies for a delayed review. LGTM. Over to NVIDIA/CUTLASS (cc: @hwu36 ) ... (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2237267835)
- `2024-08-14T06:51:42Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2237303899)
- `2024-08-14T11:35:34Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2237899553)
- `2024-08-14T11:39:50Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2237912657)
- `2024-08-14T14:32:59Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2238375866)
- `2024-08-15T21:01:52Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2241323193)
- `2024-08-15T22:10:40Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2241434291)
- `2024-08-16T09:55:06Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2242360567)
- `2024-08-16T20:41:31Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2243516434)
- `2024-08-17T06:11:28Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2243976229)
- `2024-08-19T07:35:09Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2244809932)
- `2024-08-20T20:18:37Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2249019959)
- `2024-08-20T23:30:12Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2249274530)
- `2024-08-29T16:19:52Z` `COMMENTED` by `alexsamardzic` - Thanks for the fix! (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2269402895)
- `2024-08-30T03:10:59Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/1413#pullrequestreview-2270975057)

## Inline Comment Hotspots

- `python/cutlass_library/generator.py`: 11 inline comment(s)
- `include/cutlass/gemm/warp/mma_mixed_input_tensor_op.h`: 3 inline comment(s)
- `test/unit/gemm/device/gemm_universal_s4t_s8n_s32t_mixed_input_tensor_op_s32_sm80.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2024-03-22T15:40:23Z` `issue` by `alexsamardzic`; signals: alignment, compile, cutlass, gemm, hang, kernel, tile; excerpt: "Added generator support for S8/S4 and S4/S8. --- AFAIK, implementing generator support for given operation is not specifically documented, so I want to clarify ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2015366925)
- `2024-07-05T09:20:16Z` `issue` by `alexsamardzic`; signals: gemm, memory, perf, performance, register, shared memory, tile; excerpt: "When profiling a single GEMM, do you think the performance of s4/s8 will be better than that of of s8/s8? In my test s8/s8(int8 ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2210519252)
- `2024-06-03T13:33:47Z` `issue` by `Hongbosherlock`; signals: cutlass, gemm, hang, layout, tensorrt, warp; excerpt: "Thanks, I’m trying this, but it’s not going well currently. To make it clearer, what I want to do is exactly the following： Well, ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2145219985)
- `2024-08-14T11:35:34Z` `inline` by `alexsamardzic` `include/cutlass/gemm/warp/mma_mixed_input_tensor_op.h`:129; signals: cutlass, gemm, hang, register, warp; excerpt: "Yes, the shuffler is reused from F16xS8, namely in both cases, for each 32 bits loaded into a thread registers through ldmatrix, two groups ..." (https://github.com/NVIDIA/cutlass/pull/1413#discussion_r1716767117)
- `2024-08-14T14:32:59Z` `inline` by `manishucsd` `include/cutlass/gemm/warp/mma_mixed_input_tensor_op.h`:129; signals: cutlass, gemm, hang, kernel, warp; excerpt: "Yeah, the last time went in looking deep into 1190 I saw mainloop changes. Those changes will affect almost all the Ampere kernels. While ..." (https://github.com/NVIDIA/cutlass/pull/1413#discussion_r1717050034)
- `2024-08-15T21:01:52Z` `inline` by `alexsamardzic` `python/cutlass_library/generator.py`:2901; signals: cutlass, gemm, kernel, warp; excerpt: "There was a build issue after rebasing on the latest main: basically, OpMultiplyAddSaturate for MmaTensorOpPolicy in the specialization of struct DefaultMmaTensorOp (in include/cutlass/gemm/warp/default mma ..." (https://github.com/NVIDIA/cutlass/pull/1413#discussion_r1718987815)
- `2024-03-22T19:48:30Z` `issue` by `alexsamardzic`; signals: cutlass, epilogue, gemm, kernel; excerpt: "Hi @alexsamardzic, thanks for working on this. Just wanted to clarify, will this kernel support int4 grouped per channel weight quantization + int8 per ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2015799758)
- `2024-05-06T09:28:54Z` `issue` by `Hongbosherlock`; signals: cutlass, epilogue, gemm, kernel; excerpt: "Hi @alexsamardzic, thanks for working on this. Just wanted to clarify, will this kernel support int4 grouped per channel weight quantization + int8 per ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2095551792)
- `2024-05-08T13:11:32Z` `issue` by `alexsamardzic`; signals: cutlass, gemm, hang, hopper; excerpt: "I'm a beginner with Cutlass, I have on idea how to use my own constructed s4/s8 data to run this GEMM. Could you please ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2100545262)
- `2024-05-16T03:46:16Z` `issue` by `Hongbosherlock`; signals: cutlass, gemm, hang, hopper; excerpt: "I'm a beginner with Cutlass, I have on idea how to use my own constructed s4/s8 data to run this GEMM. Could you please ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2113971576)
- `2024-05-23T10:25:50Z` `issue` by `alexsamardzic`; signals: cutlass, epilogue, gemm, perf; excerpt: "Assuming that A is int8 and (M, K), B is int4 and (K, N), after GEMM: C = A·B, and C will be (M, ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2126757458)
- `2024-05-28T07:29:36Z` `issue` by `Hongbosherlock`; signals: cutlass, epilogue, gemm, perf; excerpt: "Assuming that A is int8 and (M, K), B is int4 and (K, N), after GEMM: C = A·B, and C will be (M, ..." (https://github.com/NVIDIA/cutlass/pull/1413#issuecomment-2134528390)
