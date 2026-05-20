# PR Discussion Digest

- Source PR: [vllm-project/vllm#23991](https://github.com/vllm-project/vllm/pull/23991)
- Source page: `sources/prs/vllm/PR-23991.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23991`
- Generated at: `2026-05-20T15:37:44.543824+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-30T14:40:57Z`
- Merged: `2025-09-25T04:53:41Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 29 (approved=2, commented=27)
- Inline review comments: 27
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=1, outdated=11
- Human participants with discussion text: DarkLight1337, OftenDream, Xu-Wenqing, bnellnm, dragonhyq, mergify, simon-mo, unknown
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-08-30T14:43:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the LongCat-Flash model, including its architecture and a multi-token prediction ... (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3171065570)
- `2025-09-03T03:25:48Z` `COMMENTED` by `DarkLight1337` - Seems that some of the changes in this PR are not related to the model, can you fix ... (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3178817063)
- `2025-09-03T09:51:37Z` `COMMENTED` by `dragonhyq` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3179870523)
- `2025-09-03T11:36:14Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3180224141)
- `2025-09-05T03:29:04Z` `COMMENTED` by `dragonhyq` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3187884649)
- `2025-09-05T03:34:35Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3187889824)
- `2025-09-08T16:57:38Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3197358749)
- `2025-09-10T13:05:17Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3206073131)
- `2025-09-11T17:39:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3212987161)
- `2025-09-16T09:54:09Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3228817281)
- `2025-09-18T02:11:12Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3236982139)
- `2025-09-18T02:36:49Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3237063321)
- `2025-09-18T04:08:02Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3237203353)
- `2025-09-18T12:55:38Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3239525052)
- `2025-09-19T03:25:22Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3242730590)
- `2025-09-19T18:14:50Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246336408)
- `2025-09-19T18:15:15Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246338270)
- `2025-09-19T18:22:32Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246371352)
- `2025-09-19T18:26:15Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246390477)
- `2025-09-19T18:29:57Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246409041)
- `2025-09-19T18:30:46Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3246413066)
- `2025-09-21T09:01:56Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3249907874)
- `2025-09-21T09:02:03Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3249908711)
- `2025-09-21T09:02:09Z` `COMMENTED` by `OftenDream` (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3249908997)
- ... 5 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 12 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 5 inline comment(s)
- `vllm/model_executor/models/registry.py`: 4 inline comment(s)
- `vllm/config/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-03T07:29:17Z` `issue` by `OftenDream`; signals: attention, block, hang, pipeline; excerpt: "Seems that some of the changes in this PR are not related to the model, can you fix them? Member Thanks for the review! ..." (https://github.com/vllm-project/vllm/pull/23991#issuecomment-3248026042)
- `2025-09-18T04:08:02Z` `inline` by `OftenDream` `vllm/model_executor/layers/fused_moe/layer.py`:1726; signals: correctness, moe, triton; excerpt: "I have considered your suggested modification before. However, in zero experts compute triton, we set any values in topk ids greater than num experts ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2357456955)
- `2025-09-18T02:36:49Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1726; signals: hang, moe; excerpt: "Another option to simplify this further would be to make the quant method.apply return the topk weights and topk ids and then zero expert ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2357363939)
- `2025-09-19T18:26:15Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/fp8.py`:1004; signals: fp8, moe; excerpt: "Why not do topk weights, topk ids, zero expert result = FusedMoE.select experts(...) unconditionally?" (https://github.com/vllm-project/vllm/pull/23991#discussion_r2364039574)
- `2025-09-03T03:25:48Z` `review` `COMMENTED` by `DarkLight1337`; signals: hang; excerpt: "Seems that some of the changes in this PR are not related to the model, can you fix them?" (https://github.com/vllm-project/vllm/pull/23991#pullrequestreview-3178817063)
- `2025-09-04T20:23:18Z` `issue` by `simon-mo`; signals: hang, moe; excerpt: "I'm still looking the main concern is where do we put zero computation experts argument (given putting them in fused moe will change every ..." (https://github.com/vllm-project/vllm/pull/23991#issuecomment-3255486997)
- `2025-09-08T17:06:01Z` `issue` by `bnellnm`; signals: hang, moe; excerpt: "I'm still looking the main concern is where do we put zero computation experts argument (given putting them in fused moe will change every ..." (https://github.com/vllm-project/vllm/pull/23991#issuecomment-3267187225)
- `2025-09-08T16:57:37Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:548; signals: moe; excerpt: "This looks like it is going to cause problems with shared experts outputs (the tuple[torch.Tensor, torch.Tensor] case)" (https://github.com/vllm-project/vllm/pull/23991#discussion_r2330824668)
- `2025-09-10T13:05:17Z` `inline` by `OftenDream` `vllm/model_executor/layers/fused_moe/layer.py`:548; signals: moe; excerpt: "Thank you for observation. I have to return result and zero expert result separately because result need reduce and combine but zero expert result ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2336700479)
- `2025-09-11T17:39:22Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:499; signals: moe; excerpt: "Could this logic for the zero experts be moved to FusedMoE.forward impl around the call to self.quant method.apply? Then it wouldn't need to be ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2341892404)
- `2025-09-16T09:54:09Z` `inline` by `OftenDream` `vllm/model_executor/layers/fused_moe/layer.py`:499; signals: moe; excerpt: "Sure, I tried implementing your suggestion, but it introduces some difficulties. If the zero experts logic is moved to FusedMoE.forward impl, then topk weights ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2351747397)
- `2025-09-18T12:55:37Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1726; signals: moe; excerpt: "Ok, it was not obvious that topk ids was being mutated. Maybe the logic could be movied into select experts instead and it could ..." (https://github.com/vllm-project/vllm/pull/23991#discussion_r2359126364)
