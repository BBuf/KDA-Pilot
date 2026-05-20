# PR Discussion Digest

- Source PR: [sgl-project/sglang#18389](https://github.com/sgl-project/sglang/pull/18389)
- Source page: `sources/prs/sglang/PR-18389.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18389`
- Generated at: `2026-05-20T15:28:38.517803+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-07T03:44:12Z`
- Merged: `2026-02-16T01:29:55Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 5 (commented=5)
- Inline review comments: 13
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: Fridge003, rainj-me
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-07T04:04:21Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Deepseek v3.2 NVFP4 with the trtllm mla sparse fp8 attention ... (https://github.com/sgl-project/sglang/pull/18389#pullrequestreview-3766194053)
- `2026-02-11T11:49:08Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18389#pullrequestreview-3783788556)
- `2026-02-11T21:39:17Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/18389#pullrequestreview-3787611522)
- `2026-02-11T21:40:06Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/18389#pullrequestreview-3787614131)
- `2026-02-11T23:31:04Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/18389#pullrequestreview-3788025205)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 9 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 3 inline comment(s)
- `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-11T11:47:10Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1979; signals: attention, kernel, perf, performance; excerpt: "Seems when prefill batch doesn't use mha, it will also be routed to this kernel. Will that cause performance degradation?" (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792839352)
- `2026-02-11T10:24:42Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:330; signals: attention, cache, hang, kv cache; excerpt: "maybe change to a name with clearer meaning, like kv cache data type" (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792488287)
- `2026-02-11T10:24:04Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:2131; signals: accuracy, attention, hang; excerpt: "Why changing speculative num steps. Will this change affect accept len/accuracy?" (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792485409)
- `2026-02-11T11:52:35Z` `issue` by `Fridge003`; signals: cache, fp8, kv cache; excerpt: "If trtllm backend is faster on fp8 kv cache, then we might modify the set default nsa backends function in server args.py" (https://github.com/sgl-project/sglang/pull/18389#issuecomment-3883951770)
- `2026-02-13T22:41:14Z` `issue` by `rainj-me`; signals: cache, fp8, kv cache; excerpt: "If trtllm backend is faster on fp8 kv cache, then we might modify the set default nsa backends function in server args.py Let's bake ..." (https://github.com/sgl-project/sglang/pull/18389#issuecomment-3899951297)
- `2026-02-11T09:56:02Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:1512; signals: attention, mla; excerpt: "There's a same function in trtllm mla backend.py. Can we combine them and put it in attention/utils.py, if they are exactly the same?" (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792359522)
- `2026-02-11T09:57:17Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`:498; signals: cache, kernel; excerpt: "These two arguments are confusing. Can we pass one single argument on whether we use trtllm kernels for both prefill and decoding on nsa ..." (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792365029)
- `2026-02-11T11:48:35Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:2041; signals: accuracy, attention; excerpt: "We set max kv len to self.nsa index topk in consideration of accuracy (since the model only ensures the accuracy of MHA on seq ..." (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792844894)
- `2026-02-11T21:39:17Z` `inline` by `rainj-me` `python/sglang/srt/layers/attention/nsa_backend.py`:1979; signals: attention, throughput; excerpt: "Currently, the logic is forced to use mha for trtllm nsa backend. I will check how to leverage trtllm sparse attn backend for prefill ..." (https://github.com/sgl-project/sglang/pull/18389#discussion_r2795655740)
- `2026-02-11T11:15:07Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:2095; signals: attention, mla; excerpt: "The same, can we put it in the utils.py file and share it with trtllm mla backend" (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792709132)
- `2026-02-11T09:47:32Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:1487; signals: attention; excerpt: "Can we open a new function for checking whether the fuse rope can be applied. We don't need to modify dispatch attn forward method, ..." (https://github.com/sgl-project/sglang/pull/18389#discussion_r2792321970)
- `2026-02-11T21:40:06Z` `inline` by `rainj-me` `python/sglang/srt/layers/attention/nsa_backend.py`:2041; signals: attention; excerpt: "Good idea." (https://github.com/sgl-project/sglang/pull/18389#discussion_r2795658517)
