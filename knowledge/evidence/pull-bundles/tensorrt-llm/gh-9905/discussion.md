# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9905](https://github.com/NVIDIA/TensorRT-LLM/pull/9905)
- Source page: `sources/prs/tensorrt-llm/PR-9905.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9905`
- Generated at: `2026-05-20T15:19:29.077918+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-11T09:28:50Z`
- Merged: `2026-01-14T23:29:15Z`

## Discussion Counts

- Issue comments: 50
- Review submissions: 18 (approved=5, commented=13)
- Inline review comments: 19
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=8
- Human participants with discussion text: HuiGao-NV, JintaoPengCS, Kefeng-Duan, benzh-2025, byshiue, coderabbitai, dc3671, liji-nv, symphonylyh, tensorrt-cicd, yizhang-nv, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-11T09:32:49Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/fusedLayernormKernels/ws layernorm.cuh (1) 1-2: Update copyright year to include ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3566531810)
- `2026-01-12T05:25:46Z` `COMMENTED` by `yizhang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649202739)
- `2026-01-12T07:49:24Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649495490)
- `2026-01-12T07:49:30Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649495762)
- `2026-01-12T07:53:09Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649506606)
- `2026-01-12T08:06:05Z` `APPROVED` by `yizhang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649545588)
- `2026-01-12T08:34:52Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649625436)
- `2026-01-12T09:00:17Z` `COMMENTED` by `byshiue` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649723455)
- `2026-01-12T09:05:07Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649732424)
- `2026-01-12T09:10:21Z` `APPROVED` by `byshiue` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649772527)
- `2026-01-12T09:20:42Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649757437)
- `2026-01-12T09:29:25Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649851823)
- `2026-01-12T09:34:44Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649871339)
- `2026-01-12T09:36:24Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3649877273)
- `2026-01-12T11:09:48Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3650230002)
- `2026-01-12T11:28:48Z` `COMMENTED` by `JintaoPengCS` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3650323960)
- `2026-01-13T05:13:58Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3653862162)
- `2026-01-13T07:07:34Z` `APPROVED` by `symphonylyh` (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3654185155)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/thop/fusedAddRMSNormQuant.cpp`: 6 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_llama.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/modules/rms_norm.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/fusedLayernormKernels/low_latency_layernorm.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-11T09:32:49Z` `review` `COMMENTED` by `coderabbitai`; signals: block, compile, cuda, dtype, fp4, hang, kernel, layout; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/fusedLayernormKernels/ws layernorm.cuh (1) 1-2: Update copyright year to include 2025. The copyright header should be ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#pullrequestreview-3566531810)
- `2025-12-11T09:32:45Z` `issue` by `coderabbitai`; signals: bf16, compile, cuda, dtype, fp4, hang, kernel, register; excerpt: "📝 Walkthrough Walkthrough Introduces a new fused CUDA kernel operation combining Add, RMSNorm/LayerNorm, and FP4 quantization for PyTorch. Changes include C++ implementation with input ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#issuecomment-3641051298)
- `2025-12-11T09:32:48Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fusedAddRMSNormQuant.cpp`:137; signals: cute, fp4, hang, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 2397 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2609852625)
- `2026-01-12T09:29:25Z` `inline` by `JintaoPengCS` `cpp/tensorrt_llm/kernels/fusedLayernormKernels/low_latency_layernorm.cuh`:157; signals: cuda, kernel, latency, tensorrt; excerpt: "Keep the CUDA ARCH has exactly same check for all cudaTriggerProgrammaticLaunchCompletion() and cudaGridDependencySynchronize(). As a result, i added the && ( CUDA ARCH = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681466004)
- `2026-01-12T09:06:40Z` `inline` by `liji-nv` `cpp/tensorrt_llm/kernels/fusedLayernormKernels/low_latency_layernorm.cuh`:157; signals: cuda, kernel, latency, tensorrt; excerpt: "Why the CUDA ARCH = 900 check in if not sufficient?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681386875)
- `2026-01-12T09:05:02Z` `inline` by `liji-nv` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1861; signals: tensorrt; excerpt: "Any reason to add this to torch custom ops.py rather than let caller to directly call torch.ops.trtllm.fused add rms norm quant. This file should ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681380502)
- `2026-01-12T05:18:11Z` `inline` by `yizhang-nv` `tensorrt_llm/_torch/models/modeling_llama.py`:694; signals: tensorrt; excerpt: "Please remove the comment here." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2680900011)
- `2026-01-12T05:23:03Z` `inline` by `yizhang-nv` `tensorrt_llm/_torch/modules/rms_norm.py`:125; signals: tensorrt; excerpt: "Please remove the comment before merge" (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2680906155)
- `2026-01-12T05:25:44Z` `inline` by `yizhang-nv` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1888; signals: tensorrt; excerpt: "Just for double check, this custom op does not involve inplace update the input args, right?" (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2680910169)
- `2026-01-12T07:49:24Z` `inline` by `JintaoPengCS` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1888; signals: tensorrt; excerpt: "YES" (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681171630)
- `2026-01-12T07:49:30Z` `inline` by `JintaoPengCS` `tensorrt_llm/_torch/modules/rms_norm.py`:125; signals: tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681171832)
- `2026-01-12T07:53:09Z` `inline` by `JintaoPengCS` `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`:1888; signals: tensorrt; excerpt: "this custom op does not involve inplace update the input args." (https://github.com/NVIDIA/TensorRT-LLM/pull/9905#discussion_r2681180375)
