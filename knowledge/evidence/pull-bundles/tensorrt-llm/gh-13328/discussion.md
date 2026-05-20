# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13328](https://github.com/NVIDIA/TensorRT-LLM/pull/13328)
- Source page: `sources/prs/tensorrt-llm/PR-13328.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13328`
- Generated at: `2026-05-20T15:18:37.754929+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T08:29:14Z`
- Merged: `2026-05-05T08:35:39Z`

## Discussion Counts

- Issue comments: 50
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 16
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=14, outdated=5
- Human participants with discussion text: ChristinaZ, coderabbitai, litaotju, longlee0622, tensorrt-cicd, xxi-nv, yweng0828
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T08:42:13Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 13 🧹 Nitpick comments (4) tensorrt llm/ torch/custom ops/trtllm gen custom ops.py (1) 92-103: Reuse ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4153213621)
- `2026-04-22T09:11:42Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4153429317)
- `2026-04-22T09:52:47Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4153712256)
- `2026-04-22T11:38:02Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4154300583)
- `2026-04-23T08:26:11Z` `APPROVED` by `litaotju` (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4160860506)
- `2026-04-24T12:01:59Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4170245503)

## Inline Comment Hotspots

- `tests/unittest/_torch/modules/moe/test_moe_module.py`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`: 2 inline comment(s)
- `cpp/tests/unit_tests/kernels/routing/routingCustomTest.cpp`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomPolicy.cuh`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingDeepSeek.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingDevKernel.h`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingFromTopKIds.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/thop/cuteDslMoeUtilsOp.cpp`: 1 inline comment(s)
- `cpp/tests/unit_tests/kernels/routing/routingDeepSeekTest.cpp`: 1 inline comment(s)
- `cpp/tests/unit_tests/kernels/routing/routingTest.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-22T08:42:13Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, benchmark, block, cute, fp4, fp8, hang, kernel; excerpt: "Actionable comments posted: 13 🧹 Nitpick comments (4) tensorrt llm/ torch/custom ops/trtllm gen custom ops.py (1) 92-103: Reuse one dummy correction bias per tuning ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#pullrequestreview-4153213621)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/cuteDslMoeUtilsOp.cpp`:81; signals: benchmark, bf16, cute, dtype, failing, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Reject unsupported routing logits dtypes instead of treating them as bf16. This maps every non-Float tensor to btg::Dtype::Bfloat16. If ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634683)
- `2026-04-22T08:42:07Z` `issue` by `coderabbitai`; signals: accuracy, block, compile, cute, dtype, failing, fp4, fp8; excerpt: "📝 Walkthrough Walkthrough This PR refactors the TensorRT-LLM MoE routing kernel infrastructure from macro-based dispatch to a unified policy-driven system. It consolidates multiple routing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#issuecomment-4294784013)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`:980; signals: block, failing, kernel, moe, pipeline, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Validate mTopK and mNumExperts before the precomputed-topK fast path returns. This branch reaches runPostTopKPipeline() before the MaxSupportedTopExperts / MaxSupportedExperts ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634656)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomPolicy.cuh`:767; signals: block, correctness, kernel, moe, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major Reject unsupported policy pairs instead of silently remapping them. This dispatcher ignores mPostprocessType for SigmoidBias, Sigmoid, and most Softmax ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634660)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingDevKernel.h`:169; signals: bf16, block, dtype, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Validate mDtypeInput before selecting the bf16 specialization. Both routing-custom dispatch macros only special-case tg::Dtype::Fp32. Any other mDtypeInput with mDtypeOutput ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634673)
- `2026-04-22T08:42:11Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/test_moe_module.py`:1294; signals: bf16, correctness, dtype, hang, moe, regression; excerpt: "⚠️ Potential issue 🟠 Major Assert correctness, not just “no crash”. This regression test still passes if the fp32 bias buffer is read with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634731)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`:655; signals: block, cuda, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Move the PDL completion trigger below the permutation writes. cudaTriggerProgrammaticLaunchCompletion() fires before Phase 5 fills mPtrExpandedIdxToPermutedIdx / permutation outputs. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634650)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingDeepSeek.cu`:228; signals: block, dtype, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Don't round fp32 routing bias down to OutputT before selection. loadScalar(..., params.mDtypeBias) already gives you a float, but this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634667)
- `2026-04-22T08:42:10Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingFromTopKIds.cu`:142; signals: block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Fail fast on unsupported post-topK buffer combinations. This helper now backs the early-return Llama4/DeepSeek paths, but every launch it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634679)
- `2026-04-22T08:42:11Z` `inline` by `coderabbitai` `cpp/tests/unit_tests/kernels/routing/routingDeepSeekTest.cpp`:464; signals: dtype, hang, kernel; excerpt: "⚠️ Potential issue 🟠 Major Verify the float32-bias result, not just kernel survivability. This new case only proves that the kernel does not crash ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634716)
- `2026-04-22T08:42:11Z` `inline` by `coderabbitai` `cpp/tests/unit_tests/kernels/routing/routingCustomTest.cpp`:1287; signals: dtype, kernel; excerpt: "⚠️ Potential issue 🟠 Major Assert numerical outputs in the mixed-bias-dtype test. This case only verifies that the kernel launch does not crash. A ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13328#discussion_r3122634710)
