# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2368](https://github.com/Dao-AILab/flash-attention/pull/2368)
- Source page: `sources/prs/flash-attention/PR-2368.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2368`
- Generated at: `2026-05-20T15:16:54.124903+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-18T00:24:12Z`
- Merged: `2026-03-18T09:02:19Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Luosuu, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-18T05:47:56Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2368#pullrequestreview-3965256580)
- `2026-03-18T05:52:48Z` `COMMENTED` by `Luosuu` (https://github.com/Dao-AILab/flash-attention/pull/2368#pullrequestreview-3965272286)
- `2026-03-18T05:52:58Z` `COMMENTED` by `Luosuu` (https://github.com/Dao-AILab/flash-attention/pull/2368#pullrequestreview-3965272801)
- `2026-03-18T05:53:41Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2368#pullrequestreview-3965275442)
- `2026-03-18T09:02:01Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2368#pullrequestreview-3966141674)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-18T04:20:17Z` `issue` by `Luosuu`; signals: aligned, alignment, bf16, compile, cute, layout, memory, shared memory; excerpt: "avoids the uneven kv smem offset logic that cp.async can't handle due to alignment constraints What's the alignment constraints that doesn't work w cp.async? ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079576767)
- `2026-03-18T05:47:56Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm100.py`:2694; signals: cute, dtype, fp8, sm100; excerpt: "let's do divby=128 // self.dtype.width so that this will eventually work for fp8 as well." (https://github.com/Dao-AILab/flash-attention/pull/2368#discussion_r2951089346)
- `2026-03-18T03:48:40Z` `issue` by `tridao`; signals: compile, kernel, tile, tma; excerpt: "interface.py line 497-503: When max seqlen q <= tile m (128 ≤ 128), the interface sets q stage=1, which compiles a different kernel that ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079429075)
- `2026-03-18T05:52:58Z` `inline` by `Luosuu` `flash_attn/cute/flash_fwd_sm100.py`:2694; signals: cute, dtype, sm100; excerpt: "I just use k dtype here" (https://github.com/Dao-AILab/flash-attention/pull/2368#discussion_r2951105225)
- `2026-03-18T04:40:51Z` `issue` by `tridao`; signals: aligned, compile, cute; excerpt: "The dst mem address is actually aligned, it's just the compiler can't prove it. You'll need to provide hint that the new address is ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079642222)
- `2026-03-18T05:52:48Z` `inline` by `Luosuu` `flash_attn/cute/flash_fwd_sm100.py`:2694; signals: cute, sm100; excerpt: "thank you. done" (https://github.com/Dao-AILab/flash-attention/pull/2368#discussion_r2951104663)
- `2026-03-18T04:41:48Z` `issue` by `tridao`; signals: kernel, tma; excerpt: "interface.py line 497-503: When max seqlen q then i think we should fix that kernel instead of routing around it. Would you like to ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079644802)
- `2026-03-18T03:40:36Z` `issue` by `tridao`; signals: alignment; excerpt: "avoids the uneven kv smem offset logic that cp.async can't handle due to alignment constraints What's the alignment constraints that doesn't work w cp.async?" (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079409079)
- `2026-03-18T04:24:13Z` `issue` by `Luosuu`; signals: kernel; excerpt: "interface.py line 497-503: When max seqlen q then i think we should fix that kernel instead of routing around it. Would you like to ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079588083)
- `2026-03-18T05:46:09Z` `issue` by `Luosuu`; signals: general review; excerpt: "@tridao Thanks very much for the suggestion! Would you like to review again? Now the fix should be very minimal. I tested it on ..." (https://github.com/Dao-AILab/flash-attention/pull/2368#issuecomment-4079912643)
