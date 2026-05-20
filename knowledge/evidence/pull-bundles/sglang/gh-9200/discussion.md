# PR Discussion Digest

- Source PR: [sgl-project/sglang#9200](https://github.com/sgl-project/sglang/pull/9200)
- Source page: `sources/prs/sglang/PR-9200.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9200`
- Generated at: `2026-05-20T15:31:32.897619+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-14T21:01:00Z`
- Merged: `2025-08-22T19:19:46Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 10 (approved=3, commented=7)
- Inline review comments: 11
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: elfiegg, fzyzcjy, kaixih, pavanimajety, wenscarl
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-14T21:01:12Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @kaixih, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3122108934)
- `2025-08-14T21:02:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new quantization operator, scaled fp4 grouped quant, designed for FlashInfer's grouped ... (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3122111458)
- `2025-08-15T22:14:09Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3125272203)
- `2025-08-15T23:38:09Z` `APPROVED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3125354607)
- `2025-08-17T13:47:51Z` `APPROVED` by `fzyzcjy` - since this kernel is temporary and only serve to make accuracy correct and will be removed later, it ... (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3126348118)
- `2025-08-18T18:19:44Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3129426220)
- `2025-08-18T18:22:41Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3129433659)
- `2025-08-18T23:10:51Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3130210834)
- `2025-08-18T23:48:53Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3130255570)
- `2025-08-19T00:11:58Z` `APPROVED` by `pavanimajety` - LGTM, thanks for the PR! (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3130284287)

## Inline Comment Hotspots

- `sgl-kernel/python/sgl_kernel/gemm.py`: 11 inline comment(s)

## High-Signal Discussion

- `2025-08-18T18:22:41Z` `inline` by `kaixih` `sgl-kernel/python/sgl_kernel/gemm.py`:327; signals: blackwell, gemm, kernel, tcgen05, tile; excerpt: "I added a line to clarify what these constants mean. I’m a bit reluctant to call them tile sizes, since I think they differ ..." (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283131964)
- `2025-08-18T23:10:51Z` `inline` by `elfiegg` `sgl-kernel/python/sgl_kernel/gemm.py`:327; signals: flashinfer, fp4, gemm, kernel; excerpt: "FYI 128x4 quant in Flashinfer : vs. 8x4 quant in Flashinfer: both for trtllm fp4 gemm and bmm:" (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283680610)
- `2025-08-15T23:37:10Z` `inline` by `elfiegg` `sgl-kernel/python/sgl_kernel/gemm.py`:327; signals: gemm, kernel, tile; excerpt: "can you do me a favor to name 4 and 128 to a tile size constant? the reason is trtllm-gen supports other tile sizes ..." (https://github.com/sgl-project/sglang/pull/9200#discussion_r2280028868)
- `2025-08-19T00:09:55Z` `inline` by `pavanimajety` `sgl-kernel/python/sgl_kernel/gemm.py`:327; signals: gemm, kernel; excerpt: "Since Grouped Gemm is the next operation after Quantization - I am not sure if there is support for more basic chunk shapes -" (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283743588)
- `2025-08-15T22:14:08Z` `inline` by `wenscarl` `sgl-kernel/python/sgl_kernel/gemm.py`:311; signals: gemm, kernel; excerpt: "Shouldn't it be [m, k // (2 16), l]?" (https://github.com/sgl-project/sglang/pull/9200#discussion_r2279965507)
- `2025-08-18T18:19:44Z` `inline` by `kaixih` `sgl-kernel/python/sgl_kernel/gemm.py`:311; signals: gemm, kernel; excerpt: "Not really. The quantized output shouldn't be divided by 16. The output scales should be." (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283126202)
- `2025-08-18T23:48:53Z` `inline` by `pavanimajety` `sgl-kernel/python/sgl_kernel/gemm.py`:317; signals: gemm, kernel; excerpt: "Could you please add clarification for what rm and rk stand for? I take it it is the quotient?" (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283718334)
- `2025-08-19T00:11:17Z` `inline` by `pavanimajety` `sgl-kernel/python/sgl_kernel/gemm.py`:349; signals: gemm, kernel; excerpt: "Awesome, great that you were able to reuse the existing implementation!" (https://github.com/sgl-project/sglang/pull/9200#discussion_r2283744868)
- `2025-08-17T13:47:51Z` `review` `APPROVED` by `fzyzcjy`; signals: accuracy, kernel; excerpt: "since this kernel is temporary and only serve to make accuracy correct and will be removed later, it LGTM as long as the shape ..." (https://github.com/sgl-project/sglang/pull/9200#pullrequestreview-3126348118)
- `2025-08-22T17:50:04Z` `issue` by `kaixih`; signals: fp4, kernel; excerpt: "I have added a new fused kernel to do silu+fp4 quant." (https://github.com/sgl-project/sglang/pull/9200#issuecomment-3215152859)
- `2025-08-18T18:23:58Z` `issue` by `kaixih`; signals: hang; excerpt: "@fzyzcjy Could you help merge this? It will allow @wenscarl to test his branch without needing to patch my changes." (https://github.com/sgl-project/sglang/pull/9200#issuecomment-3197962936)
