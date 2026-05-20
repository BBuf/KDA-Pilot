# PR Discussion Digest

- Source PR: [sgl-project/sglang#20501](https://github.com/sgl-project/sglang/pull/20501)
- Source page: `sources/prs/sglang/PR-20501.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20501`
- Generated at: `2026-05-20T15:29:04.417865+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-13T05:14:30Z`
- Merged: `2026-04-02T04:46:36Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 10 (approved=3, changes_requested=1, commented=6)
- Inline review comments: 8
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: BBuf, DarkSharpness, Godmook
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-03-26T06:40:33Z` `CHANGES_REQUESTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4011778258)
- `2026-03-26T13:10:18Z` `COMMENTED` by `Godmook` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4014021096)
- `2026-03-26T13:15:20Z` `COMMENTED` by `Godmook` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4014057868)
- `2026-03-26T13:23:45Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4014125513)
- `2026-03-26T19:10:51Z` `COMMENTED` by `Godmook` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4016754121)
- `2026-03-30T08:19:55Z` `APPROVED` by `DarkSharpness` - LGTM. I just wonder how long it would take to compile & autotune this triton kernel? Also, the ... (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4028858437)
- `2026-04-02T00:31:28Z` `APPROVED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4047746462)
- `2026-04-02T04:39:37Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4048313533)
- `2026-04-02T04:45:45Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4048331104)

## Inline Comment Hotspots

- `python/sglang/srt/layers/sampler.py`: 4 inline comment(s)
- `python/sglang/srt/layers/fused_sampling.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-26T19:10:51Z` `inline` by `Godmook` `python/sglang/srt/layers/fused_sampling.py`:108; signals: benchmark, correctness, cuda, flashinfer, kernel, speedup, throughput, tma; excerpt: "Thanks for the pointer! Benchmarked against flashinfer.sampling.softmax on A100. Results bs vocab triton ip (μs) flashinfer (μs) speedup ---- ------- --------------- ----------------- --------- 1 ..." (https://github.com/sgl-project/sglang/pull/20501#discussion_r2997130114)
- `2026-03-30T11:57:32Z` `issue` by `Godmook`; signals: autotune, bf16, cache, compile, dtype, hang, kernel, latency; excerpt: "LGTM. I just wonder how long it would take to compile & autotune this triton kernel? Also, the autotune must be done in warm-up ..." (https://github.com/sgl-project/sglang/pull/20501#issuecomment-4154485207)
- `2026-04-01T19:39:14Z` `issue` by `Godmook`; signals: aligned, correctness, cuda, flashinfer, kernel, latency, memory, perf; excerpt: "Sampling Kernel: Correctness Fix + Hybrid Dispatch Problem The original fused Triton kernel used a numerically different computation order from PyTorch, causing structured output ..." (https://github.com/sgl-project/sglang/pull/20501#issuecomment-4172530564)
- `2026-03-30T11:58:36Z` `issue` by `Godmook`; signals: autotune, cache, compile, flashinfer, hang, kernel, tma; excerpt: "I added autotune. Changes 1. python/sglang/srt/layers/fused sampling.py Added warmup fused temperature softmax() at the end of the file. Runs both fused temperature softmax and ..." (https://github.com/sgl-project/sglang/pull/20501#issuecomment-4154491181)
- `2026-03-26T13:15:20Z` `inline` by `Godmook` `python/sglang/srt/layers/fused_sampling.py`:108; signals: compile, flashinfer, kernel, tma, triton; excerpt: "Thanks for the pointer! I looked into this — flashinfer.sampling doesn't have a softmax function with a temperature parameter. Temperature scaling and softmax are ..." (https://github.com/sgl-project/sglang/pull/20501#discussion_r2994813063)
- `2026-03-26T06:40:25Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/fused_sampling.py`:108; signals: flashinfer, perf, performance, tma; excerpt: "FYI, have you compared the performance of the implementation with flashinfer.sampling.softmax which also supports passing an optional temperature?" (https://github.com/sgl-project/sglang/pull/20501#discussion_r2992803314)
- `2026-03-30T08:19:55Z` `review` `APPROVED` by `DarkSharpness`; signals: autotune, compile, kernel, triton; excerpt: "LGTM. I just wonder how long it would take to compile & autotune this triton kernel? Also, the autotune must be done in warm-up ..." (https://github.com/sgl-project/sglang/pull/20501#pullrequestreview-4028858437)
- `2026-04-02T00:26:34Z` `issue` by `DarkSharpness`; signals: flashinfer, memory, tma; excerpt: "/ temp → softmax) so grammar- constrained decoding works correctly on either path. Memory access pattern comparison: For now, the baseline is naive torch ..." (https://github.com/sgl-project/sglang/pull/20501#issuecomment-4173745103)
- `2026-03-26T06:37:47Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/sampler.py`:37; signals: cuda, triton; excerpt: "Why except ImportError here? On cuda platform, triton always exists. There should be no import error here." (https://github.com/sgl-project/sglang/pull/20501#discussion_r2992794625)
- `2026-03-26T13:10:18Z` `inline` by `Godmook` `python/sglang/srt/layers/sampler.py`:37; signals: cuda; excerpt: "Nice Catch! I removed the try/except. Now it does a direct import under if is cuda()." (https://github.com/sgl-project/sglang/pull/20501#discussion_r2994780095)
- `2026-03-26T13:23:44Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/fused_sampling.py`:108; signals: general review; excerpt: "try this:" (https://github.com/sgl-project/sglang/pull/20501#discussion_r2994870660)
- `2026-04-02T04:39:37Z` `inline` by `BBuf` `python/sglang/srt/layers/sampler.py`:32; signals: general review; excerpt: "Can we move this import to the top of the file?" (https://github.com/sgl-project/sglang/pull/20501#discussion_r3025852380)
