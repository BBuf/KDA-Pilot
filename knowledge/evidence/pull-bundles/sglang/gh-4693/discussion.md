# PR Discussion Digest

- Source PR: [sgl-project/sglang#4693](https://github.com/sgl-project/sglang/pull/4693)
- Source page: `sources/prs/sglang/PR-4693.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4693`
- Generated at: `2026-05-20T15:30:12.934935+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-23T08:29:13Z`
- Merged: `2025-04-18T16:51:29Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: HaiShaw, ZhangJianwei0311, yhyang201, yizhang2077, zhaochenyang20
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-03-24T03:03:49Z` `COMMENTED` by `HaiShaw` - Can we have dummy weight and dummy weight loading work for this too? Thanks. (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2709007904)
- `2025-04-16T19:31:25Z` `COMMENTED` by `yhyang201` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2773638246)
- `2025-04-16T22:26:45Z` `COMMENTED` by `zhaochenyang20` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2773999349)
- `2025-04-16T22:30:19Z` `COMMENTED` by `zhaochenyang20` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2774003099)
- `2025-04-17T15:08:32Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2776106931)
- `2025-04-17T15:19:00Z` `COMMENTED` by `yhyang201` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2776148706)
- `2025-04-17T15:29:27Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2776178361)
- `2025-04-17T16:17:09Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2776280305)
- `2025-04-18T04:14:49Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2777501755)
- `2025-04-18T08:37:55Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2778094222)
- `2025-04-18T16:49:12Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4693#pullrequestreview-2779008251)

## Inline Comment Hotspots

- `python/sglang/srt/models/qwen3.py`: 8 inline comment(s)
- `python/sglang/srt/models/qwen3_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-17T16:53:51Z` `issue` by `yizhang2077`; signals: deepgemm, gemm, moe, perf, performance; excerpt: "LGTM overall, vllm looks like have merged qwen3/qwen3moe, could we compare the speed with it? Sure, shall we then proceed with the comparison using ..." (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2813542857)
- `2025-04-16T19:31:24Z` `inline` by `yhyang201` `python/sglang/srt/models/qwen3.py`:108; signals: attention, perf, performance; excerpt: "The following implementation is more similar to the style used in Transformers However, the current version demonstrates better performance overall. It would be greatly ..." (https://github.com/sgl-project/sglang/pull/4693#discussion_r2047617911)
- `2025-03-24T02:55:44Z` `issue` by `HaiShaw`; signals: block, fp8, pipeline; excerpt: "@yhyang201 - Is pipeline parallel necessary (I see some reference to it in - What is the model weights and activation quantization scheme? FP8? ..." (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2746754214)
- `2025-04-16T19:23:11Z` `issue` by `zhaochenyang20`; signals: benchmark, perf, performance; excerpt: "1. Profiling the speed; 2. benchmarking the performance;" (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2810545296)
- `2025-04-18T08:37:55Z` `inline` by `yizhang2077` `python/sglang/srt/models/qwen3.py`:87; signals: attention, moe; excerpt: "it is ok, attention bias is False in qwen3/qwen3moe" (https://github.com/sgl-project/sglang/pull/4693#discussion_r2050356626)
- `2025-03-23T16:11:33Z` `issue` by `yhyang201`; signals: attention, moe; excerpt: "There are a few important points to note regarding sliding window : 1. I noticed that in Transformers , Qwen2Attention/Qwen3Attention (from qwen2/qwen3) enable sliding ..." (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2746292026)
- `2025-03-27T06:46:43Z` `issue` by `ZhangJianwei0311`; signals: attention, moe; excerpt: "There is a missing line k = k by head.view(k.shape) between lines 232 and 233 in the apply qk norm method of the Attention ..." (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2756913457)
- `2025-03-27T07:02:55Z` `issue` by `yhyang201`; signals: attention, moe; excerpt: "There is a missing line k = k by head.view(k.shape) between lines 232 and 233 in the apply qk norm method of the Attention ..." (https://github.com/sgl-project/sglang/pull/4693#issuecomment-2756943802)
- `2025-04-17T15:19:00Z` `inline` by `yhyang201` `python/sglang/srt/models/qwen3.py`:87; signals: attention; excerpt: "In the Transformers implementation, this value is taken from attention bias. It might be necessary to reach out to the Qwen team for clarification." (https://github.com/sgl-project/sglang/pull/4693#discussion_r2049181686)
- `2025-04-16T22:30:19Z` `inline` by `zhaochenyang20` `python/sglang/srt/models/qwen3.py`:108; signals: hang; excerpt: "@yizhang2077 @mickqian could you help on this?" (https://github.com/sgl-project/sglang/pull/4693#discussion_r2047854406)
- `2025-04-17T16:07:13Z` `inline` by `yizhang2077` `python/sglang/srt/models/qwen3_moe.py`:227; signals: moe; excerpt: "remove this comment" (https://github.com/sgl-project/sglang/pull/4693#discussion_r2049264016)
- `2025-04-18T04:14:01Z` `inline` by `yizhang2077` `python/sglang/srt/models/qwen3_moe.py`:55; signals: moe; excerpt: "use abs path here" (https://github.com/sgl-project/sglang/pull/4693#discussion_r2049999050)
