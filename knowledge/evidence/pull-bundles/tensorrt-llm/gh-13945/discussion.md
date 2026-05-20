# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13945](https://github.com/NVIDIA/TensorRT-LLM/pull/13945)
- Source page: `sources/prs/tensorrt-llm/PR-13945.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13945`
- Generated at: `2026-05-20T15:18:58.026539+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-09T14:06:35Z`
- Merged: `2026-05-11T06:36:50Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, djns99, tensorrt-cicd, yifeizhang-c
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-09T14:08:42Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#pullrequestreview-4257878258)
- `2026-05-10T22:39:43Z` `APPROVED` by `djns99` - LGTM if it resolves the issue. Do you have an understanding of why this regressed now and not ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#pullrequestreview-4260009602)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-09T14:08:41Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`:591; signals: benchmark, compile, cutlass, epilogue, gemm, hang, kernel, moe; excerpt: "🛠️ Refactor suggestion 🟠 Major ⚡ Quick win Add a compile-time guard to lock in the segfault fix. This type transformation is correct. Please ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#discussion_r3213251776)
- `2026-05-09T14:08:42Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, gemm, hang, kernel, moe, tensorrt, tma; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#pullrequestreview-4257878258)
- `2026-05-09T14:08:38Z` `issue` by `coderabbitai`; signals: cute, cutlass, epilogue, gemm, hang, kernel, memory, moe; excerpt: "📝 Walkthrough Walkthrough This PR updates the TMA warp-specialized MoE GEMM launcher to fix type deduction for EpilogueScalars. The change strips const/volatile qualifiers and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#issuecomment-4412709585)
- `2026-05-10T22:39:43Z` `review` `APPROVED` by `djns99`; signals: compile, cutlass, hang; excerpt: "LGTM if it resolves the issue. Do you have an understanding of why this regressed now and not previously, was there a CUTLASS/compiler change?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#pullrequestreview-4260009602)
- `2026-05-11T05:34:43Z` `issue` by `yifeizhang-c`; signals: compile, cutlass, hang; excerpt: "LGTM if it resolves the issue. Do you have an understanding of why this regressed now and not previously, was there a CUTLASS/compiler change? ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#issuecomment-4417844813)
- `2026-05-09T19:46:32Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47524]( [ run ] completed with state SUCCESS. Commit: 8c9dac1 [/LLM/main/L0 MergeRequest PR pipeline 37441]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#issuecomment-4413523885)
- `2026-05-11T04:04:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47642]( [ run ] completed with state SUCCESS. Commit: 8c9dac1 [/LLM/main/L0 MergeRequest PR pipeline 37546]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13945#issuecomment-4417523430)
