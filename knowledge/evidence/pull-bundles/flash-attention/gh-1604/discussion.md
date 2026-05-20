# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1604](https://github.com/Dao-AILab/flash-attention/pull/1604)
- Source page: `sources/prs/flash-attention/PR-1604.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1604`
- Generated at: `2026-05-20T15:16:32.553643+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-21T05:49:40Z`
- Merged: `2025-04-24T03:17:27Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 0 (no states)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Graham1025, ehuaa, shcho1118, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- No review submissions were returned by GitHub.

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-04-23T05:25:07Z` `issue` by `tridao`; signals: general review; excerpt: "The hdim dispatching should be based on max(params.d, params.d v) instead of based on params.d? E.g. if d = 128, d v = 192, ..." (https://github.com/Dao-AILab/flash-attention/pull/1604#issuecomment-2823096396)
- `2025-04-23T05:31:10Z` `issue` by `shcho1118`; signals: general review; excerpt: "I was initially thinking about the case where d = 192, d v = 128 like deepseek, but max(params.d, params.d v) would be more ..." (https://github.com/Dao-AILab/flash-attention/pull/1604#issuecomment-2823108831)
- `2025-04-23T06:45:28Z` `issue` by `shcho1118`; signals: general review; excerpt: "@tridao I took your advice and extended the support a bit more, now if max(params.d, params.dv) <= 256 it should work fine." (https://github.com/Dao-AILab/flash-attention/pull/1604#issuecomment-2823236391)
