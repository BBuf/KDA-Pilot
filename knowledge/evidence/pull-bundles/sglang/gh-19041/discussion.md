# PR Discussion Digest

- Source PR: [sgl-project/sglang#19041](https://github.com/sgl-project/sglang/pull/19041)
- Source page: `sources/prs/sglang/PR-19041.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19041`
- Generated at: `2026-05-20T15:28:45.342406+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-20T02:25:17Z`
- Merged: `2026-02-22T08:20:52Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, zianglih
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-20T15:12:30Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19041#pullrequestreview-3832589520)
- `2026-02-20T21:09:38Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19041#pullrequestreview-3834223438)
- `2026-02-20T22:05:03Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19041#pullrequestreview-3834419733)
- `2026-02-21T05:00:17Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19041#pullrequestreview-3835052010)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-20T22:14:04Z` `issue` by `zianglih`; signals: bf16, gemm, perf, performance; excerpt: "Added warm-up. Now 8k/2k performance is slightly better than baseline: The warm-up for GEMM NT BF16BF16F32 is shown in the srever log:" (https://github.com/sgl-project/sglang/pull/19041#issuecomment-3937408627)
- `2026-02-20T15:12:24Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:233; signals: attention, bf16, gemm; excerpt: "Please try import deep gemm.bf16 gemm nt , and fallback when the import fails" (https://github.com/sgl-project/sglang/pull/19041#discussion_r2833709704)
- `2026-02-20T15:12:26Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:240; signals: attention, fp8, kernel; excerpt: "Do we need to warmup for this kernel? Just like fp8 kernels" (https://github.com/sgl-project/sglang/pull/19041#discussion_r2833709851)
- `2026-02-22T00:17:50Z` `issue` by `zianglih`; signals: deepgemm, gemm; excerpt: "Before [test nsa indexer.py]( failed due to an invalid shape N=1, K=5120, M=1during deepgemm warm-up. The N=1 is from index n heads, which is ..." (https://github.com/sgl-project/sglang/pull/19041#issuecomment-3939766061)
- `2026-02-20T21:09:38Z` `inline` by `zianglih` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:233; signals: attention; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/19041#discussion_r2835109299)
- `2026-02-20T22:05:02Z` `inline` by `zianglih` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:240; signals: attention; excerpt: "Added warm up in" (https://github.com/sgl-project/sglang/pull/19041#discussion_r2835289656)
- `2026-02-21T20:05:35Z` `issue` by `zianglih`; signals: hang; excerpt: "@Fridge003 added the 1 line change." (https://github.com/sgl-project/sglang/pull/19041#issuecomment-3939354652)
- `2026-02-21T23:23:42Z` `issue` by `zianglih`; signals: b200; excerpt: "[test nsa indexer.py]( still fails on my B200 machines. Investigating." (https://github.com/sgl-project/sglang/pull/19041#issuecomment-3939684424)
- `2026-02-21T12:29:25Z` `issue` by `Fridge003`; signals: general review; excerpt: "@zianglih Can you please move test nsa indexer.py to stage-b-test-large-1-gpu, since dpsk v32 is not supposed to run on 5090" (https://github.com/sgl-project/sglang/pull/19041#issuecomment-3938709697)
