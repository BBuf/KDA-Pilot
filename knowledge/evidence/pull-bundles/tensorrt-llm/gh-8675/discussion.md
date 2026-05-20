# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#8675](https://github.com/NVIDIA/TensorRT-LLM/pull/8675)
- Source page: `sources/prs/tensorrt-llm/PR-8675.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-8675`
- Generated at: `2026-05-20T15:19:19.676013+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-27T02:35:04Z`
- Merged: `2025-10-28T23:56:48Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 14 (approved=3, commented=11)
- Inline review comments: 16
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=6
- Human participants with discussion text: bobboli, coderabbitai, dongxuy04, kaiyux, tensorrt-cicd, xxi-nv, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-27T02:40:12Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3381641844)
- `2025-10-27T02:40:37Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3381642238)
- `2025-10-27T02:51:28Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3381653438)
- `2025-10-27T09:21:28Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3382489414)
- `2025-10-27T09:29:51Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3382540823)
- `2025-10-28T00:22:14Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386047872)
- `2025-10-28T00:43:49Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386078682)
- `2025-10-28T00:44:56Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386080005)
- `2025-10-28T00:47:05Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386082466)
- `2025-10-28T02:21:26Z` `APPROVED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386259848)
- `2025-10-28T02:30:36Z` `APPROVED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3386306687)
- `2025-10-28T11:08:33Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3388142971)
- `2025-10-28T11:08:46Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3388143825)
- `2025-10-28T11:09:37Z` `COMMENTED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3388148279)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 8 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/utils.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/py_executor.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-27T02:40:37Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cute, cutlass, dtype, fp4, hang, latency, memory; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#pullrequestreview-3381642238)
- `2025-10-27T02:40:32Z` `issue` by `coderabbitai`; signals: attention, correctness, cutlass, dtype, hang, kernel, latency, memory; excerpt: "📝 Walkthrough Walkthrough The changes centralize the AlltoallMethodType enum into a shared utility module and introduce alltoall method selection logic across two fused MoE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#issuecomment-3449286308)
- `2025-10-27T02:40:36Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:171; signals: cuda, cute, cutlass, dtype, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain Scan repo for other mismatched select alltoall method type calls To avoid similar TypeErrors elsewhere, search ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464296338)
- `2025-10-28T02:28:57Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:5; signals: cutlass, latency, moe, tensorrt, throughput; excerpt: "MnnvlThroughput has just been merged The previous MNNVL AlltoAll is rebranded as MnnvlLatency. You may need to solve the conflicts in this file. Sorry ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2467683496)
- `2025-10-27T02:40:35Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:149; signals: block, cutlass, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Blocker: select alltoall method type call signature mismatch Method takes only self, but call passes 4 args - runtime ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464296332)
- `2025-10-27T02:40:36Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:133; signals: benchmark, cutlass, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Fix class name in NotImplementedError Message references CutlassFusedMoE; should mention TRTLLMGenFusedMoE. 📝 Committable suggestion ‼️ IMPORTANT Carefully review the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464296342)
- `2025-10-28T00:22:14Z` `inline` by `yuxianq` `tensorrt_llm/_torch/utils.py`:320; signals: dtype, moe, tensorrt; excerpt: "Maybe move AlltoallMethodType to tensorrt llm/ torch/modules/fused moe/interface.py like MoEWeightLoadingMode is better." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2467510640)
- `2025-10-28T02:30:32Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:653; signals: moe, tensorrt, throughput; excerpt: "BTW, do you think we should add low precision combine to MnnvlThroughput in the future? This is a feature gap. cc @dongxuy04" (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2467689929)
- `2025-10-28T11:08:46Z` `inline` by `kaiyux` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:5; signals: cutlass, moe, tensorrt; excerpt: "Rebased." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2469097836)
- `2025-10-27T02:40:36Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/utils.py`:5; signals: benchmark, tensorrt; excerpt: "🛠️ Refactor suggestion 🟠 Major Add NVIDIA Apache-2.0 header (2025) at file top Required by coding guidelines; currently missing. Apply at the top of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464296346)
- `2025-10-27T02:51:28Z` `inline` by `kaiyux` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:113; signals: moe, tensorrt; excerpt: "Since @xxi-nv has already started the refactor work, I can follow his suggestion to make the life easier for him : ) @xxi-nv Do ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464306041)
- `2025-10-27T09:21:28Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:113; signals: moe, tensorrt; excerpt: "Fell free to do in your efficient way. I am writing an design doc and maybe we can have a sync this Wednesday. Anyway, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8675#discussion_r2464934030)
