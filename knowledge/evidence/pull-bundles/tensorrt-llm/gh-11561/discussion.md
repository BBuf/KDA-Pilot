# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11561](https://github.com/NVIDIA/TensorRT-LLM/pull/11561)
- Source page: `sources/prs/tensorrt-llm/PR-11561.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11561`
- Generated at: `2026-05-20T15:17:46.261212+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-18T03:26:34Z`
- Merged: `2026-05-20T01:14:02Z`

## Discussion Counts

- Issue comments: 31
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: coderabbitai, farazkh80, liji-nv, pamelap-nvidia, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-30T17:46:10Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4207298752)
- `2026-05-08T08:24:42Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4250747827)
- `2026-05-08T08:54:39Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4250914983)
- `2026-05-08T08:55:54Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4250921575)
- `2026-05-08T09:01:03Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4250950571)
- `2026-05-12T21:12:35Z` `COMMENTED` by `pamelap-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4276284982)
- `2026-05-13T02:14:00Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4277706292)
- `2026-05-19T03:07:05Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4315385588)

## Inline Comment Hotspots

- `tensorrt_llm/quantization/functional.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`: 2 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 1 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_finegrained_mixed_dtype_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-12T21:12:35Z` `inline` by `pamelap-nvidia` `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:596; signals: cutlass, fp4, fp8, gemm, kernel, mxfp4, nvfp4, sm120; excerpt: "I made it explicit to check "CutlassGemmConfig::FP4 ONLY CutlassGemmConfig::FP8FP4 MIXED". Basically we want - get candidate configs sm120 used for nvfp4 dense gemm, nvfp4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3229869639)
- `2026-04-30T17:46:06Z` `issue` by `coderabbitai`; signals: bf16, blackwell, cutlass, dtype, fp8, gemm, hang, hopper; excerpt: "📝 Walkthrough Walkthrough This pull request differentiates SM architecture version support for quantized GEMM operations, introducing separate maximum SM versions for W4A8 (FP8-based) versus ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#issuecomment-4354782294)
- `2026-04-30T17:46:10Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, dtype, gemm, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#pullrequestreview-4207298752)
- `2026-05-08T08:24:42Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:596; signals: cutlass, fp4, gemm, kernel, tensorrt; excerpt: "Does CutlassGemmConfig::FP4 ONLY mean fp4xfp4? If so, !CutlassGemmConfig::WEIGHT ONLY is enough to include it, why do we still need FP4 ONLY here?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3207386993)
- `2026-05-08T08:55:54Z` `inline` by `yuxianq` `tests/unittest/_torch/thop/parallel/test_finegrained_mixed_dtype_gemm.py`:59; signals: accuracy, dtype, gemm; excerpt: "W4A16/W4A8 in skip message is no longer accuracy now." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3207547282)
- `2026-04-30T17:46:09Z` `inline` by `coderabbitai` `tensorrt_llm/quantization/functional.py`:971; signals: sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Fix unreachable SM100/103 branch after SM remap. if sm = 90: sm = 80 makes the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3169805262)
- `2026-05-08T08:54:39Z` `inline` by `yuxianq` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1455; signals: accuracy, tensorrt; excerpt: "The W4A16/W4A8 in error message is no longer accuracy now." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3207540617)
- `2026-05-08T09:01:03Z` `inline` by `yuxianq` `tensorrt_llm/quantization/functional.py`:966; signals: tensorrt; excerpt: "This structure is a little confusing, how about using the following structure:" (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#discussion_r3207574076)
- `2026-04-30T17:59:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46416]( [ run ] completed with state FAILURE. Commit: b9b9599 [/LLM/main/L0 MergeRequest PR pipeline 36490]( completed with status: 'ABORTED' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#issuecomment-4354902781)
- `2026-05-03T04:41:36Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46578]( [ run ] completed with state SUCCESS. Commit: 68bc567 [/LLM/main/L0 MergeRequest PR pipeline 36628]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#issuecomment-4365405595)
- `2026-05-06T06:02:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46862]( [ run ] completed with state SUCCESS. Commit: a394664 [/LLM/main/L0 MergeRequest PR pipeline 36874]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#issuecomment-4385514662)
- `2026-05-12T21:42:28Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48029]( [ run ] completed with state FAILURE. Commit: 2823247 [/LLM/main/L0 MergeRequest PR pipeline 37865]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11561#issuecomment-4435071072)
