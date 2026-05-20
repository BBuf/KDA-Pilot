# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12537](https://github.com/NVIDIA/TensorRT-LLM/pull/12537)
- Source page: `sources/prs/tensorrt-llm/PR-12537.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12537`
- Generated at: `2026-05-20T15:18:12.863505+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T09:55:29Z`
- Merged: `2026-04-01T03:01:49Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=2
- Human participants with discussion text: JadoTu, coderabbitai, nv-guomingz, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T10:12:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4005505862)
- `2026-03-30T06:52:26Z` `COMMENTED` by `JadoTu` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028421067)
- `2026-03-30T06:53:16Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028424242)
- `2026-03-30T06:54:45Z` `COMMENTED` by `JadoTu` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028430450)
- `2026-03-30T06:55:22Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028433231)
- `2026-03-30T07:01:21Z` `COMMENTED` by `JadoTu` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028457144)
- `2026-03-30T07:01:39Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4028458344)
- `2026-04-01T02:30:16Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4041312719)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/thop/mamba2MTPSSMCacheOp.cpp`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`: 4 inline comment(s)
- `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.cu`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-25T10:12:05Z` `issue` by `coderabbitai`; signals: cache, compile, cuda, dtype, hang, kernel, perf, performance; excerpt: "📝 Walkthrough Walkthrough This pull request introduces a new Mamba2 MTP (Multi-Token Planning) SSM cache update operation. It adds a complete CUDA kernel implementation ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#issuecomment-4125299299)
- `2026-03-25T10:12:09Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`:116; signals: benchmark, cache, compile, kernel, overflow, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Use a stable softplus implementation here. log(1 + exp(x)) overflows for large positive dt value, and this target is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164910)
- `2026-03-25T10:12:09Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/mamba2MTPSSMCacheOp.cpp`:210; signals: cache, cuda, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🌐 Web query: In the PyTorch C++ / ATen CUDA API, when at::cuda::getCurrentCUDAStream() is called without ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164942)
- `2026-03-25T10:12:11Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 7 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : Path: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#pullrequestreview-4005505862)
- `2026-03-25T10:12:08Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.cu`:65; signals: benchmark, cache, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard the head/group ratio before dispatch. The launcher computes heads groups ratio = nheads / ngroups in mamba2MTPSSMCacheKernel.cuh at ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164883)
- `2026-03-25T10:12:09Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.h`:79; signals: cache, kernel, layout, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Clarify the real tensor layout in this public header. dt, A, D, and dt bias are documented as if ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164906)
- `2026-03-25T10:12:09Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`:384; signals: benchmark, cache, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Only restore from already-materialized parent steps. At step t, the kernel has only written intermediate states [0, t). The ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164917)
- `2026-03-25T10:12:09Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/mamba2MTPSSMCacheOp.cpp`:63; signals: cache, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 11446 --- Add host-side validation for minimum SSM ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r2987164927)
- `2026-03-30T06:53:16Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.cu`:65; signals: cache, cute, kernel, tensorrt; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 2478 --- @JadoTu, you're right — the check is already present at Line 82 of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r3007894466)
- `2026-03-30T06:55:22Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`:384; signals: cache, kernel, tensorrt, triton; excerpt: "@JadoTu, understood — keeping parity with the Triton kernel is a reasonable rationale. The parent step idx 0, to make the invariant clear for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r3007902846)
- `2026-03-30T06:54:45Z` `inline` by `JadoTu` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`:384; signals: cache, kernel, tensorrt, triton; excerpt: "The same as triton kernel." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r3007900197)
- `2026-03-30T06:52:25Z` `inline` by `JadoTu` `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.cu`:65; signals: cache, kernel, tensorrt; excerpt: "The check is in the cpp file." (https://github.com/NVIDIA/TensorRT-LLM/pull/12537#discussion_r3007891373)
