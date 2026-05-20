# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2404](https://github.com/flashinfer-ai/flashinfer/pull/2404)
- Source page: `sources/prs/flashinfer/PR-2404.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2404`
- Generated at: `2026-05-20T15:24:43.794169+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-22T21:58:56Z`
- Merged: `2026-01-26T07:34:03Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bkryu, claude, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-22T22:01:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the backend selection heuristic for FP4 GEMM operations to prioritize CUTLASS on ... (https://github.com/flashinfer-ai/flashinfer/pull/2404#pullrequestreview-3694781102)
- `2026-01-25T23:53:01Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2404#pullrequestreview-3704330606)

## Inline Comment Hotspots

- `flashinfer/gemm/gemm_base.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-22T21:59:22Z` `issue` by `coderabbitai`; signals: cuda, cutlass, flashinfer, fp4, gemm, hang, perf, sm100; excerpt: "📝 Walkthrough Walkthrough The heuristic func mm fp4 backend selection heuristic in flashinfer/gemm/gemm base.py has been modified to distinguish between SM103 and SM100 GPUs ..." (https://github.com/flashinfer-ai/flashinfer/pull/2404#issuecomment-3786966246)
- `2026-01-22T22:01:08Z` `issue` by `claude`; signals: b200, benchmark, blackwell, correctness, cuda, cutlass, flashinfer, fp4; excerpt: "Code Review for PR 2404 Summary This PR updates the backend selection heuristic for mm fp4 to prefer CUTLASS over cuDNN on SM103 (B300) ..." (https://github.com/flashinfer-ai/flashinfer/pull/2404#issuecomment-3786971749)
