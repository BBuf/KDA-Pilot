# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2061](https://github.com/flashinfer-ai/flashinfer/pull/2061)
- Source page: `sources/prs/flashinfer/PR-2061.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2061`
- Generated at: `2026-05-20T15:23:56.373777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-07T05:35:21Z`
- Merged: `2025-11-07T22:54:43Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bkryu, coderabbitai, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-07T05:38:01Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/cutlass heuristic.cpp (1) 161-161: LGTM! Correct fix ... (https://github.com/flashinfer-ai/flashinfer/pull/2061#pullrequestreview-3431743818)
- `2025-11-07T05:38:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for the sm121 architecture for FP8 grouped GEMM operations. The change ... (https://github.com/flashinfer-ai/flashinfer/pull/2061#pullrequestreview-3431745145)
- `2025-11-07T06:54:21Z` `APPROVED` by `yzh119` - Thanks for working on the fix @yongwww ! (https://github.com/flashinfer-ai/flashinfer/pull/2061#pullrequestreview-3431958803)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-11-07T05:38:01Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, block, cutlass, fp8, gemm, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/cutlass heuristic.cpp (1) 161-161: LGTM! Correct fix for SM 121 support. The addition ..." (https://github.com/flashinfer-ai/flashinfer/pull/2061#pullrequestreview-3431743818)
- `2025-11-07T05:35:31Z` `issue` by `coderabbitai`; signals: benchmark, cutlass, fp8, gemm, hang, kernel, moe, pipeline; excerpt: "Walkthrough The SM check in get candidate tiles for FP8 with GROUPED GEMM was extended to include SM 121 alongside SM 89 and SM ..." (https://github.com/flashinfer-ai/flashinfer/pull/2061#issuecomment-3500820061)
- `2025-11-07T20:02:54Z` `issue` by `yzh119`; signals: hang; excerpt: "This PR was created before was merged, and it seems 2020 have updated the condition to: which address the CI failure. But this PR ..." (https://github.com/flashinfer-ai/flashinfer/pull/2061#issuecomment-3504662755)
- `2025-11-07T21:23:26Z` `issue` by `yongwww`; signals: general review; excerpt: "Thanks, @yzh119 for the insights! if (sm == 89 sm = 120) { should fix the issue for SM121 now, if (sm == 89 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2061#issuecomment-3505037100)
- `2025-11-07T21:53:58Z` `issue` by `bkryu`; signals: general review; excerpt: "Thanks, @yzh119 for the insights! if (sm == 89 sm = 120) { should fix the issue for SM121 now, if (sm == 89 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2061#issuecomment-3505126031)
