# PR Discussion Digest

- Source PR: [sgl-project/sglang#14093](https://github.com/sgl-project/sglang/pull/14093)
- Source page: `sources/prs/sglang/PR-14093.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14093`
- Generated at: `2026-05-20T15:27:55.520366+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-28T08:35:59Z`
- Merged: `2025-12-05T16:53:55Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 16 (commented=16)
- Inline review comments: 27
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=5, outdated=14
- Human participants with discussion text: Qiaolin-Yu, harvenstar, ispobock
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-28T08:38:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fused FP8 KV cache write kernel for the TRTLLM MHA backend, ... (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3517949540)
- `2025-12-01T23:58:46Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3527580464)
- `2025-12-02T00:12:37Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3527608493)
- `2025-12-02T00:13:35Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3527610340)
- `2025-12-02T00:15:01Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3527612856)
- `2025-12-02T00:48:32Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3527660148)
- `2025-12-03T14:45:40Z` `COMMENTED` by `ispobock` - 1. share profile figure comparison to see the improvement after fusion 2. share end to end throughput improvement ... (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3535367204)
- `2025-12-03T22:28:31Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3537188722)
- `2025-12-03T22:28:47Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3537189288)
- `2025-12-03T22:28:55Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3537189596)
- `2025-12-03T22:28:59Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3537189712)
- `2025-12-03T22:29:18Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3537190337)
- `2025-12-04T09:42:45Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3538988010)
- `2025-12-04T09:55:08Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3539049522)
- `2025-12-04T09:55:15Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3539050128)
- `2025-12-04T09:55:22Z` `COMMENTED` by `harvenstar` (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3539050774)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`: 13 inline comment(s)
- `python/sglang/srt/layers/attention/trtllm_mha_backend.py`: 9 inline comment(s)
- `python/sglang/srt/models/qwen3_moe.py`: 3 inline comment(s)
- `test/srt/test_trtllm_fp8_kv_kernel.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-03T15:30:26Z` `issue` by `harvenstar`; signals: alignment, benchmark, block, cache, fp8, kv cache, latency, mla; excerpt: "1. share profile figure comparison to see the improvement after fusion 2. share end to end throughput improvement on Qwen3-235B qq: Why trtllm mla ..." (https://github.com/sgl-project/sglang/pull/14093#issuecomment-3607420439)
- `2025-12-02T00:13:35Z` `inline` by `harvenstar` `python/sglang/srt/layers/attention/trtllm_mha_backend.py`:418; signals: attention, cache, fp8, hang, kv cache, moe; excerpt: "The check should be in the backend, not model-specific code. I'll move the fusion detection logic entirely into TRTLLMHAAttnBackend. should use fused fp8 path() ..." (https://github.com/sgl-project/sglang/pull/14093#discussion_r2579140614)
- `2025-12-03T22:27:57Z` `issue` by `harvenstar`; signals: attention, cache, fp8, kernel, kv cache, mla; excerpt: "qq: Why trtllm mla don't need this fusion? In my understanding, trtllm mla uses the FlashMLA backend which has a different KV cache write ..." (https://github.com/sgl-project/sglang/pull/14093#issuecomment-3609114268)
- `2025-12-03T22:29:17Z` `inline` by `harvenstar` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:198; signals: attention, cache, fp8, kernel; excerpt: "Added test/srt/test trtllm fp8 kv kernel.py with serveral test cases covering different input/cache dimensions, scaling options, and edge cases. All passing." (https://github.com/sgl-project/sglang/pull/14093#discussion_r2586815768)
- `2025-12-03T22:28:31Z` `inline` by `harvenstar` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:47; signals: attention, block, fp8, kernel; excerpt: "Done. Moved head iteration to grid dimension via head block id = tl.program id(1)." (https://github.com/sgl-project/sglang/pull/14093#discussion_r2586814358)
- `2025-12-03T22:28:46Z` `inline` by `harvenstar` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:148; signals: attention, block, fp8, kernel; excerpt: "Done. Grid is now (tokens, head blocks, 2) where kv idx = tl.program id(2) selects K or V." (https://github.com/sgl-project/sglang/pull/14093#discussion_r2586814893)
- `2025-12-03T14:35:16Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:47; signals: attention, fp8, kernel; excerpt: "Why don't parallelize heads? (i.e. add head to grid)" (https://github.com/sgl-project/sglang/pull/14093#discussion_r2585370535)
- `2025-12-03T14:36:15Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:148; signals: attention, fp8, kernel; excerpt: "Can we also parallelize k and v?" (https://github.com/sgl-project/sglang/pull/14093#discussion_r2585374297)
- `2025-12-03T14:39:06Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:320; signals: attention, fp8, kernel; excerpt: "It seems not needed?" (https://github.com/sgl-project/sglang/pull/14093#discussion_r2585385414)
- `2025-12-03T14:39:12Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:359; signals: attention, fp8, kernel; excerpt: "It seems not needed?" (https://github.com/sgl-project/sglang/pull/14093#discussion_r2585385758)
- `2025-12-03T14:40:01Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/trtllm_fp8_kv_kernel.py`:198; signals: attention, fp8, kernel; excerpt: "Could you add unit test for this kernel?" (https://github.com/sgl-project/sglang/pull/14093#discussion_r2585388554)
- `2025-12-03T14:45:40Z` `review` `COMMENTED` by `ispobock`; signals: mla, throughput; excerpt: "1. share profile figure comparison to see the improvement after fusion 2. share end to end throughput improvement on Qwen3-235B qq: Why trtllm mla ..." (https://github.com/sgl-project/sglang/pull/14093#pullrequestreview-3535367204)
