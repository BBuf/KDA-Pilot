# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14106](https://github.com/NVIDIA/TensorRT-LLM/pull/14106)
- Source page: `sources/prs/tensorrt-llm/PR-14106.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14106`
- Generated at: `2026-05-20T15:19:02.335621+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-13T23:19:03Z`
- Merged: `2026-05-14T22:11:55Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: coderabbitai, govind-ramnarayan, tensorrt-cicd, yuanjingx87
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-13T23:26:26Z` `APPROVED` by `govind-ramnarayan` (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#pullrequestreview-4286020861)
- `2026-05-13T23:33:24Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#pullrequestreview-4286048358)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/custom_ops/normalization/flashinfer_fused_add_rms_norm.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/torch_libs/float8_python_api.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/mla_rope_utils.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_deepseek.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_glm4_moe_lite.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/fused_add_rms_norm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-13T23:33:24Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, cuda, cudagraph, deepgemm, dtype; excerpt: "Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#pullrequestreview-4286048358)
- `2026-05-13T23:33:18Z` `issue` by `coderabbitai`; signals: attention, cache, compile, cuda, cute, dtype, flashinfer, fp4; excerpt: "📝 Walkthrough Walkthrough This PR adds SPDX licensing across the AutoDeploy codebase, introduces a modular export-patch system for torch.export compatibility with multiple patch implementations, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#issuecomment-4446009438)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/models/custom/mla_rope_utils.py`:1; signals: benchmark, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Update copyright year to latest modification year. Line 1 still uses 2025, but this file is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042171)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_glm4_moe_lite.py`:1; signals: benchmark, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Update the copyright year to latest modification year (2026). This file is modified in this PR, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042186)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/normalization/flashinfer_fused_add_rms_norm.py`:1; signals: flashinfer, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Update SPDX copyright year to latest modification year (2026). This file is modified in this PR, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042140)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/torch_libs/float8_python_api.py`:7; signals: benchmark, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Update copyright year to 2026. The SPDX copyright header uses year 2025, but this file is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042144)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_add_rms_norm.py`:1; signals: benchmark, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Update copyright year to latest modification year (2026). This file is modified in this PR, but ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042202)
- `2026-05-13T23:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_deepseek.py`:1; signals: tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Update modified-year in SPDX header. Line 1 should include the latest modification year (2026) for this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#discussion_r3238042179)
- `2026-05-14T21:51:28Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 48440]( [ skip ] completed with state SUCCESS. Commit: e039b54 Skipping testing for commit e039b54 [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14106#issuecomment-4455021839)
