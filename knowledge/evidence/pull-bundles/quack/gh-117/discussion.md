# PR Discussion Digest

- Source PR: [Dao-AILab/quack#117](https://github.com/Dao-AILab/quack/pull/117)
- Source page: `sources/prs/quack/PR-117.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-117`
- Generated at: `2026-05-20T15:17:15.360512+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-23T00:14:45Z`
- Merged: `2026-04-26T13:22:32Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: Pranshu-Bahadur, tridao, wangyang59
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-24T10:56:05Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/117#pullrequestreview-4169909823)
- `2026-04-24T19:09:25Z` `COMMENTED` by `wangyang59` (https://github.com/Dao-AILab/quack/pull/117#pullrequestreview-4172836418)
- `2026-04-25T01:46:37Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/117#pullrequestreview-4174456478)
- `2026-04-26T13:22:25Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/117#pullrequestreview-4176966012)

## Inline Comment Hotspots

- `quack/gemm_sm100.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-24T10:56:05Z` `inline` by `tridao` `quack/gemm_sm100.py`:191; signals: block, gemm, sm100; excerpt: "only allow m=128 if not blockscaled" (https://github.com/Dao-AILab/quack/pull/117#discussion_r3137215934)
- `2026-04-25T11:49:24Z` `issue` by `Pranshu-Bahadur`; signals: benchmark, tile, tmem; excerpt: "Thanks! Whats' the tradeoff between cta=2 vs cta=1 when tile m=128? Here are some shapes we benchmarked. Are there other shapes that you would ..." (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4319545641)
- `2026-04-24T19:09:25Z` `inline` by `wangyang59` `quack/gemm_sm100.py`:191; signals: gemm, sm100; excerpt: "updated" (https://github.com/Dao-AILab/quack/pull/117#discussion_r3139791046)
- `2026-04-25T01:46:38Z` `inline` by `tridao` `quack/gemm_sm100.py`:194; signals: gemm, sm100; excerpt: "cluster shape mnk[0] % 2 == 0" (https://github.com/Dao-AILab/quack/pull/117#discussion_r3141078692)
- `2026-04-24T19:04:46Z` `issue` by `wangyang59`; signals: benchmark, tile; excerpt: "Thanks! Whats' the tradeoff between cta=2 vs cta=1 when tile m=128? Here are some shapes we benchmarked. Are there other shapes that you would ..." (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4315616872)
- `2026-04-26T07:41:11Z` `issue` by `wangyang59`; signals: gemm, tile; excerpt: "Some test failures look real, maybe tile K wasn't passed properly there? Thanks for raising this. Yeah, it was due to some mismatched argument ..." (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4321549832)
- `2026-04-26T07:38:57Z` `issue` by `wangyang59`; signals: tmem; excerpt: "@wangyang59 This is beautiful, thank you so much! Is N split across the 2 CTAs in mutiples of 8 (Suppose N=16, Each CTA will ..." (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4321546333)
- `2026-04-23T03:08:39Z` `issue` by `Pranshu-Bahadur`; signals: bf16; excerpt: "is this also for bf16 dense mma, not sure is 2CTA bf16 mma is a thing?" (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4301480228)
- `2026-04-23T18:04:21Z` `issue` by `wangyang59`; signals: bf16; excerpt: "is this also for bf16 dense mma, not sure is 2CTA bf16 mma is a thing? yes" (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4306671646)
- `2026-04-24T10:56:35Z` `issue` by `tridao`; signals: tile; excerpt: "Thanks! Whats' the tradeoff between cta=2 vs cta=1 when tile m=128?" (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4312631124)
- `2026-04-24T10:57:33Z` `issue` by `tridao`; signals: tile; excerpt: "the tile K thing seems fine to me" (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4312635916)
- `2026-04-25T02:03:02Z` `issue` by `tridao`; signals: tile; excerpt: "Some test failures look real, maybe tile K wasn't passed properly there?" (https://github.com/Dao-AILab/quack/pull/117#issuecomment-4317497306)
