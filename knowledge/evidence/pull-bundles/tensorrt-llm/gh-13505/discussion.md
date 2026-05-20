# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13505](https://github.com/NVIDIA/TensorRT-LLM/pull/13505)
- Source page: `sources/prs/tensorrt-llm/PR-13505.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13505`
- Generated at: `2026-05-20T15:18:44.592517+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-27T11:13:41Z`
- Merged: `2026-05-06T03:47:30Z`

## Discussion Counts

- Issue comments: 37
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 8
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=0
- Human participants with discussion text: PerkzZheng, coderabbitai, tensorrt-cicd, yunruis, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-27T11:26:04Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 🧹 Nitpick comments (2) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK1SageV1StaticContext cubin.cpp (1) 1-3: Exclude Git LFS pointer ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4180439542)
- `2026-05-05T03:04:05Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4225028122)
- `2026-05-06T02:22:42Z` `COMMENTED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4232737042)
- `2026-05-06T02:41:16Z` `COMMENTED` by `yunruis` (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4232819153)
- `2026-05-06T02:41:38Z` `COMMENTED` by `yunruis` (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4232820080)
- `2026-05-06T03:07:51Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4232905230)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/xqaDispatcher.cpp`: 4 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H128PagedKvDenseP32MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvSlidingOrChunkedCausalP32VarSeqQ16Kv128PersistentSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128PackedQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1PersistentContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128StaticContext_cubin.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-27T11:25:59Z` `issue` by `coderabbitai`; signals: alignment, attention, cache, compile, cuda, cute, hang, kernel; excerpt: "📝 Walkthrough Walkthrough The PR modifies MLA generation parameter handling in the attention operation dispatcher, changing the KV-cache maximum sequence length source from max ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#issuecomment-4326565836)
- `2026-04-27T11:26:03Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H64PackedQkvDenseVarSeqSkipsSoftmaxQ128Kv128StaticContext_cubin.cpp`:2; signals: compile, cute, kernel, pipeline, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50379 --- Ensure Git LFS objects are hydrated ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3146880294)
- `2026-04-27T11:26:04Z` `review` `COMMENTED` by `coderabbitai`; signals: compile, kernel, sm100, tensorrt, tma; excerpt: "Actionable comments posted: 4 🧹 Nitpick comments (2) cpp/tensorrt llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel QkInt8VE4m3OBfloat16H128SeparateQkvDenseVarSeqSkipsSoftmaxQ128Kv128SageQ1SageK1SageV1StaticContext cubin.cpp (1) 1-3: Exclude Git LFS pointer artifacts from C++ static-analysis/compile targets. This ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#pullrequestreview-4180439542)
- `2026-04-27T11:26:03Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H128PagedKvDenseP32MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen_cubin.cpp`:2; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3146880266)
- `2026-04-27T11:26:03Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvSlidingOrChunkedCausalP32VarSeqQ16Kv128PersistentSwapsAbForGen_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- Ensure Git LFS blobs are resolved ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3146880280)
- `2026-04-27T11:26:03Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16H128PackedQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1PersistentContext_cubin.cpp`:3; signals: cuda, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 6949 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3146880285)
- `2026-05-06T02:18:40Z` `inline` by `PerkzZheng` `cpp/tensorrt_llm/kernels/xqaDispatcher.cpp`:505; signals: attention, kernel, tensorrt; excerpt: "is it true that max attention window size = max past kv length for non-sliding-window-attention or it is MAX INT ? or we can ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3192613268)
- `2026-05-06T02:41:16Z` `inline` by `yunruis` `cpp/tensorrt_llm/kernels/xqaDispatcher.cpp`:505; signals: cuda, kernel, tensorrt; excerpt: "Not MAX INT, it is the same value with cuda graph warmup. The purpose is to select same fmha, to avoid JIT on runtime" (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3192684648)
- `2026-05-06T02:20:01Z` `inline` by `PerkzZheng` `cpp/tensorrt_llm/kernels/xqaDispatcher.cpp`:524; signals: hang, kernel, tensorrt; excerpt: "Do we need to also make the same changes to prefill kernels ?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3192616555)
- `2026-05-06T02:41:38Z` `inline` by `yunruis` `cpp/tensorrt_llm/kernels/xqaDispatcher.cpp`:524; signals: kernel, tensorrt; excerpt: "no, only decode. Reason is same as above" (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#discussion_r3192685561)
- `2026-04-30T01:29:20Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46125]( [ run ] completed with state SUCCESS. Commit: 25091f7 [/LLM/main/L0 MergeRequest PR pipeline 36259]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#issuecomment-4348907909)
- `2026-04-30T07:41:56Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46257]( [ run ] completed with state SUCCESS. Commit: 25091f7 [/LLM/main/L0 MergeRequest PR pipeline 36366]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13505#issuecomment-4350579013)
