# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2095](https://github.com/flashinfer-ai/flashinfer/pull/2095)
- Source page: `sources/prs/flashinfer/PR-2095.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2095`
- Generated at: `2026-05-20T15:24:02.857659+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-15T04:13:34Z`
- Merged: `2025-11-16T22:40:46Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: coderabbitai, yongwww, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-15T04:14:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables Persistent Data Layout (PDL) for CUTLASS FP4 GEMM kernels on both sm ... (https://github.com/flashinfer-ai/flashinfer/pull/2095#pullrequestreview-3467643028)
- `2025-11-15T17:21:42Z` `APPROVED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/2095#pullrequestreview-3468226338)

## Inline Comment Hotspots

- `include/flashinfer/gemm/fp4_gemm_template_sm100.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-15T04:13:45Z` `issue` by `coderabbitai`; signals: blackwell, cutlass, flashinfer, fp4, gemm, hang, kernel, perf; excerpt: "Walkthrough The FP4 GEMM kernel launchers for SM100 and SM120 architectures are updated to enable PDL by changing the enablePDL flag from false to ..." (https://github.com/flashinfer-ai/flashinfer/pull/2095#issuecomment-3535716138)
