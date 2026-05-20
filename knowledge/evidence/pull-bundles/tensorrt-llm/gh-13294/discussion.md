# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13294](https://github.com/NVIDIA/TensorRT-LLM/pull/13294)
- Source page: `sources/prs/tensorrt-llm/PR-13294.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13294`
- Generated at: `2026-05-20T15:18:37.742356+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-21T22:09:29Z`
- Merged: `2026-04-21T22:59:31Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 12
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: brb-nv, coderabbitai, peihu-nv, tburt-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-21T22:16:25Z` `APPROVED` by `brb-nv` - LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#pullrequestreview-4151049943)
- `2026-04-21T22:26:00Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 12 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#pullrequestreview-4151085527)
- `2026-04-21T22:46:39Z` `APPROVED` by `tburt-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#pullrequestreview-4151152894)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingDeepSeek.cu`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingDeepSeek/launchCoopKernel.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingDeepSeek/launchMainKernel.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingLlama4.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingRenormalize.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingRenormalize/launchBlockKernel.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingRenormalize/RoutingRenormalizeCommon.cuh`: 1 inline comment(s)
- `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp`: 1 inline comment(s)
- `cpp/tests/unit_tests/kernels/routing/routingTest.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-21T22:26:00Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, bf16, block, compile, cute, dtype, fp4, fp8; excerpt: "Actionable comments posted: 12 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#pullrequestreview-4151085527)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp`:77; signals: bf16, block, dtype, fp8, kernel, moe, perf, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Keep the DeepSeekV3 FP32 check ahead of the use routing scales on input branch. With the new condition order, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613506)
- `2026-04-21T22:25:54Z` `issue` by `coderabbitai`; signals: block, compile, cute, dtype, failing, fp4, fp8, hang; excerpt: "📝 Walkthrough Walkthrough This PR refactors the MoE routing kernel architecture by introducing new DeepSeek and Renormalize routing implementations with modular launch wrappers, removing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#issuecomment-4292251131)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingLlama4.cu`:287; signals: block, cuda, gemm, kernel, moe, tensorrt, warp; excerpt: "⚠️ Potential issue 🔴 Critical The single-warp path releases PDL before the permuted-index buffers are ready. cudaTriggerProgrammaticLaunchCompletion() runs before Lines 320-359 populate mPtrExpandedIdxToPermutedIdx, mPtrPermutedIdxToExpandedIdx, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613489)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingDeepSeek/launchCoopKernel.cu`:221; signals: block, cuda, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Delay PDL completion until all routing outputs are fully materialized. cudaTriggerProgrammaticLaunchCompletion() fires before Lines 228-253 finish writing mPtrExpandedIdxToPermutedIdx, mPtrPermutedIdxToExpandedIdx, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613481)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingDeepSeek/launchMainKernel.cu`:86; signals: block, cuda, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Signal PDL completion only after the top-K outputs are written. This kernel produces mPtrTopKPacked and mPtrTopKWeights, but it calls ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613483)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingRenormalize.cu`:44; signals: benchmark, block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Error message references wrong routing method. The error message says "Llama4 routing kernel expects..." but this is the Renormalize ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613492)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingRenormalize/launchBlockKernel.cu`:100; signals: benchmark, block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Unused variable minScore. The variable minScore is declared and initialized but never used. The routingTopKExperts function (called at lines ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613497)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routingRenormalize/RoutingRenormalizeCommon.cuh`:136; signals: benchmark, block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Guard the mTopK 32 case in the dispatch macro. The final branch currently sends every mTopK 16 request into ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613501)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingDeepSeek.cu`:15; signals: block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the copyright year on this new file. This file is introduced in this PR, but the header still ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613473)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingDeepSeek.cu`:64; signals: block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Don't launch launchInitExpertCounts() after nulling mPtrExpertCounts for the single-cluster path. Lines 63-64 explicitly set data.mPtrExpertCounts = nullptr for useSingleCluster, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613478)
- `2026-04-21T22:25:58Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:583; signals: hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major MiniMax-M2 still needs its correction bias on this path. MiniMaxM2MoeRoutingMethod.apply() still does sigmoid(logits) + e score correction bias, and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13294#discussion_r3120613514)
