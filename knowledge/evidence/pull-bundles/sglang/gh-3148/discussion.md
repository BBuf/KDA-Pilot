# PR Discussion Digest

- Source PR: [sgl-project/sglang#3148](https://github.com/sgl-project/sglang/pull/3148)
- Source page: `sources/prs/sglang/PR-3148.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3148`
- Generated at: `2026-05-20T15:29:58.210037+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-26T10:55:41Z`
- Merged: `2025-03-09T08:03:32Z`

## Discussion Counts

- Issue comments: 32
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: BBuf, HandH1998, hebiao064, merrymercy, xiaohanhuang, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-13T08:10:24Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2614167111)
- `2025-02-20T23:31:18Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2631414126)
- `2025-03-07T09:34:46Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2614167901)
- `2025-03-07T09:36:10Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2666726732)
- `2025-03-07T09:38:28Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2666732118)
- `2025-03-09T08:03:13Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3148#pullrequestreview-2669342579)

## Inline Comment Hotspots

- `python/sglang/test/test_block_fp8.py`: 2 inline comment(s)
- `python/pyproject.toml`: 2 inline comment(s)
- `python/sglang/srt/utils.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-12T07:07:00Z` `issue` by `HandH1998`; signals: benchmark, cuda, cutlass, fp8, kernel, perf, performance, triton; excerpt: "@merrymercy @zhyncs I have added support for falling back to the vLLM cutlass w8a8 fp8 kernel and have benchmarked dynamic quantization. The benchmark results ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2652834146)
- `2025-02-13T06:18:44Z` `issue` by `HandH1998`; signals: fp8, kernel, perf, performance, triton; excerpt: "@zhyncs The results using the new per token group quant fp8 kernel are showed in the Table row sgl kernel (updated). It is worse ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2655638020)
- `2025-02-13T08:00:36Z` `issue` by `BBuf`; signals: fp8, kernel, perf, performance, triton; excerpt: "@zhyncs The results using the new per token group quant fp8 kernel are showed in the Table row sgl kernel (updated). It is worse ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2655795106)
- `2025-03-05T00:39:47Z` `issue` by `hebiao064`; signals: benchmark, cuda, fp8, kernel, latency; excerpt: "@BBuf The vLLM's scaled fp8 quant supports both per-tensor and per-token quantization. In this PR, we use per-token quantization by default when activation is ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2699359270)
- `2025-03-07T09:38:28Z` `inline` by `HandH1998` `python/sglang/test/test_block_fp8.py`:67; signals: accuracy, block, fp8, hang; excerpt: "When I test it on another GPU, not all cases can pass under rtol=0.15, so I increase it ot 0.20. In fact, I doesn't ..." (https://github.com/sgl-project/sglang/pull/3148#discussion_r1984747847)
- `2025-01-26T12:37:19Z` `issue` by `merrymercy`; signals: kernel, perf, performance, regression; excerpt: "1. Can we still provide a flag to fallback to vllm's implementation? Similar to the custom allreduce kernel We need this at the beginning ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2614401528)
- `2025-03-08T04:45:57Z` `issue` by `HandH1998`; signals: accuracy, cutlass, fp8, kernel; excerpt: "@HandH1998 Do you think we should support similar api like scaled fp8 quant The cutlass w8a8 fp8 kernel only support per-channel activation scales, so ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2708016774)
- `2025-02-13T08:10:47Z` `inline` by `zhyncs` `python/sglang/test/test_block_fp8.py`:67; signals: block, fp8; excerpt: "Why increase the rtol?" (https://github.com/sgl-project/sglang/pull/3148#discussion_r1954013494)
- `2025-02-12T07:18:03Z` `issue` by `HandH1998`; signals: fp8, perf; excerpt: "I also added a quantization config w8a8 fp8 to support the inference of quantized model underactivation dynamic per-token quantization, weight static per-channel quantization following ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2652851217)
- `2025-02-13T08:05:23Z` `issue` by `HandH1998`; signals: kernel, triton; excerpt: "@BBuf Look forward to it! If you finish it, please let me know. I will replace the Triton kernel with yours." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2655805919)
- `2025-02-22T10:30:02Z` `issue` by `BBuf`; signals: kernel, triton; excerpt: "@BBuf Look forward to it! If you finish it, please let me know. I will replace the Triton kernel with yours." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2676137687)
- `2025-02-27T04:29:00Z` `issue` by `xiaohanhuang`; signals: kernel, triton; excerpt: "@BBuf Look forward to it! If you finish it, please let me know. I will replace the Triton kernel with yours. Nice work! Any ..." (https://github.com/sgl-project/sglang/pull/3148#issuecomment-2686834753)
