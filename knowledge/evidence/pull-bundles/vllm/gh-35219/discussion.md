# PR Discussion Digest

- Source PR: [vllm-project/vllm#35219](https://github.com/vllm-project/vllm/pull/35219)
- Source page: `sources/prs/vllm/PR-35219.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35219`
- Generated at: `2026-05-20T15:39:59.968745+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-24T19:21:59Z`
- Merged: `2026-03-10T10:32:20Z`

## Discussion Counts

- Issue comments: 42
- Review submissions: 38 (approved=2, commented=36)
- Inline review comments: 43
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=9, outdated=11
- Human participants with discussion text: LucasWilkinson, NickLucche, benchislett, heheda12345, mergify, pavanimajety, tdoublep, vadiklyutiy, voipmonitor, xinli-sw, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-24T19:25:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a bug fix for Mamba-based models, specifically addressing an issue where freed ... (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3850081822)
- `2026-02-25T14:24:16Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3854599087)
- `2026-02-25T14:49:03Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3854751496)
- `2026-02-25T15:02:26Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3854842601)
- `2026-02-25T15:57:02Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3855190126)
- `2026-02-25T15:58:25Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3855197941)
- `2026-02-25T16:27:37Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3855365505)
- `2026-02-25T21:48:14Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857126124)
- `2026-02-25T21:56:08Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857219956)
- `2026-02-25T23:00:46Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857441954)
- `2026-02-25T23:01:45Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857444619)
- `2026-02-25T23:02:12Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857445830)
- `2026-02-26T00:56:52Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3857777864)
- `2026-02-26T05:14:36Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3858511497)
- `2026-02-26T08:19:34Z` `COMMENTED` by `heheda12345` - Thanks for your contribution! I think we can find the blocks that we need to clear from gpu ... (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3859236020)
- `2026-02-26T08:23:30Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3859258704)
- `2026-02-26T13:44:42Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3861086598)
- `2026-02-26T15:08:31Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3861607190)
- `2026-02-26T18:39:56Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3862901846)
- `2026-02-27T06:52:43Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3865280177)
- `2026-02-27T09:20:51Z` `COMMENTED` by `NickLucche` - just a note to address (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3865875125)
- `2026-02-27T13:11:11Z` `COMMENTED` by `tdoublep` - I also find it unnecessary to always zero out the blocks. There is a really specific case where ... (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3866837712)
- `2026-03-02T01:41:51Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3873723530)
- `2026-03-02T01:47:37Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3873730602)
- ... 14 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/v1/worker/gpu_model_runner.py`: 35 inline comment(s)
- `vllm/tool_parsers/hermes_tool_parser.py`: 6 inline comment(s)
- `vllm/v1/worker/gpu_worker.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-26T15:24:48Z` `issue` by `vadiklyutiy`; signals: attention, block, cache, dtype, kernel, kv cache, nan, overflow; excerpt: "And IMO we only need this fix when different kv cache use different dtype. Better to only run this step for this case (and ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-3967332062)
- `2026-03-05T01:06:49Z` `issue` by `vadiklyutiy`; signals: accuracy, attention, b200, benchmark, block, cache, correctness, dtype; excerpt: "Because a lot of changes was introduced since PR was open, I fully updated PR description as below Essential problem Fixes Workaround for Hybrid ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-4001320179)
- `2026-02-27T13:11:11Z` `review` `COMMENTED` by `tdoublep`; signals: attention, block, cache, dtype, kv cache, nan; excerpt: "I also find it unnecessary to always zero out the blocks. There is a really specific case where the NaNs can creep in which ..." (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3866837712)
- `2026-03-07T07:29:38Z` `issue` by `voipmonitor`; signals: blackwell, cutlass, flashinfer, gemm, nan, race, sm120; excerpt: "Hello, I suspect that this can be related to the flashinfer race condition issue caused by enabled PDL on blackwell which needs cutlass 4.3.0 ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-4015838459)
- `2026-03-09T14:08:16Z` `issue` by `vadiklyutiy`; signals: b200, benchmark, cache, fp8, kernel, perf, triton; excerpt: "KV-Cache Zeroing: Triton Kernel vs index fill Benchmark Results Model & Hardware - Model : Qwen/Qwen3.5-35B-A3B-FP8 - GPU : 1x B200 (TP=1) Server Command ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-4024053107)
- `2026-02-27T13:02:57Z` `inline` by `tdoublep` `vllm/v1/worker/gpu_model_runner.py`:372; signals: attention, flash attention, kernel, layout, memory; excerpt: "iirc we don't actually reshape the flash attention KV tensor, but hack at the strides to make it have the layout in memory that ..." (https://github.com/vllm-project/vllm/pull/35219#discussion_r2864245531)
- `2026-02-26T08:19:34Z` `review` `COMMENTED` by `heheda12345`; signals: block, cache, dtype, kv cache; excerpt: "Thanks for your contribution! I think we can find the blocks that we need to clear from gpu model runner. We can get NewRequestData.block ..." (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3859236020)
- `2026-02-25T02:19:07Z` `issue` by `vadiklyutiy`; signals: attention, block, cache, dtype, nan; excerpt: "How does this interact with prefix caching? If we zero out blocks when their ref cnt hits zero, doesn't that mean they can't be ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-3956305407)
- `2026-02-26T08:23:31Z` `inline` by `heheda12345` `vllm/v1/worker/gpu_model_runner.py`:372; signals: attention, block, flash attention, kernel; excerpt: "does this kernel consider flash attention? it's shape is (2, num blocks, hidden) in general and we do some hack to make it (num ..." (https://github.com/vllm-project/vllm/pull/35219#discussion_r2857629692)
- `2026-03-06T20:48:37Z` `review` `COMMENTED` by `tdoublep`; signals: kernel, perf, performance; excerpt: "I think general approach looks much better now but I still have concerns about the complexity of the implementation and introducing a lot of ..." (https://github.com/vllm-project/vllm/pull/35219#pullrequestreview-3905860967)
- `2026-02-24T22:05:44Z` `issue` by `tdoublep`; signals: attention, block, cache, dtype; excerpt: "How does this interact with prefix caching? If we zero out blocks when their ref cnt hits zero, doesn't that mean they can't be ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-3954992102)
- `2026-02-25T00:42:01Z` `issue` by `vadiklyutiy`; signals: attention, block, cache, dtype; excerpt: "How does this interact with prefix caching? If we zero out blocks when their ref cnt hits zero, doesn't that mean they can't be ..." (https://github.com/vllm-project/vllm/pull/35219#issuecomment-3955643103)
