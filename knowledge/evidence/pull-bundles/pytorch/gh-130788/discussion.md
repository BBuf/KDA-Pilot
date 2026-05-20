# PR Discussion Digest

- Source PR: [pytorch/pytorch#130788](https://github.com/pytorch/pytorch/pull/130788)
- Source page: `sources/prs/pytorch/PR-130788.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-130788`
- Generated at: `2026-05-20T15:26:54.842129+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-07-16T00:15:30Z`
- Merged: `2024-07-17T20:24:43Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: drisspg, joydddd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2024-07-17T18:17:37Z` `COMMENTED` by `drisspg` (https://github.com/pytorch/pytorch/pull/130788#pullrequestreview-2183706004)
- `2024-07-17T18:17:39Z` `APPROVED` by `drisspg` (https://github.com/pytorch/pytorch/pull/130788#pullrequestreview-2183706194)
- `2024-07-17T20:21:57Z` `COMMENTED` by `joydddd` (https://github.com/pytorch/pytorch/pull/130788#pullrequestreview-2183961243)

## Inline Comment Hotspots

- `benchmarks/transformer/score_mod.py`: 3 inline comment(s)

## High-Signal Discussion

- `2024-07-17T18:12:37Z` `issue` by `joydddd`; signals: bf16, compile, dtype, kernel, perf, performance, speedup; excerpt: "Flex Decoding performance sweep: Compared to sdpa kernel (w split-K) bf16 Type Speedup score mod dtype shape(B,Hq,M,Hkv,N,D) --------- ----------- --------------- ---------------- --------------------------- Average 1.121 ..." (https://github.com/pytorch/pytorch/pull/130788#issuecomment-2233944154)
- `2024-07-17T18:12:17Z` `issue` by `joydddd`; signals: attention, compile, dtype, perf, performance, speedup; excerpt: "Flex attention w Sparsity Mask Performance (on causal mask) (vs. sdpa) Type Speedup score mod dtype shape(B,Hq,M,Hkv,N,D) --------- ----------- ------------- ---------------- ------------------------------ Average 1.320 ..." (https://github.com/pytorch/pytorch/pull/130788#issuecomment-2233943183)
- `2024-07-17T18:17:37Z` `inline` by `drisspg` `benchmarks/transformer/score_mod.py`:219; signals: benchmark; excerpt: "same tflops comment but not a big deal and a nit" (https://github.com/pytorch/pytorch/pull/130788#discussion_r1681525384)
- `2024-07-17T20:21:57Z` `inline` by `joydddd` `benchmarks/transformer/score_mod.py`:219; signals: benchmark; excerpt: "I messed up ghstack, therefore it's fixed in next PR in stack: I'll land that one directly." (https://github.com/pytorch/pytorch/pull/130788#discussion_r1681684139)
