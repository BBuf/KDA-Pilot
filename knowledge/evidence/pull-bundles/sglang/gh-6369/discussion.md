# PR Discussion Digest

- Source PR: [sgl-project/sglang#6369](https://github.com/sgl-project/sglang/pull/6369)
- Source page: `sources/prs/sglang/PR-6369.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6369`
- Generated at: `2026-05-20T15:30:39.761267+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-17T06:51:47Z`
- Merged: `2025-06-07T09:47:37Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 9
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Alcanderian, BBuf, merrymercy
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-04T14:36:48Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2897031877)
- `2025-06-05T03:55:52Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2898781823)
- `2025-06-05T04:53:14Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2898866351)
- `2025-06-05T05:02:59Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2898878831)
- `2025-06-05T05:43:55Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2898943270)
- `2025-06-05T06:01:49Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2898974758)
- `2025-06-05T07:44:39Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2899209941)
- `2025-06-05T09:22:41Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2899541285)
- `2025-06-05T09:57:19Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2899664218)
- `2025-06-05T11:03:45Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2899852445)
- `2025-06-07T09:36:31Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6369#pullrequestreview-2907209926)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-06-04T14:36:48Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: kernel, moe, perf, performance, triton; excerpt: "I wonder whether using max num tokens padded and topk ids numel as constexpr will create too many kernels without yielding significant performance benefits" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2126777121)
- `2025-06-05T03:55:52Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: cuda, kernel, moe, triton; excerpt: "The shape of topk ids is [num tokens, topk]. Under CUDA graph mode, num tokens is fixed, and num experts/topk is also fixed, so ..." (https://github.com/sgl-project/sglang/pull/6369#discussion_r2127887613)
- `2025-06-05T04:53:14Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: cuda, kernel, moe, triton; excerpt: "The shape of topk ids is [num tokens, topk]. Under CUDA graph mode, num tokens is fixed, and num experts/topk is also fixed, so ..." (https://github.com/sgl-project/sglang/pull/6369#discussion_r2127948613)
- `2025-06-05T07:44:39Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: moe, perf, performance, triton; excerpt: "Testing shows removing those two constexpr has negligible performance impact. While the absolute values fluctuate in the data below, the relative ratios remain nearly ..." (https://github.com/sgl-project/sglang/pull/6369#discussion_r2128176333)
- `2025-06-05T05:02:59Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: cuda, kernel, moe, triton; excerpt: "Right, if we need to consider prefill, does that mean we can only resolve it with a CUDA kernel?" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2127957851)
- `2025-06-05T05:43:55Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: block, moe, triton; excerpt: "Will it be very slow without constexpr? And suggestions, BLOCK SIZE = 1024" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2127998494)
- `2025-06-05T06:01:49Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: aligned, moe, triton; excerpt: "Make sense, I can set ALIGNED NUM EXPERTS P1 to 512?" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2128018028)
- `2025-06-05T09:22:41Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: aligned, moe, triton; excerpt: "Make sense, I can set ALIGNED NUM EXPERTS P1 to 512? triton.next power of 2(num experts + 1)" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2128380577)
- `2025-06-05T09:57:18Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`:658; signals: moe, triton; excerpt: "done!" (https://github.com/sgl-project/sglang/pull/6369#discussion_r2128454833)
