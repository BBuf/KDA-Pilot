# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13033](https://github.com/NVIDIA/TensorRT-LLM/pull/13033)
- Source page: `sources/prs/tensorrt-llm/PR-13033.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13033`
- Generated at: `2026-05-20T15:18:29.331611+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T09:31:08Z`
- Merged: `2026-04-18T13:32:25Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: Wanli-Jiang, coderabbitai, nv-guomingz, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-15T05:53:26Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4111123485)
- `2026-04-15T08:47:01Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4112111372)
- `2026-04-15T09:00:24Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4112205740)
- `2026-04-15T09:08:59Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4112265169)
- `2026-04-16T04:42:29Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118366595)
- `2026-04-16T04:42:34Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118366854)
- `2026-04-16T04:42:44Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118367309)
- `2026-04-16T04:43:08Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118368292)
- `2026-04-16T04:43:16Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118368620)
- `2026-04-16T06:35:28Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118742203)
- `2026-04-16T07:17:16Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4118954116)

## Inline Comment Hotspots

- `tests/unittest/_torch/modules/test_fused_add_rms_norm_quant.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_nemotron_h.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/fusedLayernormKernels/ws_layernorm.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-15T05:53:22Z` `issue` by `coderabbitai`; signals: fp4, hang, kernel, latency, memory, moe, nvfp4, tensorrt; excerpt: "📝 Walkthrough Walkthrough The changes modify fused layernorm/RMSNorm kernel implementations to conditionally gate output writes for out-of-bounds threads, enabling them to participate in warp-level ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#issuecomment-4249597186)
- `2026-04-15T05:53:26Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, fp4, hang, kernel, latency, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#pullrequestreview-4111123485)
- `2026-04-15T05:53:25Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/test_fused_add_rms_norm_quant.py`:368; signals: cute, fp4, regression, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 233 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3084272801)
- `2026-04-16T04:43:08Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/test_fused_add_rms_norm_quant.py`:368; signals: fp4, regression; excerpt: "@Wanli-Jiang, thanks for the update! The revised test fused add rms norm quant non power of 2 hidden now fully mirrors the consistency test ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3090816868)
- `2026-04-15T09:08:59Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/fusedLayernormKernels/ws_layernorm.cuh`:773; signals: kernel, tensorrt; excerpt: "Should we also add in bound check for USE BULK STORE case?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3085307311)
- `2026-04-16T04:43:16Z` `inline` by `Wanli-Jiang` `cpp/tensorrt_llm/kernels/fusedLayernormKernels/ws_layernorm.cuh`:773; signals: kernel, tensorrt; excerpt: "I added the check. For our current codes, seems USE BULK STORE is always false, BTW." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3090817221)
- `2026-04-15T08:47:01Z` `inline` by `yuxianq` `tensorrt_llm/_torch/models/modeling_nemotron_h.py`:403; signals: tensorrt; excerpt: "Can use hidden size directly instead of hs, which is hard to understand." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3085175993)
- `2026-04-16T04:42:34Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/models/modeling_nemotron_h.py`:403; signals: tensorrt; excerpt: "updated" (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#discussion_r3090815351)
- `2026-04-15T10:09:59Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 43398]( [ run ] completed with state SUCCESS. Commit: 57db189 [/LLM/main/L0 MergeRequest PR pipeline 33932]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#issuecomment-4251138712)
- `2026-04-16T05:23:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 43647]( [ run ] completed with state FAILURE. Commit: 576dda4 [/LLM/main/L0 MergeRequest PR pipeline 34135]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#issuecomment-4257565500)
- `2026-04-16T21:03:05Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 43752]( [ run ] completed with state FAILURE. Commit: 0d87134 [/LLM/main/L0 MergeRequest PR pipeline 34234]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#issuecomment-4263397386)
- `2026-04-18T13:30:50Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44088]( [ run ] completed with state SUCCESS. Commit: af4b29a [/LLM/main/L0 MergeRequest PR pipeline 34517]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13033#issuecomment-4273773620)
