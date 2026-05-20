# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2470](https://github.com/Dao-AILab/flash-attention/pull/2470)
- Source page: `sources/prs/flash-attention/PR-2470.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2470`
- Generated at: `2026-05-20T15:17:08.330297+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-17T19:31:43Z`
- Merged: `2026-04-20T16:40:44Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Johnsonms, jayhshah
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-17T21:12:40Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2470#pullrequestreview-4132145137)
- `2026-04-20T05:23:58Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2470#pullrequestreview-4137447543)
- `2026-04-20T16:38:11Z` `APPROVED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2470#pullrequestreview-4141816344)

## Inline Comment Hotspots

- `tests/cute/test_flash_attn.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-20T05:23:03Z` `issue` by `Johnsonms`; signals: hang, kernel, race, tile, tma; excerpt: "Is this specifically about seqlen k = 0? For varlen k, we were always testing possibly zero length seqlen k batches (tests pass on ..." (https://github.com/Dao-AILab/flash-attention/pull/2470#issuecomment-4278022018)
- `2026-04-17T21:12:40Z` `inline` by `jayhshah` `tests/cute/test_flash_attn.py`:2427; signals: block, cute; excerpt: "Don't we already prevent this via n block first = n block max - 1 if n block max 0 else 0?" (https://github.com/Dao-AILab/flash-attention/pull/2470#discussion_r3103293554)
- `2026-04-20T05:23:58Z` `inline` by `Johnsonms` `tests/cute/test_flash_attn.py`:2427; signals: cute, perf; excerpt: "Yes, it is exactly and perfect. Thanks @jayhshah leading me here" (https://github.com/Dao-AILab/flash-attention/pull/2470#discussion_r3108420462)
- `2026-04-17T21:03:25Z` `issue` by `jayhshah`; signals: kernel; excerpt: "Is this specifically about seqlen k = 0? For varlen k, we were always testing possibly zero length seqlen k batches (tests pass on ..." (https://github.com/Dao-AILab/flash-attention/pull/2470#issuecomment-4271245771)
