# PR Discussion Digest

- Source PR: [sgl-project/sglang#18858](https://github.com/sgl-project/sglang/pull/18858)
- Source page: `sources/prs/sglang/PR-18858.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18858`
- Generated at: `2026-05-20T15:28:42.865345+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-15T10:20:56Z`
- Merged: `2026-02-16T11:47:10Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: Kangyan-Zhou, b8zhong, mmangkad, vincentzed
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-02-15T10:24:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant performance optimization for Blackwell MXFP4 MoE weight loading, achieving an ... (https://github.com/sgl-project/sglang/pull/18858#pullrequestreview-3804328181)
- `2026-02-15T18:19:05Z` `APPROVED` by `b8zhong` - @mmangkad Thanks! Could you help show the perf is the same? As I believe the permute logics was ... (https://github.com/sgl-project/sglang/pull/18858#pullrequestreview-3805284132)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/mxfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-15T18:19:05Z` `review` `APPROVED` by `b8zhong`; signals: kernel, perf; excerpt: "@mmangkad Thanks! Could you help show the perf is the same? As I believe the permute logics was for better kernel efficiency" (https://github.com/sgl-project/sglang/pull/18858#pullrequestreview-3805284132)
- `2026-02-15T18:56:54Z` `issue` by `mmangkad`; signals: kernel, layout; excerpt: "@b8zhong as expected, this only optimizes weight loading and doesn't affect inference kernels - the final weight layout is identical. Before: After:" (https://github.com/sgl-project/sglang/pull/18858#issuecomment-3905002126)
