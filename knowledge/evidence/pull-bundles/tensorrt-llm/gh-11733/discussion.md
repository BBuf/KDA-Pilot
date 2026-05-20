# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11733](https://github.com/NVIDIA/TensorRT-LLM/pull/11733)
- Source page: `sources/prs/tensorrt-llm/PR-11733.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11733`
- Generated at: `2026-05-20T15:17:51.116006+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-26T03:39:21Z`
- Merged: `2026-02-26T08:00:12Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, litaotju, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-26T03:44:24Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#pullrequestreview-3858229892)
- `2026-02-26T04:35:50Z` `APPROVED` by `litaotju` - Auto-approved by AI (on behalf of Tao Li) This PR has been reviewed and approved automatically based on: ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#pullrequestreview-3858360427)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-26T03:44:19Z` `issue` by `coderabbitai`; signals: block, compile, cuda, cutlass, dtype, fp4, fp8, gemm; excerpt: "📝 Walkthrough Walkthrough The doActivationKernel signature is refactored to add CUDA launch bounds annotation and modify parameter handling, including removal of the use per ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#issuecomment-3963781236)
- `2026-02-26T04:35:50Z` `review` `APPROVED` by `litaotju`; signals: cutlass, dtype, fp4, moe, mxfp4, nvfp4, perf, regression; excerpt: "Auto-approved by AI (on behalf of Tao Li) This PR has been reviewed and approved automatically based on: • Scope: fix for CUTLASS MoE ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#pullrequestreview-3858360427)
- `2026-02-26T03:44:24Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, gemm, hang, kernel, moe, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#pullrequestreview-3858229892)
- `2026-02-26T03:44:22Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`:2303; signals: cutlass, gemm, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Prevent out-of-bounds read in SF padding prefetch. At Line 2299, clamping to num padding tokens allows expert == num ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#discussion_r2856717333)
- `2026-02-26T08:00:08Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36865]( [ run ] completed with state SUCCESS. Commit: 3ebc523 [/LLM/release-1.2/L0 MergeRequest PR pipeline 403]( completed with status: 'SUCCESS' [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/11733#issuecomment-3964811713)
