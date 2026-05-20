# PR Discussion Digest

- Source PR: [sgl-project/sglang#4918](https://github.com/sgl-project/sglang/pull/4918)
- Source page: `sources/prs/sglang/PR-4918.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4918`
- Generated at: `2026-05-20T15:30:17.419749+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-30T14:13:37Z`
- Merged: `2025-04-04T08:59:29Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 23 (changes_requested=1, commented=22)
- Inline review comments: 49
- Review threads observed: 33
- Resolved/outdated thread markers: resolved=22, outdated=28
- Human participants with discussion text: BBuf, DiegoD94, ch-wan, dongyibo, fzyzcjy, lambert0312, xihuai18, yiakwy-xpu-ml-framework-team, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-03-31T00:57:47Z` `COMMENTED` by `fzyzcjy` - Just some nits (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2728076842)
- `2025-03-31T04:08:33Z` `CHANGES_REQUESTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2728144622)
- `2025-03-31T14:29:05Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2729511211)
- `2025-04-01T01:26:55Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2730851313)
- `2025-04-01T01:31:47Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2730860071)
- `2025-04-01T01:35:30Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2730864028)
- `2025-04-01T03:48:07Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731029489)
- `2025-04-01T03:49:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731030456)
- `2025-04-01T03:50:17Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731031231)
- `2025-04-01T03:51:12Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731032024)
- `2025-04-01T03:56:10Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731035984)
- `2025-04-01T03:56:49Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731036522)
- `2025-04-01T04:40:59Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731093766)
- `2025-04-01T04:41:06Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731093882)
- `2025-04-01T04:41:17Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2731094053)
- `2025-04-02T04:15:46Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2734554358)
- `2025-04-02T23:59:43Z` `COMMENTED` by `fzyzcjy` - forgot to submit (nit) reviews again... (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2736548809)
- `2025-04-03T01:36:21Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2738079782)
- `2025-04-03T07:11:34Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2738748530)
- `2025-04-03T07:11:36Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2738748617)
- `2025-04-03T19:00:41Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2740874122)
- `2025-04-04T06:13:26Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4918#pullrequestreview-2741874005)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 15 inline comment(s)
- `python/sglang/srt/layers/moe/topk.py`: 13 inline comment(s)
- `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`: 7 inline comment(s)
- `sgl-kernel/tests/test_moe_align.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 3 inline comment(s)
- `python/sglang/srt/server_args.py`: 3 inline comment(s)
- `python/sglang/bench_serving.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)
- `python/sglang/srt/managers/schedule_batch.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-31T00:45:00Z` `inline` by `fzyzcjy` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:403; signals: benchmark, kernel, moe, triton; excerpt: "nit: wondering whether we should call it "share" or "shared", it seems the original code has the latter more" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020303725)
- `2025-03-31T02:57:19Z` `inline` by `ch-wan` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:406; signals: benchmark, kernel, moe, triton; excerpt: "DeepSeek-V2 has 2 shared experts. Should we multiple the number of replica with the number of shared experts?" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020359992)
- `2025-03-31T04:06:33Z` `inline` by `ch-wan` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:404; signals: benchmark, kernel, moe, triton; excerpt: "Does this variable indicates the number of replication for each shared experts? This name is confusing as it represents number of shared experts." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020388824)
- `2025-03-31T00:45:51Z` `inline` by `fzyzcjy` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:404; signals: benchmark, kernel, moe, triton; excerpt: "nit: maybe we can unify the logic as E = config.n routed experts + n shared fusion experts" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020303985)
- `2025-04-01T01:31:46Z` `inline` by `BBuf` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:404; signals: benchmark, kernel, moe, triton; excerpt: "ok" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2021992037)
- `2025-04-02T14:47:13Z` `inline` by `fzyzcjy` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:403; signals: benchmark, kernel, moe, triton; excerpt: "nit: shall we use args here, because we use serverargs as well on main code" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2024988537)
- `2025-04-03T07:11:36Z` `inline` by `BBuf` `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`:403; signals: benchmark, kernel, moe, triton; excerpt: "done" (https://github.com/sgl-project/sglang/pull/4918#discussion_r2026347236)
- `2025-03-31T00:43:20Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:641; signals: moe, triton; excerpt: "nit: wondering whether we can avoid creating a new subdirectory, because it seems the computation speed is determined by E (num experts) and may ..." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020303228)
- `2025-03-31T00:50:25Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/topk.py`:133; signals: kernel, moe; excerpt: "nit: wondering whether a 1.0 will be optimized as a, or will pytorch actually call kernels to do a computation. If the latter, maybe ..." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020305595)
- `2025-03-31T00:56:42Z` `inline` by `fzyzcjy` `sgl-kernel/tests/test_moe_align.py`:147; signals: kernel, moe; excerpt: "nit: it seems the tuning output config says E=264, thus wondering whether we need to add 264 to this list as well for a ..." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020307847)
- `2025-03-31T00:57:07Z` `inline` by `fzyzcjy` `sgl-kernel/tests/test_moe_align.py`:146; signals: kernel, moe; excerpt: "nit: not run the code, but if I understand correctly, topk now is 1 larger, so maybe we can put that value here as ..." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2020307994)
- `2025-04-01T01:26:55Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:641; signals: moe, triton; excerpt: "Ok, I agree." (https://github.com/sgl-project/sglang/pull/4918#discussion_r2021986093)
