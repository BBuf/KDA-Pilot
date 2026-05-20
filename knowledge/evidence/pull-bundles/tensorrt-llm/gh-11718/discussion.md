# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11718](https://github.com/NVIDIA/TensorRT-LLM/pull/11718)
- Source page: `sources/prs/tensorrt-llm/PR-11718.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11718`
- Generated at: `2026-05-20T15:17:48.283844+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-25T13:53:39Z`
- Merged: `2026-04-02T02:21:06Z`

## Discussion Counts

- Issue comments: 96
- Review submissions: 38 (approved=4, commented=34)
- Inline review comments: 55
- Review threads observed: 31
- Resolved/outdated thread markers: resolved=31, outdated=30
- Human participants with discussion text: PerkzZheng, chang-l, coderabbitai, nv-guomingz, tensorrt-cicd, xrq-phys, yuxianq, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-25T14:02:24Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 14 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3854464307)
- `2026-02-26T03:09:02Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858160683)
- `2026-02-26T03:11:43Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858167818)
- `2026-02-26T06:55:57Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858846655)
- `2026-02-26T06:56:22Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858847931)
- `2026-02-26T07:14:06Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858903808)
- `2026-02-26T07:15:20Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3858908872)
- `2026-02-26T16:53:50Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3862263667)
- `2026-02-27T05:34:14Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3864991410)
- `2026-02-27T05:44:48Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3865022983)
- `2026-02-27T18:58:23Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3868546095)
- `2026-03-02T02:27:59Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3873800086)
- `2026-03-02T02:34:21Z` `COMMENTED` by `PerkzZheng` - @xrq-phys do you know if this is required by any customers that are using TRTLLM ? I am ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3873784449)
- `2026-03-02T06:19:41Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874271905)
- `2026-03-02T06:19:59Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874273040)
- `2026-03-02T06:21:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874279579)
- `2026-03-02T06:22:48Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874284517)
- `2026-03-02T06:23:05Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874285676)
- `2026-03-02T06:23:44Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874288271)
- `2026-03-02T06:26:06Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3874297766)
- `2026-03-02T14:09:53Z` `COMMENTED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3876469773)
- `2026-03-03T00:09:44Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3879481247)
- `2026-03-03T01:38:24Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3879692983)
- `2026-03-03T09:25:27Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3881301046)
- ... 14 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/visual_gen/config.py`: 11 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm.py`: 10 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`: 4 inline comment(s)
- `cpp/tensorrt_llm/thop/attentionOp.cpp`: 4 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaRunner.cpp`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/kernelParams.h`: 3 inline comment(s)
- `cpp/tensorrt_llm/common/attentionOp.cpp`: 3 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/kernelMetaInfoVx.h`: 3 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16HQk64HV64SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16HQk64HV64SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OE4m3HQk256HV256SeparateQkvDenseVarSeqQ128Kv128PersistentContext_cubin.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-25T14:02:16Z` `issue` by `coderabbitai`; signals: attention, blackwell, block, cuda, hang, kernel, sm100, tensorrt; excerpt: "📝 Walkthrough Walkthrough This PR introduces support for extended FMHA kernel variants by adding Git LFS pointers for numerous prebuilt CUDA kernel binaries and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#issuecomment-3959457534)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkvE4m3OBfloat16H128SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK1SageV1StaticContext_cubin.cpp`:3; signals: block, compile, cute, hang, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 498 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231574)
- `2026-03-02T02:27:59Z` `inline` by `xrq-phys` `cpp/tensorrt_llm/thop/attentionOp.cpp`:652; signals: attention, bf16, fp4, fp8, kernel, nvfp4, tensorrt; excerpt: "Thanks for the review. My understanding is that, AttentionOp accepts FP16/BF16 inputs, optionally quantizes them into FP8 or NVFP4, and carries out the attention ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2870235925)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OE4m3HQk256HV256SeparateQkvDenseVarSeqQ128Kv128PersistentContext_cubin.cpp`:3; signals: block, compile, hang, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Missing NVIDIA copyright header — but adding one would corrupt the Git LFS pointer. This file has a .cpp ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231569)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkvE4m3OBfloat16H64SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK1SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, cutlass, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1659 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231577)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkvE4m3OE4m3H256SeparateQkvDenseVarSeqQ128Kv128PersistentContext_cubin.cpp`:3; signals: compile, cute, kernel, pipeline, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 5762 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231590)
- `2026-02-25T14:02:24Z` `review` `COMMENTED` by `coderabbitai`; signals: block, compile, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 14 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3854464307)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16HQk64HV64SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK16SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 551 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231552)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkInt8VE4m3OBfloat16HQk64HV64SeparateQkvDenseVarSeqQ128Kv128SageQ1SageK4SageV1StaticContext_cubin.cpp`:3; signals: compile, cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231564)
- `2026-02-25T14:02:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QkvE4m3OE4m3H128SeparateQkvDenseVarSeqQ128Kv128StaticContext_cubin.cpp`:3; signals: cute, kernel, pipeline, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1628 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2853231583)
- `2026-02-26T07:15:20Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:1029; signals: attention, block, cute, kernel, tensorrt; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 3538 --- @xrq-phys, confirmed! The fix looks good. Line 1028 now correctly uses numEltsPerSageAttnBlkV for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#discussion_r2857333239)
- `2026-03-02T02:34:21Z` `review` `COMMENTED` by `PerkzZheng`; signals: attention, cache, kernel, kv cache; excerpt: "@xrq-phys do you know if this is required by any customers that are using TRTLLM ? I am wondering if we could just reuse ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11718#pullrequestreview-3873784449)
