# PR Discussion Digest

- Source PR: [sgl-project/sglang#14105](https://github.com/sgl-project/sglang/pull/14105)
- Source page: `sources/prs/sglang/PR-14105.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14105`
- Generated at: `2026-05-20T15:27:55.524671+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-28T15:49:54Z`
- Merged: `2026-03-24T20:14:15Z`

## Discussion Counts

- Issue comments: 42
- Review submissions: 22 (approved=3, changes_requested=2, commented=17)
- Inline review comments: 40
- Review threads observed: 28
- Resolved/outdated thread markers: resolved=16, outdated=21
- Human participants with discussion text: Fridge003, HydraQYH, XiaotaoChen, copilot-pull-request-reviewer, jonahbernard, ping1jing2, tugot17, yushengsu-thu
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-12T23:57:58Z` `CHANGES_REQUESTED` by `yushengsu-thu` - @Jonahcb 1. According to the current codebase structure, I feel it's better to move ? Besides, lora moe ... (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3573943612)
- `2026-01-02T19:32:51Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR adds LoRA (Low-Rank Adaptation) support for MoE (Mixture of Experts) layers in SGLang, ... (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3623767803)
- `2026-02-09T23:08:55Z` `COMMENTED` by `yushengsu-thu` - @Jonahcb, I studied this PR over the past two days, and I’m considering LoRA MoE maintainability and future ... (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3775880894)
- `2026-02-16T01:29:26Z` `COMMENTED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3776750479)
- `2026-02-16T01:46:41Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3806220526)
- `2026-02-16T02:08:41Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3806283934)
- `2026-02-16T02:08:47Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3806284344)
- `2026-02-16T02:13:34Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3806291612)
- `2026-02-16T15:11:28Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3809153482)
- `2026-02-22T03:03:20Z` `APPROVED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3836589971)
- `2026-02-27T01:44:24Z` `COMMENTED` by `HydraQYH` - Please add a unit test for moe lora align kernel first. (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3864413176)
- `2026-02-27T02:11:18Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3864476048)
- `2026-02-27T11:33:27Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3866463491)
- `2026-02-27T14:02:35Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3867108232)
- `2026-02-28T03:07:58Z` `COMMENTED` by `XiaotaoChen` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3869987165)
- `2026-03-01T21:06:22Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3873384000)
- `2026-03-01T21:07:38Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3873385286)
- `2026-03-02T17:56:57Z` `CHANGES_REQUESTED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3877782580)
- `2026-03-02T18:29:57Z` `COMMENTED` by `jonahbernard` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3877941467)
- `2026-03-22T22:26:17Z` `APPROVED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3988686829)
- `2026-03-23T23:56:03Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3995347335)
- `2026-03-24T08:25:02Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3997202024)

## Inline Comment Hotspots

