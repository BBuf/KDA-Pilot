# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10479](https://github.com/NVIDIA/TensorRT-LLM/pull/10479)
- Source page: `sources/prs/tensorrt-llm/PR-10479.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10479`
- Generated at: `2026-05-20T15:17:39.889700+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-07T05:16:16Z`
- Merged: `2026-04-01T10:25:10Z`

## Discussion Counts

- Issue comments: 60
- Review submissions: 18 (approved=3, commented=15)
- Inline review comments: 35
- Review threads observed: 24
- Resolved/outdated thread markers: resolved=24, outdated=8
- Human participants with discussion text: QiJune, coderabbitai, hyukn, litaotju, tensorrt-cicd, xxi-nv, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T08:13:00Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 15 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3934697859)
- `2026-03-19T07:41:41Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3973340541)
- `2026-03-19T22:27:26Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978331490)
- `2026-03-19T22:28:13Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978334597)
- `2026-03-19T22:29:03Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978337829)
- `2026-03-20T00:02:40Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978682851)
- `2026-03-20T00:02:52Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978683298)
- `2026-03-20T00:03:52Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978685420)
- `2026-03-20T00:32:49Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978747555)
- `2026-03-20T01:18:03Z` `APPROVED` by `xxi-nv` - Thanks for the perf improvement. The MoE module level LGTM. @syuoni, could you help to reivew the kernel ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3978831172)
- `2026-03-24T13:47:19Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3999023597)
- `2026-03-24T16:29:56Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4000620246)
- `2026-03-24T16:30:29Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4000623561)
- `2026-03-24T17:33:06Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4001037412)
- `2026-03-25T08:53:37Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4005045242)
- `2026-03-25T18:30:34Z` `COMMENTED` by `zongfeijing` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4008921776)
- `2026-04-01T04:50:22Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4041654955)
- `2026-04-01T06:00:33Z` `APPROVED` by `QiJune` - LGTM for the LLM change (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-4041864241)

## Inline Comment Hotspots

- `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc1.py`: 14 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_densegemm.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`: 2 inline comment(s)
- `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc2.py`: 2 inline comment(s)
- `tests/unittest/_torch/modules/moe/moe_test_utils.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc1.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 1 inline comment(s)
- `tests/unittest/_torch/modules/moe/test_moe_backend.py`: 1 inline comment(s)
- `tests/unittest/_torch/modules/moe/test_moe_module.py`: 1 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_moe_densegemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-12T08:12:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:2900; signals: bf16, compile, cute, cutlass, dtype, gemm, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Fail fast on unsupported output dtype values. Both DenseGEMM runners silently fall back to cutlass.BFloat16 when output dtype is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922963973)
- `2026-03-12T08:12:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:3057; signals: bf16, cache, compile, cute, dtype, epilogue, fp4, gemm; excerpt: "⚠️ Potential issue 🔴 Critical Include output dtype in both DenseGEMM kernel cache keys. Both runners bake the output element type into c ptr ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922963982)
- `2026-03-12T08:12:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:2285; signals: blackwell, cute, gemm, kernel, layout, moe, tensorrt, tile; excerpt: "⚠️ Potential issue 🟠 Major Use ceil-div/padding for the swizzled SF layouts. m // 128 and n // 128 floor away boundary tiles. For ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922963992)
- `2026-03-12T08:13:00Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, cute, gemm, hang, kernel, moe, tensorrt; excerpt: "Actionable comments posted: 15 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#pullrequestreview-3934697859)
- `2026-03-24T13:29:19Z` `inline` by `hyukn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc1.py`:1504; signals: blackwell, cute, epilogue, gemm, kernel, moe, tensorrt, tile; excerpt: "Does subtile cnt = 1 exist in the real case? Will that silently skip the entire epilogue output?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2981592354)
- `2026-03-12T08:12:54Z` `issue` by `coderabbitai`; signals: accuracy, alignment, benchmark, blackwell, block, correctness, cute, cutlass; excerpt: "📝 Walkthrough Walkthrough This PR introduces Dense GEMM-based MoE support for NVFP4 quantization, adding Blackwell SM100 kernels with SwiGLU fusion (FC1) and FC2 dense ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#issuecomment-4044805418)
- `2026-03-12T08:12:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`:27; signals: blackwell, block, cute, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Replace the copied BSD header with the TensorRT-LLM Apache header. This new source file still carries a BSD-3-Clause example ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922963988)
- `2026-03-24T17:33:06Z` `inline` by `zongfeijing` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc1.py`:1504; signals: blackwell, cute, gemm, kernel, moe, tensorrt, tile; excerpt: "Since we fuse the SwiGLU function into FC1, tileN is at least 128, so subtile cnt = 1 will not occur in practice." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2983215869)
- `2026-03-12T08:12:58Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc1.py`:27; signals: block, cute, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major The license header doesn’t match the repo’s required Apache block. This file carries a BSD-3-Clause header and a 2025 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922964007)
- `2026-03-12T08:12:58Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc1.py`:924; signals: cute, gemm, kernel, moe, tensorrt, vector; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 180 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922964020)
- `2026-03-12T08:12:58Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc2.py`:27; signals: block, cute, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Use the repository's Apache-2.0 header for this new file. This script currently carries a BSD-3-Clause block instead of the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922964028)
- `2026-03-12T08:12:58Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:1126; signals: cute, cutlass, gemm, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 3905 --- DenseGEMM backend still lacks necessary kwargs ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10479#discussion_r2922963998)
