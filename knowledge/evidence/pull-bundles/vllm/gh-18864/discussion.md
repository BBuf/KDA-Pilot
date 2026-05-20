# PR Discussion Digest

- Source PR: [vllm-project/vllm#18864](https://github.com/vllm-project/vllm/pull/18864)
- Source page: `sources/prs/vllm/PR-18864.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18864`
- Generated at: `2026-05-20T15:35:23.915919+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-28T23:40:02Z`
- Merged: `2025-07-03T21:55:40Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 31 (approved=2, commented=29)
- Inline review comments: 32
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=13, outdated=7
- Human participants with discussion text: ElizaWszola, bnellnm, fxmarty-amd, mergify, tlrmchlsmth, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2025-06-02T19:06:55Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2889625356)
- `2025-06-02T22:47:21Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2890133479)
- `2025-07-02T20:48:34Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980585050)
- `2025-07-02T20:51:00Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980590002)
- `2025-07-02T20:54:23Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980599856)
- `2025-07-02T20:57:20Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980611145)
- `2025-07-02T20:58:49Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980615411)
- `2025-07-02T20:59:19Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980616461)
- `2025-07-02T21:02:32Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980624320)
- `2025-07-02T21:04:10Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980627312)
- `2025-07-02T21:08:27Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980637284)
- `2025-07-02T21:16:29Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980656112)
- `2025-07-02T21:18:25Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980661406)
- `2025-07-02T21:20:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980665300)
- `2025-07-02T21:20:51Z` `APPROVED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980666314)
- `2025-07-02T21:32:24Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980697454)
- `2025-07-02T22:21:58Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980799485)
- `2025-07-02T22:27:03Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980800126)
- `2025-07-02T22:43:03Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980838882)
- `2025-07-02T22:48:55Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2980847173)
- `2025-07-03T02:15:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2981312521)
- `2025-07-03T02:52:44Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2981381473)
- `2025-07-03T10:27:21Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2982631269)
- `2025-07-03T12:52:53Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/18864#pullrequestreview-2983053680)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 4 inline comment(s)
- `tests/kernels/moe/test_batched_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/deepep_ht_prepare_finalize.py`: 3 inline comment(s)
- `vllm/model_executor/models/granitemoe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/pplx_prepare_finalize.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-02T21:20:22Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:117; signals: gemm, moe, triton; excerpt: "Ok, cool. I couldn't think up a better name for this. It was num dp in some methods and num dispatchers in others. I ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180991864)
- `2025-07-02T21:32:24Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`:998; signals: block, gemm, moe; excerpt: "I want to hold off doing this because the one in batched deep gemm only handles deep gemm sized block quantization and not per-token ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2181011615)
- `2025-07-03T15:25:23Z` `inline` by `ElizaWszola` `tests/kernels/moe/test_batched_moe.py`:214; signals: dtype, kernel, moe; excerpt: "I see. Should there be also a condition in the test code to skip the test if input scales == True and quant dtype ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2183087581)
- `2025-07-03T16:31:41Z` `inline` by `bnellnm` `tests/kernels/moe/test_batched_moe.py`:214; signals: kernel, moe, triton; excerpt: "That's one of the conditions that needs more testing. There's some int8/int4 quantization schemes that happen outside the triton kernels. So they need to ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2183220973)
- `2025-07-02T20:48:34Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`:529; signals: moe, throughput; excerpt: "it is a fair assumption - the one case where topk ids could be -1 is the deepep high throughput case and we handle ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180944590)
- `2025-07-02T22:43:03Z` `inline` by `bnellnm` `vllm/model_executor/models/granitemoe.py`:108; signals: hang, moe; excerpt: "This is the same change that @varun-sundar-rabindranath applied to the other MoE models. I figured we needed it for granitemoe.py too. Although I just ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2181101144)
- `2025-07-03T12:52:53Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:178; signals: cutlass, moe; excerpt: "Can we have a condition here that we only zero-out c1 if expert map is not none and per act token == True? As ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2182710018)
- `2025-07-03T15:13:18Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:178; signals: cutlass, moe; excerpt: "There's another PR that has the proper condition for this. I don't want to have to rerun everything at this point. I'll let that ..." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2183047274)
- `2025-07-02T20:51:00Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:194; signals: gemm, moe; excerpt: "nit: num dispatchers docs" (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180948135)
- `2025-07-02T20:54:23Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/config.py`:85; signals: block, moe; excerpt: "nit : maybe is block quantized is a better name. just a suggestion." (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180953002)
- `2025-07-02T20:57:20Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:270; signals: cutlass, moe; excerpt: "was this a bug before ?" (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180959196)
- `2025-07-02T21:02:32Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:270; signals: cutlass, moe; excerpt: "yeah" (https://github.com/vllm-project/vllm/pull/18864#discussion_r2180966856)
