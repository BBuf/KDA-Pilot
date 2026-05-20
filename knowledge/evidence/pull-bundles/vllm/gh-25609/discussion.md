# PR Discussion Digest

- Source PR: [vllm-project/vllm#25609](https://github.com/vllm-project/vllm/pull/25609)
- Source page: `sources/prs/vllm/PR-25609.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25609`
- Generated at: `2026-05-20T15:37:56.211299+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-24T21:23:34Z`
- Merged: `2025-09-25T04:12:53Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 17
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: mgoin, samanamp, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-24T21:26:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables FBGEMM FP4 kernels for dense models, which shows a significant performance improvement ... (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264793440)
- `2025-09-24T21:35:58Z` `COMMENTED` by `yewentao256` - Looks reasonable, thanks for the work! (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264815019)
- `2025-09-24T21:46:17Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264836364)
- `2025-09-24T21:48:17Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264835246)
- `2025-09-24T21:48:36Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264840439)
- `2025-09-24T21:51:09Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264848831)
- `2025-09-24T21:51:48Z` `COMMENTED` by `mgoin` - Cool! We've been hastily waiting for fbgemm to start to be integrated <3 (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264848635)
- `2025-09-24T22:13:40Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264897095)
- `2025-09-24T22:13:51Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264897414)
- `2025-09-24T22:14:11Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264898220)
- `2025-09-24T22:14:42Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264899203)
- `2025-09-24T23:12:04Z` `APPROVED` by `mgoin` - LGTM, thanks for the nice work. Separately, what are the requirements of the package? If it isn't that ... (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264985431)
- `2025-09-25T00:56:33Z` `COMMENTED` by `samanamp` (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3265157525)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`: 10 inline comment(s)
- `benchmarks/kernels/bench_nvfp4_gemm.py`: 5 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-24T21:46:16Z` `inline` by `samanamp` `benchmarks/kernels/bench_nvfp4_gemm.py`:102; signals: benchmark, fp4, gemm, kernel, nvfp4; excerpt: "Because we're dealing with separate gemm, the current pattern used is better. Any other way would be just a different iteration of same approach." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377148900)
- `2025-09-24T21:51:04Z` `inline` by `mgoin` `benchmarks/kernels/bench_nvfp4_gemm.py`:43; signals: benchmark, fp4, gemm, kernel, nvfp4; excerpt: "Could we make it such that the benchmark will still run by default if fbgemm gpu isn't installed? It's okay to warn and skip ..." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377159167)
- `2025-09-24T21:34:45Z` `inline` by `yewentao256` `benchmarks/kernels/bench_nvfp4_gemm.py`:102; signals: benchmark, fp4, gemm, kernel, nvfp4; excerpt: "Nice bot!" (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377131818)
- `2025-09-24T22:14:41Z` `inline` by `samanamp` `benchmarks/kernels/bench_nvfp4_gemm.py`:43; signals: benchmark, fp4, gemm, kernel, nvfp4; excerpt: "Great suggestion, fixed." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377200085)
- `2025-09-24T21:48:07Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:133; signals: bf16, fp4, gemm, nvfp4; excerpt: "Since these views should be free, could we just move them into the torch.ops.fbgemm.f4f4bf16 call in apply?" (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377151475)
- `2025-09-24T21:51:09Z` `inline` by `samanamp` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:133; signals: fp4, nvfp4; excerpt: "That's true, they are free. As all weight preparation is done in this function, logically better to be here. Also we're working on a ..." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377159370)
- `2025-09-24T21:46:48Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:165; signals: fp4, nvfp4; excerpt: "Move this into the condition below" (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377149628)
- `2025-09-24T22:13:40Z` `inline` by `samanamp` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:40; signals: fp4, nvfp4; excerpt: "fixed" (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377198536)
- `2025-09-24T22:13:51Z` `inline` by `samanamp` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:165; signals: fp4, nvfp4; excerpt: "fixed." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377198800)
- `2025-09-24T22:14:11Z` `inline` by `samanamp` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:176; signals: fp4, nvfp4; excerpt: "fixed" (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377199349)
- `2025-09-25T00:56:33Z` `inline` by `samanamp` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:178; signals: fp4, nvfp4; excerpt: "fixed." (https://github.com/vllm-project/vllm/pull/25609#discussion_r2377389583)
- `2025-09-24T21:51:48Z` `review` `COMMENTED` by `mgoin`; signals: gemm; excerpt: "Cool! We've been hastily waiting for fbgemm to start to be integrated <3" (https://github.com/vllm-project/vllm/pull/25609#pullrequestreview-3264848635)