- `python/sglang/srt/lora/layers.py`: 14 inline comment(s)
- `python/sglang/srt/lora/triton_ops/fused_moe_lora_kernel.py`: 7 inline comment(s)
- `python/sglang/srt/lora/mem_pool.py`: 6 inline comment(s)
- `python/sglang/jit_kernel/moe_lora_align.py`: 4 inline comment(s)
- `python/sglang/srt/lora/lora_manager.py`: 3 inline comment(s)
- `python/sglang/srt/lora/triton_ops/per_expert_lora_moe.py`: 2 inline comment(s)
- `test/registered/lora/test_lora_moe_runner.py`: 2 inline comment(s)
- `sgl-kernel/csrc/moe/moe_lora_align_sum_kernel.cu`: 1 inline comment(s)
- `python/sglang/jit_kernel/csrc/lora/moe_lora_align_kernel.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-02T19:32:51Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: correctness, hang, kernel, memory, moe, register, triton; excerpt: "Pull request overview This PR adds LoRA (Low-Rank Adaptation) support for MoE (Mixture of Experts) layers in SGLang, enabling fine-tuned MoE models to be ..." (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3623767803)
- `2026-02-09T23:08:55Z` `review` `COMMENTED` by `yushengsu-thu`; signals: gemm, hang, kernel, moe, pipeline, race; excerpt: "@Jonahcb, I studied this PR over the past two days, and I’m considering LoRA MoE maintainability and future development; thus, I have a few ..." (https://github.com/sgl-project/sglang/pull/14105#pullrequestreview-3775880894)
- `2026-02-13T19:34:24Z` `issue` by `jonahbernard`; signals: benchmark, block, kernel, moe, perf, performance; excerpt: "@yushengsu-thu There is a lot of common functionality between the new moe lora align sum kernel.cu (vLLM's) and SGLang's current moe align kernel.cu. Merging ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3899026108)
- `2026-02-15T23:01:57Z` `issue` by `yushengsu-thu`; signals: benchmark, block, kernel, moe, perf, performance; excerpt: "@yushengsu-thu There is a lot of common functionality between the new moe lora align sum kernel.cu (vLLM's) and SGLang's current moe align kernel.cu. Merging ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3905343843)
- `2026-02-28T05:33:00Z` `issue` by `XiaotaoChen`; signals: bf16, dtype, fp8, kernel, latency, moe; excerpt: "@Jonahcb I tried it with the generated lora model by peft(script as belows), it works normally. Do you have any idea to support EPMoE, ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3976435429)
- `2026-03-01T21:29:48Z` `issue` by `jonahbernard`; signals: bf16, dtype, fp8, kernel, latency, moe; excerpt: "@Jonahcb I tried it with the generated lora model by peft(script as belows), it works normally. Do you have any idea to support EPMoE, ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3981065555)
- `2026-03-15T08:19:25Z` `issue` by `yushengsu-thu`; signals: cache, failing, hang, kernel, moe, triton; excerpt: "After the beforehead 2 PRs merge, I gotta modify below to match vllm ( acc (b/c some codes were changed on upstream): Bug Fix: ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-4062542243)
- `2026-02-15T23:08:22Z` `inline` by `yushengsu-thu` `python/sglang/srt/lora/triton_ops/fused_moe_lora_kernel.py`:6; signals: blackwell, kernel, moe, sm90, triton; excerpt: "Why do you import is arch support pdl and is sm90 supported, is blackwell supported? Their functions are similar. Besides, I found you did ..." (https://github.com/sgl-project/sglang/pull/14105#discussion_r2810077973)
- `2026-02-16T01:46:41Z` `inline` by `jonahbernard` `python/sglang/srt/lora/triton_ops/fused_moe_lora_kernel.py`:6; signals: blackwell, kernel, moe, sm90, triton; excerpt: "@yushengsu-thu is arch support pdl was a leftover import. Removed it. The GDC operations that are used in the fused moe lora kernel are ..." (https://github.com/sgl-project/sglang/pull/14105#discussion_r2810347165)
- `2026-03-01T01:57:59Z` `issue` by `yushengsu-thu`; signals: kernel, moe, nan, pipeline, triton; excerpt: "Hello @Jonahcb, we’re going to merge this PR now. To make maintenance easier, we’ll split this large PR into three parts (PRs): 1. triton ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3978842169)
- `2026-03-01T02:00:22Z` `issue` by `jonahbernard`; signals: kernel, moe, nan, pipeline, triton; excerpt: "Hello @Jonahcb, we’re going to merge this PR now. To make maintenance easier, we’ll split this large PR into three parts: 1. triton kernel ..." (https://github.com/sgl-project/sglang/pull/14105#issuecomment-3978845616)
- `2026-02-28T03:07:59Z` `inline` by `XiaotaoChen` `python/sglang/srt/lora/triton_ops/fused_moe_lora_kernel.py`:411; signals: cache, kernel, moe, triton; excerpt: "@Jonahcb Hi, I‘m a bit confused about the func，which implemnets (input feat @ lora a) @ lora b. it's okay when there are no ..." (https://github.com/sgl-project/sglang/pull/14105#discussion_r2866972227)
