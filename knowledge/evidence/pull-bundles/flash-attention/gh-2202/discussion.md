# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2202](https://github.com/Dao-AILab/flash-attention/pull/2202)
- Source page: `sources/prs/flash-attention/PR-2202.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2202`
- Generated at: `2026-05-20T15:16:45.600909+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-23T01:39:51Z`
- Merged: `2026-02-20T01:44:15Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: donglixp, endurehero, jayhshah, tridao, tzadouri, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-02-08T15:52:46Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3769905900)
- `2026-02-08T15:55:58Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3769908684)
- `2026-02-08T16:02:18Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3769916076)
- `2026-02-09T06:21:34Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3771401252)
- `2026-02-12T18:09:27Z` `COMMENTED` by `tzadouri` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3792776644)
- `2026-02-12T18:10:12Z` `COMMENTED` by `tzadouri` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3792781506)
- `2026-02-12T18:33:01Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3792916727)
- `2026-02-12T18:34:02Z` `COMMENTED` by `tzadouri` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3792921361)
- `2026-02-20T01:44:05Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2202#pullrequestreview-3829412026)

## Inline Comment Hotspots

- `flash_attn/cute/blackwell_helpers.py`: 4 inline comment(s)
- `flash_attn/cute/flash_bwd_sm100.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-12T18:33:19Z` `issue` by `tzadouri`; signals: hang, pipeline, tile, tmem; excerpt: "@endurehero Applying 2CTA to BWD is a bit tricky because, for the dQ MMA, the reduction axis naturally splits across the two CTAs, so ..." (https://github.com/Dao-AILab/flash-attention/pull/2202#issuecomment-3892697184)
- `2026-02-08T15:52:46Z` `inline` by `tridao` `flash_attn/cute/blackwell_helpers.py`:35; signals: blackwell, cute, cutlass; excerpt: "is num unroll groups always 1? What's the issue with cutlass.range constexpr? If you want to use cutlass.range you can use cutlass.range(..., unroll full=True)" (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2779440196)
- `2026-02-09T06:21:34Z` `inline` by `jayhshah` `flash_attn/cute/flash_bwd_sm100.py`:2132; signals: cute, pipeline, sm100; excerpt: "We don't need to both invoke wait and advance on pipeline Q consumer and then pipeline Q.consumer wait(consumer state Q) immediately after on the ..." (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2780826503)
- `2026-02-12T18:09:27Z` `inline` by `tzadouri` `flash_attn/cute/blackwell_helpers.py`:35; signals: blackwell, cute, register; excerpt: "Yes, due to the large reduction in dQ mma in the 2cta case, if num unroll groups = 1, there is register spilling." (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2800346269)
- `2026-02-08T15:55:58Z` `inline` by `tridao` `flash_attn/cute/blackwell_helpers.py`:388; signals: blackwell, cute; excerpt: "You can get this info from op.cta group == CtaGroup.ONE instead of having to pass cta group in as an argument" (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2779443585)
- `2026-02-08T16:02:18Z` `inline` by `tridao` `flash_attn/cute/blackwell_helpers.py`:35; signals: blackwell, cute; excerpt: "I see that num unroll groups==2 when using 2CTA. Is that necessary?" (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2779450221)
- `2026-02-12T18:10:11Z` `inline` by `tzadouri` `flash_attn/cute/flash_bwd_sm100.py`:2132; signals: cute, sm100; excerpt: "Right, will update this." (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2800349923)
- `2026-02-12T18:33:02Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm100.py`:62; signals: cute, sm100; excerpt: "hmm this reads like the mode is still disabled / not wired through to interface.py?" (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2800452788)
- `2026-02-12T18:34:02Z` `inline` by `tzadouri` `flash_attn/cute/flash_bwd_sm100.py`:62; signals: cute, sm100; excerpt: "Ya I need to update this." (https://github.com/Dao-AILab/flash-attention/pull/2202#discussion_r2800456810)
- `2026-02-03T02:58:52Z` `issue` by `endurehero`; signals: perf, performance; excerpt: "It's a really good job. Want to be sure, will you see any performance gains from using 2cta mma? @tzadouri" (https://github.com/Dao-AILab/flash-attention/pull/2202#issuecomment-3838762058)
