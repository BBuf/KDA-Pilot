# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2329](https://github.com/Dao-AILab/flash-attention/pull/2329)
- Source page: `sources/prs/flash-attention/PR-2329.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2329`
- Generated at: `2026-05-20T15:16:51.287771+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-11T18:57:49Z`
- Merged: `2026-03-12T12:13:32Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: mmdbhs, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-11T19:18:03Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2329#pullrequestreview-3931945033)
- `2026-03-11T19:18:21Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2329#pullrequestreview-3931946955)
- `2026-03-11T19:19:29Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2329#pullrequestreview-3931956317)
- `2026-03-12T12:13:23Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2329#pullrequestreview-3936098856)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-11T19:19:29Z` `inline` by `tridao` `flash_attn/cute/interface.py`:661; signals: cute, epilogue, sm90; excerpt: "i think the epilogue code between sm80 and sm90 have the same checks. In any case, for sm80 we should put a if constexpr ..." (https://github.com/Dao-AILab/flash-attention/pull/2329#discussion_r2920460730)
- `2026-03-11T19:18:03Z` `inline` by `tridao` `flash_attn/cute/interface.py`:633; signals: cute, hang; excerpt: "we should just change the sm80 call signature" (https://github.com/Dao-AILab/flash-attention/pull/2329#discussion_r2920452213)
- `2026-03-11T19:18:21Z` `inline` by `tridao` `flash_attn/cute/interface.py`:670; signals: cute, hang; excerpt: "let's change the sm80 call signature" (https://github.com/Dao-AILab/flash-attention/pull/2329#discussion_r2920453887)
