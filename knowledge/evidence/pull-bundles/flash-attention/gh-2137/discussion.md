# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2137](https://github.com/Dao-AILab/flash-attention/pull/2137)
- Source page: `sources/prs/flash-attention/PR-2137.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2137`
- Generated at: `2026-05-20T15:16:42.476090+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-05T01:02:04Z`
- Merged: `2026-01-10T00:56:47Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 9
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=6
- Human participants with discussion text: drisspg, niyunsheng, tridao, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-05T03:33:33Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625404709)
- `2026-01-05T03:34:56Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625405976)
- `2026-01-05T03:35:04Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625406108)
- `2026-01-05T03:35:30Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625406498)
- `2026-01-05T03:35:38Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625406629)
- `2026-01-05T03:36:38Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625407504)
- `2026-01-05T03:37:13Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625408008)
- `2026-01-05T03:38:19Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3625408934)
- `2026-01-05T22:38:28Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3628638338)
- `2026-01-09T20:51:47Z` `APPROVED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2137#pullrequestreview-3645532140)

## Inline Comment Hotspots

- `flash_attn/cute/flash_bwd_sm90.py`: 7 inline comment(s)
- `flash_attn/cute/interface.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-05T03:36:38Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:1222; signals: block, cute, sm90; excerpt: "Hmm this she be in previous commit, but also we should only apply masking on the partial blocks and not the full blocks" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660201354)
- `2026-01-05T03:33:33Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:933; signals: cute, sm90, tile; excerpt: "tighten up comment, note that swapAB tranposes tile so switch indexing" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660198566)
- `2026-01-05T03:34:56Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:947; signals: cute, sm90; excerpt: "not helpful comment" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660199870)
- `2026-01-05T03:35:05Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:981; signals: cute, sm90; excerpt: "not helpful comment" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660200017)
- `2026-01-05T03:35:30Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:933; signals: cute, sm90; excerpt: "just leave one [NOTE] SdP swapAB semantics and link back" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660200423)
- `2026-01-05T03:35:38Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:993; signals: cute, sm90; excerpt: "not helpful comment" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660200516)
- `2026-01-05T03:37:14Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:1295; signals: cute, sm90; excerpt: "keep S in regs and let DCE gods have mercy on us if not used" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660201844)
- `2026-01-05T03:38:19Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:986; signals: cute; excerpt: "double check this is consistent and not a flag set in init" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2660202978)
- `2026-01-09T20:49:17Z` `inline` by `v0i0` `flash_attn/cute/interface.py`:716; signals: cute; excerpt: "keep but make it [9,10,11]?" (https://github.com/Dao-AILab/flash-attention/pull/2137#discussion_r2677585408)
- `2026-01-06T15:29:09Z` `issue` by `niyunsheng`; signals: perf; excerpt: "Verified! I've tested this in our scenario and it works perfectly, and solves 2117. Really appreciate the quick turnaround and your hard work on ..." (https://github.com/Dao-AILab/flash-attention/pull/2137#issuecomment-3715136696)
- `2026-01-09T20:52:11Z` `issue` by `v0i0`; signals: triton; excerpt: "why is triton faster for small sizes?" (https://github.com/Dao-AILab/flash-attention/pull/2137#issuecomment-3730532713)
