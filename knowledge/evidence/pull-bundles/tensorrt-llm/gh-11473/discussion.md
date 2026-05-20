# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11473](https://github.com/NVIDIA/TensorRT-LLM/pull/11473)
- Source page: `sources/prs/tensorrt-llm/PR-11473.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11473`
- Generated at: `2026-05-20T15:17:42.559489+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-12T08:27:18Z`
- Merged: `2026-03-07T01:38:47Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 19 (approved=3, commented=16)
- Inline review comments: 27
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=16, outdated=10
- Human participants with discussion text: Wanli-Jiang, coderabbitai, hyukn, nv-guomingz, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-12T08:36:03Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3789440908)
- `2026-03-02T07:05:25Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3874429634)
- `2026-03-02T07:06:01Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3874431237)
- `2026-03-03T10:48:43Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3881779702)
- `2026-03-03T12:39:28Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3882305657)
- `2026-03-03T13:17:52Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3882535043)
- `2026-03-03T13:28:04Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3882588650)
- `2026-03-04T07:36:56Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887691431)
- `2026-03-04T07:37:26Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887693482)
- `2026-03-04T07:37:28Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887693721)
- `2026-03-04T07:37:37Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887694190)
- `2026-03-04T07:37:56Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887695563)
- `2026-03-04T07:38:08Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887696364)
- `2026-03-04T07:38:14Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887696977)
- `2026-03-04T07:38:34Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887698303)
- `2026-03-04T07:38:42Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887698718)
- `2026-03-04T08:35:18Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3887929015)
- `2026-03-05T09:44:51Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3895239427)
- `2026-03-06T16:15:25Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3904657119)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cu`: 11 inline comment(s)
- `tests/unittest/_torch/modules/mamba/test_layernorm_gated.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/thop/fusedGatedRMSNormQuant.cpp`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cuh`: 2 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_nemotron_h.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/CMakeLists.txt`: 1 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/mamba/ssd_chunk_scan.py`: 1 inline comment(s)
- `tests/unittest/_torch/modules/test_fused_activation_quant.py`: 1 inline comment(s)
- `tests/unittest/_torch/modules/test_fused_add_rms_norm_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-12T08:36:03Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, benchmark, bf16, block, cache, compile, correctness, cuda; excerpt: "Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#pullrequestreview-3789440908)
- `2026-02-12T08:35:58Z` `issue` by `coderabbitai`; signals: autotune, benchmark, bf16, blackwell, block, cache, compile, correctness; excerpt: "📝 Walkthrough Walkthrough This pull request introduces NVIDIA FP4 (NVFP4) quantization support throughout TensorRT-LLM, including new fused CUDA kernels for quantization-aware operations (ReLU2, GatedRMSNorm), ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#issuecomment-3889469391)
- `2026-03-03T12:39:28Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cu`:188; signals: aligned, alignment, bf16, kernel, perf, tensorrt, vector; excerpt: "Misaligned uint4 loads on strided z input — potential crash The kernel performs 16-byte vectorized loads: The thop checks z.stride(-1) == 1 but does ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878030771)
- `2026-03-03T10:48:44Z` `inline` by `yuxianq` `cpp/tensorrt_llm/thop/fusedGatedRMSNormQuant.cpp`:158; signals: compile, cuda, dtype, fp4, register, tensorrt; excerpt: "Missing register fake for trtllm::fused gated rmsnorm quant custom op This op is registered here via TORCH LIBRARY FRAGMENT and TORCH LIBRARY IMPL(trtllm, CUDA, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2877543023)
- `2026-02-12T08:36:01Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/mamba/ssd_chunk_scan.py`:753; signals: benchmark, block, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 4404 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2797474007)
- `2026-03-03T13:17:52Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cu`:452; signals: cuda, fp4, kernel, tensorrt, warp; excerpt: "Non-power-of-2 group sizes cause warp divergence in shfl xor sync — undefined behavior The grouped kernel's Phase 2 calls cvt warp fp16 to fp4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878225779)
- `2026-03-03T13:17:52Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cu`:172; signals: block, compile, kernel, tensorrt, warp; excerpt: "Missing static assert for warp reduction assumption Block-level reduction assumes numWarps <= 32 (BLOCK SIZE <= 1024). Currently safe but no compile-time guard. Same ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878225800)
- `2026-03-03T13:17:52Z` `inline` by `yuxianq` `tests/unittest/_torch/modules/mamba/test_layernorm_gated.py`:262; signals: dtype, fp4, kernel, nvfp4; excerpt: "Test uses random (possibly negative) nvfp4 scale norm.nvfp4 scale = torch.randn(hidden size, ...) — scale factors should be positive scalars. The kernel reads only ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878225787)
- `2026-03-03T13:17:52Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/fusedGatedRMSNormQuant.cuh`:48; signals: block, fp4, kernel, tensorrt; excerpt: "Unused constants FP4 E2M1 MAX and FP4 BLOCK SIZE are declared but never referenced. The .cu file uses literal 6.0f and SF VEC SIZE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878225793)
- `2026-02-12T08:36:01Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/fusedGatedRMSNormQuant/CMakeLists.txt`:2; signals: benchmark, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Copyright year should be 2026 for a new file. The header says 2022-2024 but this is a newly introduced ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2797473983)
- `2026-02-12T08:36:01Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`:1059; signals: cute, fp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 158 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2797474002)
- `2026-03-03T13:17:52Z` `inline` by `yuxianq` `cpp/tensorrt_llm/thop/fusedGatedRMSNormQuant.cpp`:58; signals: cache, cuda, tensorrt; excerpt: "cudaGetDeviceProperties called every invocation without caching SM version check runs on every call. A static local would avoid repeated queries. Suggested fix: Cache with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11473#discussion_r2878225797)
