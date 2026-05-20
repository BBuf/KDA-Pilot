# PR Discussion Digest

- Source PR: [vllm-project/vllm#13931](https://github.com/vllm-project/vllm/pull/13931)
- Source page: `sources/prs/vllm/PR-13931.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13931`
- Generated at: `2026-05-20T15:34:08.445420+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-26T22:44:59Z`
- Merged: `2025-03-05T05:27:26Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 27 (approved=1, commented=26)
- Inline review comments: 31
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=13, outdated=11
- Human participants with discussion text: DeepTecher, DefTruth, WhoisZihan, ZeldaHuang, ZhongYingMatrix, markmc, mergify, mgoin, nannaer, tlrmchlsmth, v-lmn, xiuxin121, youkaichao, zsnoob
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 19

## Review Decisions

- `2025-02-27T03:12:15Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2646460989)
- `2025-02-27T03:13:58Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2646462516)
- `2025-02-28T18:00:28Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2651462932)
- `2025-02-28T18:02:38Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2651467493)
- `2025-03-03T08:28:34Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653380711)
- `2025-03-03T08:28:50Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653381270)
- `2025-03-03T08:29:41Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653383134)
- `2025-03-03T08:31:27Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653386977)
- `2025-03-03T08:32:57Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653390045)
- `2025-03-03T09:23:05Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2653518623)
- `2025-03-03T14:21:25Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654266736)
- `2025-03-03T14:26:21Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654283426)
- `2025-03-03T16:03:38Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654570678)
- `2025-03-03T16:05:49Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654576356)
- `2025-03-03T16:07:04Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654579855)
- `2025-03-03T16:08:40Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654583935)
- `2025-03-03T16:10:50Z` `APPROVED` by `youkaichao` - LGTM in general, thanks for the great work! Do you happen to check if the output is the ... (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654592987)
- `2025-03-03T16:11:52Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654595719)
- `2025-03-03T16:24:30Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654628032)
- `2025-03-03T16:27:59Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654637067)
- `2025-03-04T01:29:30Z` `COMMENTED` by `tlrmchlsmth` - Must disable CUDA graphs by default when using DP+EP before landing, as it will deadlock otherwise (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2655707691)
- `2025-03-04T03:43:51Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2655849274)
- `2025-03-04T03:48:59Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2655856969)
- `2025-03-04T19:36:10Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2658769496)
- ... 1 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 14 inline comment(s)
- `vllm/forward_context.py`: 10 inline comment(s)
- `examples/offline_inference/data_parallel.py`: 1 inline comment(s)
- `vllm/model_executor/models/jamba.py`: 1 inline comment(s)
- `vllm/model_executor/models/dbrx.py`: 1 inline comment(s)
- `vllm/model_executor/models/aria.py`: 1 inline comment(s)
- `vllm/model_executor/models/olmoe.py`: 1 inline comment(s)
- `vllm/model_executor/models/phimoe.py`: 1 inline comment(s)
- `vllm/model_executor/models/qwen2_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-03T09:23:05Z` `inline` by `youkaichao` `vllm/model_executor/layers/fused_moe/layer.py`:788; signals: cuda, cudagraph, moe; excerpt: "this might not be compatible with cudagraph, since start depends on other ranks' data that are not considered in cudagraph." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1977148050)
- `2025-03-03T16:03:38Z` `inline` by `youkaichao` `vllm/model_executor/layers/fused_moe/layer.py`:788; signals: cuda, cudagraph, moe; excerpt: "agree cudagraph support would be tricky. let's not consider cudagraph right now then." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1977776637)
- `2025-03-03T16:10:50Z` `review` `APPROVED` by `youkaichao`; signals: h200, speedup, throughput; excerpt: "LGTM in general, thanks for the great work! Do you happen to check if the output is the same? And any throughput speedup for ..." (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2654592987)
- `2025-03-04T01:29:30Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: cuda, deadlock; excerpt: "Must disable CUDA graphs by default when using DP+EP before landing, as it will deadlock otherwise" (https://github.com/vllm-project/vllm/pull/13931#pullrequestreview-2655707691)
- `2025-02-28T18:00:28Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/layer.py`:710; signals: hang, moe; excerpt: "I'm a little opposed to this because the operations here work sufficiently differently compared to dispatch and combine that I'm not sure it makes ..." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1975823937)
- `2025-02-28T18:02:38Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/layer.py`:733; signals: cuda, moe; excerpt: "We need to reduce both within the DP group and within the TP group since each EP rank will have the partial accumulation of ..." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1975826837)
- `2025-03-03T08:31:27Z` `inline` by `youkaichao` `vllm/forward_context.py`:90; signals: hang, moe; excerpt: "we can change vllm config.compilation config.static forward context to vllm config.compilation config.static forward context.attn layers and vllm config.compilation config.static forward context.moe layers to be ..." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1977070274)
- `2025-03-03T14:26:21Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/layer.py`:788; signals: cuda, moe; excerpt: "You're right, this doesn't work with CUDA graphs. I had them working here , but the excess communication is trickier, at least without DeepEP. ..." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1977608792)
- `2025-03-04T03:42:03Z` `issue` by `youkaichao`; signals: cuda, deadlock; excerpt: "Must disable CUDA graphs by default when using DP+EP before landing, as it will deadlock otherwise let's do it in ?" (https://github.com/vllm-project/vllm/pull/13931#issuecomment-2696103439)
- `2025-03-04T03:44:56Z` `issue` by `tlrmchlsmth`; signals: cuda, deadlock; excerpt: "Must disable CUDA graphs by default when using DP+EP before landing, as it will deadlock otherwise let's do it in ? Nice, TIL about ..." (https://github.com/vllm-project/vllm/pull/13931#issuecomment-2696107099)
- `2025-02-27T03:13:58Z` `inline` by `youkaichao` `vllm/model_executor/layers/fused_moe/layer.py`:710; signals: moe; excerpt: "one suggestion (not sure if it sounds better): we can align with the terminology from deepep, use dispatch and combine here. and right now ..." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1972761224)
- `2025-03-03T16:08:40Z` `inline` by `youkaichao` `vllm/model_executor/layers/fused_moe/layer.py`:728; signals: moe; excerpt: "ideally this buffer can be static (with max size). and we can slice buffer[:cu tokens across dp cpu[-1]]." (https://github.com/vllm-project/vllm/pull/13931#discussion_r1977784635)
