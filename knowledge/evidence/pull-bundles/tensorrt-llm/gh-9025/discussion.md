# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9025](https://github.com/NVIDIA/TensorRT-LLM/pull/9025)
- Source page: `sources/prs/tensorrt-llm/PR-9025.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9025`
- Generated at: `2026-05-20T15:19:19.694764+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-09T02:09:16Z`
- Merged: `2025-11-17T02:04:29Z`

## Discussion Counts

- Issue comments: 38
- Review submissions: 22 (approved=3, commented=19)
- Inline review comments: 21
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=2
- Human participants with discussion text: IwakuraRein, OlivierDehaene, hlu1, hyukn, nekorobov, rosenrodt, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-10T06:04:41Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441014444)
- `2025-11-10T06:07:05Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441020734)
- `2025-11-10T06:10:18Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441027942)
- `2025-11-10T06:16:17Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441045201)
- `2025-11-10T06:16:17Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441045297)
- `2025-11-10T06:19:54Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441056055)
- `2025-11-10T07:01:41Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3441175793)
- `2025-11-10T11:11:56Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3442207363)
- `2025-11-11T03:55:07Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3446130373)
- `2025-11-11T06:17:05Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3446423347)
- `2025-11-11T06:17:11Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3446423531)
- `2025-11-11T06:27:37Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3446447330)
- `2025-11-12T06:50:43Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3451878948)
- `2025-11-12T21:08:04Z` `COMMENTED` by `IwakuraRein` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3455528159)
- `2025-11-13T08:17:49Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3458284032)
- `2025-11-13T08:18:39Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3458288870)
- `2025-11-14T08:11:39Z` `APPROVED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3463512605)
- `2025-11-14T19:31:29Z` `APPROVED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3466507211)
- `2025-11-17T01:20:25Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3470651735)
- `2025-11-17T01:28:51Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3470661163)
- `2025-11-17T01:29:37Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#pullrequestreview-3470661900)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`: 6 inline comment(s)
- `cpp/include/tensorrt_llm/common/utils.h`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/BatchedGemmInterface.h`: 3 inline comment(s)
- `tests/unittest/_torch/modules/test_fused_moe.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/KernelRunner.cpp`: 2 inline comment(s)
- `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/quantization.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-10T06:16:15Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/BatchedGemmInterface.h`:28; signals: flashinfer, gemm, kernel, moe, tensorrt; excerpt: "Why we need TLLM GEN EXPORT FLASHINFER? Which file is directly copied from trtllm-gen repo when we update TRTLLM MoE cubins here?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2508887875)
- `2025-11-10T06:16:17Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: alignment, gemm, hang, kernel, tensorrt; excerpt: "@IwakuraRein (Siyuan Fu) I think you added the clang-format file as part of TRT-LLM Gen export package. Could you share the background? Can we ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2508887958)
- `2025-11-12T21:08:04Z` `inline` by `IwakuraRein` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: flashinfer, gemm, kernel, tensorrt; excerpt: "@rosenrodt Hi. I added the clangformat of both flashinfer and tensorrt llm in the export script to automatically format the headers while exporting them. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2519826121)
- `2025-11-10T10:42:25Z` `inline` by `nekorobov` `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp`:119; signals: fp8, moe, tensorrt, tile; excerpt: "FP8 adds tileN=192 and 256 cubins. I have not found this added into supported tile sizes" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2509880991)
- `2025-11-11T06:17:05Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp`:119; signals: fp8, moe, tensorrt, tile; excerpt: "This op lacks the supported tiles checks. I added in [719fb18](" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2512981305)
- `2025-11-10T06:10:17Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: gemm, kernel, tensorrt; excerpt: "Why we use SortIncludes: false instead of SortIncludes: CaseSensitive like .clang-format in top-level directory? Can we remove this file?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2508876009)
- `2025-11-10T06:19:54Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/BatchedGemmInterface.h`:28; signals: gemm, kernel, tensorrt; excerpt: "Yes. The files under trtllmGen bmm export is largely a direct copy from trtllm-gen repo, except the cubins & mods in namespace and license ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2508895126)
- `2025-11-10T11:11:13Z` `inline` by `nekorobov` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:2604; signals: aligned, moe, tensorrt; excerpt: "It is important and had bug before -- the hidden dim after sharding was misaligned with SFs after sharding. I am not saying that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2510008134)
- `2025-11-13T08:17:49Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: gemm, kernel, tensorrt; excerpt: "Hmm. I think we'll remove the extra .clang-format after we sort out the script in the internal repo. I see .clang-format being copied to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2522227689)
- `2025-11-13T08:18:39Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: gemm, kernel, tensorrt; excerpt: "The CI is passing and I don't want to trigger another one. So I'd defer that to same CI some resources." (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2522231891)
- `2025-11-17T01:28:50Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/.clang-format`:65; signals: gemm, kernel, tensorrt; excerpt: "We will clean up the export package in TRTLLM Gen repo and address this issue at later time. Cc @nekorobov" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2532407288)
- `2025-11-10T10:14:42Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/KernelRunner.cpp`:157; signals: gemm, kernel, tensorrt; excerpt: "nit: I prefer explicit {}" (https://github.com/NVIDIA/TensorRT-LLM/pull/9025#discussion_r2509736658)
