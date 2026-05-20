# PR Discussion Digest

- Source PR: [vllm-project/vllm#28124](https://github.com/vllm-project/vllm/pull/28124)
- Source page: `sources/prs/vllm/PR-28124.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28124`
- Generated at: `2026-05-20T15:38:25.501386+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T12:34:42Z`
- Merged: `2025-11-08T02:20:55Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 9
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=4
- Human participants with discussion text: chatgpt-codex-connector, mgoin, pavanimajety, robertgshaw2-redhat, vadiklyutiy, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T12:36:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization by fusing sigmoid activation and bias addition into the ... (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3421735182)
- `2025-11-05T12:38:55Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3421744107)
- `2025-11-05T16:37:17Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3423187610)
- `2025-11-06T16:38:00Z` `COMMENTED` by `yewentao256` - Thanks for the work! (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3429261578)
- `2025-11-06T17:47:22Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3429642514)
- `2025-11-06T17:48:09Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3429646720)
- `2025-11-07T15:28:11Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3434667060)
- `2025-11-07T16:51:51Z` `APPROVED` by `pavanimajety` - Thanks for the PR, LGTM! (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3435173531)

## Inline Comment Hotspots

- `csrc/moe/grouped_topk_kernels.cu`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 2 inline comment(s)
- `csrc/moe/moe_ops.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-05T12:38:55Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1355; signals: bf16, dtype, kernel, memory, moe; excerpt: ". When gating output is BF16/FP16—which is common while the correction bias parameters remain FP32—the kernel will read the FP32 memory as 16‑bit values, ..." (https://github.com/vllm-project/vllm/pull/28124#discussion_r2494297804)
- `2025-11-05T16:37:17Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1343; signals: dtype, kernel, moe, tma; excerpt: "before launch. Please convert e score correction bias to the dtype of gating output (and the softmax result) before invoking the custom op, or ..." (https://github.com/vllm-project/vllm/pull/28124#discussion_r2495293515)
- `2025-11-06T17:48:09Z` `inline` by `mgoin` `csrc/moe/grouped_topk_kernels.cu`:749; signals: dtype, kernel, moe; excerpt: "I thought that pytorch requires int64 t for int dtype in the torch bindings" (https://github.com/vllm-project/vllm/pull/28124#discussion_r2500129218)
- `2025-11-05T17:37:27Z` `issue` by `vadiklyutiy`; signals: kernel, perf, performance; excerpt: "In 28086 one option is use TRT-LLM kernel. Is there any optimization(s) in TRT-LLM kernel that we don't bring to vLLM? In other words, ..." (https://github.com/vllm-project/vllm/pull/28124#issuecomment-3492524968)
- `2025-11-06T17:47:21Z` `inline` by `mgoin` `csrc/moe/grouped_topk_kernels.cu`:768; signals: kernel, moe; excerpt: "The original code in the calling function did return topk values.to(torch.float32), topk indices.to(torch.int32), so I just wanted to fuse this. I'm not sure it ..." (https://github.com/vllm-project/vllm/pull/28124#discussion_r2500126258)
- `2025-11-06T16:36:31Z` `inline` by `yewentao256` `csrc/moe/grouped_topk_kernels.cu`:749; signals: kernel, moe; excerpt: "Why don't we use int for scoring func and remove the static cast ?" (https://github.com/vllm-project/vllm/pull/28124#discussion_r2499813464)
- `2025-11-06T16:37:25Z` `inline` by `yewentao256` `csrc/moe/grouped_topk_kernels.cu`:768; signals: kernel, moe; excerpt: "What does this mean for "eliminates Python-side conversion", could you add more comments here?" (https://github.com/vllm-project/vllm/pull/28124#discussion_r2499817613)
- `2025-11-05T12:38:55Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub [Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3421744107)
- `2025-11-05T16:37:17Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub [Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3423187610)
- `2025-11-06T08:20:07Z` `issue` by `mgoin`; signals: kernel; excerpt: "I couldn't find anything obvious that the trtllm kernel does differently. This kernel was originally pulled from trtllm a few months ago, so they ..." (https://github.com/vllm-project/vllm/pull/28124#issuecomment-3495787005)
- `2025-11-06T16:38:00Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work!" (https://github.com/vllm-project/vllm/pull/28124#pullrequestreview-3429261578)
