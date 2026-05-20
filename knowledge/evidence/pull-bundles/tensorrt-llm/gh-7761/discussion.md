# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#7761](https://github.com/NVIDIA/TensorRT-LLM/pull/7761)
- Source page: `sources/prs/tensorrt-llm/PR-7761.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-7761`
- Generated at: `2026-05-20T15:19:16.455937+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-16T08:36:18Z`
- Merged: `2025-10-20T02:08:32Z`

## Discussion Counts

- Issue comments: 34
- Review submissions: 17 (approved=2, commented=15)
- Inline review comments: 25
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=12, outdated=4
- Human participants with discussion text: ChristinaZ, MatthiasKohl, coderabbitai, kaiyux, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-13T14:39:49Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 9 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3331906629)
- `2025-10-16T01:49:04Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3342811198)
- `2025-10-16T03:11:48Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3342913747)
- `2025-10-16T03:13:28Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3342915703)
- `2025-10-16T03:33:39Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3342940948)
- `2025-10-16T04:22:06Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3343010451)
- `2025-10-16T06:15:34Z` `APPROVED` by `MatthiasKohl` - LGTM. I just had a question about the structure, but this should not hold the PR back, and ... (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3343201222)
- `2025-10-16T06:58:29Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3343323124)
- `2025-10-16T12:52:10Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344692579)
- `2025-10-16T12:54:37Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344701522)
- `2025-10-16T13:17:52Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344807533)
- `2025-10-16T13:18:49Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344812501)
- `2025-10-16T13:27:50Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344854019)
- `2025-10-16T13:28:44Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3344858479)
- `2025-10-20T01:50:57Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3354825168)
- `2025-10-20T01:51:53Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3354825998)
- `2025-10-20T02:06:58Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3354842555)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`: 6 inline comment(s)
- `cpp/tensorrt_llm/kernels/moeTopKFuncs.cuh`: 5 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_deepseekv3.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/thop/fp4BlockScaleMoe.cpp`: 3 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_noaux_tc.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernel.h`: 1 inline comment(s)
- `cpp/tensorrt_llm/thop/noAuxTcOp.cpp`: 1 inline comment(s)
- `cpp/tests/unit_tests/kernels/routing/routingDeepSeekTest.cpp`: 1 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-13T14:39:49Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, block, compile, correctness, dtype, fp4, hang, kernel; excerpt: "Actionable comments posted: 9 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#pullrequestreview-3331906629)
- `2025-10-16T12:54:37Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp4BlockScaleMoe.cpp`:124; signals: autotune, block, cuda, cute, dtype, fp4, fp8, gemm; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 487 --- 🏁 Script executed: Length of output: 2187 --- @ChristinaZ Great progress on adding ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2435806499)
- `2025-10-13T14:39:44Z` `issue` by `coderabbitai`; signals: block, fp4, hang, kernel, memory, moe, mxfp4, shared memory; excerpt: "📝 Walkthrough Walkthrough Refactors and generalizes MoE routing/top‑K kernels to support larger expert counts and top‑k up to 10, adds generic warp top‑K reductions, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#issuecomment-3397808050)
- `2025-10-13T14:39:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`:270; signals: benchmark, block, kernel, moe, tensorrt, warp; excerpt: "⚠️ Potential issue 🔴 Critical Incorrect lane-to-buffer mapping; final reduction likely wrong The logic only writes at most two slots per thread and overwrites ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2426549170)
- `2025-10-13T14:39:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp4BlockScaleMoe.cpp`:124; signals: block, compile, fp4, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain Verify kernel support for top k=10 and consider using a named constant. The increase from top ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2426549176)
- `2025-10-13T14:39:47Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernel.h`:281; signals: block, kernel, moe, tensorrt, tma; excerpt: "🛠️ Refactor suggestion 🟠 Major Document the mApplySoftmaxAfterTopK flag and its usage. A new mApplySoftmaxAfterTopK flag has been added to the RoutingRenormalize path, but ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2426549160)
- `2025-10-13T14:39:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`:258; signals: benchmark, block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical OOB read when N not multiple of 4 in chunking path For the last chunk, start + i can ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2426549166)
- `2025-10-13T14:39:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/noAuxTcOp.cpp`:51; signals: benchmark, cuda, dtype, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Validate bias dtype/device/shape against scores Add strict checks: same dtype, CUDA device, and bias length equals num experts (1D). ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2426549186)
- `2025-10-16T06:12:03Z` `inline` by `MatthiasKohl` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`:217; signals: block, kernel, moe, tensorrt; excerpt: "can this be fused with what we have in kernels/moeTopKFuncs.cuh ? I'm not fully familiar with the structure and differences anymore, but it might ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2434690052)
- `2025-10-16T06:58:29Z` `inline` by `ChristinaZ` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`:217; signals: block, kernel, moe, tensorrt; excerpt: "Thanks, Matthias! Yes, that’s exactly what I had in mind as well. Before, I thought it was better to keep one within the trtllmgen ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2434785682)
- `2025-10-16T13:18:49Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingKernelTopK.cuh`:270; signals: block, kernel, moe, tensorrt; excerpt: "@ChristinaZ, great! Thank you for addressing the lane-to-buffer mapping issue. 🎉 🐰✨ ┏━━━━━━━━┓ ┃ Well ┃ ┃ done! ┃ ┗━━━━━━━━┛ ∧＿∧ (◕‿◕) ⊂ つ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2435886841)
- `2025-10-16T12:52:10Z` `inline` by `ChristinaZ` `cpp/tensorrt_llm/thop/fp4BlockScaleMoe.cpp`:124; signals: block, fp4, moe, tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/7761#discussion_r2435799146)
