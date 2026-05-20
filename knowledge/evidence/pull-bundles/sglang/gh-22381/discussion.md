# PR Discussion Digest

- Source PR: [sgl-project/sglang#22381](https://github.com/sgl-project/sglang/pull/22381)
- Source page: `sources/prs/sglang/PR-22381.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22381`
- Generated at: `2026-05-20T15:29:25.451962+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T19:57:38Z`
- Merged: `2026-04-10T05:31:53Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: Fridge003, copilot-pull-request-reviewer, yushengsu-thu
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T20:04:58Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR extends SGLang’s LoRA support to cover Kimi-K2.5 / DeepSeek-style MLA fused projections and ... (https://github.com/sgl-project/sglang/pull/22381#pullrequestreview-4077921489)
- `2026-04-10T05:30:54Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22381#pullrequestreview-4087444345)

## Inline Comment Hotspots

- `python/sglang/srt/lora/lora.py`: 1 inline comment(s)
- `python/sglang/srt/lora/layers.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-08T20:04:58Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: accuracy, block, cuda, fp8, gemm, hang, layout, mla; excerpt: "Pull request overview This PR extends SGLang’s LoRA support to cover Kimi-K2.5 / DeepSeek-style MLA fused projections and improves MoE+LoRA compatibility across multiple quantization ..." (https://github.com/sgl-project/sglang/pull/22381#pullrequestreview-4077921489)
- `2026-04-08T20:04:58Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/lora/layers.py`:829; signals: hang, kernel, moe, triton; excerpt: "FusedMoEWithLoRA currently falls back to MoeRunnerBackend.TRITON when the quant method has no runner, and then always builds quant info via quant method.get triton quant ..." (https://github.com/sgl-project/sglang/pull/22381#discussion_r3053876782)
- `2026-04-08T20:04:57Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/lora/lora.py`:268; signals: alignment; excerpt: "In normalize fused qkv a proj, the fallback for missing kv a proj with mqa uses torch.zeros like(weights[q a name]). This is only safe ..." (https://github.com/sgl-project/sglang/pull/22381#discussion_r3053876735)
- `2026-04-09T23:02:59Z` `issue` by `yushengsu-thu`; signals: general review; excerpt: "Currently, the logprb is bite large but we have three PRs will be merged to fix this class ReplicatedLinearWithLoRA(BaseLayerWithLoRA) (dsk, kimi lora use this) ..." (https://github.com/sgl-project/sglang/pull/22381#issuecomment-4218318651)
