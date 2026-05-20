# PR Discussion Digest

- Source PR: [vllm-project/vllm#15960](https://github.com/vllm-project/vllm/pull/15960)
- Source page: `sources/prs/vllm/PR-15960.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15960`
- Generated at: `2026-05-20T15:34:46.115165+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete via REST overflow fallback`, inline comments `complete`.

## Timeline

- Opened: `2025-04-02T18:31:55Z`
- Merged: `2025-04-17T20:22:40Z`

## Discussion Counts

- Issue comments: 33
- Review submissions: 118 (approved=2, commented=116)
- Inline review comments: 155
- Review threads observed: 93
- Resolved/outdated thread markers: resolved=65, outdated=76
- Human participants with discussion text: Abatom, ApostaC, Flechman, Huixxi, KuntaiDu, ShangmingCai, VertexC, WoosukKwon, chunxiaozheng, da-x, hasB4K, khayamgondal, lionelvillard, maobaolong, mergify, robertgshaw2-redhat, sdavidbd, sunshenao, tlrmchlsmth, zejun-chen
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-04-03T01:57:57Z` `COMMENTED` by `maobaolong` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2738115241)
- `2025-04-03T02:04:00Z` `COMMENTED` by `ApostaC` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2738120442)
- `2025-04-04T00:22:25Z` `COMMENTED` by `maobaolong` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2741480684)
- `2025-04-04T17:53:05Z` `COMMENTED` by `hasB4K` - Thank for for this PR 😃. Here some small changes proopsal to restore the support of V0 (broken ... (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2743731675)
- `2025-04-05T00:58:16Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744406378)
- `2025-04-05T01:00:17Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744416933)
- `2025-04-05T01:03:01Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744429072)
- `2025-04-05T01:22:37Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744492764)
- `2025-04-05T01:24:18Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744493193)
- `2025-04-05T01:24:49Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744493309)
- `2025-04-05T01:27:04Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744495305)
- `2025-04-05T01:34:36Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744499272)
- `2025-04-05T01:46:26Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744512573)
- `2025-04-05T01:54:35Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2744528387)
- `2025-04-06T15:21:16Z` `COMMENTED` by `hasB4K` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745167370)
- `2025-04-06T18:27:30Z` `COMMENTED` by `ApostaC` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745211015)
- `2025-04-06T19:02:50Z` `COMMENTED` by `ApostaC` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745218557)
- `2025-04-06T19:34:14Z` `COMMENTED` by `ApostaC` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745227550)
- `2025-04-06T20:48:42Z` `COMMENTED` by `hasB4K` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745271279)
- `2025-04-06T23:41:00Z` `COMMENTED` by `hasB4K` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745311598)
- `2025-04-07T02:02:34Z` `COMMENTED` by `maobaolong` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745388037)
- `2025-04-07T07:16:45Z` `COMMENTED` by `maobaolong` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2745744602)
- `2025-04-07T21:56:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2748201358)
- `2025-04-07T22:03:02Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2748215869)
- ... 94 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/v1/core/kv_cache_manager.py`: 36 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/v1/shared_storage_connector.py`: 28 inline comment(s)
- `vllm/v1/core/sched/scheduler.py`: 20 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/v1/base.py`: 19 inline comment(s)
- `vllm/attention/layer.py`: 13 inline comment(s)
- `vllm/distributed/parallel_state.py`: 8 inline comment(s)
- `vllm/forward_context.py`: 6 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 6 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector_agent.py`: 5 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/factory.py`: 5 inline comment(s)
- `examples/offline_inference/disaggrated-prefill-v1/prefill_example.py`: 3 inline comment(s)
- `examples/offline_inference/disaggrated-prefill-v1/decode_example.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-09T19:54:39Z` `inline` by `sdavidbd` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:105; signals: attention, cache, kv cache, latency, perf, performance, throughput; excerpt: "Thanks for the clarification. What I meant is that the triggering of the asynchronous KV cache load should ideally be done in a more ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2036053143)
- `2025-04-06T10:06:01Z` `inline` by `sdavidbd` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:105; signals: cache, kv cache, perf, performance; excerpt: "I suggest the API would support a per-layer KV cache load API similar to the save API. Controlling how many layers we prefetch will ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2030102955)
- `2025-04-11T14:31:47Z` `inline` by `zhoufang5-tal` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:175; signals: block, cache, kv cache, race; excerpt: "I used the latest commit of the branch : ERROR 04-11 07:14:42 [core.py:383] File "/workspace/apostac-vllm/vllm/v1/engine/core.py", line 376, in run engine core ERROR 04-11 07:14:42 ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2039674978)
- `2025-04-15T22:26:09Z` `review` `COMMENTED` by `WoosukKwon`; signals: attention, block, hang; excerpt: "My biggest concern on this PR is that the interface and connector design need to be updated when we merge the hybrid allocator. For ..." (https://github.com/vllm-project/vllm/pull/15960#pullrequestreview-2770055862)
- `2025-04-16T06:19:01Z` `issue` by `WoosukKwon`; signals: cache, hang, kv cache, memory; excerpt: "@robertgshaw2-redhat As discussed offline, I'm ok with merging this PR. However, I'd like to defer any other followup PRs (such as 16625) until we ..." (https://github.com/vllm-project/vllm/pull/15960#issuecomment-2808497749)
- `2025-04-06T15:19:33Z` `inline` by `hasB4K` `vllm/distributed/kv_transfer/kv_connector/v1/shared_storage_connector.py`:279; signals: block, cache, memory; excerpt: "1. in my understanding this a way to use allocate slots to make the scheduler believe that those new blocks are a prefix cached ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2030181354)
- `2025-04-06T19:02:50Z` `inline` by `ApostaC` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:138; signals: attention, cache, kv cache; excerpt: "Let me clarify a bit. The save and load have "reversed" semantics. - When loading the KV cache, the connector can initialize a load ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2030233342)
- `2025-04-08T22:47:59Z` `inline` by `sdavidbd` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:179; signals: block, cache, kv cache; excerpt: "It appears that this method must ensure all returned blocks are cached, but this requirement isn't clearly emphasized. I believe the solution would be ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2034134069)
- `2025-04-09T08:24:28Z` `inline` by `VertexC` `vllm/distributed/kv_transfer/kv_connector/v1/base.py`:154; signals: block, cache, kv cache; excerpt: "It is a bit confusing to include blocks allocation/free under the semantic of "get ". Are we trying to allocate vLLM's paged KV cache ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2034773661)
- `2025-04-11T04:38:08Z` `inline` by `ShangmingCai` `vllm/distributed/kv_transfer/kv_connector/v1/shared_storage_connector.py`:323; signals: block, cache, perf; excerpt: "Disaggregated P/D and KVCache sharing are aimed at long context scenarios. If the block to be transferred is less than a certain threshold, prefill ..." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2038785691)
- `2025-04-11T00:18:19Z` `inline` by `ApostaC` `vllm/v1/core/kv_cache_manager.py`:425; signals: block, cache, kv cache; excerpt: "During some intensive testing, this could happen when the GPU KV cache doesn't have enough blocks." (https://github.com/vllm-project/vllm/pull/15960#discussion_r2038613668)
- `2025-04-06T01:06:50Z` `issue` by `maobaolong`; signals: block, cache, kv cache; excerpt: "@ApostaC There are two question from my side. 1. Is those blocks possible to be evicted after Scheduler get external prefix cache blocks ? ..." (https://github.com/vllm-project/vllm/pull/15960#issuecomment-2781159839)
