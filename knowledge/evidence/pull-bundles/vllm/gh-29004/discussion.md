# PR Discussion Digest

- Source PR: [vllm-project/vllm#29004](https://github.com/vllm-project/vllm/pull/29004)
- Source page: `sources/prs/vllm/PR-29004.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29004`
- Generated at: `2026-05-20T15:38:36.678973+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-19T09:09:49Z`
- Merged: `2025-11-30T16:02:40Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: chatgpt-codex-connector, mergify, mgoin, omera-nv, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-19T09:11:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for non-gated activations in the NVFP4 modelopt path, which is a ... (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3481608410)
- `2025-11-19T09:17:48Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3481643109)
- `2025-11-19T14:55:24Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3482874082)
- `2025-11-19T16:16:09Z` `COMMENTED` by `omera-nv` (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3483629372)
- `2025-11-19T16:23:56Z` `COMMENTED` by `omera-nv` (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3483669758)
- `2025-11-25T14:11:34Z` `APPROVED` by `tlrmchlsmth` - Looks good to me now, thanks! (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3505266731)
- `2025-11-30T16:02:35Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3521617102)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-19T13:57:56Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:125; signals: cutlass, flashinfer, hang, moe; excerpt: "nit: try to avoid whitespace-only changes in otherwise untouched files" (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542128186)
- `2025-11-19T09:17:48Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/layer.py`:1287; signals: fp4, moe, nvfp4; excerpt: "tensor so it can compute the shard size along the TP-sharded dimension and copy the sliced view of loaded weight into the correct place. ..." (https://github.com/vllm-project/vllm/pull/29004#discussion_r2541179720)
- `2025-11-19T16:16:09Z` `inline` by `omera-nv` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:125; signals: cutlass, flashinfer, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542702805)
- `2025-11-19T16:23:56Z` `inline` by `omera-nv` `vllm/model_executor/layers/fused_moe/layer.py`:1287; signals: moe; excerpt: "param is correct when the experts are all in a single weight, param[expert id] is for when experts are kept in separate weights. Seems ..." (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542732910)
- `2025-11-19T09:17:48Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29004#pullrequestreview-3481643109)
- `2025-11-19T13:59:48Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/layer.py`:582; signals: moe; excerpt: "for clarity" (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542134676)
- `2025-11-19T14:55:22Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/layer.py`:1287; signals: moe; excerpt: "@omera-nv could you please check this?" (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542381539)
- `2025-11-19T14:53:32Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/quantization/modelopt.py`:1458; signals: general review; excerpt: "please address the bot's comment" (https://github.com/vllm-project/vllm/pull/29004#discussion_r2542373319)
- `2025-11-21T01:58:45Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @omera-nv." (https://github.com/vllm-project/vllm/pull/29004#issuecomment-3560986117)
- `2025-11-25T14:12:16Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @omera-nv." (https://github.com/vllm-project/vllm/pull/29004#issuecomment-3575854288)
