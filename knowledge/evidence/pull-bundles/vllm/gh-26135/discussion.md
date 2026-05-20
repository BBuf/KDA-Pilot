# PR Discussion Digest

- Source PR: [vllm-project/vllm#26135](https://github.com/vllm-project/vllm/pull/26135)
- Source page: `sources/prs/vllm/PR-26135.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26135`
- Generated at: `2026-05-20T15:38:03.879596+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-02T20:53:18Z`
- Merged: `2025-10-21T05:50:31Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: bnellnm, chatgpt-codex-connector, leejnau, mergify, mgoin, pavanimajety, wenscarl
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-07T02:59:18Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3308148272)
- `2025-10-16T22:16:57Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3347186020)
- `2025-10-17T00:41:22Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3347590169)
- `2025-10-17T04:35:56Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3348262662)
- `2025-10-17T14:06:43Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3350540137)
- `2025-10-17T18:57:36Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3351581770)
- `2025-10-17T21:29:00Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3352157353)
- `2025-10-18T21:21:11Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3353780104)
- `2025-10-18T21:30:02Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3353782226)
- `2025-10-20T15:30:11Z` `COMMENTED` by `wenscarl` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3356930944)
- `2025-10-20T23:57:56Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3358335692)
- `2025-10-20T23:59:34Z` `APPROVED` by `mgoin` - LGTM, although checking for local attrs in fused moe/layer.py doesn't feel good to keep doing I don't have ... (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3358350811)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-10-17T22:00:57Z` `issue` by `leejnau`; signals: accuracy, flashinfer, fp4, memory, moe, throughput; excerpt: "For the nvidia/DeepSeek-R1-0528-FP4-v2 model, in both TP4 and DP4 modes, with the FlashInfer backend, this PR raises the accuracy from 2% to 95%. server ..." (https://github.com/vllm-project/vllm/pull/26135#issuecomment-3417375697)
- `2025-10-17T04:35:56Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:1469; signals: cutlass, flashinfer, fp4, hang, moe; excerpt: "My question is specific to changing how we compute the input scale for cutlass moe fp4 path and the flashinfer paths. I think we ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2438347799)
- `2025-10-17T00:41:22Z` `inline` by `wenscarl` `vllm/model_executor/layers/quantization/modelopt.py`:1469; signals: fp4, hang, nvfp4; excerpt: "The scope should be limited to modelopt nvfp4 quantization only. To ensure consistency in subsequent multiplication dimensions, it’s preferable to preserve the original tensor ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2437920088)
- `2025-10-17T18:57:36Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1555; signals: cutlass, flashinfer, moe; excerpt: "If we want to be extra paranoid, it seems like we could limit this even further by checking if self.quant method.allow flashinfer and self.quant ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2440942930)
- `2025-10-16T22:16:57Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:1469; signals: hang, perf; excerpt: "Why are we performing a max and then running an expand? Also, w13 input scale.max(dim=1) takes a max of w1 and w3 and generates ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2437592272)
- `2025-10-17T21:29:00Z` `inline` by `wenscarl` `vllm/model_executor/layers/fused_moe/layer.py`:1555; signals: flashinfer, moe; excerpt: "yes. I will make it self.quant method.allow flashinfer and self.quant method.flashinfer moe backend in (some backends supporting EP) because the inconsistency of global scaling ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2441301010)
- `2025-10-07T02:59:18Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/layer.py`:1746; signals: moe; excerpt: "and layer.w2 input scale.max() therefore use garbage values, producing incorrect alphas for most experts. The loader should iterate over loaded weight (or parse the ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2409202995)
- `2025-10-18T21:30:02Z` `inline` by `pavanimajety` `vllm/model_executor/layers/fused_moe/layer.py`:1746; signals: moe; excerpt: "@leejnau / @wenscarl Could you please validate this? Ideally in post weight loading we want to ensure that we see different input scales for ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2442608193)
- `2025-10-20T15:30:11Z` `inline` by `wenscarl` `vllm/model_executor/layers/fused_moe/layer.py`:1746; signals: moe; excerpt: "Yes, in layer.py, 256 values are read in for each expert rank. In modelopt.py, max is taken among 256x2(w13)." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2445361952)
- `2025-10-20T23:57:36Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:1651; signals: moe; excerpt: "Would be good to put these three lines together and leave a comment on what use global sf means in this case since we ..." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2446402328)
- `2025-10-07T02:59:18Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/26135#pullrequestreview-3308148272)
- `2025-10-17T14:06:43Z` `inline` by `wenscarl` `vllm/model_executor/layers/quantization/modelopt.py`:1469; signals: hang; excerpt: "sure. Will make the change." (https://github.com/vllm-project/vllm/pull/26135#discussion_r2440156937)
