# PR Discussion Digest

- Source PR: [vllm-project/vllm#20087](https://github.com/vllm-project/vllm/pull/20087)
- Source page: `sources/prs/vllm/PR-20087.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20087`
- Generated at: `2026-05-20T15:36:00.249377+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-25T17:55:57Z`
- Merged: `2025-07-11T03:18:05Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 17 (approved=1, commented=16)
- Inline review comments: 25
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=12, outdated=13
- Human participants with discussion text: mergify, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-25T17:56:48Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yewentao256, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-2959142498)
- `2025-06-25T17:58:02Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates the new DeepGEMM library, updating the API interfaces and migrating to the ... (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-2959145382)
- `2025-07-09T15:37:02Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3001896476)
- `2025-07-09T19:45:33Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3002866887)
- `2025-07-10T17:36:51Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006665346)
- `2025-07-10T17:41:16Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006677479)
- `2025-07-10T18:02:53Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006745669)
- `2025-07-10T18:06:37Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006761179)
- `2025-07-10T18:09:11Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006770825)
- `2025-07-10T18:11:16Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006777602)
- `2025-07-10T18:22:08Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3006809377)
- `2025-07-10T20:44:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007220025)
- `2025-07-10T22:16:27Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007568030)
- `2025-07-10T22:42:21Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007632806)
- `2025-07-10T22:42:29Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007633226)
- `2025-07-10T22:42:52Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007635018)
- `2025-07-10T23:01:14Z` `APPROVED` by `mgoin` - LGTM, thank you for iterating on this (https://github.com/vllm-project/vllm/pull/20087#pullrequestreview-3007685147)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 6 inline comment(s)
- `vllm/utils/deep_gemm.py`: 6 inline comment(s)
- `tests/kernels/moe/test_deepgemm.py`: 4 inline comment(s)
- `tests/kernels/moe/test_block_fp8.py`: 2 inline comment(s)
- `tests/kernels/quantization/test_block_fp8.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 2 inline comment(s)
- `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm_b200.py`: 2 inline comment(s)
- `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-10T20:20:22Z` `inline` by `mgoin` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm_b200.py`; signals: b200, benchmark, blackwell, block, deepgemm, fp8, gemm, kernel; excerpt: "Rename this to blackwell or sm100" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198644352)
- `2025-07-10T18:02:53Z` `inline` by `yewentao256` `tests/kernels/quantization/test_block_fp8.py`:135; signals: b200, block, deepgemm, fp8, gemm, h100, kernel; excerpt: "On B200, it is supported inside the deepgemm. I should add it back for H100, thanks!" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198364528)
- `2025-07-10T22:16:27Z` `inline` by `yewentao256` `benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm_b200.py`; signals: b200, benchmark, block, deepgemm, fp8, gemm, kernel; excerpt: "Has been deleted and will have another pr for it specifically" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198868660)
- `2025-07-10T22:42:51Z` `inline` by `yewentao256` `vllm/utils/deep_gemm.py`:117; signals: accuracy, b200, blackwell, deepgemm, gemm, kernel; excerpt: "DeepGEMM kernels on Blackwell/B200 currently exhibit noticeable per-element error, causing `torch.testing.assert close to fail. Instead of checking every element, we compute a cosine-style similarity ..." (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198915513)
- `2025-07-09T14:53:29Z` `inline` by `mgoin` `tests/kernels/moe/test_block_fp8.py`:19; signals: blackwell, block, fp8, gemm, kernel, moe; excerpt: "I think we should simplify this to is blackwell deep gemm" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2195241110)
- `2025-07-09T15:29:01Z` `inline` by `mgoin` `tests/kernels/moe/test_deepgemm.py`:85; signals: block, deepgemm, gemm, kernel, moe; excerpt: "This seems hardcoded to block 128 now? We should restrict BLOCK SIZE then Also this isn't per token this is per token group?" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2195323055)
- `2025-07-10T17:36:51Z` `inline` by `yewentao256` `tests/kernels/moe/test_deepgemm.py`:85; signals: block, deepgemm, gemm, kernel, moe; excerpt: "In deepgemm, per token = per token group I rename the function to per token group for better meaning. And also add a param ..." (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198312751)
- `2025-07-09T15:29:58Z` `inline` by `mgoin` `tests/kernels/moe/test_deepgemm.py`:171; signals: deepgemm, fp8, gemm, kernel, moe; excerpt: "Where is fp8 quantize?" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2195325011)
- `2025-07-09T15:36:49Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/fp8.py`:812; signals: b200, block, fp8, gemm; excerpt: "Why not put this as an elif after the if self.allow deep gemm and not is new deep gemm api on b200(): block" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2195339149)
- `2025-07-10T18:22:08Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/fp8.py`:812; signals: blackwell, block, fp8, gemm; excerpt: "There is an elif elif not self.quant config.is checkpoint fp8 serialized: which means if checkpoint is fp16, quantize in place. I suppose we should ..." (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198402137)
- `2025-07-10T20:42:31Z` `inline` by `mgoin` `vllm/utils/deep_gemm.py`:102; signals: blackwell, deepgemm, fp8, gemm; excerpt: "It difficult to tell if this wrapper is for deepgemm specifically or can also be a wrapper for per token group quant fp8 generally. ..." (https://github.com/vllm-project/vllm/pull/20087#discussion_r2198688448)
- `2025-07-09T19:45:33Z` `inline` by `yewentao256` `tests/kernels/moe/test_block_fp8.py`:19; signals: block, fp8, kernel, moe; excerpt: "Sounds great! Fixed" (https://github.com/vllm-project/vllm/pull/20087#discussion_r2195846121)
