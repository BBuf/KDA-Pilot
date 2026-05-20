# PR Discussion Digest

- Source PR: [vllm-project/vllm#12583](https://github.com/vllm-project/vllm/pull/12583)
- Source page: `sources/prs/vllm/PR-12583.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12583`
- Generated at: `2026-05-20T15:33:45.922465+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-30T18:24:13Z`
- Merged: `2025-02-24T15:33:22Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 26 (approved=2, commented=24)
- Inline review comments: 35
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=21, outdated=16
- Human participants with discussion text: LucasWilkinson, Neo9061, cakeng, comaniac, lewisword, liweiqing1997, simon-mo, tlrmchlsmth, xiuxin121, yiz-liu, youkaichao, zarzen
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-01-30T22:40:50Z` `COMMENTED` by `comaniac` - Left some comment but overall LGTM (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2585183583)
- `2025-02-08T02:50:39Z` `COMMENTED` by `youkaichao` - the change in moe makes sense and it's great! I'm mainly concerned with the user interface. I don't ... (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2603205074)
- `2025-02-11T13:44:32Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2608798211)
- `2025-02-11T13:46:27Z` `COMMENTED` by `youkaichao` - since we have not finalize the user interface yet, I think we should not change the parallel config, ... (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2608803218)
- `2025-02-11T22:55:17Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2610293051)
- `2025-02-12T02:55:24Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2610704358)
- `2025-02-12T02:58:05Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2610707041)
- `2025-02-12T04:43:14Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2610798446)
- `2025-02-13T03:28:24Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2613739954)
- `2025-02-19T19:38:32Z` `APPROVED` by `LucasWilkinson` - Overall LGTM, left a couple comments (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627787456)
- `2025-02-19T19:41:40Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627803738)
- `2025-02-19T19:47:18Z` `COMMENTED` by `tlrmchlsmth` - The kernel looks good to me. There are a couple of places where the ep rank and the ... (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627686209)
- `2025-02-19T20:41:00Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627934902)
- `2025-02-19T20:50:56Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627952654)
- `2025-02-19T20:51:09Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627953029)
- `2025-02-19T20:51:20Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627953317)
- `2025-02-19T20:51:33Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627953728)
- `2025-02-19T20:52:45Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627955752)
- `2025-02-19T20:53:42Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627957456)
- `2025-02-19T20:54:33Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627959006)
- `2025-02-19T21:46:07Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2628051328)
- `2025-02-19T22:30:04Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2628120373)
- `2025-02-19T22:30:07Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2628120471)
- `2025-02-19T22:56:35Z` `COMMENTED` by `cakeng` (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2628156778)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 8 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 8 inline comment(s)
- `vllm/config.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/awq_marlin.py`: 4 inline comment(s)
- `vllm/engine/arg_utils.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/moe_torch_iterative.py`: 2 inline comment(s)
- `vllm/distributed/parallel_state.py`: 1 inline comment(s)
- `tests/utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-11T13:46:27Z` `review` `COMMENTED` by `youkaichao`; signals: block, hang, moe; excerpt: "since we have not finalize the user interface yet, I think we should not change the parallel config, nor add cli args for it. ..." (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2608803218)
- `2025-02-08T02:50:39Z` `review` `COMMENTED` by `youkaichao`; signals: hang, moe; excerpt: "the change in moe makes sense and it's great! I'm mainly concerned with the user interface. I don't think it makes sense to have ..." (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2603205074)
- `2025-02-19T19:47:18Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: kernel, moe; excerpt: "The kernel looks good to me. There are a couple of places where the ep rank and the tp rank in layers/fused moe.py look ..." (https://github.com/vllm-project/vllm/pull/12583#pullrequestreview-2627686209)
- `2025-02-04T18:42:27Z` `issue` by `LucasWilkinson`; signals: attention, cuda, mla; excerpt: "but the problem with CUDA graph seems to be on the current attention layer (MLA?) implementation. can you please elaborate on this, a bit? ..." (https://github.com/vllm-project/vllm/pull/12583#issuecomment-2634779819)
- `2025-02-04T23:25:05Z` `issue` by `cakeng`; signals: cuda, hang, moe; excerpt: "@youkaichao The current design support TP within an EP, but we can easily change that to have EP only on MoE layers. I think ..." (https://github.com/vllm-project/vllm/pull/12583#issuecomment-2635287239)
- `2025-02-12T02:55:24Z` `inline` by `youkaichao` `vllm/model_executor/layers/fused_moe/layer.py`:638; signals: compile, moe; excerpt: "can we directly put this into init with the correct device? doing it in forward might break torch.compile" (https://github.com/vllm-project/vllm/pull/12583#discussion_r1951905529)
- `2025-02-19T22:56:34Z` `inline` by `cakeng` `vllm/model_executor/layers/fused_moe/layer.py`:504; signals: hang, moe; excerpt: "I changed it to tp rank = 0 if self.ep size 1 else get tensor model parallel rank(), I think this is more explicit ..." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1962484850)
- `2025-02-21T09:11:47Z` `inline` by `cakeng` `vllm/model_executor/layers/fused_moe/moe_torch_iterative.py`:16; signals: kernel, moe; excerpt: "Thank you! Yes there were a bug in the test moe.py script making the iterative moe kernel from moe torch iterative.py pass when it ..." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1965131101)
- `2025-01-30T22:34:33Z` `inline` by `comaniac` `vllm/model_executor/layers/fused_moe/layer.py`:289; signals: moe; excerpt: "I feel this message may be confusing, because the TP size here is not the actual TP size provided by --tp. IIUC, it's tp ..." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1936381782)
- `2025-02-11T13:44:31Z` `inline` by `youkaichao` `vllm/config.py`:1396; signals: hang; excerpt: "why do we need to change the TP size? I think we should still create processes in the original tp size." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1950881657)
- `2025-02-11T22:55:17Z` `inline` by `cakeng` `vllm/config.py`:1396; signals: moe; excerpt: "Alright, I will remove args for expert parallel size for now and make FusedMoE layer check the env var directly." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1951721849)
- `2025-02-19T19:39:29Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/fused_moe.py`:589; signals: moe; excerpt: "Looks like if a global expert i is not on the current device, then expert map[i] == -1? Could you add this to the ..." (https://github.com/vllm-project/vllm/pull/12583#discussion_r1962267448)
