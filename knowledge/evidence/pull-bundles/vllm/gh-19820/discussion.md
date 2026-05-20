# PR Discussion Digest

- Source PR: [vllm-project/vllm#19820](https://github.com/vllm-project/vllm/pull/19820)
- Source page: `sources/prs/vllm/PR-19820.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19820`
- Generated at: `2026-05-20T15:35:35.731789+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-18T20:57:51Z`
- Merged: `2025-06-24T19:51:56Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: bnellnm, houseroad, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-18T20:58:32Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yewentao256, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2940645839)
- `2025-06-18T20:59:50Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates DeepGEMM v2.0, which involves updating API interfaces across several files. The changes ... (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2940652364)
- `2025-06-19T01:45:24Z` `APPROVED` by `houseroad` - Looks good to me. (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2941207991)
- `2025-06-19T20:36:05Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2943992767)
- `2025-06-19T20:37:52Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2943994762)
- `2025-06-20T06:36:10Z` `COMMENTED` by `mgoin` - Looks good to me, great work @yewentao256! To confirm, the interface change will be the same for Hopper ... (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2944709717)
- `2025-06-24T14:59:35Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2954255772)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 4 inline comment(s)
- `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-19T01:44:00Z` `inline` by `houseroad` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:281; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "keep this comment?" (https://github.com/vllm-project/vllm/pull/19820#discussion_r2155847773)
- `2025-06-19T20:36:05Z` `inline` by `yewentao256` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`:281; signals: benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/19820#discussion_r2157636913)
- `2025-06-20T20:43:58Z` `issue` by `yewentao256`; signals: benchmark, blackwell, hang, hopper, latency, perf; excerpt: "Looks good to me, great work @yewentao256! To confirm, the interface change will be the same for Hopper and Blackwell? If so I think ..." (https://github.com/vllm-project/vllm/pull/19820#issuecomment-2992800609)
- `2025-06-23T21:43:31Z` `issue` by `yewentao256`; signals: deepgemm, gemm, h100, perf, performance, throughput; excerpt: "I think this PR is ready to merge now after DeepGemm officially merge their version. For the low E2E throughput issue, Actually, on H100 ..." (https://github.com/vllm-project/vllm/pull/19820#issuecomment-2998029995)
- `2025-06-20T06:36:10Z` `review` `COMMENTED` by `mgoin`; signals: blackwell, hang, hopper, perf; excerpt: "Looks good to me, great work @yewentao256! To confirm, the interface change will be the same for Hopper and Blackwell? If so I think ..." (https://github.com/vllm-project/vllm/pull/19820#pullrequestreview-2944709717)
- `2025-06-19T20:37:52Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:663; signals: deepgemm, fp8, gemm; excerpt: "It is a temporary function, we will delete this when DeepGemm exposes the function, and I believe it is well tested on their side. ..." (https://github.com/vllm-project/vllm/pull/19820#discussion_r2157638107)
- `2025-06-20T06:29:26Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:663; signals: deepgemm, fp8, gemm; excerpt: "I agree a unittest is likely not needed since this is copied from deepgemm" (https://github.com/vllm-project/vllm/pull/19820#discussion_r2158152031)
- `2025-06-19T01:45:17Z` `inline` by `houseroad` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:663; signals: fp8; excerpt: "we can add some unittest for these utility functions." (https://github.com/vllm-project/vllm/pull/19820#discussion_r2155848771)
