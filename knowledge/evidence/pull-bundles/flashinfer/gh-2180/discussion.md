# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2180](https://github.com/flashinfer-ai/flashinfer/pull/2180)
- Source page: `sources/prs/flashinfer/PR-2180.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2180`
- Generated at: `2026-05-20T15:24:18.349685+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-05T18:46:36Z`
- Merged: `2025-12-06T10:56:28Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bkryu, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-05T18:47:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request makes CUPTI the default timing mechanism for microbenchmarks, which is a good improvement ... (https://github.com/flashinfer-ai/flashinfer/pull/2180#pullrequestreview-3545985172)
- `2025-12-05T18:49:58Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (2) benchmarks/flashinfer benchmark.py (2) 79-89: Clarify deprecated --use cupti help to ... (https://github.com/flashinfer-ai/flashinfer/pull/2180#pullrequestreview-3545996834)
- `2025-12-06T01:24:20Z` `APPROVED` by `yzh119` - Thanks for the improvement, as far as I remember cupti only works for cuda 13. right, where should ... (https://github.com/flashinfer-ai/flashinfer/pull/2180#pullrequestreview-3546838743)

## Inline Comment Hotspots

- `benchmarks/flashinfer_benchmark.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-05T18:49:58Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, benchmark, cuda, flashinfer, hang, kernel; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (2) benchmarks/flashinfer benchmark.py (2) 79-89: Clarify deprecated --use cupti help to describe it as a no-op and ..." (https://github.com/flashinfer-ai/flashinfer/pull/2180#pullrequestreview-3545996834)
- `2025-12-05T18:46:47Z` `issue` by `coderabbitai`; signals: benchmark, cuda, flashinfer, hang; excerpt: "Walkthrough The benchmark script is updated to deprecate the --use cupti flag while introducing a new --use cuda events option for GPU timing. The ..." (https://github.com/flashinfer-ai/flashinfer/pull/2180#issuecomment-3618112496)
- `2025-12-06T01:58:23Z` `issue` by `bkryu`; signals: b200, cuda, flashinfer; excerpt: "Thanks for the improvement, as far as I remember cupti only works for cuda 13. right, where should we inform user about this limitation? ..." (https://github.com/flashinfer-ai/flashinfer/pull/2180#issuecomment-3619202305)
- `2025-12-06T01:24:20Z` `review` `APPROVED` by `yzh119`; signals: cuda; excerpt: "Thanks for the improvement, as far as I remember cupti only works for cuda 13. right, where should we inform user about this limitation?" (https://github.com/flashinfer-ai/flashinfer/pull/2180#pullrequestreview-3546838743)
