# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2043](https://github.com/Dao-AILab/flash-attention/pull/2043)
- Source page: `sources/prs/flash-attention/PR-2043.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2043`
- Generated at: `2026-05-20T15:16:39.282734+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-03T02:07:42Z`
- Merged: `2025-12-15T22:16:30Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: drisspg, jayhshah, reubenconducts, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-03T03:34:48Z` `COMMENTED` by `reubenconducts` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3533040127)
- `2025-12-03T23:13:17Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537286721)
- `2025-12-03T23:14:10Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537289253)
- `2025-12-03T23:16:27Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537293340)
- `2025-12-03T23:16:59Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537294181)
- `2025-12-03T23:17:43Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537295353)
- `2025-12-03T23:18:05Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3537295979)
- `2025-12-04T21:20:50Z` `COMMENTED` by `reubenconducts` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3542148714)
- `2025-12-04T21:22:13Z` `COMMENTED` by `reubenconducts` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3542152627)
- `2025-12-04T21:24:39Z` `COMMENTED` by `reubenconducts` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3542159173)
- `2025-12-15T22:05:52Z` `APPROVED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2043#pullrequestreview-3580374498)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 3 inline comment(s)
- `flash_attn/cute/interface.py`: 3 inline comment(s)
- `flash_attn/cute/flash_fwd.py`: 2 inline comment(s)
- `tests/cute/score_mod_definitions.py`: 1 inline comment(s)
- `flash_attn/cute/softmax.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-03T23:16:27Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2662; signals: cute, sm100; excerpt: "whats going on here?" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2586906425)
- `2025-12-03T23:18:06Z` `inline` by `drisspg` `flash_attn/cute/softmax.py`:33; signals: cute, tma; excerpt: "thank you been meaning to do this" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2586909022)
- `2025-12-04T21:22:13Z` `inline` by `reubenconducts` `flash_attn/cute/flash_fwd_sm100.py`:2662; signals: cute, sm100; excerpt: "simplified; now q idx logical computation is after possible divmod recomputation" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2590623173)
- `2025-12-03T03:34:48Z` `inline` by `reubenconducts` `tests/cute/score_mod_definitions.py`:154; signals: cute; excerpt: "@tridao For example here, when using both relative positional bias and per-token kv bias, we need both kv idx and kv idx global." (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2583508523)
- `2025-12-03T23:13:17Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd.py`:2427; signals: cute; excerpt: "noob q, doesnt the divisor need to be build on the host?" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2586901444)
- `2025-12-03T23:16:59Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:346; signals: cute; excerpt: "nit: can we pull into utils?" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2586907328)
- `2025-12-03T23:17:43Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:351; signals: cute; excerpt: "I think this might be host side slow, I have an issue to update inspect usage in utils.hash callable" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2586908372)
- `2025-12-04T21:20:49Z` `inline` by `reubenconducts` `flash_attn/cute/flash_fwd.py`:2427; signals: cute; excerpt: "no, it's okay on device" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2590619675)
- `2025-12-04T21:24:39Z` `inline` by `reubenconducts` `flash_attn/cute/interface.py`:351; signals: cute; excerpt: "removed" (https://github.com/Dao-AILab/flash-attention/pull/2043#discussion_r2590628768)
- `2025-12-03T02:59:50Z` `issue` by `tridao`; signals: general review; excerpt: "Is there a use case where one needs both q idx and q idx global? Does it make more sense to always have q ..." (https://github.com/Dao-AILab/flash-attention/pull/2043#issuecomment-3604835115)
