# PR Discussion Digest

- Source PR: [sgl-project/sglang#10078](https://github.com/sgl-project/sglang/pull/10078)
- Source page: `sources/prs/sglang/PR-10078.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10078`
- Generated at: `2026-05-20T15:27:14.165000+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-05T13:18:06Z`
- Merged: `2025-11-02T05:24:58Z`

## Discussion Counts

- Issue comments: 38
- Review submissions: 14 (approved=2, commented=12)
- Inline review comments: 19
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=12, outdated=12
- Human participants with discussion text: AniZpZ, Fridge003, JackChuang, b8zhong, pipecat, yicwang, zejunchen-zejun, zhyncs
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-05T13:18:27Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @JackChuang, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3189345499)
- `2025-09-05T13:21:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces FP4 (E2M1) KV cache support, which is a great feature for reducing ... (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3189353565)
- `2025-09-08T23:19:48Z` `COMMENTED` by `JackChuang` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3198461539)
- `2025-09-08T23:19:58Z` `COMMENTED` by `JackChuang` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3198461745)
- `2025-09-08T23:53:34Z` `COMMENTED` by `JackChuang` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3198509227)
- `2025-09-10T03:37:13Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3204284500)
- `2025-09-10T06:50:35Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3204657144)
- `2025-09-10T11:46:40Z` `COMMENTED` by `JackChuang` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3205775027)
- `2025-09-16T02:29:49Z` `APPROVED` by `AniZpZ` - LGTM but i think we'd better note that FP4 (E2M1) KV Cache might lead to a accuracy drop ... (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3226851582)
- `2025-10-08T06:56:10Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3308718961)
- `2025-10-10T18:01:54Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3325141943)
- `2025-10-20T22:00:37Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3358068125)
- `2025-10-31T05:09:16Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3402610879)
- `2025-10-31T05:09:30Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10078#pullrequestreview-3402612328)

## Inline Comment Hotspots

- `python/sglang/srt/mem_cache/memory_pool.py`: 7 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 4 inline comment(s)
- `python/sglang/test/test_kvfp4_quant_dequant.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/kvfp4_tensor.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-21T01:29:31Z` `issue` by `zejunchen-zejun`; signals: bf16, cache, fp4, fp8, kv cache, mla, sm100; excerpt: "Good job, May I know if the sglang supports the FP8 mla kv cache or is there any plan for that? Thank you Hi ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3424323268)
- `2025-10-21T03:59:08Z` `issue` by `yicwang`; signals: bf16, cache, fp4, fp8, kv cache, mla, sm100; excerpt: "Good job, May I know if the sglang supports the FP8 mla kv cache or is there any plan for that? Thank you Hi ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3424575740)
- `2025-10-20T17:30:13Z` `issue` by `JackChuang`; signals: cache, fp4, fp8, kv cache, mla, sm100; excerpt: "Good job, May I know if the sglang supports the FP8 mla kv cache or is there any plan for that? Thank you Hi ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3423073796)
- `2025-10-08T06:56:05Z` `inline` by `Fridge003` `python/sglang/srt/mem_cache/memory_pool.py`:1310; signals: cache, kernel, memory, mla, triton; excerpt: "The set mla kv buffer triton kernel might also be moved to utils file" (https://github.com/sgl-project/sglang/pull/10078#discussion_r2412781055)
- `2025-09-16T03:55:15Z` `issue` by `JackChuang`; signals: accuracy, cache, failing, fp4, kv cache; excerpt: "LGTM but i think we'd better note that FP4 (E2M1) KV Cache might lead to a accuracy drop @AniZpZ Sounds good. Where do you ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3294789732)
- `2025-09-17T03:04:17Z` `issue` by `AniZpZ`; signals: accuracy, cache, failing, fp4, kv cache; excerpt: "LGTM but i think we'd better note that FP4 (E2M1) KV Cache might lead to a accuracy drop @AniZpZ Sounds good. Where do you ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3301072628)
- `2025-10-12T00:17:59Z` `issue` by `yicwang`; signals: cache, fp4, kernel, mxfp4, nvfp4; excerpt: "Hi, I'm currently trying to quantize kvcache with nvfp4 and noticed your PR. I see the comment here says that nvfp4 quantization was used, ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3393760336)
- `2025-10-16T22:26:08Z` `issue` by `JackChuang`; signals: cache, fp4, kernel, mxfp4, nvfp4; excerpt: "Hi, I'm currently trying to quantize kvcache with nvfp4 and noticed your PR. I see the comment here says that nvfp4 quantization was used, ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3413107415)
- `2025-10-26T04:38:27Z` `issue` by `JackChuang`; signals: cache, dtype, fp8, mla, tensorrt; excerpt: "@JackChuang Please fix the conflicts Hi @Fridge003 @zhyncs, I've rebased to v0.5.3 and fix the conflicts. Can you please launch the CI and check ..." (https://github.com/sgl-project/sglang/pull/10078#issuecomment-3448008951)
- `2025-10-08T06:53:45Z` `inline` by `Fridge003` `python/sglang/srt/mem_cache/memory_pool.py`:1275; signals: cache, fp4, memory, mla; excerpt: "Can we make FP4 MLA Pool a derived class of MLATokenToKVPool? So that we don't need these if-else conditions." (https://github.com/sgl-project/sglang/pull/10078#discussion_r2412774044)
- `2025-10-31T05:08:27Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:363; signals: attention, cuda, hang, mla; excerpt: "Can we change self.data type == getattr(torch, "float4 e2m1fn x2", None) and is cuda to a utils function for better readability?" (https://github.com/sgl-project/sglang/pull/10078#discussion_r2480178538)
- `2025-10-08T06:41:21Z` `inline` by `Fridge003` `python/sglang/srt/mem_cache/memory_pool.py`:1020; signals: cache, kernel, memory, triton; excerpt: "Maybe we can open a new utils.py file for storing these triton kernels?" (https://github.com/sgl-project/sglang/pull/10078#discussion_r2412735837)
