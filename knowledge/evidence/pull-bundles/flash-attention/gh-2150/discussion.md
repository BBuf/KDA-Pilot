# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2150](https://github.com/Dao-AILab/flash-attention/pull/2150)
- Source page: `sources/prs/flash-attention/PR-2150.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2150`
- Generated at: `2026-05-20T15:16:42.479263+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-08T08:10:23Z`
- Merged: `2026-01-09T23:24:29Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 10
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: jayhshah, kiddyboots216, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-09T21:41:16Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645607149)
- `2026-01-09T22:18:02Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645738860)
- `2026-01-09T22:27:10Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645759399)
- `2026-01-09T22:47:55Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645803864)
- `2026-01-09T22:50:54Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645808476)
- `2026-01-09T23:17:58Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645899503)
- `2026-01-09T23:19:38Z` `APPROVED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645905533)
- `2026-01-09T23:20:57Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2150#pullrequestreview-3645910538)

## Inline Comment Hotspots

- `flash_attn/cute/flash_bwd_sm100.py`: 8 inline comment(s)
- `flash_attn/cute/interface.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-09T22:18:02Z` `inline` by `jayhshah` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: block, cute, hang, sm100, tile, tma; excerpt: "You're right to call this out, I only need to not use tma store dK/dV for cu seqlens k. I'll change this. In general: ..." (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677773564)
- `2026-01-09T22:47:55Z` `inline` by `jayhshah` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: cute, kernel, sm100, tma; excerpt: "Though we also disable tma store for seqused q only in the forward kernel, so there will be an inconsistency here (albeit with rarely ..." (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677832577)
- `2026-01-09T22:50:54Z` `inline` by `jayhshah` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: cute, sm100, tma; excerpt: "To address your other implicit question: note that since we use a special padded intermediate tensor for doing TMA reduce add with dK/dV accum ..." (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677837123)
- `2026-01-09T23:17:58Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: cute, sm100, tma; excerpt: "so the idea is: if we have gqa we post-process, so we can always use tma, even with seqlen k. and we can use ..." (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677911017)
- `2026-01-09T23:20:57Z` `inline` by `jayhshah` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: cute, sm100, tma; excerpt: "Yes (assuming you mean not tma = cu seqlens k and mha). I also tried using postprocess with mha and cu seqlens k to ..." (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677919847)
- `2026-01-09T21:24:58Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm100.py`:1351; signals: cute, sm100; excerpt: "can we just stick this into seqlen or something and not repeat it a bunch of times? e.g. a seqlen.offset batch padded(...)" (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677664079)
- `2026-01-09T21:21:18Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm100.py`:407; signals: cute, sm100; excerpt: "is that meant to be an or? what is the logic here?" (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677656514)
- `2026-01-09T21:22:26Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm100.py`:742; signals: cute, sm100; excerpt: "remove debug prints" (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677658766)
- `2026-01-09T21:39:13Z` `inline` by `v0i0` `flash_attn/cute/interface.py`:799; signals: cute; excerpt: "maybe just pull these out of all the conditionals" (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677692114)
- `2026-01-09T22:27:10Z` `inline` by `jayhshah` `flash_attn/cute/interface.py`:799; signals: cute; excerpt: "I'll move it up and delete redundant instance" (https://github.com/Dao-AILab/flash-attention/pull/2150#discussion_r2677791404)
- `2026-01-08T18:23:49Z` `issue` by `kiddyboots216`; signals: blackwell; excerpt: "varlen fwd (and bwd) training matches FA2 on Blackwell" (https://github.com/Dao-AILab/flash-attention/pull/2150#issuecomment-3725103557)
