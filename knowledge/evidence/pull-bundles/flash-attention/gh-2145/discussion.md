# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2145](https://github.com/Dao-AILab/flash-attention/pull/2145)
- Source page: `sources/prs/flash-attention/PR-2145.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2145`
- Generated at: `2026-05-20T15:16:42.478163+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-07T00:21:56Z`
- Merged: `2026-01-10T01:40:52Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: drisspg, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-09T21:02:35Z` `APPROVED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2145#pullrequestreview-3645564575)
- `2026-01-10T01:01:30Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2145#pullrequestreview-3646071833)
- `2026-01-10T01:11:55Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2145#pullrequestreview-3646103158)
- `2026-01-10T01:40:30Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2145#pullrequestreview-3646205790)

## Inline Comment Hotspots

- `flash_attn/cute/block_sparse_utils.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-01-10T01:40:30Z` `inline` by `drisspg` `flash_attn/cute/block_sparse_utils.py`:121; signals: block, cute, perf; excerpt: "we dont have one in the fwd surprisngly, wired one up perf seems a lil negligible will leave as a follow up" (https://github.com/Dao-AILab/flash-attention/pull/2145#discussion_r2678136477)
- `2026-01-09T21:02:32Z` `inline` by `v0i0` `flash_attn/cute/block_sparse_utils.py`:121; signals: block, cute; excerpt: "would we ever want this to be a fast divmod? we might already have one flying around for gqa right?" (https://github.com/Dao-AILab/flash-attention/pull/2145#discussion_r2677615976)
- `2026-01-10T01:01:30Z` `inline` by `drisspg` `flash_attn/cute/block_sparse_utils.py`:121; signals: block, cute; excerpt: "let me look, not a bad idea" (https://github.com/Dao-AILab/flash-attention/pull/2145#discussion_r2678048100)
- `2026-01-10T01:11:55Z` `inline` by `drisspg` `flash_attn/cute/block_sparse_utils.py`:121; signals: block, cute; excerpt: "so we have one for bwd but not fwd .." (https://github.com/Dao-AILab/flash-attention/pull/2145#discussion_r2678069492)
