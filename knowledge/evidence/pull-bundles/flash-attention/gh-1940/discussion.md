# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1940](https://github.com/Dao-AILab/flash-attention/pull/1940)
- Source page: `sources/prs/flash-attention/PR-1940.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1940`
- Generated at: `2026-05-20T15:16:35.894567+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-15T17:06:56Z`
- Merged: `2025-11-05T01:13:26Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 2 (approved=1, changes_requested=1)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Edenzzzz, jayhshah
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-04T00:20:17Z` `CHANGES_REQUESTED` by `jayhshah` - sm90 and sm80 fwd kernels now fails tests since BlockInfo isn't properly initialized. (https://github.com/Dao-AILab/flash-attention/pull/1940#pullrequestreview-3413165678)
- `2025-11-05T00:42:10Z` `APPROVED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1940#pullrequestreview-3419108644)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd.py`: 2 inline comment(s)
- `flash_attn/cute/flash_fwd_sm100.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-03T22:21:38Z` `inline` by `jayhshah` `flash_attn/cute/flash_fwd_sm100.py`:585; signals: cute, dtype, layout, sm100, tile; excerpt: "You'll have to scale cute.cosize(sO layout) by self.o dtype.width // self.q dtype.width, otherwise smem used for sO when writing out in fp32 bleeds into ..." (https://github.com/Dao-AILab/flash-attention/pull/1940#discussion_r2488028355)
- `2025-11-04T00:20:17Z` `review` `CHANGES_REQUESTED` by `jayhshah`; signals: block, kernel, sm90; excerpt: "sm90 and sm80 fwd kernels now fails tests since BlockInfo isn't properly initialized." (https://github.com/Dao-AILab/flash-attention/pull/1940#pullrequestreview-3413165678)
- `2025-11-04T00:20:09Z` `inline` by `jayhshah` `flash_attn/cute/flash_fwd.py`; signals: cute, kernel, sm90; excerpt: "This would also brick the sm80 kernel. You can fix by initializing is split kv to False by writing: We can add the split ..." (https://github.com/Dao-AILab/flash-attention/pull/1940#discussion_r2488237309)
- `2025-11-04T00:17:46Z` `inline` by `jayhshah` `flash_attn/cute/flash_fwd.py`; signals: block, cute, sm90; excerpt: "sm90 forward now fails tests since BlockInfo isn't properly initialized in this file." (https://github.com/Dao-AILab/flash-attention/pull/1940#discussion_r2488231183)
