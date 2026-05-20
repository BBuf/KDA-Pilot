# PR Discussion Digest

- Source PR: [sgl-project/sglang#16961](https://github.com/sgl-project/sglang/pull/16961)
- Source page: `sources/prs/sglang/PR-16961.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16961`
- Generated at: `2026-05-20T15:28:23.540978+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-12T13:28:32Z`
- Merged: `2026-01-19T03:54:11Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 3 (commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, xu-yfei
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-12T13:30:36Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces two performance optimizations for Multi-Token Prediction (MTP) scenarios. First, it switches the ... (https://github.com/sgl-project/sglang/pull/16961#pullrequestreview-3650781181)
- `2026-01-16T12:37:09Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16961#pullrequestreview-3670685688)
- `2026-01-16T14:30:41Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/16961#pullrequestreview-3671149628)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/nsa_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-16T12:37:07Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/cuda_graph_runner.py`:208; signals: cuda; excerpt: "Maybe add a comment on why we take bs num tokens per bs % mul base == 0 here as condition?" (https://github.com/sgl-project/sglang/pull/16961#discussion_r2698361935)
- `2026-01-16T14:30:41Z` `inline` by `xu-yfei` `python/sglang/srt/model_executor/cuda_graph_runner.py`:208; signals: cuda; excerpt: "done" (https://github.com/sgl-project/sglang/pull/16961#discussion_r2698733387)
