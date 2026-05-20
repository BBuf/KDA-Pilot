# PR Discussion Digest

- Source PR: [vllm-project/vllm#31246](https://github.com/vllm-project/vllm/pull/31246)
- Source page: `sources/prs/vllm/PR-31246.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31246`
- Generated at: `2026-05-20T15:39:17.840007+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-23T23:25:20Z`
- Merged: `2026-01-21T22:49:51Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 26 (approved=1, commented=25)
- Inline review comments: 35
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=7, outdated=6
- Human participants with discussion text: chatgpt-codex-connector, chaunceyjiang, cursor, jeejeelee, mergify, mgoin, xyang16, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-23T23:27:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for sigmoid activation in the fused top-k Mixture-of-Experts (MoE) kernel, alongside ... (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3609547791)
- `2026-01-03T08:57:18Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3624259607)
- `2026-01-03T15:09:35Z` `COMMENTED` by `yewentao256` - Nice work! A few thoughts (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3624361098)
- `2026-01-07T06:18:45Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3633496217)
- `2026-01-07T06:19:00Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3633496731)
- `2026-01-07T06:40:47Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3633504699)
- `2026-01-07T13:47:33Z` `COMMENTED` by `chaunceyjiang` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3634982846)
- `2026-01-07T15:39:59Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3635500880)
- `2026-01-07T15:59:10Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3635520296)
- `2026-01-07T16:28:42Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3635707869)
- `2026-01-07T16:28:59Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3635709368)
- `2026-01-08T20:22:48Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3641133161)
- `2026-01-08T23:59:47Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3641776673)
- `2026-01-09T00:11:41Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3641796666)
- `2026-01-09T02:22:41Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3642084642)
- `2026-01-09T02:30:36Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3642094783)
- `2026-01-12T21:40:36Z` `COMMENTED` by `yewentao256` - Generally look good to me, please address the previous comments from @mgoin (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3652846148)
- `2026-01-20T03:55:22Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3680254877)
- `2026-01-20T20:35:11Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3684171952)
- `2026-01-20T20:51:31Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3684233792)
- `2026-01-21T20:23:54Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3635591718)
- `2026-01-21T20:32:06Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3689285787)
- `2026-01-21T20:46:20Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3689338267)
- `2026-01-21T20:46:30Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/31246#pullrequestreview-3689338773)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `csrc/moe/topk_softmax_kernels.cu`: 11 inline comment(s)
- `vllm/model_executor/models/minimax_m2.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`: 4 inline comment(s)
- `vllm/_aiter_ops.py`: 3 inline comment(s)
- `csrc/moe/torch_bindings.cpp`: 3 inline comment(s)
- `tests/kernels/moe/test_fused_topk.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-03T15:06:49Z` `inline` by `yewentao256` `csrc/moe/topk_softmax_kernels.cu`:737; signals: cuda, kernel, moe, tma; excerpt: "We could also check cuda tensor and is contiguous here" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2658967720)
- `2026-01-07T06:18:45Z` `inline` by `xyang16` `csrc/moe/topk_softmax_kernels.cu`:826; signals: kernel, moe, tma; excerpt: "Thanks for reviewing! Yes I think it's not necessary to be int64 t. But since the topk softmax also uses int64 t I just ..." (https://github.com/vllm-project/vllm/pull/31246#discussion_r2667206099)
- `2026-01-03T14:51:57Z` `inline` by `yewentao256` `csrc/moe/topk_softmax_kernels.cu`:826; signals: kernel, moe, tma; excerpt: "Is this workspace size int64 t needed?" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2658960690)
- `2026-01-07T06:19:00Z` `inline` by `xyang16` `csrc/moe/topk_softmax_kernels.cu`:737; signals: kernel, moe, tma; excerpt: "Added check. Thanks!" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2667206558)
- `2026-01-07T15:44:57Z` `inline` by `mgoin` `csrc/moe/topk_softmax_kernels.cu`:439; signals: kernel, moe, tma; excerpt: "This is missing pragma unroll to match the other case" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2668985992)
- `2026-01-07T15:46:44Z` `inline` by `mgoin` `csrc/moe/topk_softmax_kernels.cu`:40; signals: kernel, moe, tma; excerpt: "nit: consider an enum for ScoringFunc" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2668992315)
- `2026-01-07T16:28:59Z` `inline` by `xyang16` `csrc/moe/topk_softmax_kernels.cu`:439; signals: kernel, moe, tma; excerpt: "Thanks for catching this! Sorry to miss that." (https://github.com/vllm-project/vllm/pull/31246#discussion_r2669149510)
- `2026-01-08T20:22:48Z` `inline` by `yewentao256` `csrc/moe/topk_softmax_kernels.cu`:826; signals: kernel, moe, tma; excerpt: "Make sense, perhaps you can have a following up PR updating this later." (https://github.com/vllm-project/vllm/pull/31246#discussion_r2673772080)
- `2026-01-20T03:55:22Z` `inline` by `xyang16` `csrc/moe/topk_softmax_kernels.cu`:40; signals: kernel, moe, tma; excerpt: "@mgoin I have added ScoringFunc enum. Please take a look. Thanks!" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2706667607)
- `2026-01-21T20:31:35Z` `inline` by `mgoin` `csrc/moe/topk_softmax_kernels.cu`:224; signals: kernel, moe, tma; excerpt: "Might be worth a comment that you are using the original unbiased scores for output weights" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2714239436)
- `2026-01-21T20:46:20Z` `inline` by `xyang16` `csrc/moe/topk_softmax_kernels.cu`:224; signals: kernel, moe, tma; excerpt: "Added comment. Thanks!" (https://github.com/vllm-project/vllm/pull/31246#discussion_r2714282805)
- `2026-01-09T02:22:40Z` `inline` by `jeejeelee` `vllm/model_executor/models/minimax_m2.py`:105; signals: hang, moe; excerpt: "I mean wether we use topk simoid should be decided within FusedMoE, rather than change the model implementation by hardcoded way. Thus, GLM4.7 and ..." (https://github.com/vllm-project/vllm/pull/31246#discussion_r2674577478)
