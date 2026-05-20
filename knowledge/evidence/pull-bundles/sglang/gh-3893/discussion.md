# PR Discussion Digest

- Source PR: [sgl-project/sglang#3893](https://github.com/sgl-project/sglang/pull/3893)
- Source page: `sources/prs/sglang/PR-3893.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3893`
- Generated at: `2026-05-20T15:30:02.476220+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-26T16:06:19Z`
- Merged: `2025-03-02T07:01:58Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 1 (approved=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: BBuf, Cydia2018, hebiao064, xuzhenqi, zhaochenyang20
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-03-02T07:01:44Z` `APPROVED` by `zhaochenyang20` (https://github.com/sgl-project/sglang/pull/3893#pullrequestreview-2652644690)

## Inline Comment Hotspots

- `benchmark/kernels/deepseek/benchmark_deepgemm_fp8_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-28T06:52:32Z` `issue` by `BBuf`; signals: block, cutlass, deepgemm, fp8, gemm, perf, triton; excerpt: "How about the cutlass version block-wise fp8 gemm, does it perform better than triton's version? I'm not entirely sure, but I’ve updated the results. ..." (https://github.com/sgl-project/sglang/pull/3893#issuecomment-2689874687)
- `2025-02-27T12:52:17Z` `issue` by `xuzhenqi`; signals: block, cutlass, fp8, gemm, perf, triton; excerpt: "How about the cutlass version block-wise fp8 gemm, does it perform better than triton's version?" (https://github.com/sgl-project/sglang/pull/3893#issuecomment-2687876051)
- `2025-03-02T06:59:04Z` `inline` by `zhaochenyang20` `benchmark/kernels/deepseek/benchmark_deepgemm_fp8_gemm.py`:214; signals: benchmark, deepgemm, fp8, gemm, kernel; excerpt: "do not use chinese in comments." (https://github.com/sgl-project/sglang/pull/3893#discussion_r1976555284)
- `2025-03-02T02:25:40Z` `issue` by `hebiao064`; signals: deepgemm, gemm, h100; excerpt: "Nice work! I can repro on my H100 with tp=1. I noticed that DeepGEMM seems to have the most consistent advantage in large matrix ..." (https://github.com/sgl-project/sglang/pull/3893#issuecomment-2692520464)
- `2025-03-02T05:10:57Z` `issue` by `BBuf`; signals: general review; excerpt: "@BBuf who is going to review this? You can do a quick review of this, it won't affect the functionality of SGLang, and we ..." (https://github.com/sgl-project/sglang/pull/3893#issuecomment-2692561896)
