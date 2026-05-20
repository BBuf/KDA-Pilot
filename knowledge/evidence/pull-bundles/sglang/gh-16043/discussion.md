# PR Discussion Digest

- Source PR: [sgl-project/sglang#16043](https://github.com/sgl-project/sglang/pull/16043)
- Source page: `sources/prs/sglang/PR-16043.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16043`
- Generated at: `2026-05-20T15:28:18.587879+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-29T06:26:55Z`
- Merged: `2026-02-04T11:59:41Z`

## Discussion Counts

- Issue comments: 24
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 9
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: BJWang-ant, Fridge003, Jacob0226, xu-yfei
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- `2026-01-23T18:06:51Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3682389515)
- `2026-01-28T03:57:21Z` `COMMENTED` by `BJWang-ant` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3714469517)
- `2026-01-28T03:58:24Z` `COMMENTED` by `BJWang-ant` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3714471470)
- `2026-01-28T04:01:05Z` `COMMENTED` by `BJWang-ant` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3714476226)
- `2026-01-29T14:45:11Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3723184239)
- `2026-02-02T07:31:23Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3737741715)
- `2026-02-02T07:33:14Z` `COMMENTED` by `BJWang-ant` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3737746880)
- `2026-02-03T16:29:16Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16043#pullrequestreview-3746275751)

## Inline Comment Hotspots

- `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`: 4 inline comment(s)
- `python/sglang/srt/mem_cache/memory_pool.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-09T08:29:34Z` `issue` by `BJWang-ant`; signals: attention, b200, cache, compile, cuda, deepgemm, dtype, flashinfer; excerpt: "The above commit splits the for loops for getting k\scale and ke\ks into two separate kernels.Judging solely from my test results。 From the trace ..." (https://github.com/sgl-project/sglang/pull/16043#issuecomment-3727761976)
- `2026-01-23T17:41:29Z` `inline` by `Fridge003` `python/sglang/srt/mem_cache/memory_pool.py`:1837; signals: cache, correctness, kernel, memory; excerpt: "Can we open a new method for fused kernel (get fused index k scale buffer) This one can be a correctness baseline" (https://github.com/sgl-project/sglang/pull/16043#discussion_r2722214526)
- `2026-02-02T05:52:56Z` `issue` by `BJWang-ant`; signals: attention, benchmark, fp8, hang; excerpt: "@BJWang-ant Please fix the conflict @Fridge003 All the repairs have been completed. this is GPQA/AIME2025 results: server: python3 -m sglang.launch server --model-path /upfs/models/deepseek-ai/DeepSeek-V3.2 \ ..." (https://github.com/sgl-project/sglang/pull/16043#issuecomment-3833079848)
- `2026-01-20T14:11:24Z` `inline` by `Fridge003` `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`:7; signals: attention, kernel, triton; excerpt: "Can we import this kernel from srt? Since if anybody modify this kernel later, it's hard to keep the two copies synced" (https://github.com/sgl-project/sglang/pull/16043#discussion_r2708527016)
- `2026-01-28T03:57:20Z` `inline` by `BJWang-ant` `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`:7; signals: attention, kernel, triton; excerpt: "OK.No problem.I will rewrite later." (https://github.com/sgl-project/sglang/pull/16043#discussion_r2734750182)
- `2026-02-02T07:31:23Z` `inline` by `Fridge003` `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`:7; signals: attention, kernel, triton; excerpt: "cc @BJWang-ant Please resolve this" (https://github.com/sgl-project/sglang/pull/16043#discussion_r2752947322)
- `2026-02-02T07:33:14Z` `inline` by `BJWang-ant` `test/manual/layers/attention/nsa/test_get_k_scale_triton_kernel.py`:7; signals: attention, kernel, triton; excerpt: "OK" (https://github.com/sgl-project/sglang/pull/16043#discussion_r2752952174)
- `2026-01-23T17:55:21Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`:646; signals: attention, block; excerpt: "Are we launching too many blocks for this grid? Like when seq len is really long, this might be inefficient. Can we handle multiple ..." (https://github.com/sgl-project/sglang/pull/16043#discussion_r2722256078)
- `2026-01-29T14:45:11Z` `inline` by `Fridge003` `python/sglang/srt/mem_cache/memory_pool.py`:1837; signals: cache, memory; excerpt: "Oh wait... The former get index k scale buffer can be deprecated since it's only called once in nsa indexer.py. Then I think no ..." (https://github.com/sgl-project/sglang/pull/16043#discussion_r2742016869)
- `2026-01-28T03:58:24Z` `inline` by `BJWang-ant` `python/sglang/srt/mem_cache/memory_pool.py`:1837; signals: cache, memory; excerpt: "ok. No problem" (https://github.com/sgl-project/sglang/pull/16043#discussion_r2734752066)
- `2026-01-28T04:01:05Z` `inline` by `BJWang-ant` `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`:646; signals: attention; excerpt: "Yeah.I agree to postpone it for the next PR." (https://github.com/sgl-project/sglang/pull/16043#discussion_r2734756495)
- `2026-02-02T07:27:27Z` `issue` by `Fridge003`; signals: general review; excerpt: "@BJWang-ant Can you please post the GPQA result? Also are you posting V3.2 and V3.2 speciale in reverse order? I feel the result for ..." (https://github.com/sgl-project/sglang/pull/16043#issuecomment-3833429531)
