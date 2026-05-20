# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2190](https://github.com/flashinfer-ai/flashinfer/pull/2190)
- Source page: `sources/prs/flashinfer/PR-2190.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2190`
- Generated at: `2026-05-20T15:24:18.355164+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T02:34:09Z`
- Merged: `2025-12-12T00:37:10Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: aleozlx, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T02:37:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to add support for MoE kernels on the SM110 architecture. The changes ... (https://github.com/flashinfer-ai/flashinfer/pull/2190#pullrequestreview-3555034936)
- `2025-12-10T01:50:21Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/moe gemm/moe gemm template dispatch.h (1) 797-803: ... (https://github.com/flashinfer-ai/flashinfer/pull/2190#pullrequestreview-3560396724)
- `2025-12-10T02:11:53Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2190#pullrequestreview-3560429620)
- `2025-12-10T22:59:04Z` `APPROVED` by `yzh119` - LGTM, should be ready to merge once gitlab CI passed. (https://github.com/flashinfer-ai/flashinfer/pull/2190#pullrequestreview-3564837365)

## Inline Comment Hotspots

- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch_tma_ws.h`: 2 inline comment(s)
- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-10T01:50:21Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, epilogue, gemm, hang, kernel, moe, sm100, tensorrt; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/moe gemm/moe gemm template dispatch.h (1) 797-803: Consider improving clarity of the SM ..." (https://github.com/flashinfer-ai/flashinfer/pull/2190#pullrequestreview-3560396724)
- `2025-12-09T02:34:14Z` `issue` by `coderabbitai`; signals: correctness, cute, cutlass, epilogue, flashinfer, gemm, hang, kernel; excerpt: "[!NOTE] Other AI code review bot(s) detected CodeRabbit has detected other AI code review bot(s) in this pull request and will avoid duplicating their ..." (https://github.com/flashinfer-ai/flashinfer/pull/2190#issuecomment-3629940634)
- `2025-12-11T22:34:01Z` `issue` by `aleozlx`; signals: pipeline; excerpt: "ci pipeline seems clean" (https://github.com/flashinfer-ai/flashinfer/pull/2190#issuecomment-3644074042)
