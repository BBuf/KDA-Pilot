# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2489](https://github.com/Dao-AILab/flash-attention/pull/2489)
- Source page: `sources/prs/flash-attention/PR-2489.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2489`
- Generated at: `2026-05-20T15:17:09.697789+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-23T22:52:42Z`
- Merged: `2026-05-01T17:26:08Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Johnsonms, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-01T16:40:00Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2489#pullrequestreview-4212185825)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-30T21:00:06Z` `issue` by `Johnsonms`; signals: bf16, hang, kernel, latency, perf, tma, tmem, warp; excerpt: "Perf: halve page-table reads in TMA paged KV producer fe44ca87a11f4dab905add9fe6aa2cc26b56a3cf K and V share the same physical page, so the V-side mPageTable read was ..." (https://github.com/Dao-AILab/flash-attention/pull/2489#issuecomment-4356120315)
