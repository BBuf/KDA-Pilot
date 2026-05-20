# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13652](https://github.com/NVIDIA/TensorRT-LLM/pull/13652)
- Source page: `sources/prs/tensorrt-llm/PR-13652.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13652`
- Generated at: `2026-05-20T15:18:49.441196+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T06:38:28Z`
- Merged: `2026-05-09T07:02:38Z`

## Discussion Counts

- Issue comments: 51
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 13
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=12, outdated=8
- Human participants with discussion text: PerkzZheng, coderabbitai, heyuhhh, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-30T06:56:18Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#pullrequestreview-4203019937)
- `2026-04-30T06:58:36Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel QkvBfloat16OBfloat16H128PagedKvCausalP32MultiCtasKvVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen cubin.cpp (1) 1-3: Scope static analyzers away ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#pullrequestreview-4203048756)
- `2026-04-30T06:59:10Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#pullrequestreview-4203052898)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`: 4 inline comment(s)
- `cpp/tensorrt_llm/common/attentionOp.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/indexerTopK.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvDenseP32MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseP32VarSeqQ128Kv128PersistentContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128PersistentSwapsAbForGen_cubin.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-30T06:58:30Z` `issue` by `coderabbitai`; signals: attention, cache, fp8, hang, kernel, kv cache, layout, mla; excerpt: "📝 Walkthrough Walkthrough Extends MLA sparse-dimension handling with RoPE-based configuration, implements dynamic sparse MLA via per-token top-k selection, adds RoPE in-place application kernel, and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#issuecomment-4350323378)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`:3; signals: cute, hang, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 510 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159570)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`:3; signals: cute, hang, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 817 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159584)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseP32VarSeqQ128Kv128PersistentContext_cubin.cpp`:3; signals: compile, cute, kernel, pipeline, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1893 --- File is Git LFS pointer, not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159591)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159576)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128PersistentSwapsAbForGen_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159598)
- `2026-04-30T06:58:36Z` `review` `COMMENTED` by `coderabbitai`; signals: kernel, sm100, tensorrt, tma; excerpt: "Actionable comments posted: 10 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel QkvBfloat16OBfloat16H128PagedKvCausalP32MultiCtasKvVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen cubin.cpp (1) 1-3: Scope static analyzers away from Git LFS pointer artifacts. These ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#pullrequestreview-4203048756)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/common/attentionOp.cpp`:2831; signals: attention, layout, mla, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🏗️ Heavy lift The new rope append=false MLA config is still broken outside TRTLLM-GEN. These lines now admit qk ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159521)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:143; signals: cute, kernel, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift Keep sparse kernel selection consistent between isSupported() and run(). isSupported() now maps useSparseMLA && headSizeV == ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159523)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvDenseP32MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen_cubin.cpp`:3; signals: compile, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Ensure this LFS pointer is never compiled as C++ source. Line 2/Line 3 show only an ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159561)
- `2026-04-30T06:58:34Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`:3; signals: cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166159566)
- `2026-04-30T06:59:10Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`:141; signals: attention, autotune, kernel, tensorrt; excerpt: "No, for sparse attention we'll set it to dense in autotuner" (https://github.com/NVIDIA/TensorRT-LLM/pull/13652#discussion_r3166162303)
