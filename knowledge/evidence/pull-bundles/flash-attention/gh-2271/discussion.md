# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2271](https://github.com/Dao-AILab/flash-attention/pull/2271)
- Source page: `sources/prs/flash-attention/PR-2271.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2271`
- Generated at: `2026-05-20T15:16:48.369289+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-25T01:42:06Z`
- Merged: `2026-02-26T08:36:26Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: erikwijmans, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-25T05:15:24Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2271#pullrequestreview-3851909652)
- `2026-02-25T05:15:59Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2271#pullrequestreview-3851911372)
- `2026-02-25T17:15:12Z` `COMMENTED` by `erikwijmans` (https://github.com/Dao-AILab/flash-attention/pull/2271#pullrequestreview-3855628960)
- `2026-02-26T08:36:08Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2271#pullrequestreview-3859331463)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-02-25T05:15:24Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1281; signals: cute; excerpt: "we should document that the returned LSE currently doesn't support taking gradient. And we should mark it as nondifferentiable for now. We'll add support ..." (https://github.com/Dao-AILab/flash-attention/pull/2271#discussion_r2850888054)
- `2026-02-25T05:16:01Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1333; signals: cute; excerpt: "returning 20 Nones is ok" (https://github.com/Dao-AILab/flash-attention/pull/2271#discussion_r2850889482)
- `2026-02-25T17:15:12Z` `inline` by `erikwijmans` `flash_attn/cute/interface.py`:1281; signals: cute; excerpt: "Done!" (https://github.com/Dao-AILab/flash-attention/pull/2271#discussion_r2854315311)
- `2026-02-25T05:16:50Z` `issue` by `tridao`; signals: attention; excerpt: "Thanks! return lse is better. return attn probs was a confusing name (since we don't actually return the attention probabilities)." (https://github.com/Dao-AILab/flash-attention/pull/2271#issuecomment-3956889062)
