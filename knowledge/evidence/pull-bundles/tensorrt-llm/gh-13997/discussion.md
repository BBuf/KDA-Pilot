# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13997](https://github.com/NVIDIA/TensorRT-LLM/pull/13997)
- Source page: `sources/prs/tensorrt-llm/PR-13997.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13997`
- Generated at: `2026-05-20T15:19:00.105714+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T11:33:02Z`
- Merged: `2026-05-13T09:22:02Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: coderabbitai, galagam, tcherckez-nvidia, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T11:40:13Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#pullrequestreview-4263272719)
- `2026-05-11T13:18:59Z` `APPROVED` by `galagam` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#pullrequestreview-4263283083)
- `2026-05-11T13:20:54Z` `COMMENTED` by `tcherckez-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#pullrequestreview-4263986539)
- `2026-05-12T11:50:27Z` `COMMENTED` by `tcherckez-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#pullrequestreview-4271948319)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`: 4 inline comment(s)
- `tests/unittest/auto_deploy/singlegpu/transformations/library/test_moe_fusion.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-11T11:40:13Z` `review` `COMMENTED` by `coderabbitai`; signals: fp4, hang, latency, moe, nvfp4, perf, performance, regression; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#pullrequestreview-4263272719)
- `2026-05-11T11:40:09Z` `issue` by `coderabbitai`; signals: alignment, cuda, cute, fp4, hang, kernel, memory, moe; excerpt: "📝 Walkthrough Walkthrough This PR adds internal routing support to TRTLLM-Gen MoE fusion and introduces auxiliary stream scheduling for shared experts. It extends the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4420336358)
- `2026-05-11T11:40:12Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2; signals: hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add the NVIDIA copyright header to this modified Python file. This file is being changed but ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#discussion_r3218561157)
- `2026-05-11T11:42:07Z` `inline` by `galagam` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2879; signals: moe, tensorrt; excerpt: "Why is DeepSeekV3 mentioned here specifically?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#discussion_r3218571301)
- `2026-05-11T13:20:54Z` `inline` by `tcherckez-nvidia` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2879; signals: moe, tensorrt; excerpt: "type of MoE" (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#discussion_r3219207709)
- `2026-05-11T11:40:12Z` `inline` by `coderabbitai` `tests/unittest/auto_deploy/singlegpu/transformations/library/test_moe_fusion.py`:2; signals: moe; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add the NVIDIA copyright header to this modified Python file. This test file is part of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#discussion_r3218561165)
- `2026-05-11T16:34:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47733]( [ run ] completed with state SUCCESS. Commit: 39322a9 [/LLM/main/L0 MergeRequest PR pipeline 37628]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4422699134)
- `2026-05-12T10:53:00Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47892]( [ run ] completed with state SUCCESS. Commit: 66129fd [/LLM/main/L0 MergeRequest PR pipeline 37743]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4429766765)
- `2026-05-12T16:53:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47961]( [ run ] completed with state SUCCESS. Commit: 341c725 [/LLM/main/L0 MergeRequest PR pipeline 37802]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4432834725)
- `2026-05-13T09:21:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48135]( [ run ] completed with state SUCCESS. Commit: 341c725 [/LLM/main/L0 MergeRequest PR pipeline 37960]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4439366766)
- `2026-05-11T11:34:02Z` `issue` by `tcherckez-nvidia`; signals: b200, h100; excerpt: "/bot run --extra-stage "DGX B200-4 GPUs-AutoDeploy-1, DGX H100-4 GPUs-AutoDeploy-1"" (https://github.com/NVIDIA/TensorRT-LLM/pull/13997#issuecomment-4420291833)
