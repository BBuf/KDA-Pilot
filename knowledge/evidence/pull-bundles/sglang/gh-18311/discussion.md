# PR Discussion Digest

- Source PR: [sgl-project/sglang#18311](https://github.com/sgl-project/sglang/pull/18311)
- Source page: `sources/prs/sglang/PR-18311.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18311`
- Generated at: `2026-05-20T15:28:36.981550+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-05T13:03:35Z`
- Merged: `2026-03-27T15:54:37Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: DarkSharpness, huangtingwei9988, hzh0425
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-05T13:06:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for converting KV cache data between page-first and layer-first memory layouts ... (https://github.com/sgl-project/sglang/pull/18311#pullrequestreview-3756972097)
- `2026-03-12T14:30:57Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/18311#pullrequestreview-3937107423)
- `2026-03-12T14:34:33Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/18311#pullrequestreview-3937143160)
- `2026-03-25T08:08:44Z` `APPROVED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/18311#pullrequestreview-4004754005)
- `2026-03-25T12:45:36Z` `APPROVED` by `hzh0425` (https://github.com/sgl-project/sglang/pull/18311#pullrequestreview-4006390764)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/hicache.cuh`: 2 inline comment(s)
- `test/registered/hicache/test_hicache_jit_kernel.py`: 2 inline comment(s)
- `python/sglang/srt/mem_cache/memory_pool_host.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-12T14:29:48Z` `inline` by `DarkSharpness` `test/registered/hicache/test_hicache_jit_kernel.py`; signals: benchmark, cache, kernel, register; excerpt: "Could you add this to python/sglang/jit kernel/tests and align with JIT tests? FYI, there's already benchmark [here]( but there's not any coverage test for ..." (https://github.com/sgl-project/sglang/pull/18311#discussion_r2925068152)
- `2026-03-12T14:34:33Z` `inline` by `DarkSharpness` `test/registered/hicache/test_hicache_jit_kernel.py`; signals: cache, kernel, mla, register; excerpt: "For the test, it should cover common item dimension (= head dim \ num kv head), such as 128 (MHA, TP=8), 256, 512, 1024 ..." (https://github.com/sgl-project/sglang/pull/18311#discussion_r2925098083)
- `2026-02-05T13:19:50Z` `issue` by `DarkSharpness`; signals: cache, kernel, kv cache; excerpt: "I guess we can reuse the old kernels? (not 100% sure) Page-first transfers just needs to transpose the device cache back to normal layer ..." (https://github.com/sgl-project/sglang/pull/18311#issuecomment-3853611347)
