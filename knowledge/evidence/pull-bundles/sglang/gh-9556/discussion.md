# PR Discussion Digest

- Source PR: [sgl-project/sglang#9556](https://github.com/sgl-project/sglang/pull/9556)
- Source page: `sources/prs/sglang/PR-9556.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9556`
- Generated at: `2026-05-20T15:31:37.891883+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-24T08:02:20Z`
- Merged: `2025-08-30T00:17:04Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: fzyzcjy, kaixih, merrymercy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-24T08:02:34Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @kaixih, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3149230332)
- `2025-08-24T08:05:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUDA kernel cvt fp16 to fp4 masked to optimize the ... (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3149231657)
- `2025-08-25T00:06:32Z` `COMMENTED` by `fzyzcjy` - Hi, could you please test on this shape (which is of most interest) 6 local experts 1024/512/256/128 tokens ... (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3149563207)
- `2025-08-26T15:07:29Z` `COMMENTED` by `fzyzcjy` - made a very simple check and the general direction looks reasonable to me, will review in more detail ... (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3156097148)
- `2025-08-30T00:16:41Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3170752874)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/nvfp4_expert_quant.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-25T18:02:06Z` `issue` by `kaixih`; signals: accuracy, cutlass, fp4, hang, kernel; excerpt: "Just pushed some changes. And I noticed that I couldn't make it to replace the existing kernels because I see accuracy drops for dsr1 ..." (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3221221667)
- `2025-08-27T20:51:04Z` `issue` by `kaixih`; signals: benchmark, fp4, gemm, nvfp4, perf; excerpt: "@zhyncs Sure. Thx for the headsup. The last commit enabled masked quant. With it, the leading quant performs almost the same as silu-quant-masked in ..." (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3229706178)
- `2025-08-26T06:32:32Z` `issue` by `kaixih`; signals: benchmark, cuda, fp4; excerpt: "Added a benchmark script. Below is the output with varying M and K with masks (max m=4096). This PR focuses on improve cuda fused ..." (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3222806191)
- `2025-08-25T00:06:32Z` `review` `COMMENTED` by `fzyzcjy`; signals: moe; excerpt: "Hi, could you please test on this shape (which is of most interest) 6 local experts 1024/512/256/128 tokens per local expert (1024 is most ..." (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3149563207)
- `2025-08-28T04:49:53Z` `issue` by `kaixih`; signals: accuracy, hang; excerpt: "@fzyzcjy This PR ( 9199) already uses my changes for the accuracy tests (@wenscarl patched my changes in his internale repo). Without them, execution ..." (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3231872614)
- `2025-08-28T04:40:31Z` `issue` by `fzyzcjy`; signals: accuracy, kernel; excerpt: "btw, when 9199 ( passes accuracy, this kernel will be double checked e2e" (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3231855135)
- `2025-08-26T15:07:29Z` `review` `COMMENTED` by `fzyzcjy`; signals: general review; excerpt: "made a very simple check and the general direction looks reasonable to me, will review in more detail later btw @Alcanderian do you have ..." (https://github.com/sgl-project/sglang/pull/9556#pullrequestreview-3156097148)
- `2025-08-24T20:31:34Z` `issue` by `kaixih`; signals: perf; excerpt: "The collected perf can be seen [here]( The repro: [python code]( and its launcher script:" (https://github.com/sgl-project/sglang/pull/9556#issuecomment-3218359755)
