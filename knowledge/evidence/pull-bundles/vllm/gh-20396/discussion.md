# PR Discussion Digest

- Source PR: [vllm-project/vllm#20396](https://github.com/vllm-project/vllm/pull/20396)
- Source page: `sources/prs/vllm/PR-20396.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20396`
- Generated at: `2026-05-20T15:36:06.805208+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-02T18:21:20Z`
- Merged: `2025-07-28T23:13:58Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: LyrisZhong, mgoin
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-02T18:22:54Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @LyrisZhong, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20396#pullrequestreview-2980204690)
- `2025-07-02T18:26:47Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimization for FP8 GEMM on SM90 by adding support for swapping ... (https://github.com/vllm-project/vllm/pull/20396#pullrequestreview-2980222611)
- `2025-07-02T21:57:48Z` `COMMENTED` by `LyrisZhong` (https://github.com/vllm-project/vllm/pull/20396#pullrequestreview-2980750225)
- `2025-07-02T21:58:29Z` `COMMENTED` by `LyrisZhong` (https://github.com/vllm-project/vllm/pull/20396#pullrequestreview-2980752898)
- `2025-07-21T19:53:14Z` `APPROVED` by `mgoin` - Looks reasonable to me, thanks for the update and evaluations (https://github.com/vllm-project/vllm/pull/20396#pullrequestreview-3039552820)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_sm90_fp8_dispatch.cuh`: 4 inline comment(s)
- `tests/kernels/quantization/test_cutlass_scaled_mm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-02T21:57:48Z` `inline` by `LyrisZhong` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_sm90_fp8_dispatch.cuh`:250; signals: block, cutlass, fp8, gemm, sm100, sm90; excerpt: "Accordingly to existing[ PR]( for enabling swap ab for blockwise fp8 GEMM on SM100, the strides are as expected, related code in current vllm ..." (https://github.com/vllm-project/vllm/pull/20396#discussion_r2181045402)
- `2025-07-02T21:58:29Z` `inline` by `LyrisZhong` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_sm90_fp8_dispatch.cuh`:237; signals: block, cutlass, fp8, gemm, sm100, sm90; excerpt: "Accordingly to existing[ PR]( for enabling swap ab for blockwise fp8 GEMM on SM100, the strides are as expected, related code in current vllm ..." (https://github.com/vllm-project/vllm/pull/20396#discussion_r2181046606)
- `2025-07-18T23:07:38Z` `issue` by `LyrisZhong`; signals: benchmark, cutlass, fp8, gemm, kernel, memory; excerpt: "@djmmoss @mgoin I have done additional tests for the latest commit: 1)Confirmed benchmark results (by running bench fp8 gemm.py) mentioned in PR description are ..." (https://github.com/vllm-project/vllm/pull/20396#issuecomment-3091219689)
- `2025-07-21T19:52:36Z` `inline` by `mgoin` `tests/kernels/quantization/test_cutlass_scaled_mm.py`:99; signals: accuracy, cutlass, kernel; excerpt: "That is a fairly large increase in rtol.. will accept given the accuracy evals" (https://github.com/vllm-project/vllm/pull/20396#discussion_r2220154903)
- `2025-07-22T21:45:50Z` `issue` by `LyrisZhong`; signals: general review; excerpt: "@mgoin is there anything pending from my side for the failed checks above? I haven't seen anything related to the PR yet" (https://github.com/vllm-project/vllm/pull/20396#issuecomment-3104921303)
- `2025-07-28T21:40:29Z` `issue` by `mgoin`; signals: general review; excerpt: "@LyrisZhong There is general flakiness with the CI at the moment, I'll take care of getting this merged. Thanks!" (https://github.com/vllm-project/vllm/pull/20396#issuecomment-3129959770)
