# PR Discussion Digest

- Source PR: [sgl-project/sglang#7129](https://github.com/sgl-project/sglang/pull/7129)
- Source page: `sources/prs/sglang/PR-7129.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7129`
- Generated at: `2026-05-20T15:31:02.615955+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-12T09:48:16Z`
- Merged: `2025-07-08T07:19:50Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 22
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=12, outdated=7
- Human participants with discussion text: Alcanderian, AniZpZ, CatherineSue, Edwardf0t1, zhyncs
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-12T09:48:44Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @Edwardf0t1, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2920344127)
- `2025-06-12T09:50:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for ModelOpt Llama4 FP8 checkpoints. Key areas for attention include a ... (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2920350033)
- `2025-06-27T00:07:46Z` `COMMENTED` by `CatherineSue` - Thanks for the great PR. I only have a few nit comments. Has the original llama4 model been ... (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2964121790)
- `2025-06-27T20:14:17Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2967878878)
- `2025-06-27T20:14:24Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2967879327)
- `2025-06-27T20:17:42Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2967887379)
- `2025-07-03T18:28:57Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2984092640)
- `2025-07-04T05:24:15Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985636941)
- `2025-07-04T05:24:25Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985637124)
- `2025-07-04T05:24:36Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985637329)
- `2025-07-04T05:24:43Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985637470)
- `2025-07-04T05:25:14Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985638197)
- `2025-07-04T05:26:36Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2985639948)
- `2025-07-08T06:45:43Z` `APPROVED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2996200493)

## Inline Comment Hotspots

- `python/sglang/srt/models/mllama4.py`: 13 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 3 inline comment(s)
- `python/sglang/srt/model_loader/loader.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-27T00:07:46Z` `review` `COMMENTED` by `CatherineSue`; signals: fp8, hang; excerpt: "Thanks for the great PR. I only have a few nit comments. Has the original llama4 model been tested as well? (to see the ..." (https://github.com/sgl-project/sglang/pull/7129#pullrequestreview-2964121790)
- `2025-07-03T17:43:55Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:652; signals: moe, triton; excerpt: "It looks like should be moved to 661" (https://github.com/sgl-project/sglang/pull/7129#discussion_r2183384674)
- `2025-07-04T05:24:15Z` `inline` by `Edwardf0t1` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:652; signals: moe, triton; excerpt: "Good point, simplified the if-else logics here." (https://github.com/sgl-project/sglang/pull/7129#discussion_r2184446081)
- `2025-06-27T20:18:21Z` `issue` by `Edwardf0t1`; signals: fp8, hang; excerpt: "Thanks for the great PR. I only have a few nit comments. Has the original llama4 model been tested as well? (to see the ..." (https://github.com/sgl-project/sglang/pull/7129#issuecomment-3014264790)
- `2025-06-30T21:21:30Z` `issue` by `Edwardf0t1`; signals: fp8, moe; excerpt: "@CatherineSue @zhyncs Would you mind take another look for this PR? We are adding modelopt Qwen3/Qwen3 MoE/Qwen2.5/QwQ-32B fp8 support in SGLang and some of ..." (https://github.com/sgl-project/sglang/pull/7129#issuecomment-3020804583)
- `2025-06-27T20:14:17Z` `inline` by `Edwardf0t1` `python/sglang/srt/layers/quantization/modelopt_quant.py`:109; signals: hang; excerpt: "Good catch - I changed to a more targeted approach for mllama without the unintended side effects on other models." (https://github.com/sgl-project/sglang/pull/7129#discussion_r2172812944)
- `2025-06-27T20:17:42Z` `inline` by `Edwardf0t1` `python/sglang/srt/models/mllama4.py`:246; signals: moe; excerpt: "Good question! This is implementing a "chain of responsibility" design pattern for weight loading, i.e., each weight goes through a sequence of increasingly specialized ..." (https://github.com/sgl-project/sglang/pull/7129#discussion_r2172818434)
- `2025-07-03T18:05:14Z` `inline` by `Alcanderian` `python/sglang/srt/models/mllama4.py`:228; signals: hang; excerpt: "Could the "not" be moved into the function and changed to should not load weight to make it more intuitive to understand?" (https://github.com/sgl-project/sglang/pull/7129#discussion_r2183438046)
- `2025-07-04T05:25:14Z` `inline` by `Edwardf0t1` `python/sglang/srt/models/mllama4.py`:418; signals: race; excerpt: "This one is legitimate actually, it handles checkpoint/model name mismatches gracefully, e.g., if the checkpoint contains a scale name that cannot be transformed to ..." (https://github.com/sgl-project/sglang/pull/7129#discussion_r2184446920)
- `2025-06-27T00:03:52Z` `inline` by `CatherineSue` `python/sglang/srt/models/mllama4.py`:246; signals: general review; excerpt: "is there a reason for use if xxx: continue patten here, rather than calling self. handle scale mapping directly?" (https://github.com/sgl-project/sglang/pull/7129#discussion_r2170325769)
- `2025-07-04T05:26:36Z` `inline` by `Edwardf0t1` `python/sglang/srt/models/mllama4.py`:468; signals: general review; excerpt: "This one is also legit. If the model doesn't have the specific parameter names, e.g. ("experts.w13 weight", weight chunk 1, "w1"), due to architecture ..." (https://github.com/sgl-project/sglang/pull/7129#discussion_r2184448233)
- `2025-06-26T23:47:58Z` `inline` by `CatherineSue` `python/sglang/srt/layers/quantization/modelopt_quant.py`:109; signals: general review; excerpt: "Will this affect other model?" (https://github.com/sgl-project/sglang/pull/7129#discussion_r2170300397)
