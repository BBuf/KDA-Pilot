# PR Discussion Digest

- Source PR: [deepseek-ai/DeepGEMM#95](https://github.com/deepseek-ai/DeepGEMM/pull/95)
- Source page: `sources/prs/deepgemm/PR-95.md`
- Evidence bundle: `evidence/pull-bundles/deepgemm/gh-95`
- Generated at: `2026-05-20T15:21:33.379230+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-06T09:19:15Z`
- Merged: `2025-05-14T06:47:58Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LyricZhao, heuristicoder, hxdtest, zheanxu
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-05-14T06:46:35Z` `APPROVED` by `LyricZhao` (https://github.com/deepseek-ai/DeepGEMM/pull/95#pullrequestreview-2838941243)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-05-09T05:25:56Z` `issue` by `LyricZhao`; signals: cutlass, kernel, perf, performance, speedup; excerpt: "These kernels achieve a 20% speedup compared to the internal CUTLASS implementation. To clarify, you can refer to the [profile-data]( repo for internal CUTLASS ..." (https://github.com/deepseek-ai/DeepGEMM/pull/95#issuecomment-2865162912)
- `2025-05-13T07:01:15Z` `issue` by `zheanxu`; signals: fp8, gemm, perf; excerpt: "@hxdtest Thank you very much for your feedback. During backpropagation, W needs to accumulate W grad, so deep gemm.wgrad gemm fp8 fp8 fp32 nt(x, ..." (https://github.com/deepseek-ai/DeepGEMM/pull/95#issuecomment-2875277255)
- `2025-05-14T03:52:05Z` `issue` by `hxdtest`; signals: fp8, gemm, perf; excerpt: "@hxdtest Thank you very much for your feedback. During backpropagation, W needs to accumulate W grad, so deep gemm.wgrad gemm fp8 fp8 fp32 nt(x, ..." (https://github.com/deepseek-ai/DeepGEMM/pull/95#issuecomment-2878572997)
