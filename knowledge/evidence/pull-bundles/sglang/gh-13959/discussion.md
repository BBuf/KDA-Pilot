# PR Discussion Digest

- Source PR: [sgl-project/sglang#13959](https://github.com/sgl-project/sglang/pull/13959)
- Source page: `sources/prs/sglang/PR-13959.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13959`
- Generated at: `2026-05-20T15:27:53.141306+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-26T03:22:12Z`
- Merged: `2026-01-02T15:49:14Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 17 (approved=1, changes_requested=2, commented=14)
- Inline review comments: 32
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=19, outdated=9
- Human participants with discussion text: Fridge003, ch-wan, llc-kc, whybeyoung, xu-yfei, yhyang201, yiakwy-xpu-ml-framework-team
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-11-26T10:52:50Z` `COMMENTED` by `ch-wan` - Could you add some test cases? I will have a closer check tomorrow. (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3510349292)
- `2025-12-21T06:39:51Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3574276823)
- `2025-12-22T02:26:17Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3602352138)
- `2025-12-22T04:00:15Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3602556941)
- `2025-12-23T09:07:26Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3606957112)
- `2025-12-23T09:23:28Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607292105)
- `2025-12-23T09:24:58Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607301922)
- `2025-12-23T09:27:10Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607313915)
- `2025-12-23T09:30:16Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607325628)
- `2025-12-23T09:35:52Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607343532)
- `2025-12-23T09:39:24Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607353449)
- `2025-12-23T09:40:08Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607355379)
- `2025-12-23T09:41:30Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607359216)
- `2025-12-23T09:43:29Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3607364688)
- `2025-12-25T09:20:13Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3612051318)
- `2025-12-25T09:27:51Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3612065291)
- `2025-12-28T07:48:38Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13959#pullrequestreview-3614566889)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa/utils.py`: 8 inline comment(s)
- `python/sglang/srt/layers/attention/nsa_backend.py`: 6 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 4 inline comment(s)
- `python/sglang/srt/layers/communicator.py`: 4 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 3 inline comment(s)
- `docs/advanced_features/server_arguments.md`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/layers/communicator_nsa_cp.py`: 2 inline comment(s)
- `docs/basic_usage/deepseek_v32.md`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-23T07:37:04Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:1843; signals: cache, fp8, kv cache, mla; excerpt: "concat mla absorb q general is for concatnation of q. It assumes that the last dim of k nope and k pe are 512 ..." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642265344)
- `2025-11-28T03:04:15Z` `issue` by `xu-yfei`; signals: hang, moe, perf, performance; excerpt: "Out of curiosity, may I ask whether the performance before the PR was measured after tuning? If not, could you please provide the performance ..." (https://github.com/sgl-project/sglang/pull/13959#issuecomment-3587769648)
- `2025-12-23T09:24:58Z` `inline` by `xu-yfei` `python/sglang/srt/models/deepseek_v2.py`:1843; signals: cache, dtype, kv cache; excerpt: "k nope and k pe are not retrieved from the KV cache, but generated through computation, and both are in bfloat16 dtype." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642548287)
- `2025-11-27T15:43:41Z` `issue` by `yhyang201`; signals: hang, perf, performance; excerpt: "Out of curiosity, may I ask whether the performance before the PR was measured after tuning? If not, could you please provide the performance ..." (https://github.com/sgl-project/sglang/pull/13959#issuecomment-3586520005)
- `2025-12-21T06:25:54Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:258; signals: attention, hang; excerpt: "Will moving the allgather after rotation affect result? Since the q and k for rotate activateion changed" (https://github.com/sgl-project/sglang/pull/13959#discussion_r2637615451)
- `2025-12-22T02:26:17Z` `inline` by `xu-yfei` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:258; signals: attention, perf; excerpt: "The result will not be affected. rotate activation, i.e., hadamard transform, operates on the head dim dimension, while cp all gather rerange output targets ..." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2638412920)
- `2025-12-23T08:33:11Z` `inline` by `Fridge003` `python/sglang/srt/layers/communicator.py`:552; signals: kernel, moe; excerpt: "Does this apply for both cp mode? For in-seq mode, deepep doesn't apply reduce scatter after the moe kernel" (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642385491)
- `2025-12-23T08:52:41Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:496; signals: attention, hang; excerpt: "Can you please run dpsk v3.2 with pure tp 8 and see whether this change breaks anything. Or this change can be split into ..." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642436642)
- `2025-12-23T09:41:30Z` `inline` by `xu-yfei` `python/sglang/srt/layers/communicator_nsa_cp.py`:18; signals: cute, moe; excerpt: "The in-seq CP mode can execute properly, and this implementation takes both the DeepEP and Fused MoE into account." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642595771)
- `2025-12-23T08:30:51Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/utils.py`:164; signals: attention, hang; excerpt: "Can we change a name for this util function. It can be easily confused with nsa enable prefill cp" (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642380442)
- `2025-11-26T15:55:41Z` `issue` by `whybeyoung`; signals: perf, performance; excerpt: "maybe we can combine the pp to gain the best performance" (https://github.com/sgl-project/sglang/pull/13959#issuecomment-3582015179)
- `2025-12-23T08:20:13Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/utils.py`:233; signals: attention; excerpt: "We need to put this part in a new util function for all gather rearange on continuous split mode. A figure(like line 219-232 above) ..." (https://github.com/sgl-project/sglang/pull/13959#discussion_r2642355677)
