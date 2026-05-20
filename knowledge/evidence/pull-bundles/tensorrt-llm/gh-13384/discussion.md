# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13384](https://github.com/NVIDIA/TensorRT-LLM/pull/13384)
- Source page: `sources/prs/tensorrt-llm/PR-13384.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13384`
- Generated at: `2026-05-20T15:18:37.776867+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-23T14:15:13Z`
- Merged: `2026-05-08T04:49:11Z`

## Discussion Counts

- Issue comments: 32
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=0
- Human participants with discussion text: Barry-Delaney, coderabbitai, juney-nvidia, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-27T09:33:31Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#pullrequestreview-4179753523)
- `2026-04-27T09:35:06Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 5 🧹 Nitpick comments (5) tensorrt llm/ torch/modules/fused moe/mega moe/backend.py (3) 209-209: Mutable class attribute ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#pullrequestreview-4179764287)
- `2026-04-28T05:12:28Z` `APPROVED` by `juney-nvidia` - Approved from oss compliance perspective. (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#pullrequestreview-4186014890)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/mega_moe/backend.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-27T09:35:01Z` `issue` by `coderabbitai`; signals: bf16, deepgemm, fp4, fp8, gemm, hang, kernel, moe; excerpt: "📝 Walkthrough Walkthrough This PR introduces a new MegaMoE backend for fused MoE operations powered by DeepGEMM, updating the deepgemm dependency to a newer ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4325824248)
- `2026-04-27T09:35:06Z` `review` `COMMENTED` by `coderabbitai`; signals: alignment, dtype, gemm, hang, moe, tensorrt; excerpt: "Actionable comments posted: 5 🧹 Nitpick comments (5) tensorrt llm/ torch/modules/fused moe/mega moe/backend.py (3) 209-209: Mutable class attribute should use frozenset. Using a mutable ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#pullrequestreview-4179764287)
- `2026-04-27T09:35:05Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/mega_moe/backend.py`:758; signals: cute, deepgemm, gemm, hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 5574 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#discussion_r3146273235)
- `2026-04-27T07:21:39Z` `issue` by `xxi-nv`; signals: deepgemm, gemm, kernel, moe, perf, performance; excerpt: "Discussed with @Barry-Delaney. Considering that Barry has tested the functionality locally and we are in a hurry for performance, it is suggested to rename ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4325002222)
- `2026-04-27T09:35:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:714; signals: bf16, fp8, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Inconsistent x sf shape for zero-token placeholder. The x sf tensor is created with shape (0, 0), but per ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#discussion_r3146273202)
- `2026-04-27T09:35:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`:379; signals: deepgemm, gemm, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major This new backend still bypasses ConfigurableMoE. With ENABLE CONFIGURABLE MOE=1, create moe() does not route MegaMoEDeepGemmFusedMoE through the ConfigurableMoE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#discussion_r3146273222)
- `2026-04-27T09:35:05Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/mega_moe/backend.py`:14; signals: gemm, moe, pipeline, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Pipeline failure: File needs ruff format. The CI indicates this file was reformatted by ruff-format. Please run ruff format ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#discussion_r3146273227)
- `2026-04-27T09:35:04Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`:119; signals: dtype, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Pass the real activation dtype and MoE FFN size into can implement(). This guard currently hardcodes torch.bfloat16 and the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#discussion_r3146273215)
- `2026-04-27T10:03:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45701]( [ run ] completed with state FAILURE. Commit: 4ce2c3c [/LLM/main/L0 MergeRequest PR pipeline 35904]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4326013850)
- `2026-04-30T17:59:28Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46255]( [ run ] completed with state SUCCESS. Commit: 660acf2 [/LLM/main/L0 MergeRequest PR pipeline 36364]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4354898572)
- `2026-05-05T10:58:32Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46755]( [ run ] completed with state SUCCESS. Commit: e7bfb23 [/LLM/main/L0 MergeRequest PR pipeline 36782]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4378600588)
- `2026-05-08T03:41:37Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47245]( [ run ] completed with state SUCCESS. Commit: e7d80e9 [/LLM/main/L0 MergeRequest PR pipeline 37194]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13384#issuecomment-4403109874)
