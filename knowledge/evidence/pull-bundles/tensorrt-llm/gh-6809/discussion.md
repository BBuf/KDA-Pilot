# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#6809](https://github.com/NVIDIA/TensorRT-LLM/pull/6809)
- Source page: `sources/prs/tensorrt-llm/PR-6809.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-6809`
- Generated at: `2026-05-20T15:19:16.403496+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-12T03:18:46Z`
- Merged: `2025-09-04T16:03:38Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 33 (approved=2, commented=31)
- Inline review comments: 100
- Review threads observed: 84
- Resolved/outdated thread markers: resolved=84, outdated=64
- Human participants with discussion text: QiJune, cjluo-nv, coderabbitai, nekorobov, sychen52, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-12T03:31:36Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 49 🔭 Outside diff range comments (3) cpp/tensorrt llm/kernels/trtllmGenKernels/gemm/trtllmGen gemm export/cubins/Gemm Bfloat16 E4m3E4m3 Fp32 t128x8x128u2 ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3108434299)
- `2025-08-12T03:32:41Z` `COMMENTED` by `coderabbitai` - Review continued from previous batch... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3108435497)
- `2025-08-12T08:15:21Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3109075866)
- `2025-08-12T15:07:37Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3111303611)
- `2025-08-12T16:31:01Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3111812228)
- `2025-08-12T18:41:22Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112248388)
- `2025-08-12T18:41:30Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112248842)
- `2025-08-12T18:41:53Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112250206)
- `2025-08-12T18:42:00Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112250664)
- `2025-08-12T18:42:09Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112251191)
- `2025-08-12T18:42:26Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112252089)
- `2025-08-12T18:42:35Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112252908)
- `2025-08-12T18:42:43Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112253394)
- `2025-08-12T18:42:50Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3112253770)
- `2025-08-13T12:21:00Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3115700178)
- `2025-08-14T21:23:00Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122152232)
- `2025-08-14T21:23:24Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122152948)
- `2025-08-14T21:23:51Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122153683)
- `2025-08-14T21:23:59Z` `COMMENTED` by `sychen52` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122153891)
- `2025-08-14T22:35:27Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 9 🔭 Outside diff range comments (4) cpp/tensorrt llm/kernels/trtllmGenKernels/gemm/KernelRunner.h (2) 55-58: Missing include for mPassingConfigIndices ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122285919)
- `2025-08-15T21:05:32Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (4) tensorrt llm/quantization/mode.py (2) 238-255: from description: expose the new flag ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3125167735)
- `2025-08-19T11:10:24Z` `APPROVED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3131833055)
- `2025-08-19T21:33:17Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3133912442)
- `2025-08-20T17:12:15Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (4) tensorrt llm/quantization/mode.py (2) 237-255: Include new argument in raise error ... (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3137558716)
- ... 9 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/config.json`: 14 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/KernelRunner.cpp`: 11 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 11 inline comment(s)
- `tests/unittest/_torch/thop/test_fp4_gemm_quantize.py`: 6 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/KernelRunner.h`: 4 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/Enums.h`: 3 inline comment(s)
- `cpp/tensorrt_llm/thop/CMakeLists.txt`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/KernelParamsDecl.h`: 3 inline comment(s)
- `cpp/tensorrt_llm/thop/nvfp4xFp8GemmTrtllmGen.cpp`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/GemmOptions.h`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/TmaDescriptor.h`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/gemm/trtllmGen_gemm_export/GemmInterface.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-12T03:31:36Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, compile, cuda, dtype, epilogue, fp4, fp8, gemm; excerpt: "Actionable comments posted: 49 🔭 Outside diff range comments (3) cpp/tensorrt llm/kernels/trtllmGenKernels/gemm/trtllmGen gemm export/cubins/Gemm Bfloat16 E4m3E4m3 Fp32 t128x8x128u2 s4 et64x8 m64x8x32 cga1x1x1 16dp256b TN ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3108434299)
- `2025-08-14T22:35:27Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, bf16, block, cache, compile, cuda, dtype, fp4; excerpt: "Actionable comments posted: 9 🔭 Outside diff range comments (4) cpp/tensorrt llm/kernels/trtllmGenKernels/gemm/KernelRunner.h (2) 55-58: Missing include for mPassingConfigIndices (header should be self-contained) This header ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3122285919)
- `2025-08-15T21:05:32Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, dtype, epilogue, fp4, fp8, hang, kernel, mxfp4; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (4) tensorrt llm/quantization/mode.py (2) 238-255: from description: expose the new flag in error messages. Add use w4a8 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3125167735)
- `2025-08-19T21:33:17Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cuda, dtype, fp4, fp8, hang, kernel, mxfp4; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3133912442)
- `2025-08-20T17:12:15Z` `review` `COMMENTED` by `coderabbitai`; signals: block, dtype, epilogue, fp4, fp8, hang, kernel, mxfp4; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (4) tensorrt llm/quantization/mode.py (2) 237-255: Include new argument in raise error diagnostic from description added use w4a8 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3137558716)
- `2025-08-21T20:51:41Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, dtype, fp4, fp8, hang, kernel; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3142240925)
- `2025-08-21T21:06:06Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, dtype, fp4, fp8, hang, kernel, nvfp4; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3142273636)
- `2025-08-22T18:46:02Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, block, cache, compile, correctness, cuda, dtype, epilogue; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3145492738)
- `2025-08-22T20:29:55Z` `review` `COMMENTED` by `coderabbitai`; signals: compile, cuda, dtype, fp8, gemm, hang, kernel, latency; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3145880740)
- `2025-08-25T17:36:40Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, cuda, dtype, fp8, gemm, hang, kernel, race; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3152429862)
- `2025-08-26T21:07:26Z` `review` `COMMENTED` by `coderabbitai`; signals: cuda, dtype, gemm, hang, kernel, race, regression, tensorrt; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3157314681)
- `2025-08-28T01:15:12Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, dtype, fp4, fp8, hang, kernel, layout; excerpt: "Actionable comments posted: 1 ♻️ Duplicate comments (1) tensorrt llm/ torch/modules/linear.py (1) 887-932: Fix ambiguous Tensor equality and long lines; ensure float32 scalars. Using ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/6809#pullrequestreview-3162598623)
