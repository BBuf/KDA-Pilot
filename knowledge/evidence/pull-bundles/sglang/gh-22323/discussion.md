# PR Discussion Digest

- Source PR: [sgl-project/sglang#22323](https://github.com/sgl-project/sglang/pull/22323)
- Source page: `sources/prs/sglang/PR-22323.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22323`
- Generated at: `2026-05-20T15:29:23.468833+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T04:57:24Z`
- Merged: `2026-04-09T21:19:58Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, copilot-pull-request-reviewer, yushengsu-thu
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T05:15:44Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR refactors LoRA quant-info handling and adds DeepSeek V3 MLA LoRA support, while also ... (https://github.com/sgl-project/sglang/pull/22323#pullrequestreview-4072918752)
- `2026-04-08T21:20:54Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22323#pullrequestreview-4078314261)
- `2026-04-08T21:40:05Z` `COMMENTED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/22323#pullrequestreview-4078433065)
- `2026-04-09T21:19:39Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22323#pullrequestreview-4085492445)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/base_config.py`: 2 inline comment(s)
- `python/sglang/srt/lora/lora.py`: 1 inline comment(s)
- `python/sglang/srt/lora/layers.py`: 1 inline comment(s)
- `test/registered/lora/test_lora_deepseek_v3_base_logprob_diff.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-08T05:15:44Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: cache, cuda, dtype, hang, kernel, memory, mla, moe; excerpt: "Pull request overview This PR refactors LoRA quant-info handling and adds DeepSeek V3 MLA LoRA support, while also improving LoRA behavior under CUDA Graph ..." (https://github.com/sgl-project/sglang/pull/22323#pullrequestreview-4072918752)
- `2026-04-08T05:15:44Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/lora/layers.py`:823; signals: cache, fp4, fp8, kernel, moe, nvfp4, triton; excerpt: "FusedMoEWithLoRA caches self. quant info = base layer.quant method.get triton quant info(base layer), but some MoE quant methods (e.g. ModelOptFp8MoEMethod in layers/quantization/modelopt quant.py) construct ..." (https://github.com/sgl-project/sglang/pull/22323#discussion_r3049319342)
- `2026-04-08T21:20:28Z` `inline` by `Fridge003` `test/registered/lora/test_lora_deepseek_v3_base_logprob_diff.py`:39; signals: b200, register; excerpt: "Register to nightly-8-gpu-b200 Also please post the result of running this test on 8-gpu b200" (https://github.com/sgl-project/sglang/pull/22323#discussion_r3054235690)
- `2026-04-08T05:15:44Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/lora/lora.py`:271; signals: general review; excerpt: "normalize fused qkv a proj falls back to torch.zeros like(q a) when kv a proj with mqa weights are missing. For LoRA B this ..." (https://github.com/sgl-project/sglang/pull/22323#discussion_r3049319311)
- `2026-04-09T18:36:42Z` `issue` by `yushengsu-thu`; signals: b200; excerpt: "stage-b-test-4-gpu-b200" (https://github.com/sgl-project/sglang/pull/22323#issuecomment-4216571341)
- `2026-04-08T21:19:45Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/base_config.py`:121; signals: general review; excerpt: "raise NotImplementedError here since it's base class" (https://github.com/sgl-project/sglang/pull/22323#discussion_r3054232813)
- `2026-04-08T21:40:05Z` `inline` by `yushengsu-thu` `python/sglang/srt/layers/quantization/base_config.py`:121; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/22323#discussion_r3054335190)
