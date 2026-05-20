# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1823](https://github.com/Dao-AILab/flash-attention/pull/1823)
- Source page: `sources/prs/flash-attention/PR-1823.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1823`
- Generated at: `2026-05-20T15:16:34.295273+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-19T00:59:43Z`
- Merged: `2025-08-22T02:44:03Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 0 (no states)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: jayhshah
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- No review submissions were returned by GitHub.

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-08-21T17:17:26Z` `issue` by `jayhshah`; signals: kernel, perf, tile; excerpt: "We don't tune the split heuristic yet, which could be improved. We should also use a persistent tile scheduler for the combine kernel in ..." (https://github.com/Dao-AILab/flash-attention/pull/1823#issuecomment-3211468919)
- `2025-08-22T02:36:55Z` `issue` by `jayhshah`; signals: perf; excerpt: "Numbers looking good for causal perf boost: [speeds mqa8.txt]( [speeds gqa8.txt]( [speeds mha.txt](" (https://github.com/Dao-AILab/flash-attention/pull/1823#issuecomment-3212835530)
