# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#8620](https://github.com/NVIDIA/TensorRT-LLM/pull/8620)
- Source page: `sources/prs/tensorrt-llm/PR-8620.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-8620`
- Generated at: `2026-05-20T15:19:19.666080+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-23T08:27:14Z`
- Merged: `2025-10-29T04:39:03Z`

## Discussion Counts

- Issue comments: 34
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 15
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=5
- Human participants with discussion text: Njuapp, QiJune, Tracin, coderabbitai, liji-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-24T03:32:39Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374217767)
- `2025-10-24T06:02:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu (5) 186-198: Log message is misleading “Enable PDL ... (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374680077)
- `2025-10-24T06:27:06Z` `COMMENTED` by `Tracin` - Looks like it is NVFP4xNVFP4 kernel so why it is under weightOnlyGemv folder? And please add a test ... (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374725341)
- `2025-10-24T06:34:03Z` `COMMENTED` by `Tracin` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374739254)
- `2025-10-24T07:43:36Z` `COMMENTED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374926154)
- `2025-10-24T08:50:11Z` `COMMENTED` by `Njuapp` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3375211843)
- `2025-10-24T08:51:29Z` `COMMENTED` by `Njuapp` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3375217756)
- `2025-10-24T09:17:12Z` `COMMENTED` by `Njuapp` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3375320180)
- `2025-10-24T10:26:53Z` `COMMENTED` by `Njuapp` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3375621674)
- `2025-10-27T02:40:18Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3381641935)
- `2025-10-28T10:20:34Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3387899434)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`: 10 inline comment(s)
- `cpp/tensorrt_llm/thop/cudaNvfp4MM.cpp`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-24T06:02:56Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, block, compile, cuda, cutlass, dtype, fp4; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu (5) 186-198: Log message is misleading “Enable PDL in fp8 gemm plugin” is confusing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#pullrequestreview-3374680077)
- `2025-10-24T06:02:55Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:186; signals: block, cuda, fp4, gemm, hang, kernel, memory, nvfp4; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain Dispatch broken for m 16; grid assumes exact divisibility Template recursion only fires when params.m == ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2458991000)
- `2025-10-24T06:34:03Z` `inline` by `Tracin` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:240; signals: cuda, fp4, gemm, kernel, nvfp4, perf, tensorrt, tile; excerpt: "Just curiosity, we do not dispatch TILE N here so TILE N=2 have the best perf (or suitable SMEM allocation) right?" (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2459039733)
- `2025-10-24T10:26:52Z` `inline` by `Njuapp` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:240; signals: cuda, fp4, gemm, kernel, nvfp4, perf, performance, tensorrt; excerpt: "I tried TILE N=4, but performance is not substantially different. I tried batch=1/2/4/8, and for some batch size it get slightly worse but for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2459709569)
- `2025-10-24T05:50:07Z` `issue` by `coderabbitai`; signals: compile, cuda, dtype, fp4, gemm, hang, kernel, nvfp4; excerpt: "📝 Walkthrough Walkthrough This PR introduces a new CUDA core-optimized NVFP4 GEMM kernel module for TensorRT LLM. The implementation includes a tiled CUDA kernel ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#issuecomment-3441169136)
- `2025-10-24T06:02:56Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:272; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt, tile; excerpt: "⚠️ Potential issue 🟠 Major Dispatcher misses m/TILE M and n/TILE N divisibility; add checks to avoid bad grids You only gate on n ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2458991006)
- `2025-10-24T03:30:58Z` `inline` by `liji-nv` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:71; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "What is the preferred format? snake-case or camel-case. I think TRTLLM does not have a very strict coding style but it is better to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2458636874)
- `2025-10-24T03:28:12Z` `inline` by `liji-nv` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:45; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "nit: one definition per-line" (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2458629174)
- `2025-10-24T03:32:05Z` `inline` by `liji-nv` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:39; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "With k prefix?" (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2458639748)
- `2025-10-24T08:50:11Z` `inline` by `Njuapp` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:71; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "this is updated, unified to snake-case as much as possible for variable names" (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2459390235)
- `2025-10-24T08:51:28Z` `inline` by `Njuapp` `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`:39; signals: cuda, fp4, gemm, kernel, nvfp4, tensorrt; excerpt: "removed k prefix, now is step k" (https://github.com/NVIDIA/TensorRT-LLM/pull/8620#discussion_r2459394082)
