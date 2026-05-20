# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#8501](https://github.com/NVIDIA/TensorRT-LLM/pull/8501)
- Source page: `sources/prs/tensorrt-llm/PR-8501.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-8501`
- Generated at: `2026-05-20T15:19:19.649528+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-20T09:48:33Z`
- Merged: `2025-10-27T02:18:20Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=0
- Human participants with discussion text: coderabbitai, hlu1, hyukn, jinyangyuan-nvidia, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-20T09:56:00Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3355827760)
- `2025-10-21T06:14:52Z` `APPROVED` by `hyukn` - PR should be fine because both perf and CI look good. Just put some questions. Thanks (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3358875241)
- `2025-10-21T14:39:59Z` `COMMENTED` by `jinyangyuan-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3361182701)
- `2025-10-22T03:12:02Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3363548750)
- `2025-10-24T23:05:56Z` `APPROVED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3379140128)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 3 inline comment(s)
- `cpp/micro_benchmarks/mixtureOfExpertsBackendBenchmarkFixture.h`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/internal_cutlass_kernels/include/moe_kernels.h`: 1 inline comment(s)
- `cpp/tests/unit_tests/kernels/mixtureOfExpertsTest.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-20T09:56:00Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, benchmark, block, cutlass, epilogue, fp4, fp8; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3355827760)
- `2025-10-21T06:13:46Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:243; signals: cache, fp8, gemm, hang, kernel, moe, perf, regression; excerpt: "Want to confirm if I understand it correctly: Current warm-up phase does not cover the path with AlltoAll enabled. Thus, in that phase, the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2446822645)
- `2025-10-20T09:55:56Z` `issue` by `coderabbitai`; signals: attention, benchmark, block, cutlass, fp8, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough The changes refactor the Mixture of Experts (MoE) kernel interfaces and implementations to introduce new token-count parameters (num valid rows, expected ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#issuecomment-3421331968)
- `2025-10-20T09:55:59Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/internal_cutlass_kernels/include/moe_kernels.h`:433; signals: cutlass, kernel, moe, perf, performance, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Add Doxygen documentation for the new parameter. The new num valid rows parameter lacks documentation. Per coding guidelines, function ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2444483740)
- `2025-10-20T09:55:59Z` `inline` by `coderabbitai` `cpp/micro_benchmarks/mixtureOfExpertsBackendBenchmarkFixture.h`:1014; signals: benchmark, cutlass, gemm, moe; excerpt: "⚠️ Potential issue 🔴 Critical Fix the non-OSS runMoe argument order The non-OSS build now receives mHiddenSize twice before mInterSize, so the mInterSize, mNumExperts, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2444483730)
- `2025-10-21T14:39:59Z` `inline` by `jinyangyuan-nvidia` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:243; signals: autotune, perf, performance, tensorrt; excerpt: "Thanks @hyukn. I think all your understanding is correct except that the description of the calculation of expected m is incomplete. According to does ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2448610277)
- `2025-10-20T09:55:59Z` `inline` by `coderabbitai` `cpp/tests/unit_tests/kernels/mixtureOfExpertsTest.cu`:1293; signals: kernel, moe; excerpt: "⚠️ Potential issue 🔴 Critical Align non-OSS runMoe call with new signature Here too, the non-OSS path feeds mHiddenSize twice, which misaligns every subsequent ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2444483748)
- `2025-10-22T03:12:02Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:243; signals: tensorrt; excerpt: "Thanks a lot for the clarification!" (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#discussion_r2450297220)
- `2025-10-20T21:05:40Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 21898]( [ run ] completed with state SUCCESS. Commit: 55bc09c [/LLM/main/L0 MergeRequest PR pipeline 16507]( completed with status: 'SUCCESS' Pipeline passed with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#issuecomment-3423717987)
- `2025-10-21T06:14:52Z` `review` `APPROVED` by `hyukn`; signals: perf; excerpt: "PR should be fine because both perf and CI look good. Just put some questions. Thanks" (https://github.com/NVIDIA/TensorRT-LLM/pull/8501#pullrequestreview-3358875241)
