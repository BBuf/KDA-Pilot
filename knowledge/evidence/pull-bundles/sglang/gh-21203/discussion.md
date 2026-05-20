# PR Discussion Digest

- Source PR: [sgl-project/sglang#21203](https://github.com/sgl-project/sglang/pull/21203)
- Source page: `sources/prs/sglang/PR-21203.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21203`
- Generated at: `2026-05-20T15:29:10.020732+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T09:24:33Z`
- Merged: `2026-03-25T01:47:10Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=4
- Human participants with discussion text: BBuf, edwingao28, kaixih, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T09:32:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for a CuTeDSL KDA decode kernel, including the kernel implementation, integration ... (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3990431094)
- `2026-03-23T09:50:37Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3990531089)
- `2026-03-23T12:52:28Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991520529)
- `2026-03-23T12:53:01Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991523894)
- `2026-03-23T12:53:29Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991526587)
- `2026-03-23T12:54:49Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991534045)
- `2026-03-23T12:55:46Z` `APPROVED` by `BBuf` - Can we add a correct test? (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991539305)
- `2026-03-23T13:22:52Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991694636)
- `2026-03-23T13:24:36Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-3991704660)
- `2026-03-24T21:16:50Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-4002132395)
- `2026-03-25T00:18:30Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21203#pullrequestreview-4003198571)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/cutedsl_kda.py`: 6 inline comment(s)
- `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/linear/kda_backend.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-24T01:01:33Z` `issue` by `yuan-luo`; signals: cute, flashinfer, hang, kernel, layout, perf, performance, triton; excerpt: "thanks for the pr. i mainly concerned about this plan item: Support triton prefill KDA kernel with KV and VK layout switch off. i ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4114695334)
- `2026-03-24T07:28:22Z` `issue` by `BBuf`; signals: cute, flashinfer, hang, kernel, layout, perf, performance, triton; excerpt: "thanks for the pr. i mainly concerned about this plan item: Support triton prefill KDA kernel with KV and VK layout switch off. i ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4115998575)
- `2026-03-24T08:29:35Z` `issue` by `yuan-luo`; signals: cute, flashinfer, hang, kernel, layout, perf, performance, triton; excerpt: "thanks for the pr. i mainly concerned about this plan item: Support triton prefill KDA kernel with KV and VK layout switch off. i ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4116310183)
- `2026-03-24T08:18:32Z` `issue` by `edwingao28`; signals: benchmark, correctness, cute, h100, h200; excerpt: "Benchmark Results: CuTeDSL KDA Decode across A100, H100, H200 Command: Correctness: all passed on all 3 GPUs and observed improvement in most metrics cc: ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4116241927)
- `2026-03-24T08:37:08Z` `issue` by `yuan-luo`; signals: benchmark, correctness, cute, h100, h200; excerpt: "Benchmark Results: CuTeDSL KDA Decode across A100, H100, H200 Command: Correctness: all passed on all 3 GPUs and observed improvement in most metrics cc: ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4116354704)
- `2026-03-23T17:52:11Z` `issue` by `kaixih`; signals: cute, kernel, layout, triton; excerpt: "thanks for the pr. i mainly concerned about this plan item: Support triton prefill KDA kernel with KV and VK layout switch off. i ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4112588762)
- `2026-03-23T09:50:37Z` `inline` by `yuan-luo` `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`:277; signals: attention, benchmark, cute; excerpt: "Ignore as it is in exception branch." (https://github.com/sgl-project/sglang/pull/21203#discussion_r2973950181)
- `2026-03-23T12:54:50Z` `inline` by `BBuf` `benchmark/bench_linear_attention/bench_cutedsl_kda_decode.py`:472; signals: attention, benchmark, cute; excerpt: "Can we match the benchmark script's style with other bench scripts?" (https://github.com/sgl-project/sglang/pull/21203#discussion_r2974859743)
- `2026-03-24T15:23:27Z` `issue` by `yuan-luo`; signals: cute, kernel, triton; excerpt: "@BBuf I wrote a test script to verify that kda prefill triton kernel is non-deterministic, which proves two things: 1. The CuteDSL decode kernel ..." (https://github.com/sgl-project/sglang/pull/21203#issuecomment-4119159302)
- `2026-03-23T12:52:28Z` `inline` by `BBuf` `python/sglang/jit_kernel/cutedsl_kda.py`:1; signals: cute, kernel; excerpt: "Rename this file to kda cutedsl.py would be better?" (https://github.com/sgl-project/sglang/pull/21203#discussion_r2974847746)
- `2026-03-23T13:22:52Z` `inline` by `yuan-luo` `python/sglang/jit_kernel/cutedsl_kda.py`:1; signals: cute, kernel; excerpt: "There's already a file named kda cutedsl for backend. Aligning with GDN style." (https://github.com/sgl-project/sglang/pull/21203#discussion_r2975006841)
- `2026-03-24T20:37:24Z` `inline` by `kaixih` `python/sglang/jit_kernel/cutedsl_kda.py`:1393; signals: cute, kernel; excerpt: "Plz remove the debug print statements. and the Chinese comments. Also, other places." (https://github.com/sgl-project/sglang/pull/21203#discussion_r2984126258)
