# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13808](https://github.com/NVIDIA/TensorRT-LLM/pull/13808)
- Source page: `sources/prs/tensorrt-llm/PR-13808.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13808`
- Generated at: `2026-05-20T15:18:55.966971+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-06T12:55:47Z`
- Merged: `2026-05-13T05:08:52Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: PerkzZheng, coderabbitai, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-06T13:25:31Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 5 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel QkvBfloat16OBfloat16H128PagedKvCustomP32MultiCtasKvCgaVarSeqQ128Kv128StaticKeepsAbForGen cubin.cpp (1) 1-3: Static-analysis pipeline should skip ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#pullrequestreview-4236413207)
- `2026-05-06T14:26:43Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#pullrequestreview-4236946616)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK1SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1PersistentContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseStaticTokenSparseP1MultiCtasKvCgaVarSeqQ128Kv128StaticKeepsAbForGen_cubin.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-06T13:25:30Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`:3; signals: compile, cuda, cute, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#discussion_r3195753128)
- `2026-05-06T13:25:30Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseStaticTokenSparseP1MultiCtasKvCgaVarSeqQ128Kv128StaticKeepsAbForGen_cubin.cpp`:3; signals: compile, cuda, cute, gemm, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#discussion_r3195753137)
- `2026-05-06T13:25:29Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK1SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- Fix Git LFS ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#discussion_r3195753109)
- `2026-05-06T13:25:31Z` `review` `COMMENTED` by `coderabbitai`; signals: kernel, pipeline, sm100, tensorrt, tma; excerpt: "Actionable comments posted: 5 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel QkvBfloat16OBfloat16H128PagedKvCustomP32MultiCtasKvCgaVarSeqQ128Kv128StaticKeepsAbForGen cubin.cpp (1) 1-3: Static-analysis pipeline should skip unresolved Git LFS pointer stubs in ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#pullrequestreview-4236413207)
- `2026-05-06T13:25:26Z` `issue` by `coderabbitai`; signals: attention, compile, flash attention, hang, kernel, tensorrt; excerpt: "📝 Walkthrough Walkthrough This PR expands TRTLLM-GEN kernel support for Flash Attention (FMHA) by relaxing the head-size constraint in FmhaDispatcher. The condition is changed ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#issuecomment-4388491119)
- `2026-05-06T13:25:29Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 21146 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#discussion_r3195753096)
- `2026-05-06T13:25:29Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1PersistentContext_cubin.cpp`:3; signals: hang, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🔴 Critical ⚡ Quick win Replace LFS pointer with actual .cpp payload (or change artifact path/type). This file is currently a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#discussion_r3195753120)
- `2026-05-06T22:34:14Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47001]( [ run ] completed with state SUCCESS. Commit: cc9e67b [/LLM/main/L0 MergeRequest PR pipeline 36977]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#issuecomment-4392686548)
- `2026-05-11T23:18:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47723]( [ run ] completed with state SUCCESS. Commit: 1bc68aa [/LLM/main/L0 MergeRequest PR pipeline 37619]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#issuecomment-4425923317)
- `2026-05-12T14:46:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47855]( [ run ] completed with state SUCCESS. Commit: 94d5bc4 [/LLM/main/L0 MergeRequest PR pipeline 37725]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#issuecomment-4431680264)
- `2026-05-13T04:13:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48075]( [ run ] completed with state SUCCESS. Commit: 94d5bc4 [/LLM/main/L0 MergeRequest PR pipeline 37908]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13808#issuecomment-4437199583)
