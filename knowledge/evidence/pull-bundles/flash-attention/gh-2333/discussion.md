# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2333](https://github.com/Dao-AILab/flash-attention/pull/2333)
- Source page: `sources/prs/flash-attention/PR-2333.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2333`
- Generated at: `2026-05-20T15:16:52.692416+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T05:07:14Z`
- Merged: `2026-03-13T10:56:45Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: blake-snc, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T21:33:45Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2333#pullrequestreview-3939897026)
- `2026-03-12T22:02:21Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2333#pullrequestreview-3940016298)
- `2026-03-12T22:02:59Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2333#pullrequestreview-3940019492)
- `2026-03-13T10:56:40Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2333#pullrequestreview-3943178575)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd.py`: 2 inline comment(s)
- `flash_attn/cute/interface.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-12T21:49:18Z` `issue` by `blake-snc`; signals: aligned, block, kernel, tile; excerpt: "Removed the cu seqlens padding in 8093403. It was unnecessary — SingleTileVarlenScheduler already guards OOB reads: get num m blocks() checks batch idx <= ..." (https://github.com/Dao-AILab/flash-attention/pull/2333#issuecomment-4050411194)
- `2026-03-12T21:33:45Z` `inline` by `tridao` `flash_attn/cute/interface.py`:302; signals: cute, hang; excerpt: "This is very expensive because it causes a gpu-cpu sync. We should avoid changing cu seqlens q" (https://github.com/Dao-AILab/flash-attention/pull/2333#discussion_r2927526203)
- `2026-03-12T22:11:30Z` `issue` by `blake-snc`; signals: layout, sm90; excerpt: "Fixed in 74e13f8. Updated the scheduler selection condition to mCuSeqlensQ is not None or mSeqUsedQ is not None (matching SM90 forward on main), and ..." (https://github.com/Dao-AILab/flash-attention/pull/2333#issuecomment-4050526625)
- `2026-03-12T22:02:22Z` `inline` by `tridao` `flash_attn/cute/flash_fwd.py`:669; signals: cute; excerpt: "mCuSeqlensQ is not None or mSequsedQ is not None" (https://github.com/Dao-AILab/flash-attention/pull/2333#discussion_r2927635364)
- `2026-03-12T22:03:00Z` `inline` by `tridao` `flash_attn/cute/flash_fwd.py`:671; signals: cute; excerpt: "need to deal w the case where there's no cu seqlens q but there's seqused q" (https://github.com/Dao-AILab/flash-attention/pull/2333#discussion_r2927637655)
