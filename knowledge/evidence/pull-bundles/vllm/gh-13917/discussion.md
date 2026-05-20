# PR Discussion Digest

- Source PR: [vllm-project/vllm#13917](https://github.com/vllm-project/vllm/pull/13917)
- Source page: `sources/prs/vllm/PR-13917.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13917`
- Generated at: `2026-05-20T15:34:08.442150+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-26T19:19:15Z`
- Merged: `2025-03-06T01:08:51Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: LucasWilkinson, ProphetPeng, benchislett, houseroad, mgoin, youkaichao, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-26T19:30:07Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/13917#pullrequestreview-2645656414)
- `2025-02-26T19:46:48Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/13917#pullrequestreview-2645697176)
- `2025-02-27T02:14:56Z` `COMMENTED` by `ProphetPeng` (https://github.com/vllm-project/vllm/pull/13917#pullrequestreview-2646393311)
- `2025-02-27T03:21:09Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/13917#pullrequestreview-2646468937)

## Inline Comment Hotspots

- `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-02-26T23:37:27Z` `issue` by `LucasWilkinson`; signals: block, cutlass, deepgemm, gemm, h100, kernel, tile; excerpt: "Hmmm ya this is a bit inconclusive/underwhelming given that the CUTLASS blockwise kernels haven't really be tuned yet, with the exception of (which was ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686447506)
- `2025-02-26T19:30:06Z` `inline` by `ywang96` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:172; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "Shouldn't this be I was looking at the example benchmark results and got really confused" (https://github.com/vllm-project/vllm/pull/13917#discussion_r1972258915)
- `2025-02-26T19:46:48Z` `inline` by `mgoin` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:172; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "Yup Lucas caught this too" (https://github.com/vllm-project/vllm/pull/13917#discussion_r1972286150)
- `2025-02-27T02:14:56Z` `inline` by `ProphetPeng` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:81; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "Can you replace it with per token group quant fp8(A, block size[1], column major scales=True)?" (https://github.com/vllm-project/vllm/pull/13917#discussion_r1972714278)
- `2025-02-27T03:21:09Z` `inline` by `mgoin` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:81; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "This seems to make no difference" (https://github.com/vllm-project/vllm/pull/13917#discussion_r1972765390)
- `2025-02-26T21:34:46Z` `issue` by `LucasWilkinson`; signals: aligned, cutlass, fp8, tma, vector; excerpt: "do you know how slow get col major tma aligned tensor is? we can probably update per token group quant fp8 to handle this ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686252076)
- `2025-02-26T20:21:08Z` `issue` by `mgoin`; signals: deepgemm, gemm, perf, performance; excerpt: "Does the number reported match the numbers reported in their repo? It seems DeepGEMM performance is very limited in performance to the shapes they ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686106200)
- `2025-02-26T21:46:01Z` `issue` by `mgoin`; signals: compile, cutlass, kernel, triton; excerpt: "I made a prettier script and updated the table above. The numbers will look a bit worse than their results because I am including ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686273773)
- `2025-02-26T20:26:18Z` `issue` by `benchislett`; signals: benchmark, cutlass, speedup; excerpt: "Is it possible to reproduce the setup and configuration they used in their benchmark? We test all shapes potentially used in DeepSeek-V3/R1 inference (including ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686115867)
- `2025-02-27T23:14:27Z` `issue` by `mgoin`; signals: benchmark, perf, performance; excerpt: "@benchislett please see As noted here, microbenchmark performance is not good (except for very specific sizes) yet so we need to figure out how ..." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2689322237)
- `2025-03-03T07:25:55Z` `issue` by `houseroad`; signals: benchmark, kernel; excerpt: "Btw, shall we land this benchmark scripts? We may reuse to expand to other kernel libraries." (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2693493677)
- `2025-02-26T22:15:13Z` `issue` by `houseroad`; signals: gemm; excerpt: "Wondering if we can try more shapes provided from their side. Also curious about the Grouped GEMM comparison?" (https://github.com/vllm-project/vllm/pull/13917#issuecomment-2686328301)
