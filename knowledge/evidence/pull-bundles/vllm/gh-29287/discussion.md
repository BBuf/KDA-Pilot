# PR Discussion Digest

- Source PR: [vllm-project/vllm#29287](https://github.com/vllm-project/vllm/pull/29287)
- Source page: `sources/prs/vllm/PR-29287.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29287`
- Generated at: `2026-05-20T15:38:41.039639+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-24T02:11:14Z`
- Merged: `2026-01-21T15:16:30Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 31 (approved=1, changes_requested=1, commented=29)
- Inline review comments: 36
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=6, outdated=13
- Human participants with discussion text: chatgpt-codex-connector, cursor, ganyi1996ppo, gronsti-amd, heheda12345, mergify, tjtanaa, vllmellm
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-24T13:49:12Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3500475585)
- `2025-11-26T01:04:30Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3507718111)
- `2025-11-26T01:07:24Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3507730885)
- `2025-11-26T01:10:57Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3507745715)
- `2025-11-26T02:18:05Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3508055291)
- `2025-11-26T02:23:41Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3508088148)
- `2025-11-26T02:43:40Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3508199861)
- `2025-11-27T13:05:24Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3515260184)
- `2025-11-30T19:23:42Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3522135425)
- `2025-12-18T12:01:15Z` `CHANGES_REQUESTED` by `gronsti-amd` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3592554163)
- `2025-12-18T14:02:50Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3593155845)
- `2025-12-30T10:17:24Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3617820615)
- `2025-12-30T10:17:49Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3617821312)
- `2025-12-30T12:04:35Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3618010589)
- `2025-12-30T12:07:40Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3618016681)
- `2026-01-05T12:25:26Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3625982384)
- `2026-01-06T03:35:01Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3629220324)
- `2026-01-07T06:40:11Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3633549254)
- `2026-01-16T05:55:31Z` `COMMENTED` by `cursor` - Cursor Bugbot has reviewed your changes and found 4 potential issues. Bugbot Autofix is OFF. To automatically fix ... (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3669029955)
- `2026-01-16T06:00:26Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3669049728)
- `2026-01-16T06:03:10Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3669060869)
- `2026-01-16T06:06:29Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3669071271)
- `2026-01-21T02:38:48Z` `COMMENTED` by `tjtanaa` - I added some comments to expedite the review. I will add more in the next couple hours. (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3669148341)
- `2026-01-21T02:44:09Z` `COMMENTED` by `ganyi1996ppo` (https://github.com/vllm-project/vllm/pull/29287#pullrequestreview-3685119810)
- ... 7 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`: 11 inline comment(s)
- `vllm/model_executor/layers/sparse_attn_indexer.py`: 7 inline comment(s)
- `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`: 5 inline comment(s)
- `vllm/attention/ops/rocm_aiter_mla_sparse.py`: 3 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 3 inline comment(s)
- `vllm/v1/attention/backends/mla/indexer.py`: 2 inline comment(s)
- `vllm/_aiter_ops.py`: 2 inline comment(s)
- `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`: 2 inline comment(s)
- `vllm/platforms/rocm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-26T02:18:05Z` `inline` by `ganyi1996ppo` `vllm/attention/ops/rocm_aiter_mla_sparse.py`:19; signals: attention, block, cache, cuda, deepgemm, fp8, gemm, kernel; excerpt: "Thanks for the comments. This triton kernel is mainly used to do the layout shuffle aside from quant and cache functionality. we will shuffle ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2562546489)
- `2025-12-18T12:00:53Z` `inline` by `gronsti-amd` `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`:146; signals: attention, cuda, cudagraph, mla, perf, speedup; excerpt: "We did some profiling for DeepSeek v3.2, and noticed unexpected cuda graph breaks in decode. It seems that they are caused by a small ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2630777277)
- `2025-11-24T13:49:12Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`:185; signals: attention, block, cache, kernel, mla; excerpt: ", but the ROCM metadata builder still initializes paged kv last page len to all ones and never derives the actual last-page lengths before ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2556362032)
- `2025-11-26T01:04:30Z` `inline` by `heheda12345` `vllm/attention/ops/rocm_aiter_mla_sparse.py`:19; signals: attention, cuda, kernel, mla, triton; excerpt: "@LucasWilkinson do you think it is a good idea to use these triton kernel for CUDA platform? I'm not sure whether it is faster ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2562272603)
- `2025-11-26T02:23:41Z` `inline` by `ganyi1996ppo` `vllm/attention/ops/rocm_aiter_mla_sparse.py`:19; signals: attention, cuda, cudagraph, mla, triton; excerpt: "Although, we might consider to rewrite those part of code to cuda, to reduce the host overhead triton might brought during piecewise cudagraph, but ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2562567491)
- `2026-01-20T16:05:17Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:415; signals: attention, fp8, kernel, mla, triton; excerpt: "In the AITER version used in the Dockerfile.rocm base, the kernel existed already. However, the path is different from the one used in latest ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2709033828)
- `2025-11-26T02:43:40Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/backends/mla/indexer.py`:239; signals: attention, kernel, mla, oom; excerpt: "I think that kernel still have room for improvement..... And I'm doing that too, will file a PR to optimize it recently." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2562647817)
- `2026-01-16T06:29:43Z` `inline` by `tjtanaa` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:115; signals: attention, cache, fp8, mla; excerpt: "there is a helper function current platform.is fp8 fnuz(), can you also help to add cache decorator to is fp8 fnuz ?" (https://github.com/vllm-project/vllm/pull/29287#discussion_r2697169690)
- `2026-01-21T02:45:45Z` `inline` by `ganyi1996ppo` `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`:115; signals: attention, cache, compile, mla; excerpt: "I found cache decorator can not be captured by torch.compile, maybe we can leave this one? This host overhead should minor to big models ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2710757962)
- `2025-11-26T01:10:57Z` `inline` by `heheda12345` `vllm/v1/attention/backends/mla/indexer.py`:239; signals: attention, kernel, mla; excerpt: "what's the difference between AMD kernel and NV kernel? Why NV kernel doesn't need this token to seq?" (https://github.com/vllm-project/vllm/pull/29287#discussion_r2562298422)
- `2025-12-30T12:07:40Z` `inline` by `ganyi1996ppo` `vllm/_aiter_ops.py`:1171; signals: attention, mla, triton; excerpt: "@tjtanaa I move the defination of rocm aiter sprase atn indexer and other triton ops back to the vllm/attention/ops/rocm aiter mla sparse, but keep ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2652870998)
- `2026-01-16T05:55:32Z` `inline` by `cursor` `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`:196; signals: attention, bf16, mla; excerpt: "Buffer undersized causing crash when tokens exceed sequences High Severity The paged kv last page len buffer is sized to max num seqs and ..." (https://github.com/vllm-project/vllm/pull/29287#discussion_r2697065796)
