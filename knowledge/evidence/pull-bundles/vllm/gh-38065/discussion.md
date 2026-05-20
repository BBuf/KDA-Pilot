# PR Discussion Digest

- Source PR: [vllm-project/vllm#38065](https://github.com/vllm-project/vllm/pull/38065)
- Source page: `sources/prs/vllm/PR-38065.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38065`
- Generated at: `2026-05-20T15:40:28.625139+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T04:01:20Z`
- Merged: `2026-04-27T05:44:16Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 23 (approved=1, commented=22)
- Inline review comments: 33
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=9, outdated=12
- Human participants with discussion text: Isotr0py, ProExpertProg, mergify, zhandaz
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T04:06:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces comprehensive support for FP8 attention in multimodal encoders (specifically ViT) within the ... (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4003780397)
- `2026-03-27T17:01:24Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4022356741)
- `2026-04-02T20:52:56Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4053159776)
- `2026-04-02T20:55:39Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4053170267)
- `2026-04-02T20:55:51Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4053171488)
- `2026-04-02T20:58:41Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4053182742)
- `2026-04-02T22:02:33Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4053428979)
- `2026-04-03T17:39:42Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4056592661)
- `2026-04-06T17:31:43Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4063433752)
- `2026-04-06T17:36:00Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4063459092)
- `2026-04-21T06:54:06Z` `COMMENTED` by `Isotr0py` - Overall look reasonable. Have some nits. PTAL! (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4144951078)
- `2026-04-22T15:32:04Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4155929891)
- `2026-04-22T15:35:10Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4155948568)
- `2026-04-22T15:38:43Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4155970117)
- `2026-04-22T15:41:39Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4155988015)
- `2026-04-22T16:43:35Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4156135912)
- `2026-04-23T04:11:50Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159601393)
- `2026-04-23T04:12:00Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159601772)
- `2026-04-23T04:12:13Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159602327)
- `2026-04-23T04:12:29Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159602904)
- `2026-04-23T04:12:36Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159603192)
- `2026-04-23T04:16:06Z` `COMMENTED` by `zhandaz` (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4159613535)
- `2026-04-23T07:10:48Z` `APPROVED` by `Isotr0py` - Overall LGTM now! Thanks for your patience! (https://github.com/vllm-project/vllm/pull/38065#pullrequestreview-4160364272)

## Inline Comment Hotspots

- `vllm/model_executor/layers/attention/mm_encoder_attention.py`: 11 inline comment(s)
- `vllm/config/multimodal.py`: 6 inline comment(s)
- `vllm/envs.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/input_quant_fp8.py`: 4 inline comment(s)
- `vllm/model_executor/models/vision.py`: 4 inline comment(s)
- `vllm/model_executor/models/qwen3_vl.py`: 2 inline comment(s)
- `vllm/utils/flashinfer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-02T22:02:33Z` `inline` by `zhandaz` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:66; signals: accuracy, attention, bf16, fp8, kernel; excerpt: "Yeah. You raised a very good point and it is a design choice we wanted to discuss. Because we typically don't apply PTQ to ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3030581072)
- `2026-04-23T04:16:06Z` `inline` by `zhandaz` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:358; signals: attention, cache, fp8, kv cache, register; excerpt: "Thanks for the confirmation! Done. MMEncoderAttention is now added to the auto-scan tuple in vllm/model executor/model loader/utils.py: Following the existing pattern used by Attention, ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3128311364)
- `2026-04-21T06:26:47Z` `inline` by `Isotr0py` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:604; signals: attention, fp8, kernel, triton; excerpt: "I think it's better to place this as helper function in vllm/kernels/triton/qkv padded fp8 quant.py instead of class method." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3115462061)
- `2026-04-06T17:34:19Z` `issue` by `zhandaz`; signals: fp8, hang, kernel, triton; excerpt: "@ProExpertProg Thanks for the review, the triton kernel is moved to the corresponding dir. @Isotr0py We also add a new feat to dump the ..." (https://github.com/vllm-project/vllm/pull/38065#issuecomment-4193878685)
- `2026-03-27T16:47:48Z` `inline` by `Isotr0py` `vllm/model_executor/layers/quantization/input_quant_fp8.py`:34; signals: cuda, fp8, triton; excerpt: "I think we don't need the if statement here, because triton utils has guarded the @triton.jit for non cuda-like platform." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3002071790)
- `2026-04-02T20:55:39Z` `inline` by `zhandaz` `vllm/envs.py`:1243; signals: cuda, cudagraph, hang; excerpt: "good point! The original design is based on: 1. In some cases (e.g., for our test on Shopify dataset), scale = 1.0 is actually ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3030335624)
- `2026-04-03T17:39:42Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/input_quant_fp8.py`:29; signals: fp8, kernel, triton; excerpt: "Can you move this into vllm/kernels/triton/qkv padded fp8 quant.py?" (https://github.com/vllm-project/vllm/pull/38065#discussion_r3033718352)
- `2026-04-24T17:34:03Z` `issue` by `zhandaz`; signals: failing, fp8, hopper; excerpt: "Seems the newly added tests are failing on our L4 CI ( 😅 Hmm, turns out that L4 has FP8 hw but cudnn spda ..." (https://github.com/vllm-project/vllm/pull/38065#issuecomment-4315114777)
- `2026-03-27T16:58:52Z` `inline` by `Isotr0py` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:66; signals: attention, fp8; excerpt: "Any example model with scales file? BTW, I think loading FP8 scales from json looks a bit weird tbh, because we usually load them ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3002142196)
- `2026-04-22T15:38:43Z` `inline` by `zhandaz` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:451; signals: attention, hang; excerpt: "Good point to maintain the convention. Currently MMEncoderAttention is not in the model loader's auto-scan for process weights after loading, so I call the ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3125138249)
- `2026-04-22T16:03:06Z` `inline` by `Isotr0py` `vllm/model_executor/layers/attention/mm_encoder_attention.py`:358; signals: attention, fp8; excerpt: "One more open question for process weights after loading, whether we want to add MMEncoderAttention to be auto scanned in model loader/utils. I think ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3125293985)
- `2026-04-22T16:12:36Z` `inline` by `Isotr0py` `vllm/utils/flashinfer.py`:796; signals: flashinfer, fp8; excerpt: "Should we check whether the GPU has native FP8 support as well? get supported vit attn backends and cudnn.is available() will both return supported=True ..." (https://github.com/vllm-project/vllm/pull/38065#discussion_r3125348863)
