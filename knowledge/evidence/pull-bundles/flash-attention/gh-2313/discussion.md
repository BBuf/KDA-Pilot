# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2313](https://github.com/Dao-AILab/flash-attention/pull/2313)
- Source page: `sources/prs/flash-attention/PR-2313.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2313`
- Generated at: `2026-05-20T15:16:51.285641+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-07T00:38:41Z`
- Merged: `2026-03-12T04:09:39Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Alkaid-Benetnash, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-11T18:16:03Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2313#pullrequestreview-3931545684)
- `2026-03-11T21:54:53Z` `COMMENTED` by `Alkaid-Benetnash` (https://github.com/Dao-AILab/flash-attention/pull/2313#pullrequestreview-3932771990)
- `2026-03-12T04:08:56Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2313#pullrequestreview-3933780891)

## Inline Comment Hotspots

- `flash_attn/cute/mask.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-11T17:24:42Z` `issue` by `Alkaid-Benetnash`; signals: benchmark, compile, perf, tma; excerpt: "Thanks for the quick reply! --- if we were to move by 24 instead of 32, would this generate the same code as before? ..." (https://github.com/Dao-AILab/flash-attention/pull/2313#issuecomment-4040843870)
- `2026-03-11T21:54:53Z` `inline` by `Alkaid-Benetnash` `flash_attn/cute/mask.py`:467; signals: cute, hang; excerpt: "Hi, this is not a critical change and I am happy to revert if it bothers you. The reason is to make causal row ..." (https://github.com/Dao-AILab/flash-attention/pull/2313#discussion_r2921202646)
- `2026-03-11T21:45:30Z` `issue` by `Alkaid-Benetnash`; signals: block, compile; excerpt: "since s is a compile time constant we would expect 1 int subtraction and max (i.e. 1 VIADDMNMX instruction), and 1 SHF.R instruction? Yes, ..." (https://github.com/Dao-AILab/flash-attention/pull/2313#issuecomment-4042428318)
- `2026-03-11T18:16:03Z` `inline` by `tridao` `flash_attn/cute/mask.py`:467; signals: cute; excerpt: "Whats the reason for removing the +1 to causal row offset and then add 1 to col limit right and local row offset right?" (https://github.com/Dao-AILab/flash-attention/pull/2313#discussion_r2920121644)
- `2026-03-11T17:01:10Z` `issue` by `tridao`; signals: perf; excerpt: "Conceptual question: if we were to move by 24 instead of 32, would this generate the same code as before? If so, then the ..." (https://github.com/Dao-AILab/flash-attention/pull/2313#issuecomment-4040698257)
- `2026-03-11T18:13:38Z` `issue` by `tridao`; signals: compile; excerpt: "I see. For since s is a compile time constant we would expect 1 int subtraction and max (i.e. 1 VIADDMNMX instruction), and 1 ..." (https://github.com/Dao-AILab/flash-attention/pull/2313#issuecomment-4041163671)
