# PR Discussion Digest

- Source PR: [sgl-project/sglang#3047](https://github.com/sgl-project/sglang/pull/3047)
- Source page: `sources/prs/sglang/PR-3047.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3047`
- Generated at: `2026-05-20T15:29:58.203945+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-22T08:39:42Z`
- Merged: `2025-01-26T07:46:51Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 9 (approved=1, changes_requested=1, commented=7)
- Inline review comments: 14
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=7
- Human participants with discussion text: BBuf, HandH1998, ispobock, ll2088, yiakwy-xpu-ml-framework-team, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-01-22T08:44:06Z` `CHANGES_REQUESTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2566542726)
- `2025-01-22T08:45:39Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2566551651)
- `2025-01-22T08:49:56Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2566561156)
- `2025-01-22T10:18:07Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2566780487)
- `2025-01-23T02:47:02Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2568745845)
- `2025-01-23T11:40:14Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2569614628)
- `2025-01-23T15:11:07Z` `COMMENTED` by `yiakwy-xpu-ml-framework-team` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2570149807)
- `2025-01-24T07:02:05Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2571785764)
- `2025-01-26T07:45:18Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3047#pullrequestreview-2574161721)

## Inline Comment Hotspots

- `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`: 6 inline comment(s)
- `sgl-kernel/tests/test_fp8_gemm.py`: 3 inline comment(s)
- `sgl-kernel/setup.py`: 2 inline comment(s)
- `sgl-kernel/benchmark/bench_fp8_gemm.py`: 2 inline comment(s)
- `sgl-kernel/src/sgl-kernel/csrc/utils.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-01-23T15:11:06Z` `inline` by `yiakwy-xpu-ml-framework-team` `sgl-kernel/tests/test_fp8_gemm.py`:37; signals: block, fp8, gemm, kernel, perf, performance, triton; excerpt: "Hi @HandH1998 can I have the compasion between triton version w8a8 block fp8 matmul in your last , becuase triton gemm is more stable ..." (https://github.com/sgl-project/sglang/pull/3047#discussion_r1927144287)
- `2025-01-23T02:47:02Z` `inline` by `HandH1998` `sgl-kernel/benchmark/bench_fp8_gemm.py`:72; signals: benchmark, fp8, gemm, kernel; excerpt: "I didn't find a cublas version in the vllm link. I think it is not easy to add a cuBLAS version from scratch?" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1926283860)
- `2025-01-22T08:43:45Z` `inline` by `zhyncs` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:40; signals: cuda, fp8, gemm, kernel; excerpt: "Is CUDA 12.4 the minimum requirement?" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1924921723)
- `2025-01-22T10:18:07Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_fp8_gemm.py`:72; signals: benchmark, fp8, gemm, kernel; excerpt: "Can we add a CuBlas version to compare, refer to ." (https://github.com/sgl-project/sglang/pull/3047#discussion_r1925063068)
- `2025-01-24T07:02:05Z` `inline` by `HandH1998` `sgl-kernel/tests/test_fp8_gemm.py`:37; signals: cutlass, fp8, gemm, kernel; excerpt: "This cutlass implementation only supports w8a8 per-row fp8." (https://github.com/sgl-project/sglang/pull/3047#discussion_r1928175460)
- `2025-01-24T11:04:10Z` `issue` by `HandH1998`; signals: kernel, perf, performance, sm90; excerpt: "We have fixed the review issues and resolved the conflicts. And we also tried to optimize the performance on sm90, but it can't still ..." (https://github.com/sgl-project/sglang/pull/3047#issuecomment-2612255816)
- `2025-01-22T08:42:29Z` `inline` by `zhyncs` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:12; signals: fp8, gemm, kernel; excerpt: "use include instead" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1924920024)
- `2025-01-22T08:45:38Z` `inline` by `HandH1998` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:40; signals: fp8, gemm, kernel; excerpt: "for sm89, yes" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1924924347)
- `2025-01-23T11:30:20Z` `inline` by `ispobock` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:40; signals: fp8, gemm, kernel; excerpt: "add conditional compilation where the function is called would be enough?" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1926828226)
- `2025-01-23T11:32:24Z` `inline` by `ispobock` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:456; signals: fp8, gemm, kernel; excerpt: "remove unused comments." (https://github.com/sgl-project/sglang/pull/3047#discussion_r1926830741)
- `2025-01-23T11:37:41Z` `inline` by `ispobock` `sgl-kernel/tests/test_fp8_gemm.py`:33; signals: fp8, gemm, kernel; excerpt: "Can we use random input and avoid involve additional logic and deps?" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1926837092)
- `2025-01-23T11:38:45Z` `inline` by `ispobock` `sgl-kernel/src/sgl-kernel/csrc/fp8_gemm_kernel.cu`:154; signals: fp8, gemm, kernel; excerpt: "Why it's unused?" (https://github.com/sgl-project/sglang/pull/3047#discussion_r1926838327)
