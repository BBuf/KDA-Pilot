# PR Discussion Digest

- Source PR: [sgl-project/sglang#25532](https://github.com/sgl-project/sglang/pull/25532)
- Source page: `sources/prs/sglang/PR-25532.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25532`
- Generated at: `2026-05-20T15:29:50.229323+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-17T15:38:51Z`
- Merged: `2026-05-20T05:20:37Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 24 (approved=2, commented=22)
- Inline review comments: 24
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=12, outdated=6
- Human participants with discussion text: BBuf, kaixih, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-17T15:40:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUTLASS 3.x based FP8 GEMM implementation for SM90, featuring custom ... (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4305666791)
- `2026-05-18T02:31:59Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4306897351)
- `2026-05-18T02:32:55Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4306899230)
- `2026-05-18T02:37:07Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4306907786)
- `2026-05-18T02:39:46Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4306914183)
- `2026-05-18T02:40:31Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4306915682)
- `2026-05-19T02:09:03Z` `COMMENTED` by `BBuf` - Can we move it to jit kernel? We can use flashinfer cutlass. (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4315206777)
- `2026-05-19T13:06:51Z` `COMMENTED` by `BBuf` - Please clean used code such as sgl-kernel/csrc/cutlass extensions/epilogue/broadcast load epilogue array c3x.hpp (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319188942)
- `2026-05-19T13:17:59Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319280845)
- `2026-05-19T13:36:38Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319455216)
- `2026-05-19T13:41:04Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319491150)
- `2026-05-19T13:41:58Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319498001)
- `2026-05-19T13:43:30Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319510258)
- `2026-05-19T13:47:04Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319540528)
- `2026-05-19T14:28:06Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4319901222)
- `2026-05-19T14:43:42Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4320039969)
- `2026-05-19T14:59:37Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4320185210)
- `2026-05-19T15:03:49Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4320220620)
- `2026-05-19T15:09:44Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4320268631)
- `2026-05-19T15:10:37Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4320275622)
- `2026-05-19T19:30:08Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4322458884)
- `2026-05-20T00:06:36Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4324226663)
- `2026-05-20T03:14:13Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4324901015)
- `2026-05-20T03:37:11Z` `APPROVED` by `kaixih` (https://github.com/sgl-project/sglang/pull/25532#pullrequestreview-4324975140)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`: 14 inline comment(s)
- `sgl-kernel/csrc/cutlass_extensions/epilogue/broadcast_load_epilogue_array_c3x.hpp`: 4 inline comment(s)
- `sgl-kernel/csrc/gemm/fp8_gemm_kernel.cu`: 2 inline comment(s)
- `sgl-kernel/tests/test_fp8_gemm.py`: 2 inline comment(s)
- `sgl-kernel/benchmark/bench_fp8_gemm_swap_ab.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-19T13:36:38Z` `inline` by `BBuf` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:445; signals: accuracy, aligned, cutlass, fp8, gemm, kernel, regression, sm90; excerpt: "For M64 N1280 with TileN=16 and ClusterShape in swap mode, the number of CTAs along kernel-N is ceil(M orig / 16) ∈ {2, 3, ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3266711879)
- `2026-05-19T14:43:41Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:445; signals: accuracy, bf16, cutlass, fp8, gemm, kernel, sm90, tile; excerpt: "Good question. Both verified: (a) gemm op.can implement(args) returns Status::kSuccess for M orig ∈ {17, 20, 33, 48} with N ≤ 1280 routing to ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3267203056)
- `2026-05-20T03:14:13Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:519; signals: bf16, cuda, cudagraph, cutlass, fp8, gemm, h200, kernel; excerpt: "Ran bench fp8 gemm on Llama-3.3-70B-Instruct shapes ((K, N) = (8192, 10240) / (8192, 8192) / (8192, 57344) / (28672, 8192)) at M ∈ ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3271010974)
- `2026-05-18T02:39:46Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:371; signals: correctness, cutlass, fp8, gemm, hang, kernel, sm90; excerpt: "Acknowledged. Empirically the cluster kernel launches cleanly (60 correctness tests pass) and the bucket beats main by 23-29% in the M<=16 N<=1280 region. Keep ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3256044834)
- `2026-05-19T19:29:53Z` `inline` by `kaixih` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:519; signals: benchmark, cutlass, fp8, gemm, kernel, sm90, tile; excerpt: "So, for all m 128, we now use Cutlass3xGemmDefault. But main had separate SM90 configs for 128 < m <= 256 and 256 < ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3269055979)
- `2026-05-19T13:17:59Z` `inline` by `BBuf` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:499; signals: accuracy, cutlass, fp8, gemm, kernel, sm90; excerpt: "The argument order (b scales, a scales) vs (a scales, b scales) is currently selected at the dispatcher call site based on whether the ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3266574624)
- `2026-05-19T13:41:04Z` `inline` by `BBuf` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:279; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Nits: M16 N8192 (and M32 N8192, M64 N8192) is misleading — the dispatcher routes any n 1280 here, not just n=8192. Could you rename ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3266741999)
- `2026-05-19T14:28:05Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:499; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Good catch. Thanks. This is fixed now. Added a cutlass gemm caller sm90 fp8 scaled wrapper that takes scales in the canonical (a scales, ..." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3267079071)
- `2026-05-18T02:37:07Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:521; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Fixed." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3256038636)
- `2026-05-19T13:41:58Z` `inline` by `BBuf` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:437; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Why we choose 1280? Any comment can be added?" (https://github.com/sgl-project/sglang/pull/25532#discussion_r3266748127)
- `2026-05-19T14:59:37Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:279; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Fine. Updated and renamed." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3267318892)
- `2026-05-19T15:03:49Z` `inline` by `yuan-luo` `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh`:437; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "Added comment for choosing 1280." (https://github.com/sgl-project/sglang/pull/25532#discussion_r3267348193)
