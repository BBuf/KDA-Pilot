# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2136](https://github.com/Dao-AILab/flash-attention/pull/2136)
- Source page: `sources/prs/flash-attention/PR-2136.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2136`
- Generated at: `2026-05-20T15:16:42.474082+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-05T01:02:03Z`
- Merged: `2026-01-10T00:54:12Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 19
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=12, outdated=11
- Human participants with discussion text: drisspg, tridao, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-05T03:22:09Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625394729)
- `2026-01-05T03:22:27Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625395003)
- `2026-01-05T03:22:41Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625395200)
- `2026-01-05T03:23:38Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625396013)
- `2026-01-05T03:24:24Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625396679)
- `2026-01-05T03:24:49Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625397036)
- `2026-01-05T03:29:00Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625400692)
- `2026-01-05T03:30:21Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3625401894)
- `2026-01-05T21:20:30Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628463209)
- `2026-01-05T22:50:01Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628657204)
- `2026-01-05T23:09:43Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628699488)
- `2026-01-06T01:12:33Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628938386)
- `2026-01-06T01:12:54Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628938846)
- `2026-01-06T01:13:02Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628939023)
- `2026-01-06T01:13:09Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3628939199)
- `2026-01-06T19:00:20Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3632117073)
- `2026-01-06T19:04:39Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3632130215)
- `2026-01-09T20:44:38Z` `APPROVED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3645510285)
- `2026-01-09T20:51:12Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2136#pullrequestreview-3645536580)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 9 inline comment(s)
- `flash_attn/cute/flash_bwd_sm90.py`: 6 inline comment(s)
- `flash_attn/cute/block_sparse_utils.py`: 2 inline comment(s)
- `flash_attn/cute/mask.py`: 1 inline comment(s)
- `csrc/cutlass`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-05T03:22:09Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:586; signals: block, cute, tiling; excerpt: "This was mostly to find the GCD between a m block size that would fit and the base block m of 128 from fwd ..." (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660188164)
- `2026-01-05T03:22:27Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:646; signals: block, cute, tiling; excerpt: "This was mostly to find the GCD between a m block size that would fit and the base block m of 128 from fwd ..." (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660188534)
- `2026-01-05T03:29:00Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:763; signals: block, cute, sm90; excerpt: "we should probably pool the block sparse code into block-sparse produce so that this is more grokable" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660194432)
- `2026-01-05T22:48:31Z` `inline` by `tridao` `flash_attn/cute/flash_bwd_sm90.py`:776; signals: cute, hang, sm90; excerpt: "stylistically: can we put the non-sparsity code first so that reader knows what happens usually, then the sparsity code after. It's just changing the ..." (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2663013736)
- `2026-01-05T03:23:38Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:1011; signals: cute, tile; excerpt: "nb: bwd subtile factor is always 2 but we could make this larger in a follow up and allow for smaller tile sizes" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660189453)
- `2026-01-05T03:24:24Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:1123; signals: cute, hang; excerpt: "this change isnt needed, remove" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660190151)
- `2026-01-05T03:24:49Z` `inline` by `drisspg` `flash_attn/cute/mask.py`:144; signals: cute, sm100; excerpt: "replay from sm100 basically" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660190567)
- `2026-01-05T03:30:21Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:1051; signals: cute, sm90; excerpt: "Ditto here and make a consumer loop" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2660195632)
- `2026-01-05T21:20:30Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:1035; signals: cute, sm90; excerpt: "so these are fixe din the top commit, nasty rebase.." (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2662838273)
- `2026-01-05T23:09:43Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:776; signals: cute, sm90; excerpt: "totally agree, let me update" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2663052157)
- `2026-01-06T19:04:39Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:776; signals: cute, sm90; excerpt: "flip flopped em" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2665978012)
- `2026-01-09T20:40:53Z` `inline` by `v0i0` `flash_attn/cute/block_sparse_utils.py`:1171; signals: block, cute; excerpt: "i think this could be less repetitive" (https://github.com/Dao-AILab/flash-attention/pull/2136#discussion_r2677564932)
