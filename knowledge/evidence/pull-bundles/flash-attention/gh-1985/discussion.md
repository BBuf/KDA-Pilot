# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1985](https://github.com/Dao-AILab/flash-attention/pull/1985)
- Source page: `sources/prs/flash-attention/PR-1985.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1985`
- Generated at: `2026-05-20T15:16:37.364106+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T00:23:13Z`
- Merged: `2025-11-18T00:58:03Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: drisspg, reubenconducts, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T00:23:45Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3419072571)
- `2025-11-05T00:24:27Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3419073676)
- `2025-11-11T04:56:10Z` `COMMENTED` by `reubenconducts` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3446247970)
- `2025-11-11T05:30:21Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3446322933)
- `2025-11-12T01:12:29Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3450792747)
- `2025-11-12T20:26:35Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3455357352)
- `2025-11-18T00:57:55Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1985#pullrequestreview-3475092474)

## Inline Comment Hotspots

- `flash_attn/cute/block_sparse_utils.py`: 3 inline comment(s)
- `flash_attn/cute/flash_fwd_sm100.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-11T04:56:10Z` `inline` by `reubenconducts` `flash_attn/cute/block_sparse_utils.py`:646; signals: block, cute, sm100, tma; excerpt: "I find this name a bit confusing, since "consume" is ambiguous -- my $0.02 would be to have softmax block sparse sm100 and load ..." (https://github.com/Dao-AILab/flash-attention/pull/1985#discussion_r2512838003)
- `2025-11-05T00:24:27Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1148; signals: cute, hang, sm100; excerpt: "I hate that github renders it this way, ill change to not use so its easier to review" (https://github.com/Dao-AILab/flash-attention/pull/1985#discussion_r2492399315)
- `2025-11-12T01:12:29Z` `inline` by `drisspg` `flash_attn/cute/block_sparse_utils.py`:578; signals: block, cute; excerpt: "had to dupe alot here but still think its better, having very large IF Else indents makes it harder to rebase / iterate on ..." (https://github.com/Dao-AILab/flash-attention/pull/1985#discussion_r2516321911)
- `2025-11-05T00:23:45Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:885; signals: cute, sm100; excerpt: "delete" (https://github.com/Dao-AILab/flash-attention/pull/1985#discussion_r2492398376)
- `2025-11-11T05:30:21Z` `inline` by `drisspg` `flash_attn/cute/block_sparse_utils.py`:646; signals: block, cute; excerpt: "great point, will update" (https://github.com/Dao-AILab/flash-attention/pull/1985#discussion_r2512902081)
- `2025-11-14T03:26:38Z` `issue` by `drisspg`; signals: perf; excerpt: "@tridao Okay, finally rebased, perf looks good and tests are green" (https://github.com/Dao-AILab/flash-attention/pull/1985#issuecomment-3530663514)
