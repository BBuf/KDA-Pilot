# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9838](https://github.com/NVIDIA/TensorRT-LLM/pull/9838)
- Source page: `sources/prs/tensorrt-llm/PR-9838.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9838`
- Generated at: `2026-05-20T15:19:26.782904+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T08:13:01Z`
- Merged: `2026-01-06T02:16:42Z`

## Discussion Counts

- Issue comments: 48
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 23
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=5
- Human participants with discussion text: StudyingShao, coderabbitai, djns99, rosenrodt, tensorrt-cicd, yumin066
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T08:18:36Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3556047338)
- `2025-12-19T01:31:32Z` `APPROVED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3595994504)
- `2025-12-19T01:37:24Z` `COMMENTED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596098420)
- `2025-12-19T01:40:00Z` `COMMENTED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596114632)
- `2025-12-19T01:43:54Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596137177)
- `2025-12-19T01:51:55Z` `COMMENTED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596183911)
- `2025-12-19T02:46:36Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596488000)
- `2025-12-19T02:55:08Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596530257)
- `2025-12-19T02:55:20Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596530852)
- `2025-12-19T02:57:28Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596537230)
- `2025-12-19T03:13:26Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3596590272)
- `2025-12-19T07:35:55Z` `COMMENTED` by `yumin066` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3597361041)
- `2025-12-22T06:57:13Z` `COMMENTED` by `StudyingShao` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3602824728)
- `2025-12-22T08:29:29Z` `COMMENTED` by `yumin066` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3603112239)
- `2025-12-25T07:13:58Z` `COMMENTED` by `yumin066` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3611946106)
- `2025-12-30T06:39:16Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3617394021)
- `2025-12-30T06:40:57Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3617395917)
- `2025-12-30T10:10:13Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3617808505)
- `2026-01-05T04:18:41Z` `APPROVED` by `StudyingShao` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3625447786)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`: 11 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`: 7 inline comment(s)
- `cpp/tests/unit_tests/kernels/mixtureOfExpertsTest.cu`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-09T08:18:36Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, block, compile, cuda, cutlass, dtype, epilogue; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#pullrequestreview-3556047338)
- `2025-12-19T01:37:24Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2259; signals: block, cutlass, gemm, kernel, moe, nan, perf, tensorrt; excerpt: "FYI it was pointed out to me that this last block of padding might not actually be required. All the associated data is OOB ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633258914)
- `2025-12-19T01:51:55Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2124; signals: cache, cutlass, gemm, kernel, moe, perf, register, tensorrt; excerpt: "How much does this improve perf compared to the old version? Since we aren't staging in smem/registers afaict. I would have assumed we would ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633283723)
- `2025-12-09T08:18:33Z` `issue` by `coderabbitai`; signals: alignment, cutlass, dtype, epilogue, fp4, fp8, gemm, hang; excerpt: "📝 Walkthrough Walkthrough The changes introduce epilogue fusion mode configuration to MOE GEMM kernels. Updates replace gating condition flags (use w4 groupwise → use ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#issuecomment-3630939081)
- `2025-12-18T14:54:59Z` `issue` by `rosenrodt`; signals: benchmark, block, fp8, hang, hopper, kernel, moe, perf; excerpt: "@djns99 @StudyingShao Need your help reviewing this PR. @yumin066 added the finalize fusion for W4A8 MoE, and enable single-kernel topk routing for W4A8 MoE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#issuecomment-3670708180)
- `2025-12-19T02:46:36Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2124; signals: compile, cutlass, gemm, hang, kernel, moe, tensorrt; excerpt: "I did not measure before and after for this change, so all the gain L1 or L2 reuse was my wishful thinking :) TBH ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633388678)
- `2025-12-25T07:13:58Z` `inline` by `yumin066` `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`:830; signals: cutlass, dtype, fp4, h100, kernel, moe, tensorrt; excerpt: "H100 PCIe-PyTorch-3.unittest. torch.modules.test fused moe.test fused moe wfp4a16[CUTLASS-2880-dtype0] failed when I removed !use wfp4a16. I think the reason is finalize fusion kernel for wfp4a16 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2646656114)
- `2025-12-19T01:10:45Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2095; signals: block, cutlass, gemm, kernel, moe, tensorrt; excerpt: "Would it make more sense to use a block shape of dims3(1, ACTIVATION THREADS PER BLOCK, 1) that way we can use: int64 t ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633211092)
- `2025-12-19T02:57:28Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2095; signals: cutlass, gemm, hang, kernel, moe, tensorrt; excerpt: "Good suggestion. I can make the changes locally and push them opportunistically when we need a rebase or a bug fix. I'd like to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633406778)
- `2025-12-19T03:13:26Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:3875; signals: autotune, cutlass, gemm, kernel, moe, tensorrt; excerpt: "Good point. I haven't considered autotuner yet because prequant fusion hardcoded as part of W4A8 AWQ recipe hence not tunable. Or do you mean ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633428820)
- `2025-12-19T01:19:26Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:3875; signals: autotune, cutlass, gemm, kernel, moe, tensorrt; excerpt: "Does the autotuner need updated to enable this?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633222782)
- `2025-12-19T02:55:20Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2259; signals: cutlass, gemm, hang, kernel, moe, tensorrt; excerpt: "Good to know. But I would like to keep changes to a minimum if you do not mind :)" (https://github.com/NVIDIA/TensorRT-LLM/pull/9838#discussion_r2633402829)
