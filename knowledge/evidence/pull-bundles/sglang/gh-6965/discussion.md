# PR Discussion Digest

- Source PR: [sgl-project/sglang#6965](https://github.com/sgl-project/sglang/pull/6965)
- Source page: `sources/prs/sglang/PR-6965.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6965`
- Generated at: `2026-05-20T15:30:56.480692+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-08T02:38:20Z`
- Merged: `2025-06-08T12:09:17Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 6 (approved=2, changes_requested=1, commented=3)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: merrymercy
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-08T02:38:39Z` `COMMENTED` by `gemini-code-assist` - Hello @fzyzcjy, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908046633)
- `2025-06-08T02:39:50Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request aims to optimize the handling of num token non padded by making its ... (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908047016)
- `2025-06-08T02:54:26Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908056945)
- `2025-06-08T09:11:53Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908295571)
- `2025-06-08T09:12:52Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908296774)
- `2025-06-08T09:45:51Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6965#pullrequestreview-2908319030)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 3 inline comment(s)
- `python/sglang/srt/model_executor/forward_batch_info.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-08T02:54:23Z` `inline` by `merrymercy` `python/sglang/srt/model_executor/cuda_graph_runner.py`:555; signals: cuda; excerpt: "copy from forward batch.num token non padded is better because it is GPU-GPU copy, this statement incurs some GPU-CPU copy" (https://github.com/sgl-project/sglang/pull/6965#discussion_r2134359585)
